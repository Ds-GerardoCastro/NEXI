# Skill: Meta-Regulation (framework-neutral)

A drop-in skill for AI systems with **explicit runtime regulators-of-regulators**. Adds an L3 meta-regulator layer that observes the L2 regulator's behaviour and dynamically up- or down-regulates it in response to deployment-context signals. Distinct from training-time meta-learning.

> **Skill kind:** `runtime` (the meta-regulator's observation-and-modulation loop runs during deployment, not at training time). Configuration is design-time.

---

## System-prompt fragment

```
Your architecture has THREE explicit layers, not two:

  L1: Substrate (model weights, experts, agents, memory stores).
  L2: Regulator (routing, attention, dispatcher) — has dynamic parameters.
  L3: Meta-regulator (observes L2, modulates L2's parameters at runtime).

When designing or deploying:

  - Treat L3 as a FIRST-CLASS architectural layer, not as a training-time
     meta-learner that's frozen at deployment.
  - L3 observes (regulator_state, deployment_context) and produces a
     MetaSignal — a recommendation to modulate L2's parameters.
  - L3 modulates L2 via specific operations: up-regulation (increase
     L2's influence) or down-regulation (suppress it).
  - L3's OWN parameters are pre-trained and frozen at deployment. Do not
     add an L4 meta-meta-regulator at runtime — terminate the regress.
  - Keep MULTIPLE L3 meta-regulators when the substrate has heterogeneous
     regulator types (one per regulator family, not a single global L3).
     Diversity at L3 produces graceful degradation if any one mis-fires.

When you observe drift, distribution shift, or non-stationarity at L1
or L2, the right response is to surface a MetaSignal at L3 — NOT to
retrain L1 weights or modify L2's structure.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: register_regulator
    description: >
      Declare an L2 regulator with dynamic parameters.
    parameters:
      regulator_id: string
      modulatable_params: list[{name, range, semantics}]

  - name: register_meta_regulator
    description: >
      Declare an L3 meta-regulator. Each meta-regulator targets a specific
      regulator (or a family of regulators) and has its own observation
      window and modulation policy.
    parameters:
      meta_regulator_id: string
      target_regulator_ids: list[string]
      observation_window_ms: number
      modulation_policy: enum [up_only, down_only, bidirectional]

  - name: observe_regulator_state
    description: >
      Snapshot the L2 regulator's current state for L3 to evaluate.
    parameters:
      regulator_id: string
    returns:
      state_snapshot: dict
      recent_decisions: list

  - name: apply_meta_regulation
    description: >
      L3 produces a MetaSignal and applies it to mutate the targeted L2
      regulator's parameters.
    parameters:
      meta_regulator_id: string
      target_regulator_id: string
      meta_signal: dict
    returns:
      applied_changes: dict
      rationale: string

  - name: lesion_test
    description: >
      Diagnostic — temporarily disable a meta-regulator to measure whether
      its presence is load-bearing. Falsifiable claim sub-test.
    parameters:
      meta_regulator_id: string
      duration_ms: number
    returns:
      baseline_metric: number
      lesioned_metric: number
      delta: number
      is_load_bearing: bool # delta significantly worse than removing equivalent compute elsewhere
```

---

## Memory pattern

```yaml
meta_regulation_state:
  meta_regulators:
    <meta_regulator_id>:
      target: <regulator_id_or_list>
      observation_window: <ms>
      recent_observations: <list>
      recent_modulations: <list>
      lesion_test_history:
        - lesion_ts: <ms>
          baseline: <metric>
          lesioned: <metric>
          delta: <number>
  regulators:
    <regulator_id>:
      modulatable_params: <list>
      current_param_values: <dict>
      modulation_audit_log: <list>
```

The `lesion_test_history` is essential — without lesion experiments, claims that the meta-regulator is doing useful work cannot be validated.

---

## Translation notes

| Stack                        | Mapping                                                                                                                                                          |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HyperNet architectures**   | The HyperNet is L3. Make its modulation observable and runtime-configurable rather than fixed at training.                                                       |
| **MoE / Switch Transformer** | The gating network is L2. Add an L3 meta-gating layer observing deployment-context and adjusting gating temperature, expert pool composition, or load-balancing. |
| **LLM agent frameworks**     | The agent loop control is L2. Add L3 meta-controller watching recent trajectory and adjusting loop depth, retry budget, tool-selection bias.                     |
| **Production ML serving**    | Load balancer / fallback router is L2. L3 meta-regulator observes deployment-wide metrics and adjusts L2's behaviour.                                            |
| **Multi-agent RL**           | Population dispatcher is L2. L3 observes population outcomes and adjusts dispatcher params (population size, exploration, reward shaping).                       |

---

## Evaluation signals (falsifiable claims)

1. **Distribution shift advantage.** Under input distribution shift mid-deployment, meta-regulated architectures should show ≥10% reduction in performance degradation vs flat-regulation baselines at matched cost.
2. **Lesion experiment.** Removing the meta-regulator should produce measurably worse degradation than removing equivalent compute from any other layer. If not, the meta-regulator is not load-bearing.
3. **Diversity-of-meta-regulators robustness.** A single global L3 meta-regulator failing should produce catastrophic degradation; a family of L3 meta-regulators should degrade more gracefully when any single one fails.
4. **Regress termination.** Adding an L4 meta-meta-regulator at runtime should _not_ improve performance over the L3-frozen baseline. If it does, the L3 layer has insufficient stability.

## Examples

Working examples under [`examples/`](examples/) as the catalog matures.

## See also

- [`../README.md`](../README.md), [`../architecture/overview.md`](../architecture/overview.md), [`../references.md`](../references.md)
- Collection: [`../../collections/acerebrate-decision-making/`](../../../collections/acerebrate-decision-making/)
