# Expansion-Readout Circuit

> **NEXI status:** draft · **Formats available:** architecture · **Audience:** builder
>
> **Cluster:** [`substrate-independent-cognition`](../../clusters/substrate-independent-cognition/)
>
> _Flexible cognition rests on an expand-then-read-out circuit motif: convergent multimodal afferents fan out onto a vast sheet of tiny interneurons (a high-dimensional expansion layer), then are read back out through a sparse projection bottleneck. The same motif has evolved independently across five non-homologous substrates — a candidate substrate-independent design primitive._

---

## At a glance

The mainstream way to add representational capacity to a network is to make it deeper or wider and train it densely. The comparative-neuroanatomy record points at a more specific move: a fixed structural motif that separates **representation** from **selection**. A small number of large projection neurons carrying convergent multimodal input diverge onto an enormous sheet of tiny, densely packed interneurons; that sheet is read back out through a sparse projection bottleneck. Functionally this is a high-dimensional expansion layer feeding a sparse readout — sparse coding / expansion-recoding — not merely "many neurons and many connections."

| Question          | Short answer                                                                                                          |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| **Use this when** | You need a representational stage for rapid associative generalisation under a bounded parameter or compute budget.   |
| **Skip it when**  | There is no associative-generalisation demand, latency forbids a wide expansion, or you are constructing the substrate itself. |
| **What it adds**  | Cheap, well-generalising associative recall; a convergently-evolved, substrate-general circuit target.                |
| **What it costs** | A wide (dense) expansion sheet where the cost sits; routing complexity in the sparse readout.                         |

The computer-science analogues are already familiar in isolation: cerebellum-like circuits, reservoir computing, mixture-of-experts with sparse routing, and random-feature expansion all instantiate one half or the other. This NEXI names the whole motif and grounds it in convergent evolution.

---

## The natural exemplar

The source paper is a comparative synthesis of how complex brains and high intelligence arose independently in several animal lineages. Its load-bearing observation for this NEXI is a **cytoarchitectural motif that recurs across substrates sharing no complex-brain common ancestor**:

- **Honeybee mushroom body.** ~300,000 Kenyon cells read roughly 800 projection neurons through ~1 million presynaptic contacts. The Kenyon-cell somata are the smallest among insects and are packed roughly 15× more densely than the densest vertebrate neurons — density, not absolute count, is the axis that scales the expansion layer.
- **Octopus vertical lobe.** ~1.8 million afferent fibres penetrate ~26 million tiny interneurons, which converge back onto ~65,000 large projection neurons in an orthogonal, en-passant / crossbar arrangement.

The same expand-then-read-out shape reappears in the cichlid pallium, the corvid and psittacid avian pallium, and the mammalian isocortex. None of these are anatomical homologues. The convergence is the argument: when radically different substrates evolve the same circuit shape under selection for flexible cognition, the shape is a candidate **substrate-general** design primitive rather than an accident of one lineage.

See [`references.md`](references.md) for the full citation chain.

---

## The pattern

```
   convergent multimodal afferents
              │
              ▼
   ┌─────────────────────────┐
   │  few large projection   │   ← small number of high-fan-in neurons
   │       neurons           │
   └────────────┬────────────┘
                │ diverge (fan-out)
                ▼
   ┌─────────────────────────────────────────────┐
   │   vast sheet of tiny, densely packed         │
   │   interneurons  —  orthogonal crossbar       │   ← HIGH-DIMENSIONAL
   │   (en-passant connectivity)                  │      EXPANSION LAYER
   └────────────┬────────────────────────────────┘
                │ read out
                ▼
   ┌─────────────────────────┐
   │   sparse projection      │   ← SPARSE READOUT
   │      bottleneck          │      (selection)
   └────────────┬────────────┘
                ▼
        downstream / associative output
```

Two commitments distinguish the motif from generic width scaling:

1. **The expansion sheet is the substrate of representational richness.** It is wide, sparse-coded, and its capacity is scaled by neuron *density*, not by absolute count. This is where high-dimensional recoding happens.
2. **The readout is a sparse bottleneck, and it is the substrate of selection.** The system does not read the whole sheet densely; a small projection reads back out, which is what keeps activation cost bounded and drives associative generalisation.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for components, interfaces, and the design decisions each stage forces.

In summary, three stages:

1. **Convergent fan-in.** A small number of high-fan-in units carry the (multimodal) input into the circuit.
2. **High-dimensional expansion.** A wide, fixed-or-random projection into a sparse-coded expansion sheet — the analogue of the granule-cell layer in cerebellum-like circuits, the reservoir in reservoir computing, or the expert bank in sparse MoE.
3. **Sparse readout.** A narrow, learned projection reads the expansion sheet back out. Selection and associative recall happen here.

The pattern composes directly with [`multi-modal-integration`](../multi-modal-integration/): integration specifies *what* meets on the shared substrate; this NEXI specifies *how the circuit that hosts the integration is shaped*. It also relates to [`action-selection-as-common-substrate`](../action-selection-as-common-substrate/), which supplies the downstream selection layer that a sparse readout naturally feeds.

---

## When to use

- Designing a representational stage for **rapid associative generalisation** under a bounded parameter or compute budget, when the choice is between depth/width scaling of a dense network and an explicit expansion-then-sparse-readout stage.
- When a substrate-general, convergently-evolved circuit motif is preferable to an ad-hoc representational design — e.g. cerebellum-inspired models, sparse-coding front-ends, associative-memory modules.
- Where activation cost must stay bounded while representational dimensionality stays high (the sparse readout is exactly the lever for this).

## When not to use

- Tasks with **no associative-generalisation demand**, where a dense network at equal budget is already adequate.
- **Extreme-latency** settings where the width (density) of the expansion sheet is unaffordable.
- **Substrate-construction (pretraining)** regimes — this motif operates below the level being built, on the representational stage rather than the foundation substrate.

## Tradeoffs

- **Where the cost sits.** The expansion sheet is wide, and its density is the expensive axis. The natural systems pay this cost with soma miniaturisation (packing more, smaller units); artificial systems pay it in parameters or memory for the expansion projection.
- **Routing complexity.** The sparse readout controls activation cost but adds routing / selection machinery. Against a dense baseline, the motif trades parameter density in a fixed/random expansion for cheaper, better-generalising associative recall — worthwhile only where associative generalisation is the actual bottleneck.

## Falsifiable hypothesis

> Architectures with a fixed-or-random high-dimensional expansion stage followed by a sparse projection readout (cf. cerebellum-like circuits, reservoir computing, mixture-of-experts with sparse routing, random-feature expansion) outperform flat or depth-only-scaled baselines on tasks requiring rapid associative generalisation under bounded compute, at equal parameter count.
>
> **Refutation.** If equal-parameter dense networks match expansion-plus-sparse-readout on associative-generalisation benchmarks at matched compute, this pattern's claim is refuted.

## References

See [`references.md`](references.md) — Roth (2015) as the primary cross-phyletic source, with the octopus vertical-lobe mechanism (Shomrat et al. 2008), the mushroom-body ecological driver (Farris & Schulmeister 2011), and avian-pallium homology (Jarvis et al. 2005) as supporting circuit-level and comparative literature.
