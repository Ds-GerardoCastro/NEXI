# NEXI Catalog

The catalog has two layers: **clusters** (intelligence models — coherent systems of co-dependent patterns) and **patterns** (the individual NEXIs that constitute clusters). For most use cases, browse clusters first.

## Clusters

| Slug                                                                         | Name                           | Status   | Members | Problem class                                                                                   |
| ---------------------------------------------------------------------------- | ------------------------------ | -------- | ------- | ----------------------------------------------------------------------------------------------- |
| [`distributed-social-cognition`](clusters/distributed-social-cognition/)     | Distributed Social Cognition   | template | 5       | Building models of peers under partial observability                                            |
| [`bounded-cognitive-architecture`](clusters/bounded-cognitive-architecture/) | Bounded Cognitive Architecture | draft    | 3       | Designing cognitive architectures under cost constraint, conditional on the deployment niche    |
| [`acerebrate-decision-making`](clusters/acerebrate-decision-making/)         | Acerebrate Decision-Making     | draft    | 3       | Decision-making without a centralised processing unit, using only substrate-flexible primitives |

## Patterns

| Slug                                                                 | Name                         | Status    | Formats             | Cluster                        | Natural exemplar                                                                                           |
| -------------------------------------------------------------------- | ---------------------------- | --------- | ------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| [`eavesdropping`](nexi/eavesdropping/)                               | Eavesdropping                | template  | architecture, skill | distributed-social-cognition   | Zebra finch (_Taeniopygia castanotis_)                                                                     |
| [`identity-by-pattern`](nexi/identity-by-pattern/)                   | Identity by Pattern          | draft     | architecture, skill | distributed-social-cognition   | Zebra finch (_T. castanotis_)                                                                              |
| [`multi-modal-integration`](nexi/multi-modal-integration/)           | Multi-Modal Integration      | draft     | architecture, skill | distributed-social-cognition   | Zebra finch (_T. castanotis_)                                                                              |
| [`context-bound-semantics`](nexi/context-bound-semantics/)           | Context-Bound Semantics      | draft     | architecture, skill | distributed-social-cognition   | Zebra finch (_T. castanotis_)                                                                              |
| [`social-hotspots`](nexi/social-hotspots/)                           | Social Hotspots              | draft     | architecture, skill | distributed-social-cognition   | Zebra finch (_T. castanotis_)                                                                              |
| [`niche-specification`](nexi/niche-specification/)                   | Niche Specification          | canonical | architecture, skill | bounded-cognitive-architecture | Multi-source: Turner et al. 2026 + Hagedoorn et al. 2026 (zebra finch) — first canonical NEXI 2026-05-09   |
| [`cognitive-regime-selection`](nexi/cognitive-regime-selection/)     | Cognitive Regime Selection   | draft     | architecture, skill | bounded-cognitive-architecture | Cross-species evolutionary regimes (Turner et al. 2026)                                                    |
| [`capacity-first-scaling`](nexi/capacity-first-scaling/)             | Capacity-First Scaling       | draft     | architecture, skill | bounded-cognitive-architecture | Mathematical evolutionary-optimality model (Turner et al. 2026)                                            |
| [`coincidence-detection-gating`](nexi/coincidence-detection-gating/) | Coincidence-Detection Gating | draft     | architecture, skill | acerebrate-decision-making     | Bacteria — _Vibrio cholerae_ biofilm commitment (Nesin & Chandrankunnel 2025)                              |
| [`stochastic-memory-coupling`](nexi/stochastic-memory-coupling/)     | Stochastic-Memory Coupling   | draft     | architecture, skill | acerebrate-decision-making     | Bacteria — _E. coli_ + multi-species (Nesin & Chandrankunnel 2025; theoretical model Landmann et al. 2021) |
| [`meta-regulation`](nexi/meta-regulation/)                           | Meta-Regulation              | draft     | architecture, skill | acerebrate-decision-making     | Bacteria — anti-σ proteins regulating σ factors (Nesin & Chandrankunnel 2025)                              |

---

_The catalog will eventually be generated from `nexi.yaml` and `cluster.yaml` files by a tool in `tools/`. For now it is hand-maintained._

**Status legend:** `template` = canonical exemplar that propagates structure · `draft` = single-source evidence · `canonical` = multi-source evidence, passed curation review · `deprecated` = replaced or refuted.
