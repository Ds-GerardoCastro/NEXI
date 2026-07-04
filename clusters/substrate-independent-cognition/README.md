# Substrate-Independent Cognition

> **Cluster status:** draft · **Members:** 2 · **Audience:** builder
>
> A young cluster asking: **which architectural commitments are necessary for flexible cognition independent of the substrate that implements them — and how do we read those commitments off convergent evolution?** It groups patterns that recur across non-homologous natural substrates (neural tissues sharing no complex-brain common ancestor), treating that convergent recurrence as evidence that the pattern is a substrate-general design primitive rather than an accident of one lineage.

---

## Why this cluster exists

When two lineages that last shared an ancestor before either had a complex brain nonetheless evolve the *same* architectural feature under selection for flexible cognition, that feature is a strong candidate for being **substrate-general**: required by the problem, not by the tissue. The comparative-neuroanatomy record supplies exactly this kind of evidence. Dedicated multimodal integration centres and an expand-then-read-out circuit motif both appear — independently — in insect mushroom bodies, the octopod vertical lobe, the cichlid pallium, the corvid and psittacid avian pallium, and the mammalian isocortex. None of these are anatomical homologues.

The perceptron lineage of AI inherited one substrate (dense, homogeneous, gradient-trained layers) and treats its architectural choices as the space of possibilities. This cluster does the opposite: it starts from the features that *many* substrates converge on, on the bet that those features are the portable ones — the commitments worth carrying across to an artificial substrate precisely because nature reached them repeatedly from different starting points.

The cluster is **deliberately young**. It is seeded on a single comparative-neuroanatomy source and exists to accumulate cross-substrate architectural invariants as further sources land. Its composition claim is a hypothesis, not settled evidence.

The primary source is a comparative synthesis of how complex brains and high intelligence arose independently across five lineages ([Roth 2015](https://doi.org/10.1098/rstb.2015.0049)). The vault consolidation hubs `Convergent-Divergent Fan`, `Multi-Modal Integration`, and `Non-Human Intelligence Patterns` are the upstream of this cluster.

## Member NEXIs

| Slug                                                                     | Name                       | Layer in the architecture                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`multi-modal-integration`](../../nexi/multi-modal-integration/)         | Multi-Modal Integration    | **What-is-integrated layer.** A dedicated centre where multiple sensory streams meet in a shared latent space. Convergently evolved as an integration hub across five non-homologous lineages. **Status: canonical** — multi-source.                |
| [`expansion-readout-circuit`](../../nexi/expansion-readout-circuit/)     | Expansion-Readout Circuit  | **How-the-circuit-is-shaped layer.** The expand-then-read-out motif — a wide sparse-coded expansion sheet feeding a sparse projection readout — that implements such integration centres across phyla. **Status: draft** — single-source.           |

## How the patterns compose

```
   ┌─────────────────────────────────────────────────────────┐
   │              multi-modal-integration                     │
   │   (WHAT is integrated — a dedicated centre where          │
   │    multiple sensory streams meet in a shared latent      │
   │    space; the integration hub itself)                    │
   └─────────────────────────────┬───────────────────────────┘
                                 │ implemented-by
                                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │             expansion-readout-circuit                    │
   │   (HOW the hub is built — convergent fan-in → wide        │
   │    sparse expansion sheet → sparse projection readout;   │
   │    the cytoarchitecture that hosts the integration)      │
   └─────────────────────────────────────────────────────────┘
```

The two members address different layers of the same substrate-general question. `multi-modal-integration` says **what** the hub does — bring multiple channels into a shared representation. `expansion-readout-circuit` says **how a hub that does it is built** — the expand-then-read-out motif the source cytoarchitecture shows recurring across phyla. Integration is the function; the expansion-readout circuit is the circuit shape that realises it. Together they are the substrate-general answer the convergence evidence points to.

## What this cluster claims (system falsifiable hypothesis)

> If a cognitive capability is substrate-general, then the architectural commitments that recur convergently across non-homologous natural substrates (a dedicated multimodal integration centre; an expand-then-read-out circuit motif) should transfer to artificial substrates and improve flexible-generalisation capability there — and a system adopting both commitments together should outperform a system adopting either alone at matched budget on tasks demanding cross-modal, rapidly-generalising behaviour.
>
> **Refutation.** If the two commitments confer no joint benefit beyond the better of the two individually (i.e. the cluster adds nothing over its strongest member) on cross-modal associative-generalisation benchmarks at matched compute, the cluster's substrate-general-composition claim is refuted — the patterns may still be individually useful as standalone NEXIs.

## The framing that matters: substrate-independence *of pattern*, not substrate-irrelevance

This is the cluster's load-bearing distinction. The stance is **substrate-independence of the architectural pattern**, not substrate-irrelevance. The source account is itself *substrate-restrictive* — it binds intelligence to associative neuronal networks and does not claim any medium will do. The cluster takes the weaker, defensible reading: the *pattern* recurs across non-homologous **neural** substrates and is therefore a candidate for porting to artificial ones, without asserting that any substrate whatsoever suffices.

This distinguishes the cluster from a naïve "substrate doesn't matter" claim and connects it to the project-wide substrate-independence-of-pattern position. The [`acerebrate-decision-making`](../acerebrate-decision-making/) cluster (molecular / non-neural) and the [`embodied-action-selection`](../embodied-action-selection/) cluster (vertebrate CBGTC) supply the other two vertices of the same three-way framing; this cluster is the convergent-neural vertex.

## When to adopt

- Design and evaluation work where the question is *"which of our architectural commitments are substrate-general and therefore worth porting across very different implementation substrates?"* and where a convergent-evolution grounding is preferable to a single-substrate design story.
- When combining a multimodal integration stage with an expansion-readout representational stage in one system — the cluster is the design rationale for wiring them together.

## When not to adopt

- Single-substrate optimisation where portability is not a concern.
- Single-modality systems with nothing to integrate.
- Deployments where neither an integration centre nor an expansion-readout stage addresses an observed bottleneck.
- As settled evidence: the cluster is young and single-source — do not treat its composition claim as established.

## Tradeoffs

Committing to substrate-generality trades the efficiency of a substrate-tuned design for portability and a convergence-grounded design target. The cluster's members can be adopted independently; adopting them as a cluster only pays where a system genuinely needs both cross-modal integration and rapid associative generalisation.

## Comparison with the other clusters

| Cluster                                                                | Shape / framing vertex                                | Layer                          |
| ---------------------------------------------------------------------- | ----------------------------------------------------- | ------------------------------ |
| [`distributed-social-cognition`](../distributed-social-cognition/)     | Constellation (mutually-enabling runtime patterns)    | Multi-agent runtime            |
| [`bounded-cognitive-architecture`](../bounded-cognitive-architecture/) | Pipeline (sequenced design-time stages)               | Single-agent design-time       |
| [`acerebrate-decision-making`](../acerebrate-decision-making/)         | Composition — molecular vertex of the substrate framing | Single-agent runtime           |
| [`embodied-action-selection`](../embodied-action-selection/)           | Isomorphism — vertebrate-CBGTC vertex of the framing  | Single-agent embodied          |
| **`substrate-independent-cognition`** _(this cluster)_                 | **Convergent-neural vertex — what/how integration layers** | **Cross-substrate design-time** |

## Natural exemplars

| Source                                                                                                            | What it contributes                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Roth (2015)](https://doi.org/10.1098/rstb.2015.0049) — _Convergent evolution of complex brains and high intelligence_ | Primary source and cluster seed. Documents both member patterns co-occurring across five independent lineages (insect mushroom bodies, octopod vertical lobe, cichlid pallium, corvid/psittacid avian pallium, mammalian isocortex): a dedicated multimodal integration centre and the expand-then-read-out circuit motif that implements it, on anatomically non-homologous substrates. |

**Promotion gate.** A second circuit-level source — e.g. cephalopod electrophysiology, Drosophila mushroom-body computation, or a non-neural substrate documenting expand-then-readout — would lift the cluster past its single-source seeding.

## See also

- Cluster cousins: [`distributed-social-cognition`](../distributed-social-cognition/) · [`acerebrate-decision-making`](../acerebrate-decision-making/) · [`embodied-action-selection`](../embodied-action-selection/).
- Catalog index: [`../../CATALOG.md`](../../CATALOG.md).
- Methodology: [`../../docs/methodology.md`](../../docs/methodology.md).
- What a NEXI is: [`../../docs/what-is-a-nexi.md`](../../docs/what-is-a-nexi.md).
