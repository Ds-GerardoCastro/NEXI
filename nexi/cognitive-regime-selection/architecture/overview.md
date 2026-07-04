# Architecture: Cognitive Regime Selection

This document specifies the architectural primitive for the cognitive-regime-selection pattern — how to map a typed deployment niche to one of three structurally distinct regimes and produce the regime's characteristic component mix.

## The three regimes (definitional)

Each regime is defined by the relative cognitive investment $\gamma / (\kappa + \gamma)$ — control's share of total cognitive resources — and by the qualitative component mix that supports the regime's cognitive signature.

```
                  γ / (κ + γ)
                     │
         control     │    ▲
         dominant    │    │
                     │    │
                     │    └─── capacity-heavy   ─── tail of the design space
                     │         (lots of κ AND γ,
                     │          but γ has hit
                     │          diminishing returns)
                     │
                     │    ◀── control-enhanced  ─── synergy-dominant zone
                     │         (κ and γ growing
                     │          together, control
                     │          yields high MR)
                     │
                     │    └── passive-storage   ─── low-payoff niche
                     │         (κ only, γ ≈ 0)
                     │
                     └────────────────────────────► κ + γ
                                                   absolute investment
```

## Components

### 1. Niche-parameter intake

Accepts the typed niche object from upstream [`niche-specification`](../../niche-specification/):

```
intake(niche) -> {benefit, cost, cue_reliability, task_complexity_bits}
```

Required fields, in order of decision-leverage:

- `benefit` — task payoff per correct response
- `cost` — compute / latency / dollar cost per response
- `cue_reliability` — q ∈ [0, 1], how informative the input signal is for the task
- `task_complexity_bits` — the niche's information-theoretic complexity, if estimable

If any of these is unspecified, the classifier refuses to produce a regime — it raises `NicheUnderspecified` rather than guessing.

### 2. Regime classifier

The core mapping function:

```
classify(niche) -> {regime, boundary_distance, adjacent_regime, rationale}
```

The regime is determined by the relative-benefit ratio `B = benefit / cost`:

```
if B < LOW_THRESHOLD:
    regime = "passive-storage"
elif B < HIGH_THRESHOLD:
    regime = "control-enhanced"
else:
    regime = "capacity-heavy"
```

The thresholds `LOW_THRESHOLD` and `HIGH_THRESHOLD` are calibrated empirically per task family — Turner et al. derive numerical example values for working-memory tasks, but generalising to AI deployments requires per-domain calibration. Without calibration, treat the classifier output as a hypothesis to validate, not a deterministic answer.

`boundary_distance` ∈ [0, 1] reports how close the niche is to a regime boundary — 0 means on the boundary, 1 means deep in regime. Useful for drift monitoring.

### 3. Component-mix recommender

Given the regime + budget constraints, produce the regime's characteristic component mix:

```
recommend(regime, budget) -> {capacity_components, control_components, warnings}
```

The mixes are structurally distinct, not just sized:

| Regime               | Capacity components                                                       | Control components                                               | Distinguishing feature                                  |
| -------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- |
| **passive-storage**  | Long context window, embedding-based retrieval, compressed external store | (minimal — no agentic loops)                                     | Storage in the absence of regulation                    |
| **control-enhanced** | RAG, episodic memory, medium context                                      | Bounded agentic loop, structured tool use, attention routing     | Balanced storage + regulation, exploiting synergy       |
| **capacity-heavy**   | Very long context, retrieval, episodic memory, MoE expert pool            | Mature attention, deep reasoning (in maintenance mode), tool use | Absolute control growth but relative capacity dominance |

A flagship is **not** a "scaled-up edge model." The flagship is in a different regime and uses a structurally different component mix; only the cost / parameter count axis differs trivially.

## Data flow

```
                  ┌──────────────────────────┐
                  │ niche-specification      │  upstream — produces typed niche
                  │ (typed niche object)     │
                  └─────────────┬────────────┘
                                │
                                ▼
                  ┌──────────────────────────┐
                  │ Niche-parameter intake   │
                  │ (B, q, m, energy)        │
                  └─────────────┬────────────┘
                                │
                                ▼
                  ┌──────────────────────────┐
                  │ Regime classifier        │
                  │ (3 regimes + boundary)   │
                  └─────────────┬────────────┘
                                │
            ┌───────────────────┼───────────────────┐
            ▼                   ▼                   ▼
      passive-storage    control-enhanced     capacity-heavy
            │                   │                   │
            └───────────┬───────┴───────────┬───────┘
                        │                   │
                        ▼                   ▼
                  ┌──────────────────────────┐
                  │ Component-mix            │
                  │ recommender              │
                  └─────────────┬────────────┘
                                │
                                ▼
                  ┌──────────────────────────┐
                  │ capacity-first-scaling   │  downstream — consumes regime + mix
                  └──────────────────────────┘
```

## Pseudocode — design-time regime selection

```python
def select_regime(niche):
    if not niche.is_complete():
        raise NicheUnderspecified(niche.unspecified_fields)

    B = niche.benefit / niche.cost
    q = niche.cue_reliability
    m = niche.task_complexity_bits

    # Primary classification axis
    if B < LOW_THRESHOLD(domain=niche.domain):
        regime, primary = "passive-storage", "low-payoff niche"
    elif B < HIGH_THRESHOLD(domain=niche.domain):
        regime, primary = "control-enhanced", "synergy-dominant zone"
    else:
        regime, primary = "capacity-heavy", "diminishing-returns on control"

    # Boundary-distance check
    boundary_distance = compute_boundary_distance(B, niche.domain)
    adjacent = adjacent_regime(regime, B, niche.domain)

    # Modulators (don't override but add caveats)
    warnings = []
    if q < 0.3:
        warnings.append("Low cue reliability reduces synergy gains; "
                        "control investment will yield lower returns even in "
                        "control-enhanced regime.")
    if boundary_distance < 0.2:
        warnings.append(f"Niche is close to {adjacent} boundary; monitor for drift.")

    return RegimeClassification(
        regime=regime,
        boundary_distance=boundary_distance,
        adjacent_regime=adjacent,
        rationale=primary,
        warnings=warnings
    )

def recommend_component_mix(regime, budget):
    if regime == "passive-storage":
        return ComponentMix(
            capacity=["large_context", "embedding_retrieval", "compressed_store"],
            control=[],
            note="No agentic loops. Control investment is likely wasted in this regime."
        )
    elif regime == "control-enhanced":
        return ComponentMix(
            capacity=["medium_context", "rag_retrieval", "episodic_memory"],
            control=["bounded_agentic_loop", "structured_tool_use", "attention_routing"],
            note="Synergy is highest here; balanced investment yields strong returns."
        )
    elif regime == "capacity-heavy":
        return ComponentMix(
            capacity=["very_long_context", "rag_retrieval", "episodic_memory", "moe_expert_pool"],
            control=["mature_attention", "deep_reasoning", "tool_use"],
            note="Control in maintenance mode; capacity dominates relative investment."
        )
```

## Phase-boundary handling

Phase transitions between regimes are real — small changes in niche parameters near a boundary can flip the optimal architecture qualitatively. Two operational consequences:

1. **At classification time:** report `boundary_distance` and recommend monitoring for drift if low. Do not over-trust the classification at boundaries.
2. **At deployment time:** when telemetry suggests the deployed niche is drifting (cost budget shifts, payoff structure changes, signal reliability degrades), re-run the classifier. A regime change should trigger architecture migration, not just hyperparameter retuning.

The `adjacent_regime` field tells you which way the niche would drift to. Architecture migration plans should pre-stage components for the adjacent regime.

## Integration notes

| Stack                                                                          | How to integrate                                                                                                                                                                           |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Multi-tier model families** (Phi / Llama / GPT-tier-style)                   | Use the classifier per tier. Edge tier ≈ passive-storage, mid-tier ≈ control-enhanced, flagship ≈ capacity-heavy. Each tier gets its own architecture, not a re-sized version of the same. |
| **Deployment platforms with niche metadata** (Vertex AI, Bedrock, Together-AI) | Surface niche parameters as deployment-spec fields. Compute regime as a deploy-time annotation. Use the annotation to gate which model architecture serves the deployment.                 |
| **MLOps / ModelOps**                                                           | Persist regime classification per deployment as a versioned artefact. Re-classify on niche-spec changes. Use boundary-distance for drift alarms.                                           |
| **Architecture-as-code** (architecture configs in version control)             | Regime is part of the architecture spec, not part of hyperparameters. Changing regime = new architecture file.                                                                             |

## Interaction with the collection

This NEXI is the **middle stage** of the [`bounded-cognitive-architecture`](../../../collections/bounded-cognitive-architecture/) pipeline:

```
niche-specification ──► cognitive-regime-selection ──► capacity-first-scaling
```

It consumes the typed niche object from the upstream specification skill and produces a regime + component-mix recommendation that the downstream capacity-first allocation policy operates within.

A regime classification without a niche specification is meaningless. A regime classification without downstream allocation is just a tier label.
