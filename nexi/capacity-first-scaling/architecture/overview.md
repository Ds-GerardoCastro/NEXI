# Architecture: Capacity-First Scaling

This document specifies the architectural primitive for the capacity-first scaling pattern — components, interfaces, data flow, and integration notes for both LLM-stack and reinforcement-learning settings.

## Components

### 1. Component tagger

A function that classifies each named component of an architecture as `capacity`, `control`, or `mixed`:

```
tag(component) -> {capacity | control | mixed, rationale, decomposition?}
```

Canonical tags:

| Component                           | Default tag | Notes                                                                                                       |
| ----------------------------------- | ----------- | ----------------------------------------------------------------------------------------------------------- |
| Context window length               | `capacity`  | More tokens that can be held                                                                                |
| Retrieval store size                | `capacity`  | External capacity expansion                                                                                 |
| Memory-token slot count             | `capacity`  | Internal capacity                                                                                           |
| MoE expert pool size                | `capacity`  | Sparse capacity expansion                                                                                   |
| KV-cache budget                     | `capacity`  | Inference-time capacity                                                                                     |
| Attention-head count                | `control`   | Regulation over representations                                                                             |
| Attention-routing sophistication    | `control`   | Where attention goes                                                                                        |
| Reasoning-chain depth               | `control`   | Iterative regulation                                                                                        |
| Agentic-loop iteration cap          | `control`   | Outer-loop regulation                                                                                       |
| Planner branching factor            | `control`   | Search-time regulation                                                                                      |
| Tool-call retry depth               | `control`   | Failure-mode regulation                                                                                     |
| Vanilla transformer parameter count | `mixed`     | Scales capacity (weights as memory) and control (attention computation) jointly; requires sub-decomposition |

`mixed` components are decomposed when possible (e.g. transformer with explicit KV-cache treats the cache as `capacity` and the attention computation as `control`).

### 2. Niche threshold estimator

A function that estimates the deployment niche's task complexity in bits:

```
estimate_threshold(niche) -> {bits, confidence, assumptions}
```

The estimate is informed by:

- The niche's `task_complexity_bits` field if pre-specified (consumed from upstream `niche-specification`).
- Task examples and prompts, if no pre-specified value.
- Heuristics: number of distinct items required to solve the task; depth of relational structure; required precision.

### 3. Allocation policy

The core decision function:

```
allocate(architecture, delta_budget, niche) -> {recommendations: list[component, share, rationale], warnings: list[string]}
```

The policy is:

1. Tag all components.
2. Estimate the niche threshold.
3. If estimated capacity < threshold → spend `delta_budget` on capacity components first.
4. Else if intermediate-investment regime (per upstream regime classifier) → balanced allocation, exploiting synergy.
5. Else (high-investment regime) → capacity-leaning allocation (~70% capacity, ~30% control); control still pays in absolute terms but its diminishing returns mean capacity wins relatively.

## Data flow

```
                       ┌──────────────────────────┐
                       │ niche-specification      │  upstream
                       │ (typed niche object)     │
                       └─────────────┬────────────┘
                                     │
                                     ▼
                       ┌──────────────────────────┐
                       │ cognitive-regime-        │  upstream
                       │ selection                │
                       │ (regime + component mix) │
                       └─────────────┬────────────┘
                                     │
                                     ▼
   ┌──────────────────┐   ┌──────────────────────────┐
   │ Architecture     │──▶│ Component tagger         │
   │ specification    │   └─────────────┬────────────┘
   └──────────────────┘                 │
                                        ▼
   ┌──────────────────┐   ┌──────────────────────────┐
   │ Budget increase  │──▶│ Niche threshold          │
   │ ΔB               │   │ estimator                │
   └──────────────────┘   └─────────────┬────────────┘
                                        │
                                        ▼
                       ┌──────────────────────────┐
                       │ Allocation policy        │
                       └─────────────┬────────────┘
                                     │
                                     ▼
                       ┌──────────────────────────┐
                       │ Recommended allocation   │
                       │ + warnings               │
                       └──────────────────────────┘
```

## Pseudocode — design-time scaling decision

```python
def capacity_first_allocate(architecture, delta_budget, niche, regime):
    tagged = [tag_component(c) for c in architecture.components]
    capacity_components = [c for c in tagged if c.tag == "capacity"]
    control_components  = [c for c in tagged if c.tag == "control"]
    mixed_components    = [c for c in tagged if c.tag == "mixed"]

    if mixed_components:
        # require sub-decomposition before proceeding
        return AllocationError(
            "Mixed components must be decomposed: "
            f"{[c.name for c in mixed_components]}"
        )

    threshold_bits = estimate_threshold(niche)
    current_capacity_bits = sum(c.capacity_bits for c in capacity_components)

    if current_capacity_bits < threshold_bits:
        return prioritize(capacity_components, delta_budget)

    # Capacity is adequate — defer to regime
    if regime == "control-enhanced":
        return balanced(capacity_components, control_components, delta_budget,
                        capacity_share=0.5)
    elif regime == "capacity-heavy":
        return balanced(capacity_components, control_components, delta_budget,
                        capacity_share=0.7)
    elif regime == "passive-storage":
        return prioritize(capacity_components, delta_budget,
                          warning="Passive-storage regime — control investment "
                                  "is likely wasted; prefer capacity expansion.")
```

## Pseudocode — RL-flavour for cost-budget tuning

In a reinforcement-learning setting where capacity (replay buffer size, observation-window length, memory-augmented network size) and control (attention sophistication, planning depth, value-function expressiveness) compete for parameter budget:

```python
def rl_capacity_first(env, total_budget, niche):
    components = enumerate_rl_components(env)
    tagged = [tag_component(c) for c in components]

    # Initial allocation: minimum-viable capacity to clear the threshold
    threshold_bits = estimate_threshold(niche)
    capacity_alloc = bring_to_threshold(tagged, threshold_bits)

    remaining = total_budget - sum(capacity_alloc.values())
    if remaining < 0:
        # Cannot reach threshold within budget — flag and either
        # accept under-capacity or request budget increase.
        return UnderCapacity(deficit=-remaining)

    # Allocate remaining budget per regime
    regime = classify_regime(niche)
    return capacity_alloc + allocate_remaining(remaining, tagged, regime)
```

## Integration notes

| Stack                                                          | How to integrate                                                                                                                                                                                                      |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Transformer LLM stacks** (HuggingFace, Llama, etc.)          | Tag context-window-length, retrieval store, KV-cache, MoE expert count as `capacity`. Tag attention sophistication, agentic-loop depth as `control`. Apply the rule when planning model-family scaling between tiers. |
| **Retrieval-augmented generation** (REALM / RAG / RETRO style) | The retrieval store is the most direct capacity dial. Below threshold, expand the store before adding reranker / generator complexity.                                                                                |
| **Mixture-of-Experts** (Switch / Mixtral / DeepSeek-MoE)       | Expert-pool size = capacity; routing sophistication = control. The empirical pattern that MoE scales best when expert count grows faster than routing complexity is consistent with the rule.                         |
| **Multi-agent RL** (Ray RLlib, PettingZoo, Mava)               | Replay-buffer size, observation-window length, memory-network size = capacity. Policy-network depth, planner branching = control. Apply the rule before scaling either axis.                                          |
| **Agentic frameworks** (LangGraph, CrewAI, AutoGen)            | Context window per agent + retrieval store + episodic memory = capacity. Agent-loop depth + tool-retry budget + planner sophistication = control. Use the rule when sizing agent crews under cost constraints.        |

## Performance and cost considerations

The rule's strongest form assumes capacity-cost and control-cost are roughly proportional per unit. When this fails:

- **Quadratic-attention regime.** If full attention over very long context dominates compute (capacity expansion becomes O(n²)), the cost-adjusted recommendation may flip toward control investment. Mitigation: use sparse / linear / streaming attention to recover linear capacity cost, or use retrieval as a sub-quadratic capacity primitive.
- **Cheap-control regime.** If control is _substantially_ cheaper than capacity per unit of effective recall improvement, the rule is reversed. Empirically rare — rare enough that Turner et al. note it as the only condition under which capacity-first is overturned.
- **Already-saturated capacity.** Once capacity is well above the niche threshold, control investment dominates marginal returns until it too saturates. The rule degenerates into balanced allocation in this regime, with capacity-leaning weight (~70% per the high-investment regime) only when well above threshold.

## Interaction with the collection

This NEXI is the most downstream stage of the [`bounded-cognitive-architecture`](../../../collections/bounded-cognitive-architecture/) pipeline:

```
niche-specification ──► cognitive-regime-selection ──► capacity-first-scaling
```

The niche-threshold estimate consumes the niche object produced by the upstream specification skill. The regime-conditional balance share consumes the regime classification produced by the upstream regime classifier. Without both upstreams, the allocation policy operates on incomplete information.
