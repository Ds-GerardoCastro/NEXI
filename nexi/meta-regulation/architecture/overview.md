# Architecture: Meta-Regulation

This document specifies the architectural primitive for the meta-regulation pattern — components, interfaces, data flow, and integration with the regulator layer.

## The three-level hierarchy

```
   ┌──────────────────────────────────────────────────┐
   │  L3: Meta-regulator layer (anti-σ-style)          │  ← runtime dynamics,
   │      observes the regulator, modulates it         │     terminates regress
   └──────────────────────┬───────────────────────────┘
                          │ regulates parameters / activation of...
                          ▼
   ┌──────────────────────────────────────────────────┐
   │  L2: Regulator layer (σ-factor-style)             │  ← standard control
   │      routing, attention, agent dispatch           │     logic
   └──────────────────────┬───────────────────────────┘
                          │ regulates...
                          ▼
   ┌──────────────────────────────────────────────────┐
   │  L1: Substrate layer                              │  ← model weights,
   │      experts, attention heads, agents, memory     │     compute units
   └──────────────────────────────────────────────────┘
```

## Components

### 1. Substrate layer (L1)

What's being regulated. Examples in current AI: model weights, MoE expert pools, attention heads, agent populations, retrieval stores.

This layer is unchanged from standard architectures. It exposes a regulatable interface.

### 2. Regulator layer (L2)

Standard control logic — routing decisions, attention computation, agent dispatch. Has its own parameters and dynamics.

```
regulator.parameters: dict       # e.g. attention temperature, routing thresholds
regulator.observe(input) -> RegState
regulator.act(state) -> Action_on_substrate
```

The regulator's parameters are **dynamic** — adjustable by the meta-regulator at runtime.

### 3. Meta-regulator layer (L3)

The first-class architectural commitment. Components that observe the regulator's behaviour and dynamically up- or down-regulate it.

```
meta_regulator.observe_regulator(regulator_state, deployment_context) -> MetaSignal
meta_regulator.modulate(regulator) -> None  # mutates regulator.parameters
```

Two flavours of modulation:

- **Up-regulation:** increase regulator influence under specific conditions. Analog: anti-σ proteolysis releases σ-factors → more transcription regulation.
- **Down-regulation:** suppress regulator activity under others. Analog: anti-σ binding sequesters σ-factors → less transcription regulation.

Critical design choice: **meta-regulator parameters are themselves fixed at deployment** (or pre-trained). This terminates the control regress at L3 and prevents control-of-control-of-control instability.

## Data flow

```
                 deployment_context (signals from environment)
                              │
                              ▼
   ┌─────────────────────────────────────────────────────┐
   │   L3: meta-regulator observes (regulator_state,     │
   │        deployment_context), produces MetaSignal      │
   └──────────────────────┬──────────────────────────────┘
                          │ modulates regulator parameters
                          ▼
   ┌─────────────────────────────────────────────────────┐
   │   L2: regulator (now with modulated parameters)     │
   │        observes input, produces Action               │
   └──────────────────────┬──────────────────────────────┘
                          │ acts on substrate
                          ▼
   ┌─────────────────────────────────────────────────────┐
   │   L1: substrate (gates, weights, experts, agents)   │
   └─────────────────────────────────────────────────────┘
```

## Pseudocode — runtime meta-regulation step

```python
def architectural_step(input, deployment_context, regulator, meta_regulator, substrate):
    # L3: meta-regulator observes state and context, decides modulation
    regulator_state = regulator.observe(input)
    meta_signal = meta_regulator.observe_regulator(regulator_state, deployment_context)

    # L3 mutates L2's parameters
    meta_regulator.modulate(regulator, meta_signal)

    # L2: regulator with modulated parameters acts on substrate
    action = regulator.act(regulator_state)

    # L1: substrate produces output
    output = substrate.execute(action)

    return output
```

## Diversity at the regulator-level

Bacteria have multiple σ-factor types AND multiple anti-σ types per strain. The architectural translation: **the meta-regulator should not be a single global controller**. It should be a _family_ of meta-regulators, each specialising in a particular regulator-type or deployment-context-type.

```
meta_regulators: dict[regulator_type, MetaRegulator]
```

This produces graceful degradation: if one meta-regulator is mis-calibrated, others continue functioning. It also matches the bacterial pattern more faithfully — the cell has a _toolkit_ of meta-regulators it deploys depending on stress type.

## Avoiding the regress

The infinite regress (meta-meta-regulator, meta-meta-meta-regulator) is unstable in biology and would be unstable in AI. The bacterial answer: terminate at a layer with stable, slowly-changing dynamics.

Architectural rule: **the L3 meta-regulator's own parameters are pre-trained and frozen at deployment**. They do not have an L4 meta-meta-regulator. If runtime adaptation of L3 itself is needed, that adaptation belongs in offline training, not in deployed runtime.

This rule keeps the architecture's runtime control hierarchy at exactly three levels. Deeper hierarchies are a research frontier, not a deployment-default.

## Integration notes

| Stack                            | How to integrate                                                                                                                                                                                        |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **HyperNet-style architectures** | The HyperNet that generates regulator parameters _is_ the meta-regulator. Make it observable in L3 explicitly, with an interface for runtime modulation rather than a fixed pre-computed pass.          |
| **Mixture-of-Experts**           | The gating network is L2. Add an L3 meta-gating layer that observes deployment-context and dynamically adjusts the gating network's temperature, expert pool composition, or load-balancing parameters. |
| **LLM agent frameworks**         | The agent loop's control logic is L2. Add an L3 meta-controller that watches the agent's recent trajectory and adjusts the loop's depth, retry budget, tool-selection bias.                             |
| **Multi-agent RL**               | The dispatcher is L2. The meta-regulator is L3 — observes population-level outcomes, adjusts dispatcher parameters (population size, exploration policy, reward shaping).                               |
| **Production ML serving**        | The serving controller (load balancer, fallback router) is L2. The meta-regulator monitors deployment-wide metrics and adjusts the serving controller's behaviour.                                      |

## Interaction with the collection

This NEXI is the **control-over-control layer** of the [`acerebrate-decision-making`](../../../clusters/acerebrate-decision-making/) collection. It composes with:

- [`coincidence-detection-gating`](../../coincidence-detection-gating/) — the meta-regulator can dynamically adjust the gate's thresholds and required-stream set in response to deployment-context signals.
- [`stochastic-memory-coupling`](../../stochastic-memory-coupling/) — the meta-regulator dynamically adjusts the coupling parameter `β` and memory decay rate, keeping both components actively contributing.
