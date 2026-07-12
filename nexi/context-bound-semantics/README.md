# Context-Bound Semantics

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Member of collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
>
> _Meaning as a function of signal × context. Architectures that bind interpretation to the current setting can capture semantics that pure pattern-statistics models can miss._

---

## At a glance

Token-statistical models bind meaning to co-occurrence: a word means what it usually appears near. This works for many tasks. It can miss the cases where **the same signal means different things in different settings**.

This NEXI argues for one core capability:

1. **Context-conditional interpretation** — decode signal meaning given the current state of the world, the participants, and the role of the signal in that setting. Meaning = f(signal, context).

| Question          | Short answer                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| **Use this when** | Same signal carries different meaning in different contexts; pragmatics matter.                            |
| **Skip it when**  | Signals have stable context-independent meaning; tight latency budgets; context isn't reliably observable. |
| **What it adds**  | Pragmatic interpretation; robustness to context shift.                                                     |
| **What it costs** | A larger function class to fit; harder training-data curation; conditional reasoning compute.              |

---

## The natural exemplar

From the zebra finch source paper: the **same song appears to serve different functions across social contexts**. In the breeding colony the authors suggest song may primarily reinforce pair bonds and act as reproductive cues; at the social hotspot they suggest it might have a wider social trigger, potentially coordinating breeding. The signal is the same; its interpreted function shifts with context — it cannot be read off the signal alone. ("Function" is the paper's term; where this NEXI says "meaning" it is an interpretive gloss on that function, not a source quote.)

This is a single observational study — an **unrefereed bioRxiv preprint** — and serves as a natural analog for context-conditional interpretation, not as empirical support for the machine-learning hypothesis below.

---

## The pattern

```
                     Signal observation
                            │
       ┌────────────────────┴────────────────────┐
       │                                         │
       ▼                                         ▼
  Current state                            Participants
  (where, when)                            (who, roles)
       │                                         │
       └─────────────────────┬───────────────────┘
                             ▼
                   ┌──────────────────┐
                   │ Context encoder  │
                   │ (settings, roles)│
                   └──────────────────┘
                             │
                             ▼
              ┌────────────────────────────────┐
              │   Conditional decoder          │
              │   meaning = f(signal, context) │
              └────────────────────────────────┘
                             │
                             ▼
                   Context-bound meaning
```

The architectural commitment is that the decoder is _parameterised by context_, not by signal alone.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md).

- **Context encoder** producing a representation of the current setting, participants, and constraints.
- **Conditional decoder** that maps signal × context → meaning. FiLM-style modulation or cross-attention to context is the reliable default; context-gated mixture-of-experts is aspirational, since semantic/context routing for MoE is not a solved problem.

## Skill specification

See [`skill/skill.md`](skill/skill.md).

- **System-prompt fragment** instructs the agent to interpret signals conditionally on context.
- **Tool** `interpret_signal(signal, context)` returns context-bound meaning with confidence.

---

## When to use it

- ✅ Multi-domain or multi-context agents (the same word, file, or signal means different things across contexts).
- ✅ Pragmatic dialogue (politeness, irony, indirection, role-bound speech).
- ✅ Multi-agent settings where the same message has different meaning depending on who's involved.

## When not to use it

- ❌ Stable-semantics tasks (most classification, most code).
- ❌ Strict latency budgets — conditional reasoning costs.
- ❌ Settings where context isn't reliably observable.

---

## Theoretical background & evidence

The pattern connects to **pragmatics in linguistics** (Grice 1975; Rational Speech Acts framework, Goodman & Frank 2016), where meaning is interpreted conditional on speaker, listener, and situation rather than read off the literal signal. The animal-communication literature offers a natural analog for context-conditional signal function in non-human cognition (Snijders & Naguib 2017; Hagedoorn et al. 2025 — an unrefereed, observational bioRxiv preprint, cited as analog rather than as empirical support for the ML hypothesis).

A specific computational instantiation: **conditional decoders with FiLM (Feature-wise Linear Modulation; Perez et al. 2018)** modulate the decoder's activations as a function of context, achieving the architectural shape this NEXI specifies, while adding only a small number of parameters. Cross-attention to context is an equivalent-shape alternative.

Full citations: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H_context.** Architectures with explicit context-conditional decoders outperform context-independent baselines on tasks where semantic interpretation shifts across contexts, at equal training compute.
>
> **Operationalisation.** On a named, pre-registered, compute-matched pragmatic-implicature / context-shift NLU benchmark and split (e.g. an RSA-derived implicature suite or a dialogue-with-implicature benchmark, with the split fixed in advance), context-conditional decoders should achieve ≥10% relative gain on that benchmark's context-shift metric at equal compute.
>
> **Refutation.** If a context-independent baseline of matched compute equals the context-conditional model on that pre-registered context-shift split, this pattern's claim is refuted.

---

## Tradeoffs

- **Function class.** A conditional decoder realises a larger _function class_ than a context-independent one — a family of input-output mappings indexed by context. This is expressive power, not raw parameter count: a FiLM-style modulation adds only a few parameters.
- **Data curation.** Training data must include the same signal in multiple contexts, with context labels. This is harder than i.i.d. sampling.
- **Routing is unsolved for MoE.** Context-gated mixture-of-experts is attractive but semantic/context routing is not a solved problem; prefer FiLM-style modulation or cross-attention and treat MoE routing as aspirational.

## Boundary conditions

This NEXI specifies _interpretation_ of signals conditional on context. It does not specify _how to acquire_ the context representation — that depends on perception (modalities), identity tracking, and world-model state. The collection of which this is a member ([Distributed Social Cognition](../../collections/distributed-social-cognition/)) addresses those upstream concerns. Reasoning from what is NOT observed is handled by the sibling NEXI [`negative-evidence-reasoning`](../negative-evidence-reasoning/).

---

## Related

- **Collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
- **Sibling NEXI:** [`negative-evidence-reasoning`](../negative-evidence-reasoning/) — reasoning from what is NOT observed.
- **Co-dependent NEXIs:** [`eavesdropping`](../eavesdropping/), [`identity-by-pattern`](../identity-by-pattern/), [`multi-modal-integration`](../multi-modal-integration/), [`social-hotspots`](../social-hotspots/)
- **Vault provenance (private):** principle `P07`; metamodel `MM3 — Context-Bound Semantics`.
- **References:** [`references.md`](references.md)
