# Skill: Cognitive Regime Selection (framework-neutral)

A drop-in **design-time classification** skill for an engineering agent (or human-in-the-loop architecture-design assistant) that maps a typed deployment niche to a position on a continuous optimality surface, reads off the nearest of three qualitatively distinct cognitive regimes, and recommends that regime's characteristic component mix. Framework-neutral — see translation notes for stack-specific mappings.

> **Skill kind:** `design-time-classification`. Operates on a niche specification (consumed from upstream) and produces a regime classification (nearest region on a continuous surface + a continuous control-share estimate) plus a component mix that downstream skills consume.

---

## System-prompt fragment

Insert this into the system or developer prompt of any agent that should classify a niche into a regime:

```
You are locating a deployment niche on a CONTINUOUS optimality surface
and reading off which of three qualitatively distinct regions it lands
in. The regions are NOT smaller/larger versions of one shape — their
component mixes differ qualitatively — but they sit on a continuous
surface with SOFT boundaries. Report the nearest region AND how close
the niche is to a boundary; a niche can legitimately sit near a border.

The three regions:
  - PASSIVE-STORAGE   — capacity-only; no agentic loops; storage in
                         the absence of regulation. Low-payoff niches;
                         control share ~0.
  - CONTROL-ENHANCED  — capacity AND control growing together; synergy
                         is highest here; control yields high marginal
                         returns. Intermediate-payoff niches with a
                         reliable-enough cue and moderate complexity.
  - CAPACITY-HEAVY    — both grow absolutely, but capacity dominates
                         relatively; control hits diminishing (sublinear)
                         returns. High-payoff niches; control share falls
                         back toward capacity.

All FOUR inputs matter to the placement — not payoff/cost alone:
  - Task payoff per correct response (benefit term).
  - Compute / latency / cost budget per response (cost term).
  - Cue reliability q — how informative is the input signal? Low q
    SUPPRESSES the synergy gain and can move a niche OUT of
    control-enhanced even at unchanged benefit/cost.
  - Task complexity m — bits / items to hold. High m raises the capacity
    requirement and pushes the control share DOWN.

Synergy is NON-MONOTONIC: control earns little when total investment is
too small OR too large, and peaks in a mid band. Do not treat this as a
single monotone benefit/cost ramp.

If any of these are unspecified, INVOKE the niche-specification skill
upstream. Do not guess. The classifier requires typed niche parameters
to operate.

Outputs you must produce:
  - The recommended regime.
  - The component mix characteristic of that regime.
  - Phase-boundary flags: if the niche is near a regime boundary, say
    so explicitly and recommend monitoring for regime drift.
  - Adjacent regime: which way would the niche drift to.

Do NOT recommend a "scaled-up" version of an architecture from a lower
regime. Regime change is qualitative; cross-regime architectures differ
structurally, not just in size.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: gather_niche_parameters
    description: >
      Extract the four niche parameters required for regime classification
      from the typed niche object produced by the niche-specification skill.
    parameters:
      niche: { type: object, description: 'Typed niche object' }
    returns:
      benefit: { type: number, description: 'Task payoff per correct response' }
      cost: { type: number, description: 'Cost per response' }
      cue_reliability: { type: number, minimum: 0, maximum: 1 }
      task_complexity_bits: { type: number }
      confidence: { enum: [low, medium, high] }
      unspecified_fields: { type: array, items: { type: string } }

  - name: classify_regime
    description: >
      Estimate the niche's optimal control share γ*/(κ*+γ*) on a continuous
      optimality surface from ALL FOUR inputs (benefit, cost, cue reliability,
      task complexity), reproducing the non-monotonic synergy, then return the
      nearest of three regions plus boundary distance. Cue reliability and task
      complexity materially affect the classification — not benefit/cost alone.
    parameters:
      benefit: { type: number }
      cost: { type: number }
      cue_reliability:
        {
          type: number,
          minimum: 0,
          maximum: 1,
          description: 'q — scales the synergy gain; low q can move a niche out of control-enhanced',
        }
      task_complexity_bits:
        {
          type: number,
          description: 'm — raises the capacity requirement; high m pushes control share down',
        }
      domain:
        {
          type: string,
          description: 'Used for per-domain calibration of the synergy shape and region boundaries',
        }
    returns:
      regime:
        {
          enum: [passive-storage, control-enhanced, capacity-heavy],
          description: 'Nearest region on a continuous surface, not a discrete id',
        }
      control_share_estimate:
        {
          type: number,
          minimum: 0,
          maximum: 0.5,
          description: 'Continuous position s = γ*/(κ*+γ*)',
        }
      boundary_distance:
        {
          type: number,
          minimum: 0,
          maximum: 1,
          description: 'Distance to nearest soft region boundary',
        }
      adjacent_regime: { enum: [passive-storage, control-enhanced, capacity-heavy, none] }
      rationale: { type: string }
      warnings: { type: array, items: { type: string } }

  - name: recommend_component_mix
    description: >
      Produce the architecture component mix characteristic of the classified
      regime, conditioned on the budget envelope.
    parameters:
      regime: { enum: [passive-storage, control-enhanced, capacity-heavy] }
      budget_constraints: { type: object }
    returns:
      capacity_components:
        type: array
        items:
          type: object
          properties:
            name: { type: string }
            share: { type: number }
            rationale: { type: string }
      control_components:
        type: array
        items:
          type: object
          properties:
            name: { type: string }
            share: { type: number }
            rationale: { type: string }
      warnings: { type: array, items: { type: string } }
      structural_distinction_note:
        { type: string, description: 'How this mix differs structurally from adjacent regimes' }

  - name: monitor_drift
    description: >
      For deployed systems with periodically updated niche metadata,
      detect when the niche has drifted across a regime boundary and
      recommend architecture migration.
    parameters:
      deployment_id: { type: string }
      current_niche_version: { type: string }
      previous_niche_version: { type: string }
    returns:
      drift_detected: { type: boolean }
      from_regime: { type: string }
      to_regime: { type: string }
      migration_plan: { type: object }
```

---

## Memory pattern

Regime classifications persist as deployment-scoped artefacts:

```yaml
deployment_regime_memory:
  - deployment_id: <id>
    niche_version: <semver>
    regime: <passive-storage | control-enhanced | capacity-heavy>
    boundary_distance: <number>
    adjacent_regime: <regime>
    classified_at: <iso8601>
    component_mix: <recommendation>

    # Drift history
    drift_events:
      - from_niche_version: <semver>
        to_niche_version: <semver>
        from_regime: <regime>
        to_regime: <regime>
        migration_status: <planned | in-progress | complete>
```

Drift events with `migration_status: complete` create a feedback signal: did the regime-migrated architecture actually outperform the pre-migration architecture on niche-specific evaluation? Outcome data refines threshold calibration over time.

---

## Translation notes

| Stack                                               | Mapping                                                                                                                                                                                            |
| --------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude skills**                                   | `~/.claude/skills/regime-selection/SKILL.md`. The classification tools become Claude tool definitions; the system-prompt fragment goes in `system_prompt_addition`.                                |
| **OpenAI function calling**                         | Tools become OpenAI function schemas. The system-prompt fragment is concatenated to the design-time-review system message.                                                                         |
| **MCP tools**                                       | Each tool becomes an MCP `tool.json`. Drift monitoring can run as a periodic MCP-server-driven task.                                                                                               |
| **LangChain / LlamaIndex agents**                   | Tools become `Tool` objects; system-prompt fragment goes in the agent prefix. The classifier output can flow into a downstream LangChain `Chain` for capacity-first allocation.                    |
| **MLOps platforms** (Vertex AI, SageMaker, Bedrock) | Surface niche parameters as deployment-spec metadata; expose the regime classifier as a deploy-time annotation service. Architecture configs reference the regime classification by deployment_id. |

---

## Evaluation signals (falsifiable claims)

The skill's classifications should pass these falsification tests:

1. **Regime-matched architectures outperform one-size-fits-all at matched cost on niche-specific evaluation.** When the skill recommends architecture A for niche 1 and architecture B for niche 2, deploying A on niche 1 and B on niche 2 should outperform a single architecture deployed on both. Failure: weakens the prescriptive value of the regime taxonomy.
2. **Boundary flags predict regime drift.** When the skill flags a niche as near a regime boundary, observed deployments in that niche cross regimes more frequently than for deep-in-regime niches. Failure: the boundary-distance signal is not informative.
3. **Regime change produces qualitative — not just quantitative — architectural differences.** Re-classifying a deployment from one region to another should yield structural component-mix differences, not just hyperparameter shifts. Failure: the regions are descriptive labels only, and a single monotone scaling axis would have sufficed.
4. **Refusal under under-specification is robust.** When the niche has unspecified parameters, the skill refuses to classify and routes upstream to niche-specification, rather than synthesising plausible values. Failure: the upstream-coupling discipline is not load-bearing.

---

## Examples

Working examples will be added under [`examples/`](examples/) as the catalog matures.

---

## See also

- Pattern README: [`../README.md`](../README.md)
- Architectural primitive: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Collection: [`../../collections/bounded-cognitive-architecture/`](../../../collections/bounded-cognitive-architecture/)
- Upstream skill: [`niche-specification`](../../niche-specification/)
- Downstream skill: [`capacity-first-scaling`](../../capacity-first-scaling/)
