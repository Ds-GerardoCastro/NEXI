---
nexi: capacity-first-scaling
status: draft
validated: 2026-07-12
method: adversarial (two independent reviewers plus a skeptic)
updated: 2026-07-12
---

# Capacity-First Scaling — Validation Record

**Pattern:** capacity-first-scaling
**Status:** draft
**Date:** 2026-07-12

A validation record for the `capacity-first-scaling` pattern — a design-time rule that decomposes an architecture into capacity and control components and, under a fixed budget increase, expands storage capacity before scaling control sophistication — assessed against documented needs in current AI research and for faithfulness to its source.

## AI-research standpoint — RELEVANT

The pattern names a real discipline, but much of its LLM-stack framing re-expresses scaling practice the field already applies: compute-optimal allocation (Chinchilla) already rebalances toward the data/capacity axis, retrieval augmentation already treats an external store as a capacity dial, and Mixture-of-Experts already scales expert-pool capacity sparsely. Its genuinely distinctive contribution is narrower: a single **capacity/control-separation principle**, imported from an independent biological optimality result, applied at design time. It touches documented needs in **world-model and reinforcement-learning controller** design — where representation and the credit-assigned controller should scale on different budgets — but only as an **enabler**: it supplies the ordering, not the mechanism that separates capacity from credit or resists forgetting. Verdict: **Relevant, not Grounded**, and the write-up now positions the rule explicitly against established scaling practice.

## Scientific-writing standpoint — Aligned

The write-up is faithful to Turner et al. (2026). The linear-capacity / sublinear-control asymmetry is the paper's own result, correctly scoped to the system's ability to concentrate resources around the optimal allocation (with raw recall treated as concave). The capacity-prioritisation claim is stated as broadly holding across metabolic-benefit levels, reversing only when control is substantially cheaper per unit — as the paper has it. The retro-cue estimates are quoted exactly (humans 0.26 [0.19, 0.34]; rhesus macaques 0.05 [0.02, 0.16], both in the control-enhanced regime), and the result is framed as complementary to the information-capacity hypothesis, as the authors frame it. The brain-evolution "storage before regulation" ordering is presented as the authors' own hedged speculation rather than a settled finding. The falsifiable hypothesis is scoped to sub-quadratic capacity primitives, since a quadratic full-attention context dial would break the linear-capacity assumption.

## Method

Adversarially verified: two independent reviewers (AI-research and scientific-writing) plus a dedicated skeptic, with the source claims read directly from the primary PDF.

## Honest open items

- The pattern substantially re-describes established compute-optimal / retrieval / Mixture-of-Experts scaling practice; its distinctive value is the design-time capacity/control-separation discipline, not the observation that capacity helps.
- Its strongest form assumes capacity-cost and control-cost are roughly proportional per unit; where a capacity dial is super-linear in cost (full attention over very long context), the cost-adjusted recommendation can flip toward control.
- It rests on a single, unrefereed preprint (Turner et al. 2026); the ordering claim is the more speculative part of that source and could revise as further evidence accumulates.
