# Ecological Context Model

> **NEXI status:** draft · **Formats:** architecture, skill · **Audience:** builder
>
> **Cluster:** [`embodied-action-selection`](../../clusters/embodied-action-selection/)
>
> A design-time architectural commitment to a **named formal framework with three numbered equations** for embodied-agent action selection. Rather than describing agent-environment interaction informally, the model specifies context, behaviour selection, and goal-achievement as relational structures with explicit terms — and treats the agent's internal state (cognitive architecture, behavioural repertoire, circadian rhythm, memories, interoceptions) as _part of_ the environment `E`, not a separate inner stage.

---

## At a glance

The default mental model in AI is to describe agent-environment interaction informally — "the agent observes the world, decides on an action, and acts" — without committing to typed relational structure. The Ecological Context Model says that for embodied agents, this informality leaks: it makes goal-context-action provenance hard to track, transfer of learning hard to attribute, and embodiment claims hard to operationalise.

The model's commitment is small but consequential: **context, behaviour selection, and goal-achievement get three numbered equations**, and the agent's internal state is part of the environment `E` rather than a separate hidden layer. The result is a citable framework that downstream design choices (action-selection module, habit-formation logic, transfer-of-learning evaluation) can reference directly.

The architectural translation: AI systems committing to the ECM formalism gain decision-provenance auditability (which goal, which context, which behaviour, which outcome — all with typed structure), transfer-failure attribution (was the failure due to inadequate perception `P`, or to environment `E` differing in goal-relevant ways the agent couldn't perceive?), and a foundation that supports the rest of the [`embodied-action-selection`](../../clusters/embodied-action-selection/) cluster.

---

## The natural exemplar

[Nordli & Todd (2022)](https://doi.org/10.3389/fpsyg.2022.841972) — peer-reviewed conceptual-analysis article, _Frontiers in Psychology_ — introduces the Ecological Context Model in §4 of the source paper. The model generalises Lewin's (1936) field-theory equation `B = f(A, E)` (behaviour as a function of agent and environment) to specify what context, behaviour selection, and goal-achievement mean as relational structures. Three numbered equations result.

The verbatim equations from the source (transcribed exactly):

**Equation (1)** — context as agent-toward-goal in environment (§5):

$$C = \{A(g),\, E\}$$

**Equation (2)** — behaviour in context as a function of repertoire and associations (§5):

$$B(C) = f\bigl(Br,\, Ba(g, P)\bigr)$$

**Equation (3)** — goal achievement as a function of behaviour and environmental structure (§5):

$$g+(C) = f(B, E)$$

Where:

- `A` is the agent
- `E` is the environment as a set of structural features `E = {f₁, f₂, …, fₙ}`
- `E(A)` is the agent-perceptible subset of `E` (perceptibility is agent-specific; UV light is in `E` for both humans and birds, but in `E(A)` only for birds)
- `Br = {b₁, b₂, …, bₙ}` is the agent's behavioural repertoire
- `P = {p₁, p₂, …, pₙ}` is the agent's recent perceptions
- `Ba(g, P) = {b₁p₁g, b₁p₂g, b₂p₁g, …}` is the set of behavioural associations given goal `g` and perceptions `P`
- `B = [bᵢ, bⱼ, bₖ, …]` is the planned/executed behaviour or sequence
- `g` is the goal in pursuit
- `g+` is goal achieved

The state-merger commitment: `E` and `E(A)` _include the agent's own internal state_ — cognitive architecture, behavioural repertoire, circadian rhythm, memories, emotions, interoceptions — alongside features external to the agent. Embodiment is formalised as a unified state schema, not a layer atop a separate environment.

See [`references.md`](references.md) for full citation chain and computational analogs.

---

## The pattern

**Default informal agent-environment description:**

```
   agent.observe()  →  agent.decide()  →  agent.act()  →  environment.respond()
```

No commitment to what context means, what behaviour selection depends on, or what determines goal achievement.

**Ecological Context Model:**

```
   For each step:
       C  := { A(g), E }                          # eq. 1 — context construction
       B  := f(Br, Ba(g, P))                      # eq. 2 — behaviour selection
       g+ := f(B, E)                              # eq. 3 — goal achievement check

       if g+:
           reinforce Ba(g, P) for the executed B
       else:
           attribute failure:
               P inadequate? → improve perception
               E differs from training? → handle unobservability
```

The non-trivial design choice is **what features get assigned to `E` vs. `E(A)` vs. `P`**. Features in `E` but not `E(A)` are unobservable to the agent (failure attribution: the agent was blind to a goal-relevant structural feature). Features in `E(A)` but not `P` are observable but unobserved (failure attribution: perception was inadequate). Features in `P` are the basis of the current selection.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — components, interfaces, data flow, and integration with the rest of the cluster.

In summary, four components:

1. **Unified state `E`.** A typed data structure containing both agent-internal and agent-external features. Supports introspective access (the agent's own machinery as features) and external access (the world's structure as features) under one schema.
2. **Agent-perceptible filter `E(A)`.** A function that selects which features of `E` are perceptible to the agent given its perceptual apparatus. Defines the boundary between observable and unobservable.
3. **Behavioural-association store `Ba(g, P)`.** A persistent data structure mapping (goal, perception-signature) → ranked actions. Updated by reinforcement post-outcome; consulted by the selection mechanism via equation (2).
4. **Goal-achievement evaluator `g+(C)`.** A function applying equation (3) — given the executed behaviour `B` and the full environment `E`, did the goal `g` get achieved? When `g+` fails, runs failure-attribution logic distinguishing perception-failure from unobservability-failure.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for an engineering-agent or runtime decision system:

- **System-prompt fragment** that instructs the agent to surface context construction, behaviour selection, and goal-achievement evaluation as explicit steps with typed terms.
- **Tool definitions** for `construct_context`, `lookup_behavioural_association`, `evaluate_goal_achievement`, `attribute_failure`.
- **Translation notes** for stack-specific mappings.

---

## When to use

- Embodied-AI deployments where agent-internal state and agent-external state share goal-relevant structure (e.g. robot manipulation where the robot's joint positions and the workpiece's pose are both load-bearing).
- Systems where goal-context-action provenance is a deliverable (debugging, audit, lesion experiments).
- Long-horizon agents where transfer of learned behavioural associations across contexts is a primary efficiency lever.
- Research / engineering work where a citable formal framework with verbatim equations is preferable to ad-hoc descriptions.
- As the foundation layer of the [`embodied-action-selection`](../../clusters/embodied-action-selection/) cluster — the other three NEXIs depend on the ECM formalism for their own definitions.

## When not to use

- Single-shot perception or classification systems where goal-context-action structure is absent.
- Pure-substrate construction (foundation-model pretraining) where the formalism's relational structure does not yet apply.
- Deployments where the cost of formalism-discipline outweighs the payoff in decision provenance and transfer attribution.
- Research / exploratory contexts deliberately operating without a goal-directed framing.

## Tradeoffs

- **Formalism-discipline upfront cost.** Committing to typed `C`, `B`, `g`, `E`, `P`, `Br`, `Ba` structure costs design effort and ongoing schema maintenance.
- **Goal-cyclicity dependence.** The formalism assumes goals are the temporal organisational primary (cyclic recurrence of goals drives reinforcement). Deployments where goal recurrence is sparse or absent get less payoff from the reinforcement structure.
- **Single-goal simplification (footnote 6 of the source).** The model is organised around a single goal at a time. Multi-goal continuous-time dynamics require extension; deployments with concurrent competing goals must specify how transitions between contexts work.

In return: decision-provenance auditability, transfer-failure attribution (perception-failure vs. unobservability-failure), explicit support for downstream NEXIs in the same cluster, and a citable formal framework that doesn't require the project to invent its own.

## Falsifiable hypothesis

> At matched compute and identical task budgets, AI architectures committing to the Ecological Context Model formalism outperform agent-environment-separated architectures on tasks requiring (a) goal-context-action provenance, (b) cross-domain transfer of learned behavioural associations via overlap in P, and (c) goal-achievement attribution distinguishing perception-failure from environment-failure. Specifically, when an action fails to achieve its goal, ECM-formalism architectures should be measurably better at distinguishing "the agent's perceptions P were inadequate" from "the environment E differed from training in goal-relevant ways the agent could not perceive" — these have different remedies. Refutation: if ECM-formalism architectures perform indistinguishably on these axes at matched cost, the formalism's architectural payoff claim is empirically weak.

A second testable claim: **transfer attribution diagnosticity.** Given a controlled distribution shift between training and evaluation, ECM-formalism architectures should be able to report whether the failure was a `P`-failure (perception inadequate), an `E`-failure (unobservable goal-relevant difference), or a `Ba`-failure (behavioural association incorrect for the new context). Architectures without the formalism cannot make these distinctions cleanly.

## References

See [`references.md`](references.md) — Nordli & Todd (2022) as primary source, plus Lewin (1936) for the field-theory equation the model generalises, and computational analogs in cognitive architectures (ACT-R, Soar) and embodied AI.
