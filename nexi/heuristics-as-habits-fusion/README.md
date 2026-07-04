# Heuristics as Habits Fusion

> **NEXI status:** draft · **Formats:** architecture, skill · **Audience:** builder
>
> **Collection:** [`embodied-action-selection`](../../clusters/embodied-action-selection/)
>
> A design-time architectural commitment to **unifying heuristic decision-making and motor-habit-formation under a single context-overlap-driven selection mechanism** — rather than implementing them as separate Type 1 (fast / heuristic) and Type 2 (deliberative / chunked) modules. The pattern argues that the dichotomy is misframed at the architectural level: both are the same mechanism operating on different repertoires.

---

## At a glance

The default mental model in cognitive science and AI is that fast-and-frugal heuristics and deliberative-and-chunked habits are different cognitive faculties, often grouped under "Type 1 vs. Type 2" or "System 1 vs. System 2" frameworks. The empirical record from comparative neuroscience contradicts this default: both are the same architectural mechanism — context-overlap-driven action selection from a learned repertoire — operating on different repertoires (cognitive operations vs. motor actions).

The strongest documented case: the recognition-heuristic worked example. When asked "which city is more populous, Tokyo or Yokohama?", American students often use the recognition heuristic: choose the recognised one. This succeeds when only one option is highly recognised (e.g., Yokohama vs. Nagasaki → Yokohama, correctly chosen) and fails when both are highly recognised but the heuristic's underlying assumption breaks (e.g., Tokyo vs. Yokohama → both recognised; the heuristic doesn't discriminate; the wrong choice arises). The structural failure mode here is _identical_ to the structural failure mode of grasping at empty air for a steering-wheel-shifter that's actually on the rental car's center console: same goal `g`, overlapping perceptions `P(C)`, but different environmental structure `E` produces different goal-achievement `g+(C)` outcomes.

Both failures arise via [`ecological-context-model`](../../ecological-context-model/) equation (3): `g+(C) = f(B, E)`. Same context-overlap-driven selection (eq. 2: `B(C) = f(Br, Ba(g, P))`); same context-incompatibility failure mode (eq. 3); just different repertoires.

The architectural translation: AI systems that unify habit and heuristic decision-making under one mechanism (rather than two separate modules) extract architectural simplification and gain cross-domain error analysis: a heuristic-decision failure has the same diagnostic structure as a motor-habit failure, and remedies for one transfer to the other.

---

## The natural exemplar

[Nordli & Todd (2022)](https://doi.org/10.3389/fpsyg.2022.841972) — peer-reviewed conceptual-analysis article, _Frontiers in Psychology_ — develops the heuristics-as-habits formal equivalence in §6 and §7. The recognition-heuristic worked example draws on the foundational work of [Goldstein & Gigerenzer (2002)](https://doi.org/10.1037/0033-295X.109.1.75) on the _less-is-more_ effect.

The worked example (verbatim source argument): an American student facing a comparison between Japan's two largest cities (Tokyo / Yokohama, both highly recognised) cannot use the recognition heuristic to discriminate — both options are recognised. A comparison between Yokohama / Nagasaki (Yokohama better recognised) succeeds because the heuristic's underlying environmental assumption (recognised = more populous) holds. A comparison between Tokyo / Yokohama fails because the assumption holds for one direction (Tokyo is in fact larger) but the heuristic's discrimination logic doesn't fire — both are recognised.

The failure structure is the source paper's central architectural claim: heuristic-based errors and habit-based errors are _formally indistinguishable_. The ECM equations express both. Cognitive search / decision-making and motor selection / habit formation share substrate (the cortico-basal ganglia-thalamo-cortical loop) and share architectural mechanism (context-overlap-driven action selection from a learned repertoire). The dichotomy between them is descriptive, not architectural.

See [`references.md`](references.md) for full citation chain and computational analogs.

---

## The pattern

**Default dual-process architecture:**

```
    │
    ├──► Type 1 module (fast, heuristic, automatic)
    │        ├── recognition heuristic
    │        ├── take-the-best
    │        └── elimination-by-aspects
    │
    ├──► Type 2 module (slow, deliberative, chunked)
    │        ├── working-memory operations
    │        ├── multi-step reasoning
    │        └── deliberate planning
    │
    └──► Mode-switch logic (when to use which?)
```

**Heuristics-as-habits fusion:**

```
    │
    └──► Unified action-selection mechanism
             B(C) = f(Br, Ba(g, P))
             (drawn from action-selection-as-common-substrate NEXI)
             │
             │   Br is a unified repertoire spanning motor and cognitive ops:
             │     - bᵢ = "press the C key with index finger"  (motor)
             │     - bⱼ = "apply recognition heuristic"           (cognitive)
             │     - bₖ = "execute multi-step plan"               (cognitive)
             │     - bₗ = "grasp the shifter"                    (motor)
             │
             │   Selection logic is the same: context-overlap-driven
             │   competition; chunking happens when reinforcement crosses threshold;
             │   transfer happens when P overlaps across contexts.
             │
             ▼
        Selected behaviour B (motor or cognitive) committed
```

The non-trivial design choice is **how to encode "fastness" or "frugality" in a unified architecture without reverting to two modules**. The answer the source implies: speed and frugality are properties of _which behavioural protocol_ is selected, not properties of _which mechanism_ selected it. A frugal heuristic is a chunked behavioural protocol with low evaluation cost; a deliberative procedure is a longer chunked protocol with higher evaluation cost. Both are entries in the same `Br`.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — components, interfaces, data flow, and integration with the rest of the collection.

In summary, three components:

1. **Unified repertoire `Br`.** A typed structure containing both motor actions and cognitive operations as protocol entries. Each entry has an evaluation-cost annotation (cheap heuristic vs. expensive deliberation) but is otherwise selected via the same mechanism.
2. **Cost-aware competition.** Equation (2) extended to account for evaluation cost — fast / cheap protocols are favoured under tight budgets; deliberative / expensive protocols are favoured under high-stakes commitments. Cost-awareness is a property of the competition function, not a separate Type 1 / Type 2 routing layer.
3. **Cross-domain error-analysis layer.** Failure attribution (from the [`ecological-context-model`](../../ecological-context-model/) NEXI) reports the same structure for heuristic and motor failures: `P_failure` (perception inadequate) / `E_failure` (unobservable goal-relevant difference) / `Ba_failure` (incorrect behavioural association). Cross-domain comparison surfaces remedies that transfer.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for an engineering-agent or runtime decision system:

- **System-prompt fragment** that instructs the agent to treat heuristics and habits as protocol entries in a unified repertoire, selected via the same mechanism.
- **Tool definitions** for `register_protocol_in_repertoire`, `select_protocol_with_cost`, `attribute_protocol_failure`, `cross_domain_error_analysis`.
- **Translation notes** for stack-specific mappings.

---

## When to use

- AI deployments that currently implement dual-process (Type 1 / Type 2) reasoning as separate modules, where unification would simplify architecture.
- Embodied agents that mix motor and cognitive commitments under shared goal stacks.
- Research / engineering work testing whether dual-process architectures can be replaced with single-mechanism architectures.
- Bounded-cognition contexts where the adaptive-toolbox framing (Gigerenzer, Todd) is the natural design lens.
- Cases where cross-domain error analysis (heuristic failures and motor-habit failures with the same diagnostic structure) is valuable for debugging or audit.

## When not to use

- Deployments where Type 1 and Type 2 reasoning are implemented by genuinely different substrates that should remain separate (hardware accelerators for fast paths vs. general-purpose CPUs for deliberative paths).
- Pure-perception or pure-classification systems with no decision-among-alternatives structure.
- Cases where the dual-process architecture is performing well at low cost and unification would add complexity without payoff.
- Cases where the unified-repertoire scoping would force comparison between protocols that shouldn't compete (e.g. routing decisions vs. content-generation decisions).

## Tradeoffs

- **Architectural simplification.** One mechanism replaces two, with a unified repertoire instead of separate modules. Reduces module-boundary complexity but adds repertoire-management complexity.
- **Cross-domain error-analysis capability.** Heuristic failures and motor-habit failures share diagnostic structure; remedies transfer across domains.
- **Loss of dual-process descriptive convenience.** The Type 1 / Type 2 framing is a useful description even when not architecturally load-bearing; users / debuggers may need re-training.
- **Cost-awareness implementation.** The competition function must encode evaluation cost without devolving into a Type 1 / Type 2 router; this is a non-trivial design choice.

In return: simpler architecture, richer error analysis, alignment with the natural-system case, and explicit support for the [`exaptation-architectural-reuse`](../../exaptation-architectural-reuse/) NEXI's cross-domain claims.

## Falsifiable hypothesis

> At matched compute and identical task budgets, AI architectures that unify habit-style and heuristic-style decision-making under a single context-overlap-driven selection mechanism outperform same-budget architectures that implement Type 1 / Type 2 reasoning as separate modules on tasks mixing motor and cognitive commitments. Error patterns should be structurally similar across motor and cognitive domains: when a heuristic fails, the failure signature should match the structure of motor-habit failure — both arising from overlap of `g` and `P` between contexts where `E` differs in goal-relevant ways the agent cannot perceive. A second testable claim: training improvements to the unified selection mechanism should transfer symmetrically across motor and cognitive domains. Refutation: if unified-mechanism systems do not show structurally similar error signatures across domains and do not show symmetric transfer of training improvements, the heuristics-as-habits formal equivalence is empirically weak.

A third testable claim: **lesion experiment robustness on the unified repertoire.** Removing the repertoire's cost-awareness should produce comparable degradation across heuristic-style and habit-style decisions. If degradation is asymmetric, the architecture has not actually unified the two regimes — it has just placed two modules under one wrapper.

## References

See [`references.md`](references.md) — Nordli & Todd (2022) as primary source, plus the foundational ecological-rationality and adaptive-toolbox literature (Gigerenzer, Todd, Goldstein), the dual-process literature (Kahneman, Stanovich), and computational analogs in cognitive architectures and bounded-rationality AI.
