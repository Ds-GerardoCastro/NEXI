# Identity by Pattern

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Member of collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
>
> _Identifying specific individuals from distinctive sensory patterns — embeddings that preserve particularity, not just category._

---

## At a glance

Off-the-shelf perception models tell you _what kind of thing_ you are looking at — bird, car, voice, face. They are typically much worse at telling you _which specific instance_ — this individual bird, this exact voice, this same agent as yesterday. A multi-agent system that needs to track peers needs the second capability, not the first; without identity, observed interactions are noise.

This pattern argues that **identity is encoded in distinctive signal patterns** and is recoverable from sensory data alone — but only with embeddings explicitly trained for _within-class discriminability_.

| Question          | Short answer                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Use this when** | You need to recognise specific individuals (agents, voices, vehicles, faces) persistently, from observation alone. |
| **Skip it when**  | Category-level recognition is enough, or signals are not naturally distinctive.                                    |
| **What it adds**  | Embedding space that preserves particularity; persistent identity tracking.                                        |
| **What it costs** | Specialised training objective; larger embeddings; harder evaluation.                                              |

---

## The natural exemplar

Wild zebra finches identify each other from **distinctive song**. Each finch has a stable, individually-distinctive song; researchers map social networks acoustically by individual signature alone, without physical tagging.

Two important nuances from the source paper:

- The authors use pretrained **species-level BirdNET embeddings** only as an _impartial validator_ of manually assigned individual IDs — songs from the same individual are measurably more similar than songs from different individuals (intra < inter cosine distance) — and describe this as _"a promising approach to scale up"_ individual-level study, while cautioning that recording conditions confound the signal. Off-the-shelf, species-trained embeddings were **not** developed into a standalone individual classifier. That distinction — category-level statistics carrying, but not yet operationalising, particular-level identity — is the same gap this pattern targets.
- Identity is in the _pattern itself_, not in any external label. Nothing tags the bird. The signature is recoverable from observation.

---

## The pattern

```
        Sensory observation (signal)
                   │
                   ▼
    ┌─────────────────────────────┐
    │   Identity encoder          │
    │   (within-class             │
    │    discriminability loss)   │
    └─────────────────────────────┘
                   │
                   ▼
        Identity embedding (preserves particularity)
                   │
                   ▼
    ┌─────────────────────────────┐
    │   Memory keyed by individual│
    │   (re-id, persistent track) │
    └─────────────────────────────┘
```

The architectural commitment is the _training objective_: it explicitly preserves within-class differences, instead of collapsing them into a category prototype.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for components and pseudocode.

- **Identity encoder** with within-class discriminability loss (contrastive triplet, ArcFace-style margin).
- **Identity memory** keyed by individual; supports re-identification and persistent tracking over time.
- **Confidence + uncertainty** on every identification — calibrated, because individual-level recognition is structurally hard.

## Skill specification

See [`skill/skill.md`](skill/skill.md).

- **System-prompt fragment** instructs the agent to track other agents as specific individuals across observations, not as instances of a class.
- **Tool** `identify_agent(signal)` returns an individual identity with confidence and uncertainty.

---

## When to use it

- ✅ Multi-agent settings where peers have stable, distinctive sensory signatures.
- ✅ Tasks requiring persistent re-identification (longitudinal tracking, social-network mapping).
- ✅ Used jointly with [Eavesdropping](../eavesdropping/) — eavesdropping needs identity to be useful.

## When not to use it

- ❌ Category-level recognition is sufficient.
- ❌ Signals are not naturally distinctive (anonymous crowds, fungible inputs).
- ❌ Adversarial settings — peers may spoof signatures.

---

## Theoretical background & evidence

The pattern draws on **animal-communication ecology** (Snijders & Naguib 2017; Hagedoorn et al. 2025) and on parallel ML research on **face recognition and re-identification**, where within-class discriminability is the central problem. Convergent: nature and ML face the same gap — pattern statistics aggregate well at category level, fail at particular level.

> **Exemplar status.** Hagedoorn et al. (2025) is an **unrefereed bioRxiv preprint** and is **observational / correlational**. It functions here as a _natural analog_ of the category-vs-particular gap, not as empirical support for the ML training-objective hypothesis below — that hypothesis is grounded in the face- and speaker-re-identification literature and is tested on its own terms.

Computational analogs:

- **Contrastive representation learning** (SimCLR, CLIP).
- **Face / person re-identification** with margin-based losses (ArcFace, CosFace).
- **Speaker recognition** (x-vectors, ECAPA-TDNN) — the closest analog to song-based individual ID.

NEXI's contribution is to name this as a **deliberate architectural commitment**, distinct from generic representation learning, with an explicit dependency on use cases that need particular-level (not category-level) discrimination.

Full citations: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H_identity.** Embedding architectures trained with within-class-discriminability objectives (margin-based contrastive losses, triplet objectives, ArcFace-style margins) achieve higher accuracy on individual-level re-identification tasks than embeddings trained only on category-level objectives, at equal training compute.
>
> **Operationalisation (pre-registered).** On the **VoxCeleb1 speaker re-identification** benchmark under an **open-set verification split** (test identities disjoint from training identities), a particularity-preserving embedding should achieve ≥10% relative gain in top-1 identification accuracy over a category-only baseline trained at equal compute on the same data.
>
> **Refutation.** If the category-only baseline matches the particularity-preserving embedding on that open-set split at equal compute, this pattern's claim is refuted.

---

## Tradeoffs

- **Training cost.** Within-class discriminability requires careful tuple sampling and is more expensive per step.
- **Embedding size.** Identity-preserving embeddings are typically larger.
- **Evaluation.** Individual-level metrics need longitudinal datasets.

## Boundary conditions

This NEXI specifies **recognising** individuals, not **modelling** them. Building rich models of each identified peer (their goals, knowledge, relationships) is the job of [Eavesdropping](../eavesdropping/) combined with [Context-Bound Semantics](../context-bound-semantics/).

---

## Related

- **Collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
- **Co-dependent NEXIs:** [`eavesdropping`](../eavesdropping/), [`multi-modal-integration`](../multi-modal-integration/), [`context-bound-semantics`](../context-bound-semantics/), [`social-hotspots`](../social-hotspots/)
- **Vault provenance (private):** principles `P03`, `P09`; metamodel `MM4 — Identity Through Distinctive Patterning`.
- **References:** [`references.md`](references.md)
