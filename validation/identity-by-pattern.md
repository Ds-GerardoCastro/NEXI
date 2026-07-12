---
nexi: identity-by-pattern
status: draft
validated: 2026-07-12
method: adversarial (two independent reviewers plus a skeptic)
updated: 2026-07-12
---

# Identity by Pattern — Validation Record

**Pattern:** identity-by-pattern
**Status:** draft
**Date:** 2026-07-12

A validation record for the `identity-by-pattern` pattern, assessed against documented needs in current AI research and against the faithfulness of its write-up.

## AI-research standpoint — GROUNDED

The pattern addresses limitations that are documented, not speculative, in the multi-agent and machine-perception literature. It maps onto recognised needs:

- **Re-identifying specific partners under partial observability (Direct).** A decentralised agent with a limited field of view must keep track of _which_ teammate or rival is which across time and occlusion, from observation alone. Category-level perception answers "what kind of thing is this"; it does not answer "is this the same individual I saw before." Identity-by-pattern supplies exactly the persistent, observation-only re-identification that recurrent memory of unobserved agents depends on.
- **Behaviour-based recognition of co-learners and opponents (Direct).** Recognising a specific adversary or partner normally assumes access to its parameters or an assumed learning rule. Identity-by-pattern recovers a stable per-individual signature from observed behaviour alone, without weight access — relaxing the known-parameter assumption that limits existing opponent-modelling approaches. (At the pattern's own stated boundary: its guidance flags adversarial signature-spoofing as a limit case.)
- **The category-versus-particular failure mode (Direct).** Off-the-shelf perception and representation models aggregate well at category level and systematically lose particular-level information. The pattern names the deliberate architectural commitment — embeddings trained for within-class discriminability — that preserves particularity, distinct from generic representation learning.

The pattern is disciplined about scope: it specifies **recognising** individuals, and explicitly delegates **modelling** them (their goals, knowledge, relationships) to eavesdropping combined with context-bound-semantics. Recognition is the prerequisite that those modelling patterns build on; identity-by-pattern does not overclaim their territory. On balance, three direct need-matches traceable to documented failure modes. **GROUNDED.**

## Scientific-writing standpoint — Aligned

The write-up is faithful to its sources and epistemically honest. It rests on two separate evidentiary bases and keeps them distinct: the zebra-finch communication-network study serves as a **natural analog** (individual identity is recoverable from distinctive signals, observed without tagging), while the testable engineering claim — that within-class-discriminability objectives beat category-only objectives on individual-level re-identification — is grounded in the face and speaker re-identification literature (ArcFace, FaceNet, ECAPA-TDNN), not in the natural exemplar. Citations are canonical and correctly attributed. The falsifiable hypothesis is genuine, pre-registered against a named benchmark and open-set split, with a coherent refutation criterion.

## Method

Adversarially verified: two independent reviewers (one AI-research, one scientific-writing) plus a dedicated skeptic, with the natural-exemplar source checked against its primary text.

## Honest open items

- The link from this pattern to an agent's own **self-identity stability** (a self assembled from a distinctive pattern of acts) is an architectural analogy, not the same recognition mechanism. It is retained as a candidate for future work rather than presented as validated.
- Margin-based identity training (ArcFace / CosFace) assumes a closed, labelled set of identities at training time; **open-world enrollment of previously unseen individuals** relies instead on triplet or contrastive-instance objectives. This is a real engineering boundary the architecture spells out.
