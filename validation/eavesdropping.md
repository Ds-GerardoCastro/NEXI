---
nexi: eavesdropping
status: template
validated: 2026-07-12
method: adversarial (two independent reviewers plus a skeptic)
updated: 2026-07-12
---

# Eavesdropping — Validation Record

**Pattern:** eavesdropping
**Status:** template
**Date:** 2026-07-12

A validation record for the `eavesdropping` pattern, assessed against documented needs in current AI research.

## AI-research standpoint — GROUNDED

The pattern addresses limitations that are documented, not speculative, in the multi-agent and machine-social-inference literature. It maps onto four recognised needs:

- **Machine theory of mind / peer-belief modelling (Direct).** Current systems lack an explicit, updatable model of another agent's latent goals and relationships. Where such models exist, they typically assume the observer sees everything the observed agent sees. Eavesdropping describes inferring peers' hidden goals and relationships from _observed third-party interactions_, under the observer's _own_ partial observability — relaxing the omniscient-observer assumption that limits existing approaches.
- **Partial-observability third-party state inference (Direct).** A decentralised agent with a limited field of view must maintain belief over teammates and rivals it cannot currently see. Eavesdropping populates that belief cheaply from overheard third-party exchanges rather than requiring direct interaction with, or a bespoke learned model of, each partner.
- **Multi-agent credit assignment (Partial).** Attributing a shared team reward to an individual agent needs a signal for how _others_ would have responded. Eavesdropping supplies exactly this responsive-others observational signal, which a counterfactual credit estimate can consume.
- **Opponent modelling (Partial).** Inferring an adversary's latent state normally assumes access to that adversary's parameters or a simple assumed learning rule. Eavesdropping infers the latent state from observed behaviour alone, without weight access — a partial contribution, and explicitly at the pattern's own stated boundary (its guidance flags adversarial contexts as a limit case).

On balance: two direct need-matches and two partial ones, all traceable to documented failure modes. **GROUNDED.**

## Method

Adversarially verified: two independent reviewers plus a dedicated skeptic.

## Honest open item

One mechanistic leg of the pattern — **trained edge/relational attention over observed dyadic interactions** — has no documented AI-need match yet. It is retained as a candidate for future work rather than presented as validated.
