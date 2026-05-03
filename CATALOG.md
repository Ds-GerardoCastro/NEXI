# NEXI Catalog

The catalog has two layers: **clusters** (intelligence models — coherent systems of co-dependent patterns) and **patterns** (the individual NEXIs that constitute clusters). For most use cases, browse clusters first.

## Clusters

| Slug                                                                     | Name                         | Status   | Members | Problem class                                        |
| ------------------------------------------------------------------------ | ---------------------------- | -------- | ------- | ---------------------------------------------------- |
| [`distributed-social-cognition`](clusters/distributed-social-cognition/) | Distributed Social Cognition | template | 5       | Building models of peers under partial observability |

## Patterns

| Slug                                                       | Name                    | Status   | Formats             | Cluster                      | Natural exemplar                       |
| ---------------------------------------------------------- | ----------------------- | -------- | ------------------- | ---------------------------- | -------------------------------------- |
| [`eavesdropping`](nexi/eavesdropping/)                     | Eavesdropping           | template | architecture, skill | distributed-social-cognition | Zebra finch (_Taeniopygia castanotis_) |
| [`identity-by-pattern`](nexi/identity-by-pattern/)         | Identity by Pattern     | draft    | architecture, skill | distributed-social-cognition | Zebra finch (_T. castanotis_)          |
| [`multi-modal-integration`](nexi/multi-modal-integration/) | Multi-Modal Integration | draft    | architecture, skill | distributed-social-cognition | Zebra finch (_T. castanotis_)          |
| [`context-bound-semantics`](nexi/context-bound-semantics/) | Context-Bound Semantics | draft    | architecture, skill | distributed-social-cognition | Zebra finch (_T. castanotis_)          |
| [`social-hotspots`](nexi/social-hotspots/)                 | Social Hotspots         | draft    | architecture, skill | distributed-social-cognition | Zebra finch (_T. castanotis_)          |

---

_The catalog will eventually be generated from `nexi.yaml` and `cluster.yaml` files by a tool in `tools/`. For now it is hand-maintained._

**Status legend:** `template` = canonical exemplar that propagates structure · `draft` = single-source evidence · `canonical` = multi-source evidence, passed curation review · `deprecated` = replaced or refuted.
