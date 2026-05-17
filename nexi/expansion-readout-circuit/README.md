# Expansion-Readout Circuit

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder · **Version:** 0.1.0 (created 2026-05-17)
>
> **Cluster:** _pending_ — held for the future `substrate-independent-cognition` cluster (anchor candidate alongside [`multi-modal-integration`](../multi-modal-integration/); awaiting a third source confirming the circuit motif at the functional level).
>
> **Vault-internal terminology:** *convergent-divergent fan* (the biological-origin name preserved in the vault knowledge graph). The public NEXI slug uses the CS-functional name `expansion-readout-circuit` for engineer discoverability.
>
> _A specific circuit topology — expand input dimensionality onto a sparse-activation interneuron sheet, read out via a small population of large projection neurons — that has independently evolved in five non-homologous neural substrates. Substrate-architectural companion to [`multi-modal-integration`](../multi-modal-integration/)._

---

## At a glance

| Question          | Short answer                                                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Use this when** | Architectures that need rapid associative generalisation, multi-modal binding under partial input, or pattern completion under noise. |
| **Skip it when**  | Dense feature compositionality with abundant training data (depth-scaled dense feedforward has the right inductive bias).             |
| **What it adds**  | Expansion-then-readout substrate: a high-dimensional expansion stage feeding a sparse projection bottleneck.                          |
| **What it costs** | Parameter width in the expansion layer; routing/selection mechanism in the readout; new debugging surface (which subset was selected).|
| **Evidence**      | Roth (2015) cross-phyletic synthesis across five phyla — mushroom body, vertical lobe, pallium variants, isocortex.                   |

---

## The natural exemplar — five phyla, one circuit motif

Roth (2015) synthesises comparative-neuroanatomy evidence that complex brains and high intelligence have evolved several times independently across the animal kingdom — and that the convergent endpoint is the **same circuit motif** on non-homologous neural substrates. The motif:

> A small bottleneck of large projection neurons receives convergent multimodal afferents that then diverge onto a vast sheet of tiny, densely packed interneurons forming orthogonal en-passant contacts.

Quantitative cytoarchitecture (drawn by Roth from primary sources — Strausfeld for insects, Hochner/Shomrat for cephalopods):

| Lineage                              | Expansion sheet                                                                          | Sparse readout                                       | Input convergence                                                                            |
| ------------------------------------ | ---------------------------------------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Honeybee mushroom body** (Hymenoptera) | ~300 000 Kenyon cells — densest neuropil among insects; cell soma the smallest in insect brain, 15× packing density of densest vertebrate neurons | Projection neurons (small population)                | ~800 antennal-lobe projection neurons feeding ~1M presynaptic contacts (~375× expansion)     |
| **Octopus vertical lobe** (Cephalopoda) | ~26M tiny interneurons (smallest in the cephalopod brain)                                | 65 000 large projection neurons                      | 1.8M afferent fibres, penetrating the interneuron sheet in a *rectangular* en-passant grid   |
| **Cichlid pallium** (Teleostei)      | Pallial associative cells (qualitative description in Roth's review)                     | Sparse projection populations                        | Multi-sensory convergence                                                                    |
| **Corvid/psittacid avian pallium** (Aves) | Pallial associative cells (qualitative)                                                  | Sparse projection populations                        | Multi-sensory convergence                                                                    |
| **Mammalian isocortex** (Mammalia)   | Layer-IV stellate / layer-II/III pyramidal populations                                   | Layer-V pyramidal neurons (sparse)                   | Thalamic + cortico-cortical convergence                                                      |

The lineages do not share ancestry at the relevant anatomical level — their last common ancestor predates the architectural feature. Convergence is therefore evidence that the architecture is *selected for* rather than *inherited*. Roth's phrase for the architectural commitment: intelligence is *"invariantly bound to multimodal centres... all of which contain highly ordered associative neuronal networks"*. This NEXI specifies the precise computational signature behind the looser phrase: **expand-then-readout via orthogonal crossbar**, not "many neurons + many connections."

---

## The pattern

```
   Convergent multimodal afferents
   (e.g. olfactory + visual + somatosensory)
                  │
                  ▼
   ┌──────────────────────────────────────┐
   │ Orthogonal crossbar projection       │
   │ (input fibres cross interneuron      │
   │  processes; en-passant contacts at   │
   │  each crossing form associative      │
   │  sites — substrate, not weights)     │
   └──────────────────────────────────────┘
                  │
                  ▼
   ┌──────────────────────────────────────┐
   │ Expansion sheet                      │
   │ (vast population of densely packed   │
   │  small interneurons; sparse          │
   │  activation under any single input)  │
   └──────────────────────────────────────┘
                  │
                  ▼
   ┌──────────────────────────────────────┐
   │ Sparse readout                       │
   │ (small population of large           │
   │  projection neurons; integrates over │
   │  the active subset of the expansion  │
   │  sheet)                              │
   └──────────────────────────────────────┘
                  │
                  ▼
              Behavioural output
```

The structural commitment is the geometric topology — orthogonal crossbar over a dense expansion sheet, with sparse readout. Plasticity (Hebbian, neuromodulatory, etc.) operates **on top of** this substrate, not as the substrate itself.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for components and pseudocode.

- **Expansion stage** producing a high-dimensional sparse representation from lower-dimensional multi-modal input.
- **Orthogonal-crossbar input connectivity** — fixed-or-random projection that preserves topographic structure across modalities.
- **Sparse readout** via a small projection population, with explicit top-k selection or competitive routing.

## Skill specification

See [`skill/skill.md`](skill/skill.md).

- **Design-time skill** for architects: when reviewing an AI architecture, audit whether it has an expansion-then-readout layer. If the task requires associative generalisation and the architecture is depth-scaled dense, propose an expansion stage.

---

## When to use it

- ✅ Rapid associative generalisation from few examples (few-shot learning, contextual binding).
- ✅ Multi-modal binding under partial input (one modality missing or noisy).
- ✅ Pattern completion under noise (degraded input → clean output).
- ✅ Substrate-independence as a design priority — the motif recurs across phyla, suggesting substrate-general implementation choices are valid.

## When not to use it

- ❌ Tasks dominated by dense feature compositionality with abundant training data.
- ❌ Severe parameter-budget constraints — the expansion stage adds width.
- ❌ Architectures already employing reservoir computing or mixture-of-experts in the expansion direction (this NEXI is what they implicitly implement).

---

## Theoretical background & evidence

The motif Roth (2015) documents is not a new architectural idea in computing — it has well-established CS analogs:

- **Cerebellum-like circuits** in computational neuroscience: granule cells (millions, small, densely packed) feeding Purkinje cells (few, large) is the cerebellum's instantiation of the same motif. Marr (1969) and Albus (1971) developed the foundational computational theory; Yamazaki & Tanaka (2007), Dean et al. (2010) are modern syntheses.
- **Reservoir computing / Liquid State Machines** (Jaeger 2001; Maass et al. 2002): fixed/random high-dimensional projection (the reservoir) + sparse readout. The most direct CS analog of the convergent-divergent fan.
- **Random-projection feature expansion** (Rahimi & Recht 2007; locality-sensitive hashing): expansion-then-readout at the algorithmic level. Applied broadly in kernel methods.
- **Mixture-of-experts with sparse routing** (Fedus et al. 2022): expansion at parameter level, sparse readout at forward pass. Closest mainstream-AI analog.

Roth's contribution is empirical-evolutionary: the motif has been independently selected across five non-homologous neural substrates spanning ~600M years of evolution. The substrate-general claim turns the motif from a niche architectural choice into a default architectural commitment for AI systems pursuing associative-generalisation competence.

Full citations: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H_expansion-readout.** At matched parameter count and matched compute, AI architectures with a fixed-or-random high-dimensional expansion stage feeding a sparse projection readout outperform equal-parameter dense feedforward baselines on tasks requiring rapid associative generalisation.
>
> **Operationalisation.** On cerebellum-inspired benchmarks (associative-generalisation suite of CIFAR-FS, mini-ImageNet, omniglot-extended) the expansion-readout architecture should outperform equal-parameter dense baselines by ≥10% relative on few-shot accuracy.
>
> **Refutation.** If dense feedforward of equal parameter count matches expansion-readout on associative-generalisation benchmarks at matched compute, this pattern's claim is refuted and the convergent-evolution evidence becomes biological observation without computational implication.

---

## Tradeoffs

- **Width parameter cost.** The expansion stage adds parameter width that is not free even when activations are sparse.
- **Routing/selection overhead.** Sparse readout requires either routing (MoE) or explicit top-k selection, adding inference-time overhead.
- **New debugging surface.** Inspection shifts from "which layer learned what" to "which subset of the expansion layer was selected by the readout." Interpretability tools must be tailored.

## Boundary conditions

This NEXI specifies a *circuit topology*, not a learning algorithm or a task-specific architecture. Plasticity, routing strategy, and downstream task heads are independent design choices made on top of this substrate. The motif is what Roth (2015) treats as universal across his five phyla; the implementation choices are substrate-specific.

The pattern is currently **single-source** (Roth 2015), held in `draft` status. Promotion to `canonical` requires a second independent source confirming the circuit motif at the *functional* level (sparse coding, expansion-recoding) rather than just the anatomical level. Watch list: cephalopod electrophysiology of vertical-lobe dynamics; *Drosophila* mushroom-body computational analysis; non-neural substrate documenting expand-then-readout (plant signal integration, slime mold path computation, eusocial colony collective computation).

---

## Related

- **Cluster:** _pending_ — `substrate-independent-cognition` (held for third-source confirmation).
- **Substrate-functional companion:** [`multi-modal-integration`](../multi-modal-integration/) — the *functional* claim (joint multi-modal encoders > late fusion) that this NEXI provides the *substrate-architectural* implementation for. Together they are the proposed founding members of `substrate-independent-cognition`.
- **Adjacent NEXIs:** [`action-selection-as-common-substrate`](../action-selection-as-common-substrate/) — Roth's evidence also adds a fourth substrate vertex to this canonical NEXI.
- **Vault provenance (private):** principles `P47 — Convergent-Divergent Fan Circuit Motif`, `P48 — Orthogonal Crossbar Substrate`, `P49 — Soma Miniaturisation as Capacity Scaling Axis`, `P50 — Polyphyletic Intelligence via Non-Homologous Modules`; consolidation hub `Convergent-Divergent Fan`; metamodel `MM1 — Expand-Then-Readout as Substrate-General Circuit Motif (Roth)`.
- **References:** [`references.md`](references.md)
