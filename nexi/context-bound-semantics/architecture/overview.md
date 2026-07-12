# Architecture: Context-Bound Semantics

Components, pseudocode, integration notes for context-conditional interpretation — meaning = f(signal, context).

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

The interpretation function is parameterised by the context vector. In order of reliability:

- **FiLM (Feature-wise Linear Modulation)** — context vector produces (γ, β) that modulate decoder activations. Adds only a few parameters; the reliable default.
- **Cross-attention to context** — context tokens attend with the signal at decoder time. Equivalent-shape alternative to FiLM.
- **Mixture of experts gated by context** — context vector routes to one of several specialist decoders. Aspirational: semantic/context routing for MoE is not a solved problem, so prefer FiLM or cross-attention unless routing is demonstrably reliable for your domain.

```
ConditionalDecoder {
  decode(signal_embedding, context_vector) -> meaning_distribution
}
```

The architectural commitment: meaning is a _conditional_ distribution over interpretations given (signal, context), not a marginal distribution over interpretations given signal alone.

---

## Pseudocode

```python
class ContextBoundInterpreter:
    def __init__(self, context_encoder, conditional_decoder):
        self.context_encoder = context_encoder
        self.decoder = conditional_decoder

    def interpret(self, signal, world_state):
        context = self.context_encoder.encode(world_state)
        meaning = self.decoder.decode(signal, context)
        return meaning
```

---

## Integration notes

| Stack              | How to integrate                                                                                                                                                           |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LLM agents**     | The system prompt establishes context; the conditional decoder is the LLM itself, _but_ engineered with explicit context tokens (not just buried in conversation history). |
| **Multi-agent RL** | Context = observation of other agents + environment state. Use FiLM modulation in the policy network.                                                                      |
| **Robotics**       | Context = current task, location, role, goal state. Conditional decoder modulates the perception-to-action pipeline.                                                       |

---

## Performance considerations

- **Function class, not parameter count.** A conditional decoder realises a _larger function class_ than a context-independent one — a family of mappings indexed by context — rather than simply "more parameters." FiLM modulation is cheap per-step: only the modulation parameters (γ, β) add cost, and they are few; the decoder itself is unchanged.
- **Inference latency** rises with context complexity — cache context encodings when context changes slowly.

## Edge cases and failure modes

- **Context drift.** When context changes mid-task, conditional decoders can be slow to adapt. Pair with a context-change detector.
- **Spurious context features.** Conditional decoders can over-fit to incidental context features if training data has narrow contexts. Mitigate with diverse-context augmentation.
- **Missing-context fallback.** When context is unobservable, the conditional decoder should reduce gracefully to a context-marginal interpretation, not fail entirely.
