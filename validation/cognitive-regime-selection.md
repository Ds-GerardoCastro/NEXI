---
nexi: cognitive-regime-selection
status: draft
validated: 2026-07-12
method: adversarial (two independent reviewers plus a skeptic)
updated: 2026-07-12
---

# Cognitive Regime Selection — Validation Record

**Pattern:** cognitive-regime-selection
**Status:** draft
**Date:** 2026-07-12

A validation record for the `cognitive-regime-selection` pattern — classifying a deployment niche into a cognitive regime at design time and matching the architecture's component mix to it — assessed against documented needs in current AI research and for faithfulness to its source.

## AI-research standpoint — RELEVANT

The pattern is well-motivated: different deployment niches favour qualitatively different architectures, and choosing a niche-appropriate regime at design time is a real discipline. But much of it describes **established practice** — production model families and neural-architecture-search already produce structurally different architectures across tiers. Its genuinely novel contribution is narrower: a _design-time, niche-parameterised selection criterion_ grounded in an evolutionary-optimality model. It touches the documented need for task-conditioned reconfiguration only as a **design-time enabler** — the deeper unmet need there is a _runtime_ meta-controller, which this pattern does not provide. Verdict: **Relevant, not Grounded**, and the write-up now separates the established-practice part from the new proposal.

## Scientific-writing standpoint — Aligned

The write-up is faithful to Turner et al. (2026): the three regime names are the paper's own, the phylogenetic placements it reports are the paper's, and the retro-cue estimates are quoted exactly (humans 0.26 [0.19, 0.34]; rhesus macaques 0.05 [0.02, 0.16], both control-enhanced). Crucially, the pattern presents the regimes as **qualitatively distinct regions on a continuous optimality surface** — matching the paper's explicitly continuous model — and frames the human/macaque result as **complementary to** the information-capacity hypothesis, as the authors do. The engineering claim is grounded in deployment-tier and architecture-search practice, not in the biology, and the falsifiable hypothesis is genuinely testable.

## Method

Adversarially verified: two independent reviewers (AI-research and scientific-writing) plus a dedicated skeptic, with the source claims read directly from the primary PDF.

## Honest open items

- The pattern substantially re-describes established deployment-tier / architecture-search practice; its distinctive value is the design-time, evolution-grounded _selection criterion_, not the observation that tiers differ.
- The regime classifier is a principled approximation of a continuous multi-factor optimality model and requires per-domain calibration; regime boundaries are soft, not hard thresholds.
- It rests on a single, unrefereed preprint (Turner et al. 2026); the regime taxonomy could revise if further evidence accumulates.
