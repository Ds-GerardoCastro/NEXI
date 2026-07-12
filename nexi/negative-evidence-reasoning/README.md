# Negative-Evidence Reasoning

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Member of collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
>
> _Information carried by the **absence** of an expected signal — the dog that didn't bark. Treat expected-but-missing signals, and negation, as first-class evidence rather than gaps in perception._

---

## At a glance

Most models weight what is present. A token that appears raises the probability of related tokens; a feature that fires contributes to the output. What is _not_ present contributes nothing. For a large class of tasks that is exactly wrong: the diagnostic information lives in the signal that was expected and did not arrive.

This NEXI argues for one capability: **reasoning from absence**. A system should

1. maintain explicit **expectations** about what should be present in a given context,
2. **detect deviations** — what is missing, and what is unexpectedly present, and
3. **interpret the gap** — treat an expected-but-missing signal as evidence, and treat negation as truth-reversing rather than as a near-synonym of the un-negated statement.

It was originally packaged as a leg of [Context-Bound Semantics](../context-bound-semantics/); it is split out here because it targets a **different documented AI gap** — the insensitivity of language models to negation and absence — and deserves separate validation.

| Question          | Short answer                                                                                                        |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Use this when** | The answer turns on what is missing or negated: anomaly detection, diagnosis, security, negation-heavy language.    |
| **Skip it when**  | You cannot characterise what should be present; missing and merely-unobserved are indistinguishable; tight latency. |
| **What it adds**  | Absence as evidence; negation handled as truth-reversing; robustness where present-token models are blind.          |
| **What it costs** | An expectation model to build, calibrate, and diff; extra inference compute; a hallucinated-absence failure mode.   |

---

## The natural exemplar

In many territorial songbirds, dawn song is strongly tied to territory defence and shows a pronounced dawn peak. In wild zebra finches, the source paper reports **no dawn-song peak**, and reads that missing peak as consistent with a non-territorial social system.

The point is that the distinguishing observation is an _absence_. Nothing was heard at dawn — and the fact that nothing was heard, against an expectation set by related species, is what carries the information. A pipeline that only scored the songs that _were_ produced would have no place to put this evidence.

> **Exemplar status.** Hagedoorn et al. (2025) is an **unrefereed bioRxiv preprint** and is **observational**. It functions here as a _natural analog_ of reasoning-from-absence, not as empirical support for the ML hypothesis below — that hypothesis is grounded in the negation-probing literature on language models and is tested on its own terms.

---

## The documented AI need

This is not a speculative capability gap. Pretrained language models are largely **insensitive to negation** and do not represent what is not true:

- **Ettinger (2020)** shows BERT predicts nearly the same completions for _"A robin is a [MASK]"_ and its negation, and that the model's expectations are barely perturbed by the word _not_ — it fails to use negation to reverse its predictions.
- **Kassner & Schütze (2020)** show pretrained models frequently assign _higher_ probability to the **false** completion of a negated statement (e.g. treating _"Birds cannot [MASK]"_ much like _"Birds can [MASK]"_), on their negated-LAMA probes.

Both are published evidence that reasoning-from-absence / negation is an **unmet need** in current systems, and both give a concrete, named benchmark to test against. The same blind spot underlies a familiar failure: models **over-generate** and **hallucinate** because "I have no evidence for this" is not a state they naturally represent — absence of support does not lower their confidence the way presence of support raises it.

---

## The pattern

```
             Context                     Actual observations
                │                                │
                ▼                                │
    ┌───────────────────────┐                    │
    │  Expectation model     │                    │
    │  expected_signals(ctx) │                    │
    └───────────────────────┘                    │
                │                                │
                ▼                                ▼
          expected set  ─────►  ┌────────────────────────────┐
                                │  Deviation detector        │
                                │  diff(expected, actual)     │
                                │   -> {missing, unexpected}  │
                                └────────────────────────────┘
                                             │
                                             ▼
                                ┌────────────────────────────┐
                                │  Gap interpreter           │
                                │  interpret_gap(missing,ctx) │
                                └────────────────────────────┘
                                             │
              present-signal evidence        │  absence evidence
                        └──────────┬──────────┘
                                   ▼
                        ┌────────────────────────┐
                        │  Fusion operator        │
                        │  log-linear combine()   │
                        └────────────────────────┘
                                   │
                                   ▼
                     Meaning including what is missing
```

The architectural commitment: absence is scored, not skipped. The fusion operator adds an **evidence term for expected-but-missing signals** to the present-signal evidence, inside a single log-linear meaning model — so a missing signal can move the answer just as a present one can.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md).

- **Expectation model** `expected_signals(context)` — what should be present here, each with an expected-presence probability.
- **Deviation detector** `diff(expected, actual) -> {missing, unexpected}`.
- **Gap interpreter** `interpret_gap(missing, context)` — the meaning an absence carries.
- **Fusion operator** `combine(...)` — additive log-likelihood combination of present-signal and absence evidence in a log-linear model (specified concretely, not a black box).
- **Hallucinated-absence guard** — abstain from asserting an absence unless the expected-presence probability clears a **calibrated threshold**, with the expectation model calibrated on held-out data.

## Skill specification

See [`skill/skill.md`](skill/skill.md).

- **System-prompt fragment** instructs the agent to reason explicitly about what should be present and isn't, and to treat negation as truth-reversing.
- **Tool** `check_for_absences(expected_signals, actual_observations)` returns `{missing, unexpected, interpretation}`.

---

## When to use it

- ✅ Anomaly / fault detection — the missing heartbeat, the log line that never arrived.
- ✅ Diagnostic reasoning — absent findings rule diagnoses in or out (medical, root-cause).
- ✅ Security monitoring — the absence of an expected authentication step is the alarm.
- ✅ Negation-heavy language — instructions, policies, and constraints phrased as what is _not_ allowed or _not_ true.

## When not to use it

- ❌ You cannot characterise the expected-signal set — absence then carries no information.
- ❌ Observation is so incomplete that _missing_ and _merely unobserved_ can't be told apart.
- ❌ Strict latency budgets that preclude maintaining and diffing an expectation model.

---

## Theoretical background & evidence

The **documented AI need** is negation insensitivity in pretrained language models: **Ettinger (2020)** and **Kassner & Schütze (2020)** are the real, published evidence that reasoning-from-absence is unmet, and they supply the named benchmark (the negated-LAMA probes) this NEXI is validated against.

The **mechanistic substrate** comes from two lines of work:

- **Predictive coding / prediction-error** (Friston 2010): a system emits explicit predictions of what it expects to observe, and treats the deviation (prediction error) as the signal. Noticing what is not there is functionally identical to a large prediction error on an expected-but-absent observation.
- **Counterfactual reasoning** (Pearl 2009): interpreting an absence requires asking what _would_ have been observed under alternative hypotheses, and comparing that to what actually was — the structure of a counterfactual query.

The animal-communication literature supplies the natural analog (Snijders & Naguib 2017; Hagedoorn et al. 2025 — preprint, observational).

Full citations: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H_absence.** Architectures with explicit expectation machinery plus a deviation/negation-handling operator outperform baselines that weight only present tokens, at equal training compute, on tasks whose answer turns on negation or absence.
>
> **Operationalisation (pre-registered).** On the **negated-LAMA probes of Kassner & Schütze (2020)** — where pretrained models assign higher probability to the false completion of negated statements — an expectation-plus-deviation model should reduce the **negation error rate** (share of negated probes where the false completion outscores the true one) by **≥20% relative** to a matched-compute baseline that only weights present tokens. A negation NLI set (contradiction detection over negated premise/hypothesis pairs) may serve as a second bound with the same ≥20% relative error-reduction target.
>
> **Refutation.** If the present-token baseline of matched compute equals the expectation model on that pre-registered negation split, this pattern's claim is refuted.

---

## Tradeoffs

- **Enumeration cost.** Reasoning about what is not there means enumerating or sampling expected signals — more expensive than scoring present tokens.
- **Calibration burden.** The expectation model must be calibrated on held-out data or it fabricates absences.
- **Sensitivity vs. hallucination.** A more-sensitive expectation model finds more diagnostic gaps but also imagines more; the abstention threshold sets this trade-off and is deployment-specific.

## Boundary conditions

This NEXI specifies reasoning from **absence and negation**. It does not specify how the context that sets expectations is acquired, nor how the same present signal is interpreted across contexts — that is the job of its sibling [Context-Bound Semantics](../context-bound-semantics/). The two are complementary: context fixes what a present signal means; this pattern handles the signal that isn't there.

---

## Related

- **Collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
- **Sibling (split from):** [`context-bound-semantics`](../context-bound-semantics/) — context fixes the meaning of present signals; this pattern handles absence and negation.
- **Co-dependent NEXIs:** [`eavesdropping`](../eavesdropping/), [`identity-by-pattern`](../identity-by-pattern/), [`multi-modal-integration`](../multi-modal-integration/), [`social-hotspots`](../social-hotspots/)
- **Vault provenance (private):** principle `P08`; metamodel `MM3 — Context-Bound Semantics`.
- **References:** [`references.md`](references.md)
