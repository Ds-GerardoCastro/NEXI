# Architecture: Ecological Context Model

This document specifies the architectural primitive for the Ecological Context Model — components, interfaces, data flow, and integration with the rest of the [`embodied-action-selection`](../../../collections/embodied-action-selection/) collection.

## Components

### 1. Unified state `E`

A typed data structure containing both agent-internal and agent-external features. The state-merger commitment: there is no separate "agent state" type and "world state" type — both live under one schema.

```
E := {f1, f2, f3, ..., fn}   # set of structural features

where each feature has:
    - id: string
    - source: enum [external, agent_internal]
    - kind: enum [observable_to_human, observable_to_agent, structural_only]
    - value: any
```

Design-time: the schema for `E` is defined per deployment. Agent-internal features (cognitive architecture, replay buffer state, attention weights, goal stack, circadian-style internal cycles) are first-class citizens.

### 2. Agent-perceptible filter `E(A)`

A function that returns the agent-perceptible subset of `E` given the agent's perceptual apparatus. Distinguishes "in `E` but not `E(A)`" (unobservable) from "in `E(A)` but not currently perceived" (observable but unattended).

```
E_of_A(E: State, agent: Agent) -> Set[Feature]
```

The footnote-5 illustration: ultraviolet light is always in `E` (a structural feature of the environment), but for humans without special tools it is _not_ in `E(A)`; for most birds it is. Perceptibility is agent-specific within the same physical environment.

### 3. Behavioural-association store `Ba(g, P)`

A persistent data structure mapping `(goal, perception-signature)` → ranked actions. This is the learnable component — equation (2) consults it for behaviour selection; reinforcement updates it post-outcome.

```
Ba := {
    (g₁, signature_of_P₁): {action_id: strength, ...},
    (g₁, signature_of_P₂): {action_id: strength, ...},
    (g₂, signature_of_P₁): {action_id: strength, ...},
    ...
}

interface:
    lookup(goal, perceptions) -> ranked Actions    # for eq. (2)
    reinforce(goal, perceptions, action) -> void   # post-success
    weaken(goal, perceptions, action) -> void      # post-failure
```

Critical: `signature_of_P` is a perception-signature function, not raw perceptions. This is what enables transfer — equation (2) selects behaviour `B` based on overlap in perception-signatures across contexts (see [`P45 — Context-Overlap-Driven Behavior Transfer`] in vault).

### 4. Goal-achievement evaluator `g+(C)`

A function applying equation (3): given the executed behaviour `B` and the _full_ environment `E` (not just `E(A)`), did the goal `g` get achieved? When `g+` fails, runs failure-attribution logic.

```
g_plus(C: Context, B: Behaviour) -> GoalAchievementResult

GoalAchievementResult:
    achieved: bool
    if not achieved:
        attribution: enum [P_failure, E_failure, Ba_failure, unknown]
        reasoning: string
```

The failure attribution is the architectural payoff. If `B` was selected based on overlap in `P` between this context and prior contexts where it succeeded, but `g+` fails because `E(C)` differed from `E(C′)` in goal-relevant ways the agent could not perceive, that's an `E_failure` (unobservability) — distinct from a `P_failure` (perception inadequate) or a `Ba_failure` (behavioural association incorrect).

## Data flow

```
   external world ─┐
                   ├──► E (unified state, typed)
   agent internal ─┘
                            │
                            ▼
                   ┌─────────────────────┐
                   │   E(A) filter       │ ◄── agent's perceptual apparatus
                   └──────────┬──────────┘
                              │ E(A) — agent-perceptible features
                              ▼
                       (agent perceives subset)
                              │
                              ▼
                          P — recent perceptions
                              │
                              ▼
                   ┌─────────────────────┐
                   │   eq. 1: C = {A(g), E} │ ◄── current goal g
                   └──────────┬──────────┘
                              │ context C
                              ▼
                   ┌─────────────────────┐
                   │   eq. 2: B(C) = f(Br, Ba(g, P)) │ ◄── repertoire Br, associations Ba
                   └──────────┬──────────┘
                              │ behaviour B
                              ▼
                       commit and execute
                              │
                              ▼
                   ┌─────────────────────┐
                   │   eq. 3: g+(C) = f(B, E) │
                   └──────────┬──────────┘
                              │
              ┌───────────────┼───────────────┐
              ▼               ▼               ▼
          achieved       not achieved     unknown
              │               │
              ▼               ▼
    reinforce Ba      attribute failure
                          (P / E / Ba)
                              │
                              ▼
                  apply remedy (improve P / handle E / weaken Ba)
```

## Pseudocode — full ECM-formalism step

```python
def ecm_step(agent, current_E, current_goal_g):
    # Apply E(A) filter — what does the agent see?
    E_A = filter_perceptible(current_E, agent.perceptual_apparatus)

    # Agent updates perceptions
    P = agent.perceive_from(E_A)

    # Eq. 1: construct context
    C = Context(agent=agent, goal=current_goal_g, environment=current_E)

    # Eq. 2: select behaviour
    Br = agent.repertoire
    Ba = agent.behavioural_associations
    candidates = lookup_associations(Ba, current_goal_g, signature_of(P))
    B = select_via_equation_2(Br, candidates)  # delegates to action-selection NEXI

    # Commit and execute
    outcome_state = execute(B, current_E)

    # Eq. 3: evaluate goal achievement
    g_plus_result = evaluate_goal_achievement(C, B, outcome_state)

    if g_plus_result.achieved:
        Ba.reinforce(current_goal_g, signature_of(P), B)
        if Ba.strength(B) > CHUNKING_THRESHOLD:
            # Habit formation — see P40 / heuristics-as-habits-fusion NEXI
            Br.add_chunk(B)
    else:
        attribution = attribute_failure(C, B, outcome_state)
        if attribution.kind == "P_failure":
            agent.improve_perception(attribution.feature)
        elif attribution.kind == "E_failure":
            agent.handle_unobservability(attribution.feature)
        elif attribution.kind == "Ba_failure":
            Ba.weaken(current_goal_g, signature_of(P), B)

    return ecm_step_result(C, B, g_plus_result)
```

## Integration notes

| Stack                                        | How to integrate                                                                                                                                                                                                                                              |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LLM agent frameworks** (LangGraph, CrewAI) | The unified state `E` is the agent's working-memory + tool-state + context-window contents. `E(A)` filters by what the agent is conditioned on. `Ba(g, P)` is the persistent goal-context-action memory store. `g+` is the post-action evaluation step.       |
| **Embodied AI / robotics**                   | `E` includes both world state (object poses, joint positions) and agent-internal state (battery level, internal clock). `E(A)` is the sensor stack. `Ba(g, P)` is the learned policy's goal-context-action mapping. `g+` is the task-success classifier.      |
| **RL agents**                                | The standard RL formalism (state, action, reward, policy) maps onto the ECM but with explicit additional structure. State maps to `E`/`E(A)`/`P`. Policy is `f(Br, Ba(g, P))`. Reward signals goal achievement; the ECM extension tracks failure attribution. |
| **Cognitive architectures** (ACT-R, Soar)    | The ECM is structurally close to declarative-procedural-memory architectures. `Ba(g, P)` resembles ACT-R's procedural-memory chunks. Integration: adopt the ECM's failure-attribution layer as a complement to existing chunk-firing logic.                   |

## Performance and cost considerations

- **State-schema overhead.** The unified `E` typing adds upfront design cost. For deployments with stable agent-environment boundaries, the cost is low; for evolving deployments, the schema may need versioning.
- **Failure-attribution complexity.** Distinguishing `P_failure` from `E_failure` from `Ba_failure` requires comparison between current and reference contexts. For tight-loop deployments, this may be too expensive; defer to post-hoc analysis.
- **Multi-goal extension overhead.** The single-goal simplification (footnote 6 of source) keeps the formalism tractable. Multi-goal continuous-time dynamics require additional machinery (motivation levels, goal-transition logic) — non-trivial extension.

## Interaction with the collection

This NEXI is the **formalism layer** of the [`embodied-action-selection`](../../../collections/embodied-action-selection/) collection. It composes with:

- [`action-selection-as-common-substrate`](../../action-selection-as-common-substrate/) — the substrate-invariant selection mechanism is defined in terms of the ECM's equations (the competition function uses eq. (2); the reinforcement loop uses eq. (3)).
- [`exaptation-architectural-reuse`](../../exaptation-architectural-reuse/) — the ECM's domain-agnostic typing of `B` (motor or cognitive) is what makes exaptive reuse feasible. Without the formalism, exaptation is a verbal claim; with it, the same equations operate on either domain.
- [`heuristics-as-habits-fusion`](../../heuristics-as-habits-fusion/) — the heuristics-as-habits formal equivalence is articulated in terms of the same equations operating on cognitive vs. motor `Br` and `Ba(g, P)`.
