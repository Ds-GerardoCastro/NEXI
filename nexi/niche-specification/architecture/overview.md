# Architecture: Niche Specification

This document specifies the architectural primitive for the niche-specification pattern — the typed niche schema, the elicitation dialogue, persistence and versioning, and the downstream consumption interfaces.

## The niche schema (typed object)

A niche specification has six axes. Each axis is a typed sub-schema; the full niche object is the union.

```yaml
niche:
  name: string # human-readable label
  version: semver # niches are versioned artefacts

  task_structure:
    primary_task_family: string # e.g. "long-document QA", "multi-agent coord"
    task_complexity_bits: number # bits required to encode solution, if estimable
    task_compressibility: enum[low, medium, high]
    hierarchical_structure: bool
    multi_modal_required: bool
    expected_input_distribution: string # informal description

  signal_environment:
    cue_reliability: number # 0..1
    distribution_stability: enum[stationary, slowly-shifting, non-stationary]
    adversarial: bool
    noise_profile: enum[clean, noisy, structured-noise]

  resource_envelope:
    cost_per_response_usd: number
    latency_budget_ms: number
    memory_budget_mb: number
    energetic_constraint: enum[edge, mid, server, datacenter]
    inference_concurrency: number # expected QPS

  error_profile:
    correctness_premium: enum[low, medium, high, critical]
    failure_mode_tolerance: enum[graceful_degrade, hard_fail_ok, hard_fail_unacceptable]
    recovery_path: enum[retry, fallback, escalate-to-human, none]

  social_surround:
    multi_agent: bool
    other_agent_observability: enum[none, partial, full]
    human_in_loop: bool
    human_oversight_frequency: enum[continuous, periodic, post-hoc, none]

  evaluation_protocol:
    in_niche_benchmark: string # path or identifier — NOT a generic benchmark
    success_threshold: number # niche-specific success metric target
    out_of_niche_behaviour: enum[graceful_decline, refuse, undefined]
    re_evaluation_cadence: enum[continuous, weekly, monthly, on-deployment-change]
```

The schema is **closed-world** for the typed enums (no extensibility at v1) but open-world for free-form fields like `expected_input_distribution`. Engineers can add a v2 sub-schema for richer niche descriptions; v1 enforces the minimum required to make the downstream regime classifier work.

## Components

### 1. Specification dialogue

Elicits values for each axis from a deployment description. Refuses to synthesise plausible-sounding defaults.

```
elicit(deployment_description) -> partial_niche
```

The dialogue iterates per axis until each is filled or explicitly marked `unknown` with a confidence note:

```
for axis in [task_structure, signal_environment, resource_envelope,
             error_profile, social_surround, evaluation_protocol]:
    while not axis.is_complete():
        ask_targeted_question(axis, current_partial)
        accept_value_or_unknown_with_note()
```

Pushback is built in: vague descriptions ("help users with general questions") trigger a refusal-to-proceed with a request for more specificity. The dialogue is **not** an autocomplete — it is a forcing function.

### 2. Validator

Checks completeness and coherence:

```
validate(partial_niche) -> {complete: bool, missing: list, incoherent: list}
```

Coherence checks include:

- `correctness_premium: critical` + `failure_mode_tolerance: graceful_degrade` → flag (these usually disagree).
- `multi_agent: true` + `other_agent_observability: none` → flag (multi-agent without observability has no surface for [`eavesdropping`](../../eavesdropping/) or peer modelling).
- `energetic_constraint: edge` + `cost_per_response_usd > 0.10` → flag (edge usually implies very low per-response cost).
- `out_of_niche_behaviour: undefined` → flag (always require an explicit declaration).

### 3. Persistence

Niche objects are stored as **versioned artefacts**:

```
persist(niche, deployment_id) -> {niche_version, artefact_path}
```

Storage shape:

```
deployments/<deployment_id>/niches/
  v1.0.0.yaml
  v1.1.0.yaml         # update when niche params shift
  v2.0.0.yaml         # major version when schema axes are renegotiated
  current -> v2.0.0.yaml
```

Architectures reference the niche by version, not by transient values. Re-specifying the niche (a new version) triggers re-design downstream — re-run regime classification and capacity-first allocation against the new niche.

### 4. Multi-niche detector

Detects when a deployment is being asked to serve multiple distinct niches and recommends a router-of-niche-specialists pattern instead of a single niche commitment:

```
detect_multi_niche(description) -> {is_multi_niche: bool, sub_niches: list, recommendation}
```

The detector flags:

- Heterogeneous user segments with structurally different task expectations.
- Heterogeneous deployment surfaces (mobile + web + voice) with structurally different resource envelopes.
- Heterogeneous payoff structures (free-tier vs. paid-tier with different correctness premiums).

Recommendation: replace the single niche with a **router** that classifies incoming requests into sub-niches, plus per-sub-niche specialist architectures. Each specialist is niche-bound; the router itself is not.

## Data flow

```
   ┌─────────────────────────────┐
   │ Deployment description      │
   │ (free-form input)           │
   └──────────────┬──────────────┘
                  │
                  ▼
   ┌─────────────────────────────┐
   │ Multi-niche detector        │  ────► if multi-niche →
   │                             │        recommend router-of-specialists,
   │                             │        invoke per sub-niche
   └──────────────┬──────────────┘
                  │ (single niche)
                  ▼
   ┌─────────────────────────────┐
   │ Specification dialogue      │
   │ (per-axis elicitation)      │
   └──────────────┬──────────────┘
                  │
                  ▼
   ┌─────────────────────────────┐
   │ Validator                   │  ◀── reject if incomplete or incoherent
   └──────────────┬──────────────┘
                  │
                  ▼
   ┌─────────────────────────────┐
   │ Typed niche object          │
   │ (versioned)                 │
   └──────────────┬──────────────┘
                  │
                  ▼
   ┌─────────────────────────────┐
   │ Persistence                 │
   └──────────────┬──────────────┘
                  │
                  ▼
   ┌─────────────────────────────┐
   │ Downstream consumption:     │
   │ - cognitive-regime-         │
   │   selection                 │
   │ - capacity-first-scaling    │
   │ - in-niche evaluation       │
   └─────────────────────────────┘
```

## Pseudocode — design-time niche specification

```python
def specify_niche(deployment_description):
    multi = detect_multi_niche(deployment_description)
    if multi.is_multi_niche:
        return RouterOfSpecialistsRecommendation(
            sub_niches=[specify_niche(s) for s in multi.sub_niches],
            router_spec=multi.router_spec,
        )

    partial = empty_niche(name=infer_name(deployment_description))

    AXES = ["task_structure", "signal_environment", "resource_envelope",
            "error_profile", "social_surround", "evaluation_protocol"]

    for axis in AXES:
        while not partial.axis_complete(axis):
            answer = ask_targeted_question(
                axis=axis,
                deployment_description=deployment_description,
                prior_partial=partial,
            )
            if answer.is_vague_or_aspirational():
                push_back_for_specificity(answer)
                continue
            partial = partial.merge(axis, answer)

    validation = validate(partial)
    if not validation.complete or validation.incoherent:
        raise NicheValidationError(validation)

    niche = freeze_niche(partial)
    persisted = persist(niche, deployment_id)
    return persisted
```

## Out-of-niche behaviour declaration

Every niche must declare its out-of-niche behaviour. The default `undefined` is rejected by the validator. Allowed values:

| Value                  | Meaning                                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `graceful_decline`     | When the input is recognised as out-of-niche, return a calibrated low-confidence response with a flag.                    |
| `refuse`               | When the input is out-of-niche, refuse to respond and surface the niche mismatch. Common for safety-critical deployments. |
| `route_to_alternative` | When out-of-niche, route to a different specialist (used in router-of-specialists deployments).                           |

This declaration is **operational** — it determines what the deployed system actually does when the niche boundary is crossed at inference time. The architecture must implement the declared behaviour; this is not just documentation.

## Integration notes

| Stack                                 | How to integrate                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Model card / data sheet pipelines** | The niche object is a structured supplement to the model card. Where model cards describe the model, niches describe the deployment context. Both should be versioned artefacts that ship with the deployed system. |
| **MLOps / ModelOps**                  | Persist niche objects in the deployment registry. Re-specification triggers downstream re-design. Boundary monitoring at inference time uses the niche's `out_of_niche_behaviour` declaration.                      |
| **Architecture-as-code**              | Niche objects sit at the very top of the architecture spec hierarchy. Architecture choices, regime classifications, and scaling decisions all reference a specific niche version.                                   |
| **Evaluation pipelines**              | The niche specifies the in-niche benchmark. Evaluation runs against that benchmark, not against generic leaderboards. Generic-benchmark scores are demoted to secondary diagnostics.                                |
| **Router-of-specialists deployments** | Each specialist's architecture spec references its own niche; the router classifies incoming requests by niche and dispatches accordingly.                                                                          |

## Interaction with the collection

This NEXI is the **most upstream stage** of the [`bounded-cognitive-architecture`](../../../clusters/bounded-cognitive-architecture/) pipeline:

```
niche-specification ──► cognitive-regime-selection ──► capacity-first-scaling
```

Without a niche object, the downstream regime classifier and allocation policy have nothing to consume. The pattern is gating — refusing to produce a niche when the deployment is genuinely vague is the correct behaviour, even if it slows the design conversation.

The pattern also has a **standalone use** independent of the collection: even without downstream regime selection or capacity-first scaling, having a typed niche specification is what makes evaluation meaningful and out-of-niche behaviour principled. Adopting niche specification first, before deciding whether to commit to the rest of the collection, is a valid incremental adoption path.
