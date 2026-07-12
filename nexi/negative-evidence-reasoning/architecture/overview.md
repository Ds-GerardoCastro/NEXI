# Architecture: Negative-Evidence Reasoning

Components, pseudocode, and integration notes for treating expected-but-missing signals — and negation — as first-class evidence.

## Components

### 1. Expectation model

Produces, for a given context, the set of signals that _should_ be present, each with an expected-presence probability.

```
ExpectationModel {
  expected_signals(context) -> [{signal, p_present, weight}]
}
```

`p_present` is the model's calibrated probability that this signal is present given the context; `weight` is how much its presence/absence should move the downstream meaning. Implementations:

- **Predictive-coding style** — the model emits expected next observations; anything predicted with high `p_present` but not observed becomes a large prediction error.
- **Counterfactual sampling** — sample what _would_ be observed under the leading hypotheses; signals that appear across samples but not in reality are candidate absences.
- **Explicit expectation table** — for structured contexts, a checklist of expected signals with per-context presence rates estimated from data.

The expectation model **must be calibrated on held-out data**: `p_present` has to mean what it says, or the deviation detector will invent absences.

### 2. Deviation detector

Diffs the expected set against what was actually observed.

```
DeviationDetector {
  diff(expected, actual) -> {missing: [...], unexpected: [...]}
}
```

`missing` = expected signals with high `p_present` that were not observed. `unexpected` = observed signals that the expectation model did not predict. Both are evidence; the missing set is the negative evidence this pattern is named for.

### 3. Gap interpreter

Assigns meaning to an absence.

```
GapInterpreter {
  interpret_gap(missing, context) -> [{absent_signal, implication, log_evidence}]
}
```

For each confidently-missing signal it returns the implication of that absence and a signed **log-evidence** term (how much, and in which direction, the absence shifts the meaning). Negation is handled here as a special case: a negated proposition flips the sign of the evidence its affirmative form would contribute, rather than contributing a near-identical vector.

### 4. Fusion operator (`combine`) — specified concretely

`combine()` is **not** a black box. Meaning is scored in a single **log-linear model**: the unnormalised score of a candidate meaning `m` is a sum of evidence terms, and present-signal evidence and absence evidence enter as **additive log-likelihood terms** on equal footing.

For candidate meaning `m`, context `c`, present signals `S⁺`, and confidently-missing signals `S⁻`:

```
score(m) =  Σ_{s ∈ S⁺}  w_s · log p(s | m, c)                 # present-signal evidence
          + Σ_{a ∈ S⁻}  gate(a) · w_a · log p(¬a | m, c)      # absence evidence
          + log prior(m | c)

p(m | c, S⁺, S⁻) = softmax_m ( score(m) )
```

Each absent signal `a` contributes `log p(¬a | m, c)` — the log-likelihood that, _if_ meaning `m` held, signal `a` would be absent. A meaning under which `a` should have appeared is penalised exactly as strongly as a present signal that is inconsistent with `m` is penalised. `gate(a) ∈ {0,1}` is the hallucinated-absence guard (below). Presence and absence are thus the same kind of evidence — log-likelihood terms — differing only in sign of the observed variable, which is precisely the additive, log-linear property that lets an absence move the answer as much as a presence.

Minimal pseudocode:

```python
def combine(candidate_meanings, context, present, missing, gate, prior):
    scores = {}
    for m in candidate_meanings:
        s = math.log(prior(m, context))
        for sig in present:                       # present-signal evidence
            s += sig.weight * loglik_present(sig, m, context)
        for a in missing:                         # absence evidence, gated
            if gate(a, context):                  # only confident absences count
                s += a.weight * loglik_absent(a, m, context)
        scores[m] = s
    return softmax(scores)                         # normalised meaning distribution
```

`loglik_absent(a, m, context)` returns `log p(¬a | m, context)`: high (near 0) when `m` implies `a` should be absent, very negative when `m` implies `a` should have been present.

### 5. Hallucinated-absence guard

The dominant failure mode: **inventing absences** — asserting a signal is meaningfully missing when it was merely never expected, or was unobserved rather than absent. The mitigation is a real mechanism, not "just calibrate the table":

```
gate(a, context):
    return  expectation_model.p_present(a, context) >= tau
            and observation_is_complete_for(a, context)
```

- **Abstention threshold `tau`.** An absence is only admitted as evidence when the calibrated expected-presence probability `p_present(a, context)` clears `tau`. Below `tau`, `gate` returns 0 and the term drops out entirely — the system abstains from reading meaning into that gap.
- **Held-out calibration.** `tau` is chosen on a held-out calibration set to hit a target false-absence rate (e.g. reliability-diagram / temperature-scaling calibration of `p_present`, then pick `tau` at the operating point where admitted absences are correct at the required precision). Because `p_present` is calibrated, `tau` has a stable meaning across contexts.
- **Observation-completeness check.** `observation_is_complete_for` refuses to treat _unobserved_ as _absent_ when the channel that would carry `a` was not actually monitored — the missing/merely-unobserved distinction the pattern depends on.

This guard is the direct tie-in to **LLM hallucination / over-generation**: models over-assert precisely because "absence of support" is not represented. Gating absence evidence on a calibrated expected-presence threshold gives the system a principled way to say "nothing here" instead of confabulating.

---

## Pseudocode (end to end)

```python
class NegativeEvidenceReasoner:
    def __init__(self, expectation_model, deviation_detector, gap_interpreter,
                 tau, prior):
        self.expect = expectation_model
        self.deviate = deviation_detector
        self.interpret = gap_interpreter
        self.tau = tau
        self.prior = prior

    def gate(self, a, context):
        return (self.expect.p_present(a, context) >= self.tau
                and self.expect.observation_complete(a, context))

    def reason(self, candidate_meanings, actual_observations, context):
        expected = self.expect.expected_signals(context)
        dev = self.deviate.diff(expected, actual_observations)   # {missing, unexpected}
        missing = self.interpret.interpret_gap(dev["missing"], context)
        return combine(candidate_meanings, context,
                       present=actual_observations,
                       missing=missing,
                       gate=lambda a: self.gate(a, context),
                       prior=self.prior), dev

    def check_absences(self, actual_observations, context):
        expected = self.expect.expected_signals(context)
        dev = self.deviate.diff(expected, actual_observations)
        dev["missing"] = [a for a in dev["missing"] if self.gate(a, context)]
        return dev
```

---

## Integration notes

| Stack                  | How to integrate                                                                                                                                                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **LLM agents**         | The expectation model is a prompt/tool that lists what should be present in the current context; the deviation detector and gap interpreter become the `check_for_absences` tool. Negation handling is a prompt rule: treat "not" as truth-reversing, never as a near-synonym. |
| **Multi-agent RL**     | Expected observations come from the world model; missing expected observations feed an auxiliary prediction-error signal into the value/policy head.                                                                                                                           |
| **Anomaly detection**  | The expectation model is the baseline of normal behaviour; `diff` yields the anomaly (missing heartbeat, absent log line). This is the highest-value setting — the alarm _is_ the absence.                                                                                     |
| **Diagnostic systems** | Expected findings per hypothesis form the expectation set; absent findings rule hypotheses in or out via the `loglik_absent` term. Calibrated `tau` prevents over-reading incidental gaps.                                                                                     |

---

## Performance considerations

- **Enumeration cost** scales with the expected-signal set. Use sampling or hierarchical decomposition of `expected_signals` for large sets.
- **Caching.** When context changes slowly, cache `expected_signals(context)` and its `p_present` values.
- **The `combine` step is cheap** — it is a weighted sum of log-likelihoods over candidate meanings; cost is dominated by producing `expected_signals` and the per-signal likelihoods.

## Edge cases and failure modes

- **Hallucinated absences.** The headline failure: reading meaning into a gap that was never expected or was merely unobserved. Mitigated by the `gate` (calibrated `tau` + observation-completeness), **not** by hand-editing the expectation table. Note the direct tie to LLM over-generation / hallucination.
- **Miscalibrated expectations.** If `p_present` is not calibrated, `tau` loses its meaning. Recalibrate on held-out data whenever the deployment distribution shifts.
- **Missing vs. unobserved.** Never let an unmonitored channel masquerade as an informative absence — the observation-completeness check exists for exactly this.
- **Double-counting.** A signal that is both "unexpected present" and semantically the negation of an expected one must be counted once; deduplicate `unexpected` against `missing` before fusion.
