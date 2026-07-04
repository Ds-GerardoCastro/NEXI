# Cognitive Regime Selection

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Collection:** [`bounded-cognitive-architecture`](../../clusters/bounded-cognitive-architecture/)
>
> A design-time pattern for **classifying a deployment niche into one of three structurally distinct cognitive regimes** — passive-storage, control-enhanced, capacity-heavy — and committing to that regime's characteristic component mix. Architectures matched to their regime outperform a single architecture deployed across niches.

---

## At a glance

The default mental model for AI architecture is a single scaling axis: smaller / medium / larger, edge / mid-tier / flagship, points on the same curve. The regime model rejects that framing.

In Turner et al.'s evolutionary-optimality model, the interaction of capacity-control synergy non-monotonicity with metabolic-cost selection produces **three discrete attractors** in cognitive design space. Different deployment niches sit in different regimes, and the optimal architecture for each regime is **structurally distinct** — not just smaller / larger versions of the same shape.

The three regimes:

| Regime               | Niche signature                                                                      | Cognitive signature                                                                                                     | Engineering analog                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **Passive-storage**  | Low task-payoff niche; cheap to run; rare correctness pressure.                      | Capacity in the absence of control. Sensitisation-style memory; no selective attention; no shielding from interference. | Edge / on-device retrieval. Long-context with no agentic loops. Embedding-based search.                                                      |
| **Control-enhanced** | Intermediate-payoff niche; correctness matters; budget supports moderate investment. | Capacity _and_ control both grow; control yields high marginal returns thanks to synergy.                               | Mid-tier assistants. Standard chat-with-tools. RAG + bounded agent-loops + structured tool use.                                              |
| **Capacity-heavy**   | High-payoff niche; energetically expensive nervous system; correctness premium.      | Both grow in absolute terms, but **relative** investment shifts back toward capacity. Control hits diminishing returns. | Flagship foundation models. Very long context + retrieval + episodic memory + MoE pools, with attention/reasoning depth in maintenance mode. |

The pattern is to _select_ one regime for a given deployment niche and design accordingly — not to design a single architecture and deploy it across regimes.

---

## The natural exemplar

Turner et al. (2026) derive the regime structure mathematically and provide explicit phylogenetic placements:

- **Passive-storage:** jellyfish, sea anemones — simple nerve net, sensitisation-based short-term storage, no selective attention or interference shielding.
- **Transitional:** nematodes, flatworms, tardigrades — rudimentary brain-like ganglion; can track context using multiple cues; appear to shield representations from decay; manipulating representations in memory may be out of reach.
- **Control-enhanced:** corvids, elephants, cetaceans, great apes — large brains; documented working-memory control processes including rehearsal, resistance to interference, attention control.

The empirical validation: humans and rhesus macaques fit to a hierarchical Bayesian model both fall in the **control-enhanced** regime (humans 0.26 [0.19, 0.34] proportion control; macaques 0.05 [0.02, 0.16]). This is a notable null result against the information-capacity hypothesis, which would have predicted humans to be in the capacity-heavy regime.

Implication: the regime mapping is empirical, falsifiable, and the dominant prior in the field doesn't always predict it correctly. That's a feature for an engineering pattern — it forces explicit niche specification rather than reasoning by analogy.

See [`references.md`](references.md) for the full citation chain.

---

## The pattern

**Standard architecture selection:**

```
Task description
        │
        ▼
"Use the latest flagship model"
or "use a smaller efficient model"
        │
        ▼
One architecture, scaled along a single axis,
deployed across distinct deployment niches
```

**Regime-conditional architecture selection:**

```
Niche specification (typed object)
        │
        ▼
Regime classifier (Turner et al. fitness landscape)
        │
        ├── passive-storage    ──► storage-only architecture
        ├── control-enhanced   ──► balanced architecture
        └── capacity-heavy     ──► capacity-dominant architecture
        │
        ▼
Phase-boundary check: is the niche near a regime boundary?
If yes — flag for monitoring; plan for regime drift.
        │
        ▼
Regime-specific component mix recommendation
```

The boundary check matters: phase-like transitions between regimes are real. A niche that crosses from control-enhanced to capacity-heavy may benefit from a _qualitative_ architectural change, not just more parameters.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — components, interfaces, the regime-mapping function, and integration with deployment-tier infrastructure.

In summary, three components:

1. **Niche-parameter intake.** Accepts the typed niche object from upstream (produced by [`niche-specification`](../niche-specification/)).
2. **Regime classifier.** Maps niche parameters (relative benefit, cue reliability, task complexity) to one of three regimes plus a boundary-distance score.
3. **Component-mix recommender.** Given the classified regime + budget constraints, recommends the regime's characteristic component mix.

**Cross-tier rule:** an architecture optimal for one tier is **not** a strict superset of architectures optimal for the tier below. A flagship is not a "scaled-up edge model." The component mixes differ structurally.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for an engineering-agent doing design-time regime classification:

- **System-prompt fragment** that instructs the agent to classify a niche into a discrete regime, not to interpolate.
- **Tool definitions** for `gather_niche_parameters`, `classify_regime`, `recommend_component_mix`.
- **Boundary-flag pattern** for niches near regime boundaries — flag for drift monitoring rather than over-trusting the classification.
- **Translation notes** for Claude skills, OpenAI function calling, MCP tools, LangChain / LlamaIndex.

---

## When to use

- Any deployment-tier or model-family decision where deployment niches differ in task payoff, cost budget, signal reliability, or task complexity enough to fall in different regimes.
- Multi-tier model-family planning (edge / mid-tier / flagship) where you want each tier to be structurally appropriate, not just smaller / larger.
- Architecture-selection conversations where the implicit answer is "use the latest model everywhere" — the regime classifier is designed to push back on that with structural reasons.
- Decisions about whether a given deployment should add agentic-loop sophistication vs. expand its retrieval/memory surface.

## When not to use

- When deployment niches are too similar to fall in different regimes (the classifier collapses to a single answer; the pattern adds overhead without payoff).
- When architecture is fixed upstream by external constraints (existing model family, organisational lock-in, regulatory requirement). Regime classification becomes informational only.
- When the niche is genuinely on a regime boundary. Pick the closer regime, monitor for drift, plan migration. Do not over-trust the classification at boundaries.
- When the niche has not been specified. Regime selection requires a typed niche object as input — invoke [`niche-specification`](../niche-specification/) first.

## Tradeoffs

- **Architectural discontinuities across deployment tiers** complicate code-sharing. A regime-disciplined organisation accepts that an edge model and a flagship are different architectures, not the same architecture at different sizes.
- **Phase-boundary handling adds operational complexity** — boundary flags, drift monitoring, planned migration. Niches drift over their lifetime and the regime they fit may change.
- **The regime taxonomy is opinionated.** Three regimes emerges from Turner et al.'s specific synergy non-monotonicity. A different cost function or synergy shape might produce more or fewer attractors. Future versions of the NEXI may revise the count if catalog evidence accumulates against three.

## Falsifiable hypothesis

> At matched cost budget, regime-matched architectures (passive-storage, control-enhanced, or capacity-heavy as appropriate) outperform a single one-size-fits-all architecture deployed across distinct niches on niche-specific evaluation. Refutation: if regime-matched and uniform architectures perform indistinguishably across genuinely distinct niches at matched cost, the discrete-regime structure is not architecturally consequential.

A second testable claim: **regime changes produce qualitative — not just quantitative — architectural component-mix differences**. Re-classifying a deployment from one regime to another should yield structural component-mix differences, not just hyperparameter shifts. If only hyperparameter shifts result, the regime taxonomy is descriptive but not prescriptive.

## References

See [`references.md`](references.md) for the full citation chain — Turner et al. 2026 as primary source, plus computational analogs in deployment-tier reasoning, model-family scaling, regime-switching dynamical systems, phase-transition models, and architecture-as-niche-fit literature in NAS.
