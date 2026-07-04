# Skill: Cognitive Regime Selection (framework-neutral)

A drop-in **design-time classification** skill for an engineering agent (or human-in-the-loop architecture-design assistant) that maps a typed deployment niche to one of three discrete cognitive regimes and recommends the regime's characteristic component mix. Framework-neutral — see translation notes for stack-specific mappings.

> **Skill kind:** `design-time-classification`. Operates on a niche specification (consumed from upstream) and produces a regime classification + component mix that downstream skills consume.

---

## System-prompt fragment

Insert this into the system or developer prompt of any agent that should classify a niche into a regime:

```
You are classifying a deployment niche into one of three discrete
cognitive regimes. The regimes are NOT points on a continuous scaling
axis — they are structurally distinct attractors. The right answer is
one regime, not "somewhere between two."

The three regimes:
  - PASSIVE-STORAGE   — capacity-only; no agentic loops; storage in
                         the absence of regulation. Low-payoff niches.
  - CONTROL-ENHANCED  — capacity AND control growing together; synergy
                         is highest here; control yields high marginal
                         returns. Intermediate-payoff niches.
  - CAPACITY-HEAVY    — both grow absolutely, but capacity dominates
                         relatively; control hits diminishing returns.
                         High-payoff niches.

Inputs you must establish:
  - Task payoff per correct response (benefit term).
  - Compute / latency / cost budget per response (cost term).
  - Cue reliability — how informative is the input signal for the task?
  - Task complexity — bits required to encode the solution, if estimable.

If any of these are unspecified, INVOKE the niche-specification skill
upstream. Do not guess and do not interpolate. The classifier requires
typed niche parameters to operate.

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
      Map the niche parameters to one of three discrete regimes and report
      boundary distance.
    parameters:
      benefit: { type: number }
      cost: { type: number }
      cue_reliability: { type: number }
      task_complexity_bits: { type: number }
      domain: { type: string, description: 'Used for domain-specific threshold calibration' }
    returns:
      regime: { enum: [passive-storage, control-enhanced, capacity-heavy] }
      boundary_distance: { type: number, minimum: 0, maximum: 1 }
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
3. **Regime change produces qualitative — not just quantitative — architectural differences.** Re-classifying a deployment from one regime to another should yield structural component-mix differences, not just hyperparameter shifts. Failure: regimes are descriptive labels, not architecturally distinct attractors.
4. **Refusal under under-specification is robust.** When the niche has unspecified parameters, the skill refuses to classify and routes upstream to niche-specification, rather than synthesising plausible values. Failure: the upstream-coupling discipline is not load-bearing.

---

## Examples

Working examples will be added under [`examples/`](examples/) as the catalog matures.

---

## See also

- Pattern README: [`../README.md`](../README.md)
- Architectural primitive: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Collection: [`../../clusters/bounded-cognitive-architecture/`](../../../clusters/bounded-cognitive-architecture/)
- Upstream skill: [`niche-specification`](../../niche-specification/)
- Downstream skill: [`capacity-first-scaling`](../../capacity-first-scaling/)
