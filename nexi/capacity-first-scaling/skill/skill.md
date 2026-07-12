# Skill: Capacity-First Scaling (framework-neutral)

A drop-in **design-time** skill for an engineering agent (or human-in-the-loop architecture-review assistant) that audits proposed AI architectures or scaling decisions against the capacity-first rule. This spec is framework-neutral — see translation notes at the bottom for mapping to specific stacks.

> **Skill kind:** `design-time-review`. Invoked during architecture-design conversations, not at runtime. The agent does not execute this skill while serving end-user requests; it executes it while _planning_ what the production system will look like.

---

## System-prompt fragment

Insert this into the system or developer prompt of any agent that should apply the capacity-first rule:

```
When reviewing an AI architecture or scaling decision, apply the
capacity-first scaling rule:

1. Decompose the architecture into named components. Tag each as
   CAPACITY (storage / representation budget — context window,
   retrieval store, KV-cache, memory tokens, MoE expert pool) or
   CONTROL (regulation / attention / reasoning / agentic depth).
   Mixed components require explicit sub-decomposition.

2. Estimate the operating niche's task complexity in bits. If not
   estimable, ask. Do not guess silently.

3. If estimated capacity is below task complexity, recommend
   capacity expansion FIRST. Only after capacity is adequate,
   recommend control expansion.

4. Beware the parameter-count trap: a single parameter-count number
   does not tell you the capacity/control split. Decompose explicitly.

5. Justify each recommendation with the linear-vs-sublinear
   contribution argument (capacity contributes linearly to recall
   efficacy; control contributes sublinearly with diminishing returns).

6. Flag any case where capacity-component cost grows non-linearly
   faster than control-component cost (e.g. quadratic full-attention
   over very long context) — in that regime the rule's cost-adjusted
   recommendation may flip.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: tag_components
    description: >
      Classify each named component of the architecture as `capacity`,
      `control`, or `mixed`. Mixed components require separate
      decomposition before allocation can proceed.
    parameters:
      components:
        type: array
        items:
          type: object
          required: [name, role]
          properties:
            name: { type: string }
            role: { type: string, description: 'What the component does' }
            current_budget_share: { type: number }
    returns:
      tagged:
        type: array
        items:
          type: object
          properties:
            name: { type: string }
            tag: { enum: [capacity, control, mixed] }
            rationale: { type: string }
            capacity_bits:
              {
                type: number,
                description: 'Estimated storage in bits; populated for capacity components (and capacity sub-parts of a decomposed mixed component), used by recommend_allocation to compare against task_complexity_bits',
              }
            decomposition:
              { type: array, description: 'If mixed, sub-components (each itself tagged)' }

  - name: estimate_task_complexity
    description: >
      Estimate the niche's task complexity in bits — the number of bits
      required to encode the solution. This is the threshold against
      which existing capacity is judged.
    parameters:
      task_description: { type: string }
      examples: { type: array, items: { type: string } }
      niche_metadata: { type: object, description: 'From upstream niche-specification' }
    returns:
      estimated_bits: { type: number }
      confidence: { enum: [low, medium, high] }
      assumptions: { type: array, items: { type: string } }

  - name: recommend_allocation
    description: >
      Given a budget increase and the tagged architecture, recommend
      how to allocate the increase between capacity and control
      components, with explicit rationale.
    parameters:
      delta_budget: { type: object }
      tagged_architecture: { type: object }
      task_complexity_bits: { type: number }
      regime:
        {
          enum: [passive-storage, control-enhanced, capacity-heavy],
          description: 'From upstream regime selection',
        }
    returns:
      recommendation:
        type: array
        items:
          type: object
          properties:
            component: { type: string }
            share: { type: number }
            rationale: { type: string }
      warnings: { type: array, items: { type: string } }
      cost_asymmetry_flag:
        {
          type: boolean,
          description: 'True if capacity-cost grows non-linearly faster than control-cost',
        }
```

---

## Memory pattern

Tagged decompositions and threshold estimates persist across architecture-review sessions. Storage shape:

```yaml
architecture_review_memory:
  - architecture_id: <id>
    version: <semver>
    tagged_components: <output of tag_components>
    last_threshold_estimate:
      bits: <number>
      niche_version: <semver>
      timestamp: <iso8601>
    allocation_history:
      - delta_budget: <object>
        recommendation: <output>
        applied: <bool>
        outcome_metric: <number> # populated post-deployment if available
```

Persisting the allocation history with outcome metrics lets future review sessions calibrate the LOW/HIGH thresholds against observed performance — a feedback loop that closes the gap between Turner et al.'s biological thresholds and the AI deployment thresholds.

---

## Translation notes

| Stack                             | Mapping                                                                                                                                                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude skills**                 | Spec lives as `~/.claude/skills/capacity-first-review/SKILL.md`. Tools become Claude tool definitions. The system-prompt fragment is included via the SKILL.md frontmatter `system_prompt_addition`. |
| **OpenAI function calling**       | Tools become OpenAI function schemas. The system-prompt fragment is concatenated to the agent's `system` message at design-time review invocations.                                                  |
| **MCP tools**                     | Each tool becomes an MCP `tool.json`. The skill is invoked when the engineering-agent connects to an MCP server exposing this NEXI's tools.                                                          |
| **LangChain / LlamaIndex agents** | Tools become LangChain `Tool` objects. The system-prompt fragment is added to the `prefix` of the agent's prompt.                                                                                    |
| **AGNTCY / cross-framework**      | Spec serialises directly to AGNTCY's framework-neutral skill format; minimal adaptation required.                                                                                                    |

---

## Evaluation signals (falsifiable claims)

The skill's recommendations should pass these falsification tests:

1. **Capacity-first outperforms control-first at matched budget.** When the skill flags capacity as below threshold and recommends capacity expansion, capacity expansion outperforms control expansion in subsequent A/B tests on memory-intensive evaluations. Failure: weakens the rule's prescriptive value.
2. **Identified capacity bottleneck predicts capacity-scaling returns.** When the skill flags capacity as below threshold, capacity expansion produces measurable performance gains; when it flags capacity as adequate, capacity expansion produces near-zero gains. Failure: the diagnostic step is not load-bearing.
3. **Parameter count alone underspecifies the recommendation.** Two architectures with equal parameter count but different capacity/control splits should receive distinct recommendations from the skill. Failure: the decomposition step is not adding signal.
4. **Mixed-component decomposition refusal is robust.** When mixed components are present, the skill refuses to produce an allocation until decomposition is provided, and that refusal correlates with subsequent allocation accuracy. Failure: decomposition is operational overhead without payoff.

---

## Examples

Working examples in popular stacks will be added under [`examples/`](examples/) as the catalog matures. For now this skill spec is reference-grade; concrete implementations are an open invitation.

---

## See also

- Pattern README: [`../README.md`](../README.md)
- Architectural primitive: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Collection: [`../../collections/bounded-cognitive-architecture/`](../../../collections/bounded-cognitive-architecture/)
- Upstream skill: [`niche-specification`](../../niche-specification/)
- Upstream skill: [`cognitive-regime-selection`](../../cognitive-regime-selection/)
