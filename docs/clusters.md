# NEXI Clusters

> A cluster is a coherent **intelligence model** — a system of co-dependent patterns that solve a class of cognitive problems together. It is the highest-order unit in NEXI.

## Why clusters exist

The patterns in NEXI are **not independent ingredients**. They emerged from biological systems where they are layered, mutually enabling, and operate as wholes. Eavesdropping is empty without identity tracking; identity is fragile without multi-modal confirmation; both are most valuable where information aggregates spatially.

A flat catalog of patterns risks misleading builders into thinking they can pick one and bolt it onto an otherwise unchanged architecture. In practice, the natural systems that inspired the patterns implement them together; adopting only one is often lower-leverage than the engineer expects.

The cluster framework makes the complementarity explicit.

## What a cluster is

A cluster is one **named intelligence model** — a coherent way nature has solved a class of cognitive problems.

Each cluster names:

- A **problem class** — the class of cognitive problems the cluster addresses.
- A **set of member patterns** — the NEXIs that constitute the cluster.
- A **system-level falsifiable hypothesis** — a testable claim about the cluster's combined effect, _distinct from the sum of individual-pattern hypotheses_.
- **Complementarity notes** — how the member patterns enable each other, where dependencies run.

A builder pulling from NEXI should typically adopt clusters, not patterns in isolation.

## What makes something a cluster

| Required                            | What it means                                                                                                                             |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| ≥ 2 member NEXIs                    | A singleton is not a cluster. Clusters are about the relationships _between_ patterns.                                                    |
| Coherent problem class              | The cluster addresses one identifiable class of cognitive problems, not a grab-bag.                                                       |
| System-level falsifiable hypothesis | A testable claim that goes beyond the sum of individual-pattern claims (e.g. "the cluster outperforms any proper subset on benchmark X"). |
| Documented complementarity          | An explicit account of how the member patterns enable each other.                                                                         |

## Cluster status

Mirrors the NEXI status model:

| Status       | Meaning                                                                                                     |
| ------------ | ----------------------------------------------------------------------------------------------------------- |
| `template`   | Canonical exemplar that propagates structure (e.g. `distributed-social-cognition` is the cluster template). |
| `draft`      | Single-source evidence; included for visibility but not yet promoted.                                       |
| `canonical`  | Multi-source evidence across natural exemplars; system-level hypothesis stated; passed curation review.     |
| `deprecated` | Replaced, refuted, or superseded. Kept for traceability.                                                    |

## How clusters and patterns relate

- A cluster contains 2 or more patterns; a pattern can belong to 1 or more clusters.
- Patterns are documented in `nexi/<pattern-slug>/`. Clusters are documented in `clusters/<cluster-slug>/`.
- Each pattern's `nexi.yaml` lists the clusters it belongs to (`clusters: [...]`).
- Each cluster's `cluster.yaml` lists its member patterns (`member_nexis: [...]`).
- The pattern layer is the **engineering ingredient layer**; the cluster layer is the **architecture-and-theory layer**.

## Recommended adoption pattern

For a builder using NEXI:

1. Identify the cognitive problem class your system needs to solve.
2. Find the cluster(s) that target that problem class — browse [`../CATALOG.md`](../CATALOG.md).
3. Read the cluster card to understand the system-level claim and the complementarity story.
4. Adopt the cluster — implement all member patterns. The complementarity notes tell you the dependencies.
5. If you can only adopt a subset, the cluster card's tradeoffs section flags which losses to expect.

## Curation principles for clusters

- **A cluster's claim is stronger than any pattern's.** Each member pattern claims its own effect; the cluster claims a _synergistic_ effect on top. If subsetting the cluster produces no measurable degradation beyond individual-pattern losses, the cluster's synergy claim is refuted (the patterns may still be individually useful).
- **Clusters are not arbitrary groupings.** A cluster must be defensible as a coherent intelligence model that nature has implemented (or could implement) — not as a thematic bundle.
- **The catalog grows along both axes.** New patterns can be added without belonging to any cluster yet; new clusters can be created from existing patterns when complementarity becomes evident.
- **Selectivity over volume.** A small number of strong, well-grounded clusters is more useful than a sprawling set of thin ones.
