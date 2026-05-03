# Architecture: Context-Bound Semantics

Components, pseudocode, integration notes for context-conditional interpretation and negative-evidence reasoning.

## Components

### 1. Context encoder

A neural module that produces a context vector from the current state of the world, the participants, and any other relevant conditioning signals.

```
ContextEncoder {
  encode(state, participants, time, ...) -> context_vector
}
```

Implementations:

- **Aggregation of feature embeddings** — embed each context attribute, pool.
- **Transformer over context tokens** — when context has structure (multi-turn dialogue, role hierarchies).
- **State-space encoder** — when context evolves over time (RL, robotics).

### 2. Conditional decoder

The interpretation function is parameterised by the context vector. Common implementations:

- **FiLM (Feature-wise Linear Modulation)** — context vector produces (γ, β) that modulate decoder activations.
- **Mixture of experts gated by context** — context vector routes to one of several specialist decoders.
- **Cross-attention to context** — context tokens attend with the signal at decoder time.

```
ConditionalDecoder {
  decode(signal_embedding, context_vector) -> meaning_distribution
}
```

The architectural commitment: meaning is a _conditional_ distribution over interpretations given (signal, context), not a marginal distribution over interpretations given signal alone.

### 3. Negative-evidence module

Maintains expectations about what _should_ be present, and flags deviations.

```
NegativeEvidenceReasoner {
  expected_signals(context) -> set_of_expected_signals
  diff(expected, actual) -> {missing: [...], unexpected: [...]}
  interpret_gap(missing, context) -> meaning_of_absence
}
```

Implementations:

- **Predictive-coding style** — model emits expected next observations; deviations are "prediction error" used for inference.
- **Counterfactual sampling** — sample what _would_ be observed under alternative hypotheses; compare to actual.
- **Explicit expectation table** — for structured contexts, maintain a checklist of expected signals; absences become first-class observations.

---

## Pseudocode

```python
class ContextBoundInterpreter:
    def __init__(self, context_encoder, conditional_decoder, negative_evidence):
        self.context_encoder = context_encoder
        self.decoder = conditional_decoder
        self.neg_ev = negative_evidence

    def interpret(self, signal, world_state):
        context = self.context_encoder.encode(world_state)
        meaning = self.decoder.decode(signal, context)
        # Negative-evidence pass
        expected = self.neg_ev.expected_signals(context)
        gaps = self.neg_ev.diff(expected, [signal])
        if gaps["missing"]:
            absence_meaning = self.neg_ev.interpret_gap(gaps["missing"], context)
            meaning = combine(meaning, absence_meaning)
        return meaning

    def check_absences(self, observed_signals, world_state):
        context = self.context_encoder.encode(world_state)
        expected = self.neg_ev.expected_signals(context)
        return self.neg_ev.diff(expected, observed_signals)
```

---

## Integration notes

| Stack                  | How to integrate                                                                                                                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **LLM agents**         | The system prompt establishes context; the conditional decoder is the LLM itself, _but_ engineered with explicit context tokens (not just buried in conversation history). The negative-evidence module becomes a tool the agent can call. |
| **Multi-agent RL**     | Context = observation of other agents + environment state. Use FiLM modulation in the policy network.                                                                                                                                      |
| **Robotics**           | Context = current task, location, role, goal state. Conditional decoder modulates the perception-to-action pipeline.                                                                                                                       |
| **Diagnostic systems** | Context = patient state, query, history. Negative-evidence module is the most valuable component — many diagnoses turn on what's _not_ present.                                                                                            |

---

## Performance considerations

- **Conditional decoders** can be larger than marginal decoders, but FiLM modulation is cheap per-step (only the modulation parameters add cost; the decoder itself is unchanged).
- **Negative-evidence reasoning** scales with the size of the expected-signal set. For large expectation tables, use sampling or hierarchical decomposition.
- **Inference latency** rises with context complexity — cache context encodings when context changes slowly.

## Edge cases and failure modes

- **Context drift.** When context changes mid-task, conditional decoders can be slow to adapt. Pair with a context-change detector.
- **Spurious context features.** Conditional decoders can over-fit to incidental context features if training data has narrow contexts. Mitigate with diverse-context augmentation.
- **Missing-context fallback.** When context is unobservable, the conditional decoder should reduce gracefully to a context-marginal interpretation, not fail entirely.
- **Hallucinated absences.** Negative-evidence reasoning can imagine missing signals where none were expected. Calibrate the expectation table.
