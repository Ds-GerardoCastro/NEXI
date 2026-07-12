# Multi-Modal Integration

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Member of collections:** [Distributed Social Cognition](../../collections/distributed-social-cognition/) · [Substrate-Independent Cognition](../../collections/substrate-independent-cognition/)
>
> _Joint latent representations across sensory channels — not late fusion. A single underlying state is observable through multiple channels, and coherence across them is itself information. Grounded in a single natural source: cross-phyletic anatomical evidence from convergent brain evolution, where dedicated integration centres arise independently across five lineages._

---

## At a glance

A common AI architecture pattern is to encode each modality with a separate model and combine the outputs at the end, with no alignment objective (unaligned late fusion). The natural systems this NEXI draws from suggest a different emphasis: **train a cross-modal alignment objective over a shared latent space**, so that cross-channel coherence is preserved and exploitable rather than left unmodelled. The decisive axis is whether such an alignment objective is present at training time, not whether fusion happens early or late — jointly-trained late fusion aligns too.

| Question          | Short answer                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| **Use this when** | You have multiple sensory channels and tasks that benefit from cross-modal inference or redundancy.      |
| **Skip it when**  | One modality strictly dominates, you have strict latency budgets, or no aligned multi-modal data exists. |
| **What it adds**  | Cross-modal grounding, redundancy under noise, joint world-model state.                                  |
| **What it costs** | Larger encoders, aligned multi-modal training data, harder debugging.                                    |

This is a **draft** NEXI, resting on a single natural source: cross-phyletic anatomical evidence (see below).

---

## The natural exemplar

One natural source anchors this NEXI: cross-phyletic anatomical evidence that dedicated multi-modal integration centres arise convergently across independent lineages.

### Anatomical: convergent brain evolution across five lineages

A comparative synthesis of the independent evolution of complex brains, as reviewed by Roth (2015), documents **dedicated multimodal integration centres arising convergently** across five lineages that share no complex-brain common ancestor — insect mushroom bodies, the octopod vertical lobe, the cichlid pallium, the corvid and psittacid avian pallium, and the mammalian isocortex. None are anatomical homologues, yet all share the same architectural commitment: integrate multiple sensory streams on a shared associative substrate — in Roth's own framing, "multimodal centres … highly ordered associative networks".

The circuit figures, as reviewed by Roth (2015), read at the substrate level as expansion-and-convergence. The honeybee mushroom body has ~300,000 Kenyon cells receiving from ~800 projection neurons — an **expansion** (few projection neurons → many Kenyon cells); Roth gives the ~300,000 count as a personal communication (Menzel) rather than as a published primary count. The octopus vertical lobe has ~26 million interneurons converging onto ~65,000 projection neurons — a **convergence**, which Roth reviews from primary sources (Young; Shomrat & Hochner). When five non-homologous substrates independently evolve a dedicated integration centre, the _integration hub itself_ looks substrate-general rather than lineage-specific. (The circuit shape that implements these hubs is the subject of the sibling [`expansion-readout-circuit`](../expansion-readout-circuit/) NEXI.)

### Why this remains a draft

The anatomical evidence — dedicated integration centres evolving convergently across phyla — is a single natural source. It supports the architectural commitment, but with only one natural leg the NEXI is not multi-source and stays a draft. It still touches **two** collections: [Distributed Social Cognition](../../collections/distributed-social-cognition/) (the multi-agent reading) and [Substrate-Independent Cognition](../../collections/substrate-independent-cognition/) (the convergent-substrate reading).

See [`references.md`](references.md) for the full citation chain.

---

## The pattern

```
   Modality A (e.g. audio)         Modality B (e.g. spatial)
            │                              │
            ▼                              ▼
       ┌─────────────────────────────────────┐
       │   Joint encoder                     │
       │   (shared latent space; cross-modal │
       │    contrastive alignment)           │
       └─────────────────────────────────────┘
                          │
                          ▼
              Joint multi-modal embedding
                          │
                ┌─────────┴─────────┐
                ▼                   ▼
         Modality-A decoder   Modality-B decoder
         (when needed)        (when needed)
```

A cross-modal alignment objective over a shared latent space is the architectural commitment. Architectures without one keep modality-specific spaces and combine outputs unaligned; jointly-trained late fusion, by contrast, does carry an alignment objective and counts as an instance of this pattern. The natural integration centres are the biological form of exactly this shared associative space.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for components and pseudocode.

- **Joint encoder** producing a single embedding from multi-modal input.
- **Cross-modal contrastive objective** during training (e.g. CLIP-style) so the modalities align in the shared space.
- **Modality-specific projection heads** when downstream tasks need single-modality outputs.

The integration hub composes with [`expansion-readout-circuit`](../expansion-readout-circuit/): this NEXI specifies _what_ is integrated (multiple streams in a shared latent space); that one specifies _how_ the circuit hosting the integration is shaped (a wide sparse-coded expansion feeding a sparse readout).

## Skill specification

See [`skill/skill.md`](skill/skill.md).

- **System-prompt fragment** instructs the agent to treat observations across information channels as confirming or contradicting evidence about the same underlying state, not as parallel independent inputs.
- **Tool** `get_cross_modal_observations(time, modalities)` returning aligned tuples.

---

## When to use it

- ✅ Multiple sensory or information channels with non-trivial overlap (vision + audio; text + structured data; acoustic + spatial).
- ✅ Tasks requiring cross-modal inference (caption an image, ground language in vision, identify a peer from any of several signal types).
- ✅ Settings where channels can be noisy individually and redundancy adds reliability.

## When not to use it

- ❌ Single-modality systems.
- ❌ Tasks where one modality strictly dominates and others add noise without signal.
- ❌ No aligned multi-modal training data is available and curation is infeasible.
- ❌ Strict latency budgets that preclude joint encoders.

---

## Theoretical background & evidence

The pattern is described in **multimodal machine learning** literature broadly, with foundational architectures including CLIP (Radford et al. 2021), ALIGN (Jia et al. 2021), and successors. The architectural choice between _joint encoding_ and _late fusion_ is a long-running debate in the field; this NEXI takes a position on it grounded in animal-cognition evidence.

Comparative neuroanatomy, as reviewed by Roth (2015), gives the anatomical form of the claim: dedicated integration centres evolved convergently across five non-homologous lineages, each committing a shared associative substrate to fusing multiple sensory streams. This is the pattern's single natural source.

Computational analogs:

- **CLIP / ALIGN** — cross-modal contrastive alignment of image + text.
- **AudioCLIP, ImageBind** — cross-modal contrastive extensions to audio + other modalities.

A related but distinct family, **predictive joint-embedding (within-modality)** methods — I-JEPA, V-JEPA — predict in a joint latent space within a single modality. They are self-supervised predictive methods, not cross-modal contrastive alignment, and are listed here only to mark the boundary: they are not analogs of this NEXI's cross-modal commitment.

Full citations: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H_multimodal.** Architectures trained with a cross-modal alignment objective (a shared latent space aligned across modalities at training time) achieve better cross-modal grounding than architectures without one (per-modality encoders fused at output, no alignment term) on tasks requiring cross-modal inference, at a compute-matched training budget. The decisive axis is the presence of a training-time alignment objective, not early-vs-late fusion — jointly-trained late fusion aligns too.
>
> **Operationalisation.** On a named, pre-registered cross-modal retrieval benchmark and split (e.g. Flickr30K 1K test image↔text retrieval), the aligned architecture should outperform the unaligned baseline by ≥10% relative on the retrieval metric (Recall@1) at a compute-matched budget. Caveat: a calibrated cross-modal-alignment metric is itself contested, so the benchmark and split are fixed in advance.
>
> **Refutation.** If the unaligned baseline matches the aligned architecture on the pre-registered benchmark at compute-matched budget, this pattern's claim is refuted.

---

## Tradeoffs

- **Training data alignment.** Joint encoders need aligned multi-modal samples; curating these is often the dominant cost.
- **Debug surface.** Failure modes can cross channels — a defect in one modality propagates through the shared latent space. Localisation is harder.
- **Single-modality fallback.** Joint encoders should support graceful single-modality input (when one channel is missing); naïve implementations fail entirely.

## Boundary conditions

This NEXI specifies _encoding_ multiple modalities jointly. It does not specify _what to do_ with the joint embedding — that depends on the downstream task and is the domain of other patterns (identity-by-pattern, eavesdropping, world-modelling). It specifies _what_ is integrated but not _how the integrating circuit is shaped_ — that is the domain of [`expansion-readout-circuit`](../expansion-readout-circuit/).

---

## Related

- **Collections:** [Distributed Social Cognition](../../collections/distributed-social-cognition/) · [Substrate-Independent Cognition](../../collections/substrate-independent-cognition/)
- **Co-dependent NEXIs:** [`identity-by-pattern`](../identity-by-pattern/), [`eavesdropping`](../eavesdropping/), [`context-bound-semantics`](../context-bound-semantics/), [`social-hotspots`](../social-hotspots/), [`expansion-readout-circuit`](../expansion-readout-circuit/)
- **Vault provenance (private):** principles `P04 — Integration of Communication & Spatial Networks`, `P47 — Convergent-Divergent Fan Circuit Motif`, `P50 — Polyphyletic Intelligence via Non-Homologous Modules`; metamodel `MM2 — Multi-Channel × Multi-Level Coherence`.
- **References:** [`references.md`](references.md)
