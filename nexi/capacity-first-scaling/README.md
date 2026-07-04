# Capacity-First Scaling

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Collection:** [`bounded-cognitive-architecture`](../../collections/bounded-cognitive-architecture/)
>
> A scaling rule for cognitive systems: **expand storage capacity before scaling control sophistication**. Capacity contributes linearly to a system's effective ability to maintain useful representations under noise; control contributes sublinearly with severe diminishing returns. Without capacity, control has no substrate to operate on.

---

## At a glance

When you have a fixed budget increase to spend on an AI architecture — more parameters, more compute, more memory — the implicit question is: where does it go? The dominant practice scales components together, often with the control axis (attention sophistication, agentic-loop depth, reasoning chain length) outpacing the capacity axis.

The capacity-first rule says that's backwards near the capacity-bound regime. When the deployment niche has task complexity at or above existing capacity, an additional unit of capacity (longer context, larger retrieval store, more memory tokens, more MoE experts) returns more recall efficacy than an additional unit of control (more attention heads, deeper reasoning, more agentic-loop iterations).

The reason is structural, not empirical. In the formal model, capacity contributes **linearly** to the system's ability to concentrate resources around an optimal allocation; control contributes **sublinearly**. The asymmetry is not a tuning quirk — it falls out of how stochastic processes behave when the resource budget is finite.

---

## The natural exemplar

Turner et al. (2026) build a mathematical model of working-memory evolution. Capacity κ is the total resource budget for storing item representations; control γ is the rate at which the system drives current allocations toward an optimal target despite noise. The model derives evolutionary optima under a fitness function that subtracts metabolic cost from expected recall.

Two results from the model are directly load-bearing for this NEXI:

1. **Capacity is prioritised across all metabolic-benefit levels.** Evolution invests in capacity before it invests in control because control without storage has no substrate. This holds robustly except in a regime where control is _substantially_ cheaper per unit than capacity — empirically unlikely for nervous tissue.
2. **Capacity contributes linearly to recall, control sublinearly.** Specifically, with regard to the system's ability to concentrate resources around the optimal allocation, capacity scaling produces linear gains while control scaling hits severe diminishing returns.

The model also coheres with the comparative-neuroscience record of major brain-evolution transitions, where storage capabilities expand before regulation sophistication does.

See [`references.md`](references.md) for the full citation chain.

---

## The pattern

**Standard scaling decision:**

```
Budget increase ΔB
        │
        ▼
"Throw more parameters at it"
        │
        ▼
Components scale jointly with parameter count
(capacity and control entangled)
```

**Capacity-first scaling:**

```
Budget increase ΔB
        │
        ▼
Decompose architecture into CAPACITY and CONTROL
components (tag each)
        │
        ▼
Estimate task complexity in bits (the niche threshold)
        │
        ▼
If capacity < threshold:
        scale CAPACITY components first
        (context, retrieval, memory, MoE expert pool)
Else if intermediate-investment regime:
        balanced allocation, exploiting synergy
Else:
        capacity-leaning allocation;
        control hits diminishing returns
```

The non-trivial choice is the **decomposition**. Some components are obviously capacity (context window, retrieval store) or obviously control (reasoning depth, agentic-loop cap). Others are **mixed** (attention with KV-cache — capacity in the cache, control in the attention computation) and require explicit decomposition. The skill spec in [`skill/skill.md`](skill/skill.md) automates this for an architecture-review agent.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — how to tag components, how to estimate task complexity, and how to apply the rule under different cost asymmetries between capacity and control.

In summary, three components:

1. **Component tagger.** Classifies each named component of an architecture as `capacity`, `control`, or `mixed`. Mixed components require sub-decomposition.
2. **Niche threshold estimator.** Estimates the task complexity in bits for the deployment, providing the threshold against which existing capacity is judged.
3. **Allocation policy.** Given a budget increase and the tagged decomposition, recommends where to spend it — capacity-first when below threshold, regime-conditional balance when above.

The pattern composes downstream of [`cognitive-regime-selection`](../cognitive-regime-selection/) (which gives the regime within which capacity-first applies) and of [`niche-specification`](../niche-specification/) (which gives the niche from which the threshold is derived).

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for an engineering-agent or human-in-the-loop architecture-review:

- **System-prompt fragment** that instructs the agent to apply the rule before recommending any scaling decision.
- **Tool definitions** for `tag_components`, `estimate_task_complexity`, and `recommend_allocation`.
- **Memory pattern** for persisting tagged decompositions across architecture-review sessions.
- **Translation notes** for mapping the spec onto Claude skills, OpenAI function calling, MCP tools, and LangChain / LlamaIndex agents.

---

## When to use

Any architecture-design or scaling decision under a fixed budget increase, especially when the deployment's task complexity is at or above existing capacity. The rule applies most strongly **near the capacity-bound regime** — where adding storage produces outsize returns relative to adding regulation.

Specific situations where the rule is high-leverage:

- Long-document or long-context tasks where the existing context window saturates.
- Memory-intensive deployments where retrieval-store size determines task ceiling.
- Multi-tier model-family planning where the team is choosing whether to scale "thinking" or "remembering" between tiers.
- Decisions about whether to add agentic loops vs. expand the retrieval surface.

## When not to use

- Deployments where capacity already exceeds task complexity by a wide margin. The marginal returns from more capacity become small in this regime; control investment may dominate.
- Joint-scaling architectures where capacity and control scale together with parameter count without separable decisions (vanilla transformers without MoE / external memory).
- Settings where capacity-component cost grows non-linearly faster than control-component cost — full attention over very long context is the canonical example, where capacity expansion incurs O(n²) cost growth.
- When the rule's prerequisite — niche specification with task-complexity estimate — is not available. Without the threshold, "capacity is below threshold" cannot be evaluated.

## Tradeoffs

- **Decomposition discipline vs. simplicity.** Tagging every component as capacity / control / mixed costs upfront work and may surface joint components that resist clean splits. The reward is a principled allocation policy under budget changes.
- **Prerequisite-ordering vs. terminal-investment.** The rule is best stated as "capacity must be sufficient before control becomes useful" — _not_ as "always invest more in capacity than in control." Once capacity exceeds the threshold, balanced or even control-leaning allocation can be locally optimal (per Turner et al.'s empirical retro-cue result, where humans and macaques both fall in the control-enhanced regime).

## Falsifiable hypothesis

> At matched parameter / FLOP / cost budget, AI architectures that allocate marginal resources to capacity components outperform identical systems that allocate marginal resources to control components on memory-intensive and long-context evaluations by a measurable margin (≥10% improvement at matched budget). Refutation: if no systematic margin appears across an appropriate task suite, this NEXI is refuted as a scaling primitive.

A second testable claim: **below the capacity threshold, control investment yields near-zero returns**. Architectures whose effective capacity is below the task-complexity bound should see no significant performance improvement from added control. Failure to replicate would suggest control has meaningful effects without prerequisite capacity, contradicting the prerequisite-ordering claim.

## References

See [`references.md`](references.md) for the full citation chain — Turner et al. 2026 as primary source, plus computational analogs in scaling-laws (Hoffmann et al. 2022 / Chinchilla), long-context architectures (RoPE, ALiBi, FlashAttention), retrieval augmentation (REALM, RAG, RETRO), and Mixture-of-Experts (Shazeer et al. 2017, Switch Transformer / Fedus et al. 2021).
