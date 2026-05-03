# Multi-Modal Integration

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Member of cluster:** [Distributed Social Cognition](../../clusters/distributed-social-cognition/)
>
> _Joint latent representations across sensory channels — not late fusion. A single underlying state is observable through multiple channels, and coherence across them is itself information._

---

## At a glance

A common AI architecture pattern is to encode each modality with a separate model and combine the outputs at the end (late fusion). The natural systems this NEXI draws from suggest a different approach: **encode multiple modalities into a shared latent space from the start**, so that cross-channel coherence is preserved and exploitable rather than discarded.

| Question          | Short answer                                                                                             |
| ----------------- | -------------------------------------------------------------------------------------------------------- |
| **Use this when** | You have multiple sensory channels and tasks that benefit from cross-modal inference or redundancy.      |
| **Skip it when**  | One modality strictly dominates, you have strict latency budgets, or no aligned multi-modal data exists. |
| **What it adds**  | Cross-modal grounding, redundancy under noise, joint world-model state.                                  |
| **What it costs** | Larger encoders, aligned multi-modal training data, harder debugging.                                    |

---

## The natural exemplar

Wild zebra finch social networks built from **acoustic** signals (song-based) closely mirror those built from **spatial** observation (movement / co-occurrence). Male song acts as a proxy for pair co-presence — the two channels carry convergent information about the same underlying social state.

The architectural lesson is not "use both channels" but rather **a single underlying social state is jointly observable through both, and the convergence between them is information-bearing**. A finch (and a system inspired by one) does not run two separate inference pipelines and merge their conclusions; it builds a unified social model that both channels constrain.

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

The shared latent space is the architectural commitment. Late-fusion architectures don't have one; they keep modality-specific spaces and combine outputs.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for components and pseudocode.

- **Joint encoder** producing a single embedding from multi-modal input.
- **Cross-modal contrastive objective** during training (e.g. CLIP-style) so the modalities align in the shared space.
- **Modality-specific projection heads** when downstream tasks need single-modality outputs.

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

In animal-communication ecology, the convergence of acoustic and spatial networks (Snijders & Naguib 2017; Loning et al. 2026) is empirical support for the proposition that nature has solved the multi-modal integration problem by maintaining a single underlying state representation that multiple channels constrain — rather than running per-modality inference pipelines.

Computational analogs:

- **CLIP / ALIGN** — cross-modal contrastive alignment of image + text.
- **AudioCLIP, ImageBind** — extensions to audio + other modalities.
- **Joint embedding predictive architectures (JEPA, V-JEPA)** — predict in joint latent space rather than per-modality.

Full citations: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H_multimodal.** Architectures with joint multi-modal encoders (single shared latent space) achieve better cross-modal grounding than late-fusion architectures (separate per-modality encoders, fused at output) on tasks requiring cross-modal inference, at equal training compute.
>
> **Operationalisation.** On benchmarks of cross-modal retrieval, audio-visual grounding, and embodied navigation, joint architectures should outperform late-fusion equivalents by ≥10% relative on cross-modal metrics at equal training compute.
>
> **Refutation.** If late-fusion matches joint encoding on cross-modal benchmarks at equal compute, this pattern's claim is refuted.

---

## Tradeoffs

- **Training data alignment.** Joint encoders need aligned multi-modal samples; curating these is often the dominant cost.
- **Debug surface.** Failure modes can cross channels — a defect in one modality propagates through the shared latent space. Localisation is harder.
- **Single-modality fallback.** Joint encoders should support graceful single-modality input (when one channel is missing); naïve implementations fail entirely.

## Boundary conditions

This NEXI specifies _encoding_ multiple modalities jointly. It does not specify _what to do_ with the joint embedding — that depends on the downstream task and is the domain of other patterns (identity-by-pattern, eavesdropping, world-modelling).

---

## Related

- **Cluster:** [Distributed Social Cognition](../../clusters/distributed-social-cognition/)
- **Co-dependent NEXIs:** [`identity-by-pattern`](../identity-by-pattern/), [`eavesdropping`](../eavesdropping/), [`context-bound-semantics`](../context-bound-semantics/), [`social-hotspots`](../social-hotspots/)
- **Vault provenance (private):** principle `P04 — Integration of Communication & Spatial Networks`; metamodel `MM2 — Multi-Channel × Multi-Level Coherence`.
- **References:** [`references.md`](references.md)
