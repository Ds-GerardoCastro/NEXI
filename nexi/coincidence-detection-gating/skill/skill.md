# Skill: Coincidence-Detection Gating (framework-neutral)

A drop-in **runtime decision-gating** skill for AI agents that need to commit to costly or irreversible actions only when multiple independent context streams agree. Framework-neutral — see translation notes for stack-specific mappings.

> **Skill kind:** `runtime` (with design-time configuration of which streams to gate on). Used during inference, not just at architecture-design time.

---

## System-prompt fragment

Insert into the system or developer prompt of any agent that should apply coincidence-detection gating before committing to costly actions:

```
Before committing to any action whose effects are costly to reverse —
external API calls with side effects, write operations to user data,
multi-step plans with no rollback, mode changes with setup overhead —
require evidence from MULTIPLE INDEPENDENT context streams to align.

A single signal is insufficient. Specifically:

  1. Identify the action's commitment cost. If reversible at low cost,
     proceed. If costly to reverse, apply coincidence gating.
  2. Identify QUALITATIVELY DIFFERENT context streams that bear on the
     decision. Two attention reads of the same input do not qualify;
     genuine streams are e.g. user-message + retrieved-context +
     observability/log signals.
  3. For each stream, check whether the evidence supports the action.
     A stream supports the action only if its accumulated evidence
     crosses the stream-specific threshold within a recent window.
  4. Commit only when ALL required streams support. Otherwise, hold
     for more evidence or take a non-committal alternative action.
  5. If a required stream is consistently unavailable, fall back to
     the deployment-defined degraded-stream policy. Do not block
     forever; do not commit on partial evidence either.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: register_evidence_stream
    description: >
      Register a context stream as a required input to coincidence gating.
      Streams must be qualitatively independent in failure modes.
    parameters:
      stream_id: string
      description: string
      threshold: number # τ — when does this stream count as "active"?
      coincidence_window_ms: number
      degraded_policy: enum [hold, fallback_action, abort]

  - name: accumulate_evidence
    description: >
      Update one stream's evidence accumulator with a fresh observation.
    parameters:
      stream_id: string
      evidence_token: any
      timestamp_ms: number

  - name: check_coincidence_gate
    description: >
      Test whether all required streams are currently active within the
      coincidence window. Returns commit / hold / abort.
    parameters:
      action_id: string
      required_streams: list[string]
    returns:
      decision: enum [commit, hold, abort]
      rationale: string
      missing_streams: list[string] # if hold, which are not yet aligned

  - name: degraded_stream_handler
    description: >
      Apply the deployment-defined degraded-stream policy when a required
      stream is unavailable.
    parameters:
      action_id: string
      unavailable_streams: list[string]
    returns:
      action: enum [hold, fallback, abort]
      fallback_action: any | null
```

---

## Memory pattern

Per-action gating state persists across decision calls within a session:

```yaml
gating_state:
  - action_id: <id>
    required_streams: [<stream_id>, ...]
    accumulators:
      <stream_id>:
        recent_evidence: <list>
        active: <bool>
        last_active_ts: <ms>
    decision_history:
      - timestamp: <ms>
        decision: <commit|hold|abort>
        active_at_decision: <list>
```

This state is what allows lesion experiments — removing a stream from `required_streams` should produce measurable degradation if the stream is load-bearing.

---

## Translation notes

| Stack                             | Mapping                                                                                                                                                      |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Claude skills**                 | `~/.claude/skills/coincidence-gate/SKILL.md`. Tools become Claude tool definitions. The system-prompt fragment goes in `system_prompt_addition`.             |
| **OpenAI function calling**       | Tools become OpenAI function schemas. The system-prompt fragment is concatenated to the agent's `system` message.                                            |
| **MCP tools**                     | Each tool becomes an MCP `tool.json`. State persistence handled by the MCP server's session storage.                                                         |
| **LangChain / LangGraph**         | Tools become `Tool` objects. The gate sits as a conditional edge before any side-effect-producing node.                                                      |
| **MARL frameworks** (Mava, RLlib) | Coincidence gate sits before the population-level coordinated-action commit step. Streams are different agent populations or different observation channels. |

---

## Evaluation signals (falsifiable claims)

The skill's gates should pass these falsification tests:

1. **Multi-stream gates outperform single-stream baselines on irreversible-action tasks.** At matched cost, agents using the gate should show ≥20% reduction in premature-commitment rate vs single-channel baselines.
2. **Lesion experiment robustness.** Removing one required stream should produce measurably worse outcomes than removing equivalent compute from any other layer. If not, that stream wasn't load-bearing — the gate was effectively single-channel.
3. **Adversarial single-channel robustness.** A targeted perturbation of only one input stream should not fire the gate alone. If it does, the gate's coincidence requirement is not enforced.
4. **Graceful degradation under stream loss.** When one required stream becomes consistently unavailable, the deployment's defined degraded-policy should activate rather than the gate blocking forever.

---

## Examples

Working examples will be added under [`examples/`](examples/) as the catalog matures.

## See also

- Pattern README: [`../README.md`](../README.md)
- Architecture: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Collection: [`../../clusters/acerebrate-decision-making/`](../../../clusters/acerebrate-decision-making/)
