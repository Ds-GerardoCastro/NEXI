# Architecture: Cognitive Regime Selection

This document specifies the architectural primitive for the cognitive-regime-selection pattern — how to map a typed deployment niche to a position on a continuous optimality surface, read off the nearest of three qualitatively distinct regimes, and produce that regime's characteristic component mix.

## The three regimes (definitional)

The regimes are **regions on a continuous optimality surface**, not discrete points. Turner et al.'s model is explicitly continuous; the boundaries between regions are soft. Each region is located by the optimal **control share** $\gamma^* / (\kappa^* + \gamma^*)$ — control's fraction of total cognitive resources at the niche's optimum — together with the absolute investment $\kappa^* + \gamma^*$. The qualitative component mix follows from where on the surface the niche's optimum lands.

Key mechanism (from Turner et al.), which the classifier must respect:

- **Capacity contributes linearly; control contributes sublinearly** (severe diminishing returns). Evolution prioritises capacity because control cannot operate without a space to maintain representations.
- **Synergy is non-monotonic in capacity.** With too little capacity, control cannot help (noise dominates); with substantial capacity, weak control already suffices. Control's _marginal_ value therefore peaks in a mid zone and falls off at both ends.
- **Synergy strength is modulated by task complexity $m$, cue reliability $q$, and available metabolic energy** (benefit relative to per-unit cost). Low $q$ suppresses the synergy gain; high $m$ raises the capacity requirement.

```
   control share γ*/(κ*+γ*)   (a continuous surface; regions have soft boundaries)
        │
  high  │        ┌────────────────┐
        │        │ control-       │   mid payoff · reliable cue · moderate m
        │        │ enhanced       │   synergy peaks → control earns its keep
        │        └────────────────┘
        │      ↗                    ↘   (soft boundary)
   mid  │  ┌───────────┐        ┌──────────────┐
        │  │ passive-  │        │ capacity-    │   high payoff · control at
        │  │ storage   │        │ heavy        │   diminishing (sublinear)
   low  │  │ κ only,   │        │ κ and γ high │   returns → share falls back
        │  │ γ*≈0      │        │ but γ share↓ │   toward capacity
        │  └───────────┘        └──────────────┘
        └──────────────────────────────────────────► absolute investment κ*+γ*
          low payoff             high payoff
```

The control share rises from ≈0 (passive-storage) into the synergy-dominant mid zone (control-enhanced), then falls back as absolute investment grows and control hits diminishing returns (capacity-heavy). It is a hump, not a monotone ramp — which is exactly why a single benefit/cost scalar cannot classify correctly.

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
classify(niche) -> {regime, control_share_estimate, boundary_distance,
                    adjacent_regime, rationale}
```

The classifier does **not** key on a single benefit/cost scalar. It estimates the niche's optimal **control share** `s = γ*/(κ*+γ*)` as a function of all four inputs — benefit, cost, cue reliability `q`, and task complexity `m` — reproducing the non-monotonic synergy, then reports the nearest region on the continuous surface. Sketch of the proxy (a principled approximation of Turner's optimality model, not a re-derivation):

1. **Absolute-investment drive** `A = benefit / cost`. Higher payoff-per-cost buys more total resources `κ*+γ*`. This sets _how far right_ on the surface the niche sits.
2. **Effective capacity demand.** Task complexity `m` (bits / items to hold) raises the capacity that must be provisioned before control can act: `κ_req` grows with `m`. Higher `m` pushes share _down_ (more of the budget must go to capacity just to have a workspace).
3. **Synergy gain** `G(A, q, m)` — the marginal value of control. It is **non-monotonic in absolute investment**: near-zero when total resources are too small for control to bite, peaking in a mid band, then decaying as control's sublinear returns set in at high investment. It is **scaled by cue reliability** `q`: an unreliable cue (`q` low) means control has little signal to exploit, so `G` is suppressed roughly proportionally to `q`. It is **damped by high `m`**, which diverts budget to capacity.
4. **Control share** `s = clamp( G(A,q,m) / (1 + G(A,q,m)), 0, ~0.5 )` — capped below 0.5 because capacity is prioritised (control never dominates the optimum in Turner's model).

The nearest region is read off `s` **and** `A` jointly (share alone is ambiguous — a low share can mean either passive-storage at low `A` or capacity-heavy at high `A`):

- `s ≈ 0` (control earns nothing) → **passive-storage**.
- `s` in its peak band (synergy paying off) → **control-enhanced**.
- `s` falling back down _while `A` is high_ (control past its diminishing-returns knee) → **capacity-heavy**.

Because `q` scales `G` and `m` damps it, **cue reliability and task complexity can move a niche across a regime boundary**: a mid-payoff niche with an unreliable cue (`q` low) or very high complexity may fall out of control-enhanced into passive-storage or capacity-heavy respectively, even at unchanged benefit/cost. This is the material use of `q` and `m` the earlier single-scalar version lacked.

The synergy shape and its knee locations are calibrated empirically per task family — Turner et al. derive numerical example values for working-memory tasks, but generalising to AI deployments requires per-domain calibration. Without calibration, treat the classifier output as a hypothesis to validate, not a deterministic answer.

`control_share_estimate` ∈ [0, ~0.5] is the continuous position `s` — reported directly so downstream consumers see the surface position, not just a region label.

`boundary_distance` ∈ [0, 1] reports how close the niche is to a soft region boundary — 0 means on the boundary, 1 means deep in the region. Useful for drift monitoring.

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

This is a **principled approximation** of Turner et al.'s optimality model — it reproduces the mechanism (linear capacity vs. sublinear control, non-monotonic synergy, `q`-scaling, `m`-damping) with a small closed-form proxy so it can run at design time. It is **not** a re-derivation of the paper's optimal-control solution and **requires per-domain calibration** (`DomainCalibration`) before its outputs are trusted; without calibration, treat every output as a hypothesis to validate.

```python
import math

def select_regime(niche, cal=None):
    """Principled approximation of Turner et al.'s optimality model.

    Estimates the niche's optimal control share s = γ*/(κ*+γ*) as a function of
    ALL FOUR inputs — benefit, cost, cue reliability q, task complexity m — then
    returns the nearest REGION on a continuous surface (not a discrete id).
    `cal` holds per-domain calibration constants; defaults are placeholders that
    MUST be calibrated per task family before the output is trusted.
    """
    if not niche.is_complete():
        raise NicheUnderspecified(niche.unspecified_fields)

    cal = cal or DomainCalibration.default(niche.domain)

    # --- Inputs (all four are used) ---
    A = niche.benefit / niche.cost          # absolute-investment drive (payoff/cost)
    q = niche.cue_reliability               # cue reliability in [0, 1]
    m = niche.task_complexity_bits          # task complexity (bits / items to hold)

    # --- (1) Absolute investment on the surface: log-compressed, saturating ---
    #     more payoff/cost buys more total resources κ*+γ*, with diminishing gain.
    A_norm = A / (A + cal.A_half)           # in [0, 1); A_half = payoff/cost midpoint

    # --- (2) Complexity raises the capacity that must be provisioned first ---
    #     effective investment available to *synergy* is what's left after paying
    #     the m-driven capacity floor. High m => less headroom => share pushed down.
    capacity_floor = m / (m + cal.m_half)   # in [0, 1); grows with complexity
    synergy_headroom = max(A_norm - cal.floor_weight * capacity_floor, 0.0)

    # --- (3) Non-monotonic synergy gain G(A, q, m) ---
    #     hump in absolute investment: ~0 when too little to matter, peaks in a mid
    #     band, decays as control's SUBLINEAR returns set in at high investment.
    hump = math.exp(-((A_norm - cal.synergy_peak) ** 2) / (2 * cal.synergy_width ** 2))
    #     cue reliability scales the gain (unreliable cue => little signal to exploit);
    #     complexity damps it (budget diverted to capacity).
    G = hump * q * synergy_headroom

    # --- (4) Control share s = γ*/(κ*+γ*), capped < 0.5 (capacity is prioritised) ---
    s = min(G / (1.0 + G), cal.share_cap)   # continuous position on the surface

    # --- Read off nearest region from s AND A jointly (share alone is ambiguous) ---
    if s < cal.share_low:
        # low share: passive-storage at low A, capacity-heavy at high A
        if A_norm >= cal.high_investment:
            regime, primary = "capacity-heavy", "control past diminishing-returns knee"
        else:
            regime, primary = "passive-storage", "control earns ~0; storage-only niche"
    else:
        regime, primary = "control-enhanced", "synergy-dominant zone (control pays off)"

    # --- Continuous-surface boundary geometry (soft boundaries) ---
    boundary_distance = compute_boundary_distance(s, A_norm, cal)   # in [0, 1]
    adjacent = adjacent_region(regime, s, A_norm, cal)

    # --- Honest caveats (do not override the estimate) ---
    warnings = []
    if q < cal.q_warn:
        warnings.append("Low cue reliability suppresses the synergy gain; a niche "
                        "that looks control-enhanced by payoff/cost alone may sit in "
                        "passive-storage once q is accounted for.")
    if capacity_floor > cal.m_warn:
        warnings.append("High task complexity diverts budget to capacity; control "
                        "share is pushed down toward capacity-heavy.")
    if boundary_distance < cal.boundary_warn:
        warnings.append(f"Niche sits near the soft {adjacent} boundary; regions have "
                        f"no hard edges — monitor for drift, do not over-trust the label.")

    return RegimeClassification(
        regime=regime,                       # nearest region on a continuous surface
        control_share_estimate=s,            # continuous position, in [0, ~0.5]
        boundary_distance=boundary_distance,
        adjacent_regime=adjacent,
        rationale=primary,
        warnings=warnings,
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

## Region-boundary handling

The regions have **soft boundaries on a continuous surface** — there are no hard edges. Still, because the component mixes differ qualitatively, a niche whose optimum drifts across a soft boundary can warrant a qualitatively different architecture. Two operational consequences:

1. **At classification time:** report `control_share_estimate` and `boundary_distance`, and recommend monitoring for drift if the niche sits near a boundary. Do not over-trust the region label near boundaries — the surface is continuous, so a niche just inside one region is barely distinguishable from one just inside the neighbour.
2. **At deployment time:** when telemetry suggests the deployed niche is drifting (cost budget shifts, payoff structure changes, cue reliability degrades, task complexity grows), re-run the classifier. Crossing into a different region should trigger architecture migration, not just hyperparameter retuning.

The `adjacent_regime` field tells you which region the niche would drift into. Architecture migration plans should pre-stage components for the adjacent region.

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
