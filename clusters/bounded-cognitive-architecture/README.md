# Bounded Cognitive Architecture

> **Cluster status:** draft · **Members:** 3 · **Audience:** builder
>
> A coherent intelligence model for **designing AI architectures under cost constraint, conditional on the deployment niche**. The cluster groups three patterns that together form a design-time pipeline: niche specification → regime classification → capacity-first allocation.

> **Adopting this collection.** Its patterns are **independently adoptable** — take one, several, or mix them with patterns from other collections. This page groups them because they were read from the same biological system and reinforce each other; it is a **reading path and provenance record, not a required bundle**. The system-level hypothesis below is a **falsifiable research claim** — that the whole outperforms any proper subset — offered as something to test, not a guarantee to the adopting engineer. If it is refuted, the member patterns remain individually valid.

---

## Why this cluster exists

In current AI practice, "scaling" usually means a single decision: more parameters, more compute, more data. That works on the way up the curve and obscures three structural facts about cognition that hold across biological systems:

1. **Cognition is allocation under cost.** Storage and regulation are finite resources paid for in metabolism (in nature) or compute / latency / dollars (in AI). The right architecture depends on the cost function.
2. **The deployment niche shapes the optimum.** A small edge model in a low-payoff niche, a mid-tier assistant in a control-rewarding niche, and a flagship in a high-payoff niche are _structurally distinct_ designs — not points on the same scaling curve.
3. **Storage capacity is prerequisite.** Regulation (attention, reasoning, agentic loops) cannot operate without storage to act on. Capacity contributes linearly to recall efficacy; control contributes sublinearly.

Turner et al. (2026) [Cognitive capacity and control in the evolution of intelligence](https://doi.org/10.1101/2026.03.07.710317) derive these facts as evolutionary-optimality results in a mathematical model of working-memory selection, then cross-validate with retro-cue task data from humans and rhesus macaques. Independently, the zebra-finch communication-networks literature shows niche-conditional cognitive design in a wild non-mammalian system. This cluster translates the convergent biological pattern into an engineerable AI design-time pipeline.

## Member NEXIs

| Slug                                                                   | Name                       | Role in the pipeline                                                                                                                                                                        |
| ---------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`niche-specification`](../../nexi/niche-specification/)               | Niche Specification        | **Specify the niche.** Produces a typed niche object (task structure, signal environment, resource envelope, error profile, social surround, evaluation protocol). Most upstream step.      |
| [`cognitive-regime-selection`](../../nexi/cognitive-regime-selection/) | Cognitive Regime Selection | **Classify the regime.** Maps the niche to one of three discrete attractors: passive-storage, control-enhanced, capacity-heavy. Recommends the regime's characteristic component mix.       |
| [`capacity-first-scaling`](../../nexi/capacity-first-scaling/)         | Capacity-First Scaling     | **Allocate the budget.** Within the regime's component mix, scale capacity components (context, retrieval, memory) before scaling control components (attention, reasoning, agentic depth). |

## How the patterns compose

```
   ┌────────────────────────┐
   │  niche-specification   │  ← typed niche object (the entry point)
   └────────────────────────┘
                │
                ▼
   ┌────────────────────────┐
   │ cognitive-regime-      │  ← regime ∈ {passive-storage,
   │  selection             │     control-enhanced, capacity-heavy}
   └────────────────────────┘
                │
                ▼
   ┌────────────────────────┐
   │ capacity-first-scaling │  ← allocation policy under budget
   └────────────────────────┘
                │
                ▼
   ┌────────────────────────┐
   │ in-niche evaluation    │  ← measure success in the specified niche,
   │ (NOT generic           │     not on a generic benchmark
   │  benchmark)            │
   └────────────────────────┘
```

The pipeline is **strict** in the sense that each stage's output is the next stage's typed input. Skipping niche specification leaves regime selection without an input. Skipping regime selection leaves capacity-first allocation without an architectural target. Skipping capacity-first leaves the regime as a tier-label without an allocation policy.

## What this cluster claims (system falsifiable hypothesis)

> Architectures designed using the full pipeline (niche specification → regime classification → capacity-first allocation) outperform same-budget architectures designed via single-axis scaling on niche-specific evaluation, by a margin larger than the sum of individual-NEXI gains. Refutation: if pipeline-designed systems perform no better than the best individual-NEXI baseline at matched compute, the cluster's compositional claim is refuted (the patterns may still be individually useful as standalone NEXIs).

This is a stronger claim than "each pattern helps in isolation." The bet is that **composition is load-bearing** — the design-time discipline of forcing niche specification before regime selection before allocation, in that order, produces architectures that single-pattern application does not.

## Comparison with the other cluster

The catalog's first cluster, [`distributed-social-cognition`](../distributed-social-cognition/), is a **constellation** — five mutually-enabling runtime patterns that all run during inference (eavesdropping, identity-by-pattern, multi-modal-integration, context-bound-semantics, social-hotspots). Removing any one degrades the rest, but they execute in parallel in a deployed system.

This cluster is structurally different: a **pipeline** of _design-time_ patterns. They run before the deployed system exists, in sequence, each producing the input for the next. The two cluster shapes — constellation and pipeline — are both legitimate and the schema accommodates both via `complementarity_notes`.

## When to adopt

- Any architecture-design or deployment-tier decision where deployment niche, cost budget, signal environment, or error tolerance differ across deployments.
- Production AI systems serving specific contexts (vs. exploratory research).
- Multi-tier model-family planning (edge / mid-tier / flagship).
- Decisions about whether to scale context, retrieval, attention sophistication, or agentic-loop depth.
- Any time the implicit answer is "general purpose for everyone" — that's the situation the niche-specification step is designed to push back on.

## When not to adopt

- Foundation-model pretraining — that is substrate construction, not niche-bound design.
- Deployments where architecture is fixed upstream by external constraints.
- Multi-niche services where a router-of-niche-specialists is more appropriate than a single niche commitment.
- Research / exploratory architectures deliberately operating without deployment commitments.

## Tradeoffs

Pipeline-discipline imposes design-time overhead — niche specification, regime classification, capacity-tagging — that ad-hoc scaling avoids. Architectural discontinuities across deployment tiers complicate code-sharing and shared maintenance. In return, decisions become principled, evaluation becomes meaningful, and downstream components compose rather than collide.

The cluster's strongest critique of common practice is that **"scaling" as currently framed elides niche-binding**. A single scaling curve abstracted from deployment context is exactly the framing this cluster rejects.

## Natural exemplars

| Source                                                                                                                              | What it contributes                                                                                                                                                                                                                                                                                    |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Turner et al. 2026](https://doi.org/10.1101/2026.03.07.710317) — _Cognitive capacity and control in the evolution of intelligence_ | Mathematical model deriving regime structure + capacity-first ordering + metabolic-cost framing. Empirical validation via retro-cue task on humans and macaques. Phylogenetic placements across jellyfish, sea anemones, nematodes, flatworms, tardigrades, corvids, elephants, cetaceans, great apes. |
| Hagedoorn et al. 2026 — _Communication Networks of Wild Zebra Finches_ (bioRxiv preprint)                                           | Independent biological evidence for niche-conditional cognitive design — fission-fusion social architecture as response to arid-zone non-stationarity; same signal type takes different function in different contexts.                                                                                |

## Related work in current AI

- **Chinchilla compute-optimal scaling** (Hoffmann et al. 2022). The data-vs-parameters allocation result is consistent with capacity-first when read as "data is a capacity expansion."
- **Long-context architectures** — RoPE, ALiBi, sparse attention, FlashAttention. Capacity expansion at low marginal control cost.
- **Retrieval-augmented generation** — REALM, RAG, RETRO. External capacity store that the regime classifier would assign to the control-enhanced or capacity-heavy regime depending on payoff.
- **Mixture-of-Experts** — capacity scaling via expert pool size; the Switch Transformer empirical pattern (expert count grows faster than routing sophistication) is consistent with the rule.
- **No Free Lunch theorems** (Wolpert & Macready 1997). Formal grounding for the niche-specification step — no algorithm dominates across all problem distributions.

## See also

- Cluster cousin: [`distributed-social-cognition`](../distributed-social-cognition/) — the constellation-shaped runtime cluster from the zebra-finch source.
- Catalog index: [`../../CATALOG.md`](../../CATALOG.md).
- Methodology: [`../../docs/methodology.md`](../../docs/methodology.md).
- What a NEXI is: [`../../docs/what-is-a-nexi.md`](../../docs/what-is-a-nexi.md).
