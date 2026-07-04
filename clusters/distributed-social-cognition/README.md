# Distributed Social Cognition

> **Collection status:** template · **Members:** 5 patterns · **Audience:** builder
>
> *An intelligence model in which an agent builds and maintains models of its peers under partial observability, by combining observation of third-party interactions, identity-from-pattern, multi-modal grounding, context-bound interpretation, and spatial information aggregation.*

> **Adopting this collection.** Its patterns are **independently adoptable** — take one, several, or mix them with patterns from other collections. This page groups them because they were read from the same biological system and reinforce each other; it is a **reading path and provenance record, not a required bundle**. The system-level hypothesis below is a **falsifiable research claim** — that the whole outperforms any proper subset — offered as something to test, not a guarantee to the adopting engineer. If it is refuted, the member patterns remain individually valid.

---

## At a glance

This collection is a recipe, not an ingredient. It tells you what an AI system needs in combination to do **sample-efficient social inference** — building useful models of other agents without exhaustive direct interaction with each one. Picking any single member pattern in isolation gives you partial benefit; the collection claims a synergistic effect that subsetting cannot reproduce.

| Question | Short answer |
| --- | --- |
| **Adopt this collection when** | You have multiple agents in a shared environment, partial observability, and tasks that depend on inferring others' goals / knowledge / relationships. |
| **Skip it when** | Single-agent, adversarial, privacy-sensitive, or compute-strictly-bound. |
| **What it adds** | Cheap, sample-efficient social-state inference at scale. |
| **What it costs** | Five co-dependent components to engineer, multiplied compute over a baseline agent. |

---

## The natural exemplar

Wild **zebra finches** (*Taeniopygia castanotis*) in the Australian arid zone implement all five member patterns simultaneously. In their social hotspots — locations where many individuals converge in unpredictable timing — they:

- **Eavesdrop** on songs and interactions among other finches.
- **Identify** specific individuals from distinctive song motifs.
- **Integrate** acoustic signals with spatial co-occurrence.
- **Bind meaning** to context — the same song serves different functions in a breeding colony than in a hotspot.
- **Aggregate** information at the hotspot itself, which functions as a structured social hub rather than an anonymous gathering.

Removing any one capability would degrade the others. A finch that cannot identify singers cannot use what it eavesdrops; a finch that cannot bind context misreads the meaning; a finch unaware of hotspot density misses where observation pays off most.

This is the empirical case for treating these patterns as a *system* rather than as a list.

---

## The system

```
                        ┌────────────────────────────────┐
                        │   social-hotspots              │
                        │   (where observation is dense) │
                        └────────────────────────────────┘
                                       ▲
                                       │ provides high-density
                                       │ observation opportunities for
                        ┌────────────────────────────────┐
                        │   eavesdropping                │
                        │   (extract info from observed  │
                        │    third-party interactions)   │
                        └────────────────────────────────┘
                            ▲                        ▲
            requires        │                        │   requires
   ┌───────────────────────────────┐   ┌─────────────────────────────────┐
   │   identity-by-pattern         │   │   context-bound-semantics       │
   │   (who is in this exchange?)  │   │   (what does it mean here?)     │
   └───────────────────────────────┘   └─────────────────────────────────┘
                            ▲                        ▲
                  amplified by             provides context for
                            │                        │
                        ┌────────────────────────────────┐
                        │   multi-modal-integration      │
                        │   (acoustic + spatial confirm  │
                        │    each other)                 │
                        └────────────────────────────────┘
```

---

## Member patterns

| NEXI | Role in the collection | Status |
| --- | --- | --- |
| [`eavesdropping`](../../nexi/eavesdropping/) | Mechanism: extract information from observed third-party interactions. | template |
| [`identity-by-pattern`](../../nexi/identity-by-pattern/) | Identity layer: attribute what is observed to specific individuals from sensory signatures. | draft |
| [`multi-modal-integration`](../../nexi/multi-modal-integration/) | Cross-channel grounding: combine acoustic and spatial (or other modality pairs) so identity and observation are mutually confirmed. | draft |
| [`context-bound-semantics`](../../nexi/context-bound-semantics/) | Interpretation layer: bind meaning to context, including reasoning from absence (negative evidence). | draft |
| [`social-hotspots`](../../nexi/social-hotspots/) | Spatial substrate: aggregate observation where interaction density is highest. | draft |

---

## When to adopt the collection

- ✅ Multi-agent settings with shared, partially observable environment.
- ✅ Tasks where modelling peers matters: cooperative coordination, opponent modelling, social inference, role-aware delegation.
- ✅ Direct interaction is costly, infrequent, or noisy; population size is moderate (small enough that observation is tractable, large enough that eavesdropping adds signal).
- ✅ You can afford the engineering complexity of co-dependent components.

## When not to adopt

- ❌ Single-agent settings.
- ❌ Adversarial or privacy-sensitive contexts — observation creates attack surface, and observed peers may signal deceptively.
- ❌ Strict compute constraints — the collection multiplies cost by a constant factor (more encoders, larger observation streams, spatial memory).
- ❌ Tasks where direct experience suffices.

---

## Tradeoffs

- **Compute and memory:** the collection scales worse than a baseline agent. Attention scales with observable population (eavesdropping), embeddings must preserve particularity (identity), interpretation runs context-conditionally (semantics), spatial memory must be queried (hotspots).
- **Engineering complexity:** five co-dependent components mean more surface area to debug. The complementarity is the win, but it also means failures cascade — break any one component, and the others underperform.
- **Subsettability:** if you adopt only a subset, the collection's synergy claim does not apply, and you should expect closer to additive (or below-additive) gains from the patterns you do adopt.

---

## System-level falsifiable hypothesis

> **H_sys.** Multi-agent systems that adopt the full distributed-social-cognition collection outperform systems that adopt any proper subset of its member patterns on cooperative social-inference benchmarks at equal training compute, by a margin larger than the sum of the individual-pattern gains.
>
> **Operationalisation.** On a benchmark suite of N ≥ 3-agent partially-observable cooperative tasks (Hanabi, Overcooked-AI multi-agent variants, social-inference benchmarks), measure performance for: (a) baseline (none of the patterns), (b) each member pattern alone, (c) all proper subsets, (d) the full collection. The collection's gain over baseline should exceed the sum of single-pattern gains over baseline by a measurable margin (≥10%). Each subset-vs-collection comparison should show a degradation when *any* member is removed.
>
> **Refutation.** If subsetting the collection never produces degradation beyond the additive sum of individual-pattern losses, the synergy claim is refuted — the patterns are independently useful but the collection does not constitute a coherent intelligence model.

This hypothesis is *stronger* than any single member NEXI's hypothesis. The collection is making a claim about the system, not about any one part.

---

## Theoretical background

The collection generalises a pattern observed in studies of communication networks in animal-communication ecology — see references in each member NEXI's `references.md`. The key theoretical commitment is that **information about agents is jointly accessible from observation, identity, context, multi-modal grounding, and spatial structure** — and that no single one of these channels suffices.

This contrasts with two prevalent AI defaults:

1. **Single-agent baselines** that ignore peer-modelling entirely.
2. **Bolt-on attention** that adds opponent-modelling as a post-hoc layer over an architecture not designed to support it.

The collection reframes peer-modelling as a *first-class architectural commitment*, distributed across components that mutually enable each other.

---

## Boundary conditions

- The collection specifies **observation-and-interpretation** of peers, not action policy. What an agent *does* with the inferred peer-models — when to cooperate, when to defer, when to deceive — is a separate design problem downstream.
- The collection assumes *honest* observation (peers do not actively deceive observers). Adversarial robustness is out of scope and is a known failure mode.

---

## Related

- **Vault provenance (private):** consolidation hubs `Eavesdropping`, `Multi-Modal Integration`, `Context-Dependent Semantics`; metamodels MM1, MM2, MM3, MM4.
- **Member NEXIs:** see the table above.
- **Related clusters:** *(none yet — will populate as catalog grows)*
