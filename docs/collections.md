# NEXI Collections

> A **collection** is a group of NEXI patterns that were read from the same biological system, together with an account of how those patterns interlock. A collection is a **reading path and a provenance record — not a mandatory unit of adoption.**

The unit of adoption in NEXI is the **pattern (NEXI)**. Collections exist to answer a different question than "what should I adopt?" — they answer "which patterns did nature use _together_ in one system, and how do they reinforce each other?" Use a collection as a lens, never as a prerequisite.

---

## What a collection is

A collection names:

- A **source system** — the biological system the patterns were read from.
- A **set of member patterns** — the NEXIs read from that system (≥ 2).
- **Complementarity notes** — how the member patterns enable each other.
- A **shape** — the topology of how the patterns relate (e.g. constellation, pipeline, composition, isomorphism, convergence). The shape is the reusable theoretical unit; the full taxonomy is developed in the white paper.
- _(Optional)_ A **synergy hypothesis** — a falsifiable research claim that adopting the whole outperforms any proper subset. Clearly labelled as unproven. Not required for the collection to exist, and **not a promise to the adopting engineer.**

## What a collection is not

- **Not a prerequisite.** You never have to adopt a whole collection to use one of its patterns.
- **Not a container that owns patterns.** A pattern can appear in several collections (`multi-modal-integration` appears in two). Patterns are primary; collections point at them.
- **Not an arbitrary theme.** A collection must be a genuine reading of one biological system, with a documented complementarity account — not a thematic bundle.

---

## How collections and patterns relate

- A collection references 2 or more patterns; a pattern can belong to 1 or more collections.
- Patterns are documented in `nexi/<pattern-slug>/`. Collections are documented in `clusters/<collection-slug>/` _(directory name retained for now; see "Naming" below)_.
- Each pattern's `nexi.yaml` lists the collections it belongs to (the `clusters:` field). Each collection's `cluster.yaml` lists its member patterns (`member_nexis:`).
- The pattern layer is the **engineering ingredient** layer; the collection layer is the **architecture-and-theory lens.**

## Recommended use

1. Name the cognitive problem your system has.
2. Browse **patterns** in [`../CATALOG.md`](../CATALOG.md); open the ones whose one-liner fits.
3. Adopt those patterns directly — one, several, or mixed across biological sources.
4. _If you want the bigger picture_: open the collection a pattern belongs to. It shows the sibling patterns from the same biological system and how they reinforce each other — useful for deciding whether to pull in a neighbour.
5. Treat any collection-level synergy hypothesis as a research claim to test, not a guarantee.

---

## Curation principles for collections

- **A collection must be a real reading of one biological system** — not a thematic bundle.
- **Patterns can be added without belonging to any collection.** A collection forms when a source yields two or more related patterns.
- **Selectivity over volume.** A few well-grounded collections beat a sprawl of thin ones.
- **Any synergy claim is labelled and falsifiable.** If subsetting a collection produces no degradation beyond the additive sum of individual-pattern losses, the synergy hypothesis is refuted — the patterns remain individually valid. The catalog does not break when this happens, because patterns, not collections, are the unit.

## Collection status

Mirrors the NEXI status model: `template` (structure-propagating exemplar) · `draft` (single-source) · `canonical` (multi-source across natural exemplars, synergy hypothesis stated, curation-passed) · `deprecated`.

## Naming

The on-disk directory is `clusters/` and the metadata files are `cluster.yaml` for historical reasons. The user-facing term is **collection**. A future structural pass may rename the directory and fields; until then, "cluster" in a path or field name means "collection."
