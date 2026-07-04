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

| NEXI                                                                                 | What it gives you                                                                                                              | Drawn from                               |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| [`niche-specification`](nexi/niche-specification/)                                   | There is no architecture without a niche — specify, design, and evaluate against the deployment niche, not generic benchmarks. | Comparative cognition + zebra finch      |
| [`action-selection-as-common-substrate`](nexi/action-selection-as-common-substrate/) | Treat action selection as one substrate-general primitive reused across motor and cognitive domains.                           | Vertebrate CBGTC + bacterial + cnidarian |
| [`multi-modal-integration`](nexi/multi-modal-integration/)                           | Bind qualitatively different sensory channels into one percept; cross-modal fusion beats best single channel.                  | Zebra finch + cross-phyletic             |

### Template — structure-propagating exemplar

| NEXI                                   | What it gives you                                                                                                      | Drawn from  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------- |
| [`eavesdropping`](nexi/eavesdropping/) | Extract information from signals not addressed to you — monitor third-party interactions to build peer models cheaply. | Zebra finch |

### Draft — single-source, included for visibility

| NEXI                                                                     | What it gives you                                                                                                      | Drawn from                                         |
| ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [`identity-by-pattern`](nexi/identity-by-pattern/)                       | Recover individual identity from observation using embeddings trained for within-class discriminability.               | Zebra finch                                        |
| [`context-bound-semantics`](nexi/context-bound-semantics/)               | Bind signal meaning to context rather than fixing it — the same signal means different things in different situations. | Zebra finch                                        |
| [`social-hotspots`](nexi/social-hotspots/)                               | Concentrate information-gathering at high-traffic nodes where observation yield is densest.                            | Zebra finch                                        |
| [`cognitive-regime-selection`](nexi/cognitive-regime-selection/)         | Classify the task into a cognitive regime first, then select the matching processing mode.                             | Comparative cognition                              |
| [`capacity-first-scaling`](nexi/capacity-first-scaling/)                 | Expand cognitive capacity where the niche demands it before scaling uniformly.                                         | Comparative cognition                              |
| [`coincidence-detection-gating`](nexi/coincidence-detection-gating/)     | Require multiple independent evidence streams to align before an irreversible commitment.                              | Bacteria                                           |
| [`stochastic-memory-coupling`](nexi/stochastic-memory-coupling/)         | Pair random exploration with persistent memory of what worked — adapt without gradient learning.                       | Bacteria                                           |
| [`meta-regulation`](nexi/meta-regulation/)                               | Add an explicit regulator-of-regulators layer that modulates the control policy at runtime without redeployment.       | Bacteria                                           |
| [`ecological-context-model`](nexi/ecological-context-model/)             | Commit to a unified state schema where context = agent + goal + full environment, not just the perceptible subset.     | Embodied cognition                                 |
| [`exaptation-architectural-reuse`](nexi/exaptation-architectural-reuse/) | Redeploy machinery evolved for one function to a new one — reuse architecture across domains.                          | Embodied cognition                                 |
| [`heuristics-as-habits-fusion`](nexi/heuristics-as-habits-fusion/)       | Fuse fast heuristics and learned habits into one action-selection mechanism.                                           | Embodied cognition                                 |
| [`expansion-readout-circuit`](nexi/expansion-readout-circuit/)           | Expand input into a high-dimensional space, then read out — the expand-then-readout circuit motif.                     | Cross-phyletic (cerebellum / mushroom body analog) |

---

## Collections _(optional lens — not adoption bundles)_

A **collection** groups patterns by the biological system they were read from, and records how those patterns interlock in nature. Collections are a _reading path and a provenance record_, not a required unit of adoption — you are free to take a single pattern out of any collection. Each collection's page carries the deeper theoretical claim (including its _shape_: how the member patterns relate). See [`docs/collections.md`](docs/collections.md).

| Collection                                                                     | Reads from            | Patterns                                                                                                                       | Shape                                                 |
| ------------------------------------------------------------------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| [`distributed-social-cognition`](clusters/distributed-social-cognition/)       | Zebra finch           | eavesdropping · identity-by-pattern · multi-modal-integration · context-bound-semantics · social-hotspots                      | Constellation (mutually-enabling)                     |
| [`bounded-cognitive-architecture`](clusters/bounded-cognitive-architecture/)   | Comparative cognition | niche-specification · cognitive-regime-selection · capacity-first-scaling                                                      | Pipeline (sequenced)                                  |
| [`acerebrate-decision-making`](clusters/acerebrate-decision-making/)           | Bacteria              | coincidence-detection-gating · stochastic-memory-coupling · meta-regulation                                                    | Composition (layered concurrent)                      |
| [`embodied-action-selection`](clusters/embodied-action-selection/)             | Embodied cognition    | action-selection-as-common-substrate · ecological-context-model · exaptation-architectural-reuse · heuristics-as-habits-fusion | Isomorphism (same machinery under domain shift)       |
| [`substrate-independent-cognition`](clusters/substrate-independent-cognition/) | Cross-phyletic        | expansion-readout-circuit · multi-modal-integration                                                                            | Convergence (recurs across non-homologous substrates) |

> Note: `multi-modal-integration` appears in two collections. Patterns are primary; a pattern can be read through more than one lens. This is expected — it is why patterns, not collections, are the unit.
