# Context-Bound Semantics

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Member of collection:** [Distributed Social Cognition](../../clusters/distributed-social-cognition/)
>
> _Meaning as a function of signal × context. Architectures that bind interpretation to context — and reason from what's **not** observed — capture semantics that pure pattern-statistics models miss._

---

## At a glance

Token-statistical models bind meaning to co-occurrence: a word means what it usually appears near. This works for many tasks. It fails for the cases where **the same signal means different things in different settings**, and for cases where **meaning is inferable from absence** as much as from presence.

This NEXI argues for two related capabilities:

1. **Context-conditional interpretation** — decode signal meaning given the current state of the world, the participants, and the role of the signal in that setting.
2. **Negative-evidence reasoning** — derive information from what's _not_ there. The dog that didn't bark.

| Question          | Short answer                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| **Use this when** | Same signal carries different meaning in different contexts; absences are diagnostic; pragmatics matter.   |
| **Skip it when**  | Signals have stable context-independent meaning; tight latency budgets; context isn't reliably observable. |
| **What it adds**  | Pragmatic interpretation; negative-evidence reasoning; robustness to context shift.                        |
| **What it costs** | Larger conditional decoders; harder training-data curation; conditional reasoning compute.                 |

---

## The natural exemplar

Two principles from the zebra finch source paper combine here:

- **Same song, different function** (P07): zebra finch song serves _pair-bond reinforcement and reproductive cueing_ in a breeding colony, but _broader social bonding and breeding synchronisation_ in a social hotspot. The same signal — different meaning, conditional on social context.
- **Function inferred from absence** (P08): the _lack_ of a dawn-song peak distinguishes this non-territorial species from territorial ones. What isn't there is diagnostic.

Both are forms of context-binding: the meaning of the signal (or its absence) cannot be read off the signal alone.

---

## The pattern

```
                     Signal observation
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
       ▼                    ▼                    ▼
  Current state       Participants          Expected baseline
  (where, when)       (who, roles)          (what should be there)
       │                    │                    │
       └─────────┬──────────┴──────────┬─────────┘
                 ▼                     ▼
       ┌──────────────────┐   ┌─────────────────────┐
       │ Context encoder  │   │  Negative-evidence  │
       │ (settings, roles)│   │  reasoner           │
       └──────────────────┘   └─────────────────────┘
                 │                     │
                 ▼                     ▼
       ┌────────────────────────────────────────┐
       │   Conditional decoder                  │
       │   meaning = f(signal, context, gaps)   │
       └────────────────────────────────────────┘
                            │
                            ▼
                   Context-bound meaning
```

The architectural commitment is that the decoder is _parameterised by context_, not by signal alone — and that the system explicitly reasons about _what should be present and isn't_.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md).

- **Context encoder** producing a representation of the current setting, participants, and constraints.
- **Conditional decoder** that maps signal × context → meaning. Implementations range from FiLM-style modulation to mixture-of-experts gated by context.
- **Negative-evidence module** that maintains explicit expectations and flags deviations.

## Skill specification

See [`skill/skill.md`](skill/skill.md).

- **System-prompt fragment** instructs the agent to interpret signals conditionally on context and to reason about absences explicitly.
- **Tool** `interpret_signal(signal, context)` returns context-bound meaning with confidence.
- **Tool** `check_for_absences(expected_signals, actual_observations)` returns gaps that may be diagnostic.

---

## When to use it

- ✅ Multi-domain or multi-context agents (the same word, file, or signal means different things across contexts).
- ✅ Pragmatic dialogue (politeness, irony, indirection, role-bound speech).
- ✅ Diagnostic systems where missing data is informative (medical, security, anomaly detection).
- ✅ Multi-agent settings where the same message has different meaning depending on who's involved.

## When not to use it

- ❌ Stable-semantics tasks (most classification, most code).
- ❌ Strict latency budgets — conditional reasoning costs.
- ❌ Settings where context isn't reliably observable.

---

## Theoretical background & evidence

The pattern connects to **pragmatics in linguistics** (Grice 1975; Rational Speech Acts framework, Goodman & Frank 2016) and to **counterfactual reasoning in machine learning** (Pearl 2009; conditional generative modelling). The animal-communication literature provides empirical grounding for context-conditional signal function in non-human cognition (Snijders & Naguib 2017; Hagedoorn et al. 2026).

A specific computational instantiation: **conditional decoders with FiLM (Feature-wise Linear Modulation; Perez et al. 2018)** modulate the decoder's parameters as a function of context, achieving the architectural shape this NEXI specifies.

For negative-evidence reasoning: **prediction-error / surprise architectures** (predictive coding; Friston 2010) maintain explicit expectations and react to deviations, which is functionally equivalent to noticing what isn't there.

Full citations: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H_context.** Architectures with explicit context-conditional decoders and negative-evidence reasoning capacity outperform context-independent baselines on tasks where semantic interpretation shifts across contexts, at equal training compute.
>
> **Operationalisation.** On benchmarks of pragmatic language understanding (RSA-derived tasks, dialogue with implicature), context-shifted classification, and counterfactual reasoning, context-bound architectures should achieve ≥10% relative gain on context-shift metrics at equal compute.
>
> **Refutation.** If context-independent baselines match context-conditional ones at equal compute on explicitly context-shifted evaluations, this pattern's claim is refuted.

---

## Tradeoffs

- **Effective capacity.** A conditional decoder spans a richer space of input-output mappings than a marginal decoder; larger effective parameter count.
- **Data curation.** Training data must include the same signal in multiple contexts, with context labels. This is harder than i.i.d. sampling.
- **Negative-evidence cost.** Reasoning about what's not there requires enumerating or sampling expected baselines — additional compute at inference.

## Boundary conditions

This NEXI specifies _interpretation_ of signals conditional on context. It does not specify _how to acquire_ the context representation — that depends on perception (modalities), identity tracking, and world-model state. The collection of which this is a member ([Distributed Social Cognition](../../clusters/distributed-social-cognition/)) addresses those upstream concerns.

---

## Related

- **Collection:** [Distributed Social Cognition](../../clusters/distributed-social-cognition/)
- **Co-dependent NEXIs:** [`eavesdropping`](../eavesdropping/), [`identity-by-pattern`](../identity-by-pattern/), [`multi-modal-integration`](../multi-modal-integration/), [`social-hotspots`](../social-hotspots/)
- **Vault provenance (private):** principles `P07`, `P08`; metamodel `MM3 — Context-Bound Semantics`.
- **References:** [`references.md`](references.md)
