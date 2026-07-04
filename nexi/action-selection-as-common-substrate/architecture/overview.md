# Architecture: Action Selection as Common Substrate

This document specifies the architectural primitive for treating action selection as a first-class architectural commitment — components, interfaces, data flow, and integration with the rest of the [`embodied-action-selection`](../../../collections/embodied-action-selection/) collection.

## Components

### 1. Candidate-action enumeration

A typed list of possible actions, generated from the agent's behavioural repertoire `Br` given the current goal `g`. Default state: all candidates inhibited.

```
enumerate(repertoire: Br, goal: g, context: C) -> CandidateList
```

Design-time: choose which subset of `Br` is candidate-relevant for goal `g`. Runtime: the enumerator returns a typed list of candidate actions, each tagged with its predicted contribution to `g+`.

### 2. Goal-conditioned competition

Candidates compete based on their behavioural associations `Ba(g, P)` — built up by prior reinforcement. The competition function takes the form of equation (2) from the [`ecological-context-model`](../../ecological-context-model/) NEXI: `B(C) = f(Br, Ba(g, P))`.

```
compete(candidates: CandidateList, associations: Ba) -> RankedCandidates
```

Design-time: choose the competition function (winner-take-all, soft-max with temperature, tournament, etc.). Runtime: candidates are ranked by goal-conditioned strength.

### 3. Selective disinhibition gate

The default-inhibit / selective-disinhibit gating logic. By default, all candidates are inhibited; the winning candidate is _released_, not _activated_. This is the architectural commitment that distinguishes this NEXI from "select highest-scoring action" approaches.

```
gate(ranked: RankedCandidates, gate_policy: GatePolicy) -> SelectedAction | NoSelection
```

Critical: gate logic must specify what happens under (a) tied winners, (b) no candidate above threshold, (c) high-stakes contexts where multi-stream evidence should be required (delegate to [`coincidence-detection-gating`](../../coincidence-detection-gating/) NEXI).

### 4. Contextual reinforcement loop

Successful selections (those that achieve `g+`) reinforce the goal-context-action association in `Ba(g, P)`, increasing the likelihood of similar selections in similar future contexts. This is the chunking mechanism from `B(C) = bn+1` — successful sequences become repertoire entries.

```
reinforce(selection: SelectedAction, outcome: GoalAchievement, context: C) -> updated Ba
```

Design-time: choose the reinforcement policy (TD-learning, direct association update, evolved-program override, etc.). Runtime: post-selection outcomes update associations.

## Data flow

```
   goal g, context C, perceptions P
      │
      ▼
   ┌─────────────────────────┐
   │ Candidate enumeration   │ ◄── repertoire Br
   └────────────┬────────────┘
                │ CandidateList
                ▼
   ┌─────────────────────────┐
   │ Goal-conditioned compete│ ◄── associations Ba(g, P)
   └────────────┬────────────┘
                │ RankedCandidates
                ▼
   ┌─────────────────────────┐
   │ Selective disinhibition │
   │       gate              │
   └────────────┬────────────┘
                │ SelectedAction
                ▼
        commit to action
                │
                ▼
       observe outcome
                │
                ▼
   ┌─────────────────────────┐
   │ Contextual reinforcement│
   └────────────┬────────────┘
                │ updated Ba(g, P)
                ▼
        (loops back to next selection)
```

## Pseudocode — runtime selection decision

```python
def select_action(goal, context, perceptions, repertoire, associations):
    # 1. Enumerate candidates relevant to goal
    candidates = enumerate(repertoire, goal, context)
    if not candidates:
        return Selection.no_action(reason="empty repertoire for goal")

    # 2. Compete: rank by goal-conditioned strength using equation (2)
    # B(C) = f(Br, Ba(g, P))
    ranked = compete(candidates, associations.lookup(goal, perceptions))

    # 3. Selective disinhibition gate (default-inhibit, release winner)
    selected = gate(
        ranked,
        gate_policy=GatePolicy.WINNER_RELEASE,
        threshold=DEFAULT_SELECTION_THRESHOLD,
    )

    if selected.is_high_stakes:
        # Delegate to coincidence-detection-gating NEXI for irreversible actions
        return coincidence_gate.check(selected, required_streams=["goal", "context", "memory"])

    return selected

def post_outcome_update(selection, outcome, context, associations):
    # 4. Contextual reinforcement loop — equation (3): g+(C) = f(B, E)
    if outcome.achieved_goal:
        associations.reinforce(
            goal=context.goal,
            perceptions=context.perceptions,
            action=selection.action,
        )
        # Optional: chunking if reinforcement crosses threshold (see P40)
        if associations.strength(selection.action) > CHUNKING_THRESHOLD:
            repertoire.add_chunk(selection.action_sequence)
    else:
        associations.weaken(
            goal=context.goal,
            perceptions=context.perceptions,
            action=selection.action,
        )
```

## Integration notes

| Stack                                                           | How to integrate                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LLM agent frameworks** (LangGraph, CrewAI, AutoGen)           | Place the action-selection module between candidate-tool-list generation and the actual tool call. Candidates are tools; competition is goal-conditioned scoring; selection is the explicit gate before side-effect-producing operations.                                                                           |
| **RL agents** (PPO, DQN, SAC)                                   | The action head already exists but is rarely a first-class module. Wrap it in the four-component structure: explicit candidate enumeration, explicit competition, explicit gating with default-inhibit logic, explicit reinforcement loop. The wrapping is what enables lesion experiments and decision provenance. |
| **Embodied AI** (robotic manipulation, navigation)              | Motor actions are the candidates. Explicit selection makes the motor-cognitive sharing visible — when paired with [`exaptation-architectural-reuse`](../../exaptation-architectural-reuse/), the same module handles cognitive operations under shared goal stack.                                                  |
| **Tool-using agents** (Claude with tools, GPT function calling) | Tool calls are the candidates. The selection module sits between tool enumeration and tool invocation. Decision-provenance is naturally exposed at this boundary.                                                                                                                                                   |
| **Multi-agent systems**                                         | Each agent has its own selection module. Cross-agent coordination via the [`coincidence-detection-gating`](../../coincidence-detection-gating/) NEXI for high-stakes joint commitments.                                                                                                                             |

## Performance and cost considerations

- **Module boundary overhead.** Exposing the four components adds inspection points and adds typed-data passing between them. For deployments where decision provenance is valuable (debugging, audit, lesion experiments), this overhead pays. For tight-loop deployments where every microsecond matters, the overhead is non-trivial.
- **Reinforcement loop persistence.** `Ba(g, P)` must be persisted across decisions for chunking to work. Persistence overhead is low for individual sessions; non-trivial for long-running deployments.
- **Cross-domain reuse efficiency.** When the same module handles motor and cognitive selection (paired with exaptation NEXI), the marginal cost per new domain drops sharply. This is the collection's primary architectural payoff.

## Interaction with the collection

This NEXI is the **substrate-invariant layer** of the [`embodied-action-selection`](../../../collections/embodied-action-selection/) collection. It composes with:

- [`ecological-context-model`](../../ecological-context-model/) — provides the formal substrate (equations 1–3) on which this NEXI's components are defined. The competition function uses equation (2); the reinforcement loop uses equation (3).
- [`exaptation-architectural-reuse`](../../exaptation-architectural-reuse/) — the generative principle by which a single instance of this NEXI's module can be redeployed across motor and cognitive domains. Without exaptation, this NEXI would require domain-duplicate modules.
- [`heuristics-as-habits-fusion`](../../heuristics-as-habits-fusion/) — the concrete behavioural-instance NEXI that this NEXI's contextual-reinforcement loop produces (heuristics are chunked sequences of cognitive operations selected via this NEXI's mechanism).
