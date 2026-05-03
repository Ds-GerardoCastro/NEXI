# NEXI Methodology

> How patterns enter the NEXI catalog, what makes an entry defensible, and the curation gate that keeps signal high.

> **Note:** patterns are organised into **clusters** (intelligence models — coherent systems of co-dependent patterns). For the cluster framework specifically, see [`clusters.md`](clusters.md). Most builders should adopt clusters, not isolated patterns; the patterns in NEXI are co-dependent.

## What is one NEXI entry?

One NEXI = **one named pattern**. A pattern can draw evidence from multiple species, papers, and natural-system studies; one species can produce multiple NEXIs. Each NEXI is presented as a _layered document_: a builder-friendly quick-start surface with a peer-reviewable theoretical core below.

Patterns are typically members of one or more **clusters**. The pattern layer is the _engineering ingredient_ layer; the cluster layer is the _architecture-and-theory_ layer. See [`clusters.md`](clusters.md).

## Promotion path

NEXI sits downstream of an upstream research vault (private, Obsidian-based literature review and principle extraction) which feeds the catalog through three stages:

```
Scientific paper
   ↓ ingest into vault
Principles (atomic claims, graded for project relevance)
   ↓ accumulate evidence across sources
Consolidation hub (named pattern, ≥2 sources, ≥2 principles)
   ↓ promotion gate
NEXI entry (with falsifiable architectural hypothesis)
```

A consolidation hub becomes a candidate NEXI when:

1. **Multi-source evidence** — at least two independent natural-system studies support the pattern.
2. **Computational analog** — at least one architectural analog (existing or proposed) is identifiable.
3. **Falsifiable hypothesis** can be stated.

The first NEXI (`eavesdropping`) is published with `status: template` despite drawing on a single source group, because it serves as the structural exemplar the rest of the catalog follows. Subsequent entries default to `status: draft` until they accumulate multi-source evidence.

## What every NEXI must contain

| Element                              | Why                                                                                  |
| ------------------------------------ | ------------------------------------------------------------------------------------ |
| Layered card (`README.md`)           | Builder-friendly quick-start + peer-reviewable theoretical depth                     |
| Structured metadata (`nexi.yaml`)    | Machine-validatable; drives the catalog index                                        |
| At least one application format      | `architecture`, `skill`, `communication`, or `coordination` — at least one populated |
| References to peer-reviewed work     | DOIs where available; vault refs for private notes                                   |
| Falsifiable architectural hypothesis | Testable prediction, even if not yet empirically tested                              |
| When-to-use / when-not-to-use        | Boundary conditions; protects against pattern misuse                                 |

## Validation level (v1)

Every NEXI commits to **literature + falsifiable hypothesis**. This means:

- Every claim about the natural-system phenomenon cites peer-reviewed work.
- Every architectural prediction is _stated as a falsifiable hypothesis_ — a specific, testable claim that could be refuted by an experiment, even if no such experiment has yet been run.

This is the deliberate middle ground between (a) pure literature description (too soft for committee defensibility) and (c) full empirical validation per pattern (too costly to scale catalog growth).

## What "falsifiable" means here

A falsifiable hypothesis specifies:

- _What_ is being compared (architecture A vs. architecture B)
- _Under what conditions_ (benchmark family, evaluation protocol)
- _What metric_ (sample efficiency, task success rate, etc.)
- _What direction of effect_ the hypothesis predicts
- _What threshold_ would constitute a meaningful effect

A claim like _"this pattern helps multi-agent systems"_ is **not** falsifiable. A claim like _"this pattern reduces episode count to a target performance threshold by >10% on partially-observable cooperative benchmarks at equal training compute"_ **is** falsifiable.

## Status fields

| Status       | Meaning                                                                       |
| ------------ | ----------------------------------------------------------------------------- |
| `template`   | Used as an exemplar that propagates structure (e.g. `eavesdropping`).         |
| `draft`      | Single-source evidence; included for visibility but not yet promoted.         |
| `canonical`  | Multi-source evidence; falsifiable hypothesis stated; passed curation review. |
| `deprecated` | Replaced, refuted, or superseded. Kept for traceability.                      |

## Voice

Cards are written for **builders working on AI systems**. Plain language at the top; technical depth available in lower sections. Assume the reader can implement an LLM agent or RL system but does not have a graduate ML background. Define jargon on first use; link to references for deeper dives.

## Curation principles

- **Selectivity over volume.** A small catalog of well-grounded patterns is more useful than a sprawling one. Padding is not a virtue.
- **Provenance over recency.** Each entry traces back to peer-reviewed literature; novelty alone is not sufficient.
- **Architectural specificity over inspiration.** _"Nature does interesting things"_ is not enough; the entry must specify a concrete architectural primitive that maps to engineering practice.
- **Cross-clade preference.** All else equal, the catalog prefers entries from non-mammalian, non-primate species. The existing AI design template already over-represents mammalian / human cognition.
