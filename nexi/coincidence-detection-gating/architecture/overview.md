# Architecture: Coincidence-Detection Gating

This document specifies the architectural primitive for the coincidence-detection-gating pattern — components, interfaces, data flow, and integration with downstream commitment logic.

## Components

### 1. Multi-stream input mux

A wiring layer that brings qualitatively different evidence streams into the gating logic. Streams must be **genuinely independent** in their failure modes — operationally, low cross-stream error correlation, so single-channel error or single-channel adversarial perturbation cannot align them. Two attention heads on the same modality do not qualify; vision + audio + retrieved-context do.

```
mux(streams: list[Stream]) -> StreamCoordinator
```

Design-time decision: which streams. Runtime: the coordinator forwards each stream's evidence to its accumulator.

### 2. Per-stream evidence accumulator

Each stream gets its own accumulator with stream-specific:

- threshold τᵢ (when does this stream count as "active"?)
- coincidence-window Wᵢ (how recent must evidence be?)
- noise model (how reliable is this stream?)
- degradation policy (what does silence mean — uninformative, or stream-down?)

```
accumulator(stream_id, evidence_token, timestamp) -> bool active_now
```

### 3. AND-gate logic with degraded-stream handling

The gate fires when all required streams are simultaneously active within a coincidence window. Critical: graceful degradation when streams become unavailable must **never reduce the gate below two independent streams** — a one-stream "coincidence" is just single-channel gating. If fewer than two required streams are available, the gate holds (or aborts) rather than committing.

```
gate(active_states: dict[stream_id, bool], stream_health: dict[stream_id, Health]) -> CommitDecision
```

Outputs: `commit | hold | abort`. Abort is reserved for inconsistent or adversarial input states.

## Data flow

```
   Stream 1 ────► Accumulator 1 ──┐
   Stream 2 ────► Accumulator 2 ──┼──► AND-gate ──► commit / hold / abort
   ...                            │
   Stream N ────► Accumulator N ──┘
                                  ▲
                                  │
                          Stream-health monitor
                          (graceful degradation)
```

## Pseudocode — runtime gating decision

```python
# Hard floor: a coincidence gate must NEVER operate on fewer than two
# independent streams, or graceful degradation silently makes it single-channel
# — the exact failure this pattern exists to prevent.
MIN_INDEPENDENT_STREAMS = 2

def coincidence_gate(streams, action_proposal):
    # Each stream maintains its own accumulator state
    active_now = {s.id: s.accumulator.is_active(time_now) for s in streams}
    health = {s.id: s.health for s in streams}

    required = action_proposal.required_streams
    available_required = [s for s in required if health[s] != "down"]

    # Degradation must not drop the gate below the two-stream floor.
    quorum = max(MIN_INDEPENDENT_STREAMS, action_proposal.required_quorum)
    if len(available_required) < quorum:
        # Cannot form a genuine coincidence gate — refuse to commit; never
        # fall through to a single available stream.
        return Decision.hold(reason="insufficient independent streams; "
                                    "will not degrade to single-channel")

    # Abort on contradictory / adversarial states: a stream asserts the commit
    # precondition is violated while others assert it holds.
    if any(s.accumulator.contradicts(action_proposal) for s in available_required):
        return Decision.abort(reason="inconsistent / adversarial stream states")

    # AND-gate over available required streams
    if all(active_now[s] for s in available_required):
        return Decision.commit
    else:
        # Partial alignment — hold for more evidence
        unaligned = [s for s in available_required if not active_now[s]]
        return Decision.hold(reason=f"awaiting alignment from {unaligned}")
```

## Integration notes

| Stack                                                 | How to integrate                                                                                                                                                         |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **LLM agent frameworks** (LangGraph, CrewAI, AutoGen) | Place coincidence gate in front of any tool call with side effects. Streams: user-message context, retrieved documents, agent-internal state, observability/log signals. |
| **Multi-modal AI** (vision + audio + text)            | Each modality is a stream. Coincidence-gate before commitment to multi-modal predictions, especially for safety-critical outputs.                                        |
| **MARL / multi-agent RL**                             | Each agent or sub-population is a stream. Coincidence-gate before colony-level behavioural transitions.                                                                  |
| **Robotics / control systems**                        | Sensor channels are streams. Coincidence-gate before irreversible motor commitments.                                                                                     |
| **Production ML** (e.g. fraud detection)              | Multiple independent classifiers as streams. Coincidence-gate before action with high false-positive cost.                                                               |

## Performance and cost considerations

- **Latency.** Coincidence-window logic introduces decision delay. Tune Wᵢ to match the deployment's acceptable latency budget.
- **Stream overhead.** N streams cost N× the input pipeline. For large N, consider hierarchical gating (sub-gates of independent streams feed an outer gate).
- **Adversarial robustness.** Single-channel adversarial perturbation cannot fire the gate alone — coincidence requirement is an inherent defence.

## Interaction with the collection

This NEXI is the **commitment-gate layer** of the [`acerebrate-decision-making`](../../../collections/acerebrate-decision-making/) collection. It composes with:

- [`stochastic-memory-coupling`](../../stochastic-memory-coupling/) — stochastic exploration generates candidate transitions that the coincidence-gate then accepts or rejects based on multi-stream evidence.
- [`meta-regulation`](../../meta-regulation/) — the meta-regulator can dynamically adjust the gate's thresholds and required-stream set in response to deployment-context signals.
