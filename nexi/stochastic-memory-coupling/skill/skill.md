# Skill: Stochastic-Memory Coupling (framework-neutral)

A drop-in **runtime decision-making** skill for AI agents that must make decisions under environmental unpredictability. Couples stochastic state-switching with persistent memory of which states proved beneficial.

> **Skill kind:** `runtime` (state, memory, and decisions are runtime constructs). Used during inference.

---

## System-prompt fragment

```
When making decisions under environmental unpredictability, do NOT collapse
to a fixed policy or a memoryless random walk. Instead, maintain BOTH
of the following at runtime:

  1. A discrete set of behavioural STATES, each with its own action policy.
  2. A persistent MEMORY of which states have proven beneficial in
     conditions resembling the current one.

Decision logic:

  - Identify your current state. Apply its policy to produce an action.
  - Observe the outcome.
  - RECORD the outcome in the persistent memory under the current state.
  - When deciding the next state, sample STOCHASTICALLY (do not just
     pick the historically-best state) but BIAS the sampling toward
     states with high memory scores in conditions like the present.
  - Tune the bias parameter β:
      * If transitions become deterministic toward one state → reduce β
        to restore exploration.
      * If transitions stay uniformly random → increase β to give
        memory more weight.

Both components are load-bearing. Stochasticity alone is noise; memory
alone is rigid. The COUPLING is the design.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: register_state_space
    description: >
      Define the discrete set of behavioural states the agent can be in,
      with each state's action policy.
    parameters:
      states: list[{id, description, policy_spec}]

  - name: record_state_outcome
    description: >
      Update persistent memory with the outcome observed in the current state.
      Memory integrates multiple stimuli, not just a single reward channel.
    parameters:
      state_id: string
      outcome_signals: dict[string, number] # multi-stimulus integration
      timestamp_ms: number

  - name: sample_state_transition
    description: >
      Sample the next state stochastically, biased by memory scores under
      current conditions.
    parameters:
      current_state: string
      current_conditions: dict
      beta: number # inverse temperature; higher = more memory bias
    returns:
      next_state: string
      transition_logits: dict[string_id, number]
      sampled_via: enum [memory_dominant, balanced, exploration_dominant]

  - name: balance_monitor
    description: >
      Diagnostic — measures whether the coupling is in balance. Recommends
      β adjustments if entropy of recent transitions has collapsed
      (memory domination) or if memory predictiveness is near zero
      (stochasticity domination).
    parameters:
      recent_transitions: list
    returns:
      balance: enum [memory_dominant, balanced, stochasticity_dominant]
      recommended_beta_delta: number

  - name: decay_memory
    description: >
      Optional time-based decay applied to memory scores so older outcomes
      lose weight relative to recent ones.
    parameters:
      decay_rate: number
```

---

## Memory pattern

Persistent across decision steps:

```yaml
state_memory:
  current_state: <state_id>
  state_outcomes:
    <state_id>:
      visit_count: <int>
      outcome_aggregate: <multi-channel score>
      last_visited_ts: <ms>
      conditions_when_beneficial: <list of condition snapshots>
  transition_history:
    - from: <state_id>
      to: <state_id>
      outcome: <multi-channel>
      ts: <ms>
  beta: <current inverse-temperature>
  balance_indicator: <recent balance state>
```

The `conditions_when_beneficial` field is what allows context-conditional bias — memory is not a single scalar per state but a _conditional_ score based on past contexts.

---

## Translation notes

| Stack                                               | Mapping                                                                                                                                                                                                              |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RL frameworks** (Stable-Baselines3, RLlib, JaxRL) | States = options in an options framework (Sutton, Precup, Singh 1999). Memory = option-value estimates. Coupling = explicit β-weighted sampling rather than ε-greedy or pure softmax.                                |
| **LLM agent frameworks**                            | States = behavioural modes in the agent's prompt template (`exploring`, `committing`, etc.). Memory = persistent task-outcome store keyed by mode. Coupling = bias mode-selection prompt by retrieved memory scores. |
| **Multi-agent populations**                         | Each agent has its own (state, memory). Population-level diversity emerges from the coupling without explicit per-agent customisation — see [[clone-individuality\|P36]].                                            |
| **Online ML** (with feedback)                       | States = feature-set configurations or model-variant selections. Memory = online-learned configuration scores. Coupling = stochastic configuration switching biased by memory.                                       |

---

## Evaluation signals (falsifiable claims)

1. **Coupling outperforms either component alone.** At matched cost, the coupled architecture should outperform pure-stochastic and pure-memory baselines on tasks involving partial-observability and unpredictability, by ≥15%.
2. **Advantage scales with unpredictability.** The margin should grow as environmental unpredictability increases. If the margin is constant or inverse with unpredictability, the pairing is not doing the work it claims.
3. **Balance failures predict performance degradation.** When `balance_monitor` reports memory- or stochasticity-domination, performance should drop measurably until balance is restored. Non-correlation refutes the balance-monitor's load-bearing role.

## Examples

Working examples under [`examples/`](examples/) as the catalog matures.

## See also

- [`../README.md`](../README.md), [`../architecture/overview.md`](../architecture/overview.md), [`../references.md`](../references.md)
- Collection: [`../../clusters/acerebrate-decision-making/`](../../../clusters/acerebrate-decision-making/)
