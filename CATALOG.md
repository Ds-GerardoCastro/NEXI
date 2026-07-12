# NEXI Catalog

> A curated catalog of design patterns for AI systems, drawn from how intelligence is expressed across biological species. **Patterns (NEXIs) are the unit.** Browse them directly, grab what fits your problem, and consult a _collection_ only when you want the biological system a pattern came from.

> _The catalog will eventually be generated from `nexi.yaml` files by a tool in `tools/`. For now it is hand-maintained._

**Status legend:** `canonical` = multi-source evidence, passed curation review · `template` = exemplar that propagates structure · `draft` = single-source evidence, included for visibility · `deprecated` = replaced or refuted.

---

## How to use this catalog

1. Name the problem your system has (premature commitment on tool calls, weak peer models, brittle scaling, no runtime adaptation…).
2. Scan the **Patterns** index below and open any NEXI whose one-liner fits.
3. Each `nexi/<slug>/` folder is self-contained: a quick-start card, an architecture blueprint and/or drop-in skill, a falsifiable hypothesis, and `when-not-to-use` boundaries.
4. Patterns are **independently adoptable** — take one, take three, mix across biological sources. Nothing requires you to adopt a whole group.
5. Optional: the **Collections** section groups patterns by the biological system they were read from and describes how they interlock. Use it as a _lens_, not a prerequisite.

---

## Patterns

### Canonical — multi-source, curation-passed

| NEXI                                               | What it gives you                                                                                                              | Drawn from                          |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| [`niche-specification`](nexi/niche-specification/) | There is no architecture without a niche — specify, design, and evaluate against the deployment niche, not generic benchmarks. | Comparative cognition + zebra finch |

### Template — structure-propagating exemplar

| NEXI                                   | What it gives you                                                                                                                                                                                                                                                                              | Drawn from  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [`eavesdropping`](nexi/eavesdropping/) | Extract information from signals not addressed to you — monitor third-party interactions to build peer models cheaply. ✓ Validated 2026-07-12 — addresses documented AI needs (machine theory of mind, partial-observability inference); see [validation record](validation/eavesdropping.md). | Zebra finch |

### Draft — single-source, included for visibility

| NEXI                                                                 | What it gives you                                                                                                                                                                                                                                                                                                                                                               | Drawn from                                         |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [`multi-modal-integration`](nexi/multi-modal-integration/)           | Encode multiple sensory channels into one shared latent space; joint encoding preserves cross-channel coherence. ✓ Validated 2026-07-12 — Relevant (largely re-describes established joint-encoding practice); single-source draft grounded in cross-phyletic anatomy; see [validation record](validation/multi-modal-integration.md).                                          | Cross-phyletic (Roth 2015)                         |
| [`identity-by-pattern`](nexi/identity-by-pattern/)                   | Recover individual identity from observation using embeddings trained for within-class discriminability. ✓ Validated 2026-07-12 — addresses documented AI needs (partner re-identification under partial observability; behaviour-based opponent recognition); see [validation record](validation/identity-by-pattern.md).                                                      | Zebra finch                                        |
| [`context-bound-semantics`](nexi/context-bound-semantics/)           | Bind signal meaning to context rather than fixing it — the same signal means different things in different situations. ✓ Validated 2026-07-12 — enabler for documented context-conditional-interpretation needs (shared-meaning bootstrapping, peer-state modelling); see [validation record](validation/context-bound-semantics.md).                                           | Zebra finch                                        |
| [`negative-evidence-reasoning`](nexi/negative-evidence-reasoning/)   | Read information from an expected-but-missing signal — treat absence and negation as first-class evidence, not silence. ✓ Validated 2026-07-12 — addresses a documented AI need (language-model negation-insensitivity / reasoning from absence); see [validation record](validation/negative-evidence-reasoning.md).                                                           | Zebra finch                                        |
| [`social-hotspots`](nexi/social-hotspots/)                           | Concentrate information-gathering at high-traffic nodes where observation yield is densest. ✓ Validated 2026-07-12 — enabler for documented multi-agent-exploration needs (positioned against prioritized experience replay); see [validation record](validation/social-hotspots.md).                                                                                           | Zebra finch                                        |
| [`cognitive-regime-selection`](nexi/cognitive-regime-selection/)     | Classify the task into a cognitive regime first, then select the matching processing mode. ✓ Validated 2026-07-12 — Relevant (a design-time, niche-parameterised regime-selection criterion; much is established deployment-tier/NAS practice); see [validation record](validation/cognitive-regime-selection.md).                                                              | Comparative cognition                              |
| [`capacity-first-scaling`](nexi/capacity-first-scaling/)             | Under a fixed budget increase, expand storage capacity before scaling control sophistication. ✓ Validated 2026-07-12 — Relevant (largely re-expresses established compute-optimal / retrieval / Mixture-of-Experts scaling practice; distinctive value is a design-time capacity/control-separation discipline); see [validation record](validation/capacity-first-scaling.md). | Comparative cognition                              |
| [`coincidence-detection-gating`](nexi/coincidence-detection-gating/) | Require multiple independent evidence streams to align before an irreversible commitment. ✓ Validated 2026-07-12 — Grounded (addresses a documented agentic-safety need: agents commit to irreversible actions without evidence-alignment gating); see [validation record](validation/coincidence-detection-gating.md).                                                         | Bacteria                                           |
| [`stochastic-memory-coupling`](nexi/stochastic-memory-coupling/)     | Pair random exploration with persistent memory of what worked — adapt without gradient learning.                                                                                                                                                                                                                                                                                | Bacteria                                           |
| [`meta-regulation`](nexi/meta-regulation/)                           | Add an explicit regulator-of-regulators layer that modulates the control policy at runtime without redeployment.                                                                                                                                                                                                                                                                | Bacteria                                           |
| [`expansion-readout-circuit`](nexi/expansion-readout-circuit/)       | Expand input into a high-dimensional space, then read out — the expand-then-readout circuit motif.                                                                                                                                                                                                                                                                              | Cross-phyletic (cerebellum / mushroom body analog) |

---

## Collections _(optional lens — not adoption bundles)_

A **collection** groups patterns by the biological system they were read from, and records how those patterns interlock in nature. Collections are a _reading path and a provenance record_, not a required unit of adoption — you are free to take a single pattern out of any collection. Each collection's page carries the deeper theoretical claim (including its _shape_: how the member patterns relate). See [`docs/collections.md`](docs/collections.md).

| Collection                                                                        | Reads from            | Patterns                                                                                                                                | Shape                                       |
| --------------------------------------------------------------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| [`distributed-social-cognition`](collections/distributed-social-cognition/)       | Zebra finch           | eavesdropping · identity-by-pattern · multi-modal-integration · context-bound-semantics · negative-evidence-reasoning · social-hotspots | Constellation (mutually-enabling)           |
| [`bounded-cognitive-architecture`](collections/bounded-cognitive-architecture/)   | Comparative cognition | niche-specification · cognitive-regime-selection · capacity-first-scaling                                                               | Pipeline (sequenced)                        |
| [`acerebrate-decision-making`](collections/acerebrate-decision-making/)           | Bacteria              | coincidence-detection-gating · stochastic-memory-coupling · meta-regulation                                                             | Composition (layered concurrent)            |
| [`substrate-independent-cognition`](collections/substrate-independent-cognition/) | Cross-phyletic        | expansion-readout-circuit · multi-modal-integration                                                                                     | — _(shape not yet assigned; single-source)_ |

> Note: `multi-modal-integration` appears in two collections. Patterns are primary; a pattern can be read through more than one lens. This is expected — it is why patterns, not collections, are the unit.
