# NEXI — Nature Expression of Intelligence

> A curated catalog of design patterns for AI systems, drawn from how intelligence is expressed across biological species.

## What is this

NEXI is the application catalog produced by the **Nature Intelligence Project**, a research effort by _Juan Gerardo Castro Sanchez_.

The Nature Intelligence Project addresses two converging problems in modern AI:

1. **Agentic systems built on Large Language Models lack a world model.** Without an internal representation of how actions change the environment, they cannot reliably plan multi-step behaviour. The gap is architectural — scaling token prediction does not close it.
2. **Modern AI's biological inspiration is narrow.** Deep learning architectures descend from a single template — the perceptron, modelled on a simplified mammalian cortical neuron — repeated through decades of architectural variation. Intelligence as it exists in biological species takes many forms, and AI has explored only a small slice of that design space.

The project mines peer-reviewed research on intelligence across biological species and extracts architectural primitives that the perceptron lineage has not yet borrowed. **NEXI is the curated catalog of those primitives** — each entry a named, documented design pattern with implementation guidance for AI engineers and builders.

## Status

**Private. Pre-release.** This repository will be made public once a critical mass of patterns has been populated and reviewed.

## Clusters and patterns

The catalog has two layers:

- **Clusters** (under `clusters/`) are _intelligence models_ — coherent systems of co-dependent patterns that solve a class of cognitive problems together. A cluster is the recommended unit of adoption: it tells builders what to combine, not just what exists.
- **Patterns** (under `nexi/`) are individual NEXIs — the architectural primitives that constitute clusters. A pattern can belong to one or more clusters.

Most builders should browse clusters first. Patterns are the engineering ingredient layer; clusters are the architecture-and-theory layer.

See [`docs/clusters.md`](docs/clusters.md) for the cluster framework and curation rules.

## How to use a cluster or pattern

A **cluster** under `clusters/<cluster-slug>/` contains:

- `README.md` — the layered cluster card (system-level claim, member patterns, complementarity notes)
- `cluster.yaml` — structured metadata, validated against [`schema/cluster.schema.json`](schema/cluster.schema.json)

A **pattern** under `nexi/<pattern-slug>/` contains:

- `README.md` — the layered pattern card (quick-start at top, theoretical depth below)
- `nexi.yaml` — structured metadata, validated against [`schema/nexi.schema.json`](schema/nexi.schema.json)
- `architecture/` — design pattern, components, pseudocode (when applicable)
- `skill/` — drop-in agent skill specification (when applicable)
- `references.md` — peer-reviewed citations

Browse [`CATALOG.md`](CATALOG.md) for the full index.

For methodology and curation rules, see [`docs/methodology.md`](docs/methodology.md) and [`docs/clusters.md`](docs/clusters.md).

## Audience

This catalog is written for **builders working on AI systems** — multi-agent systems, LLM-based agents, reinforcement learning, robotics. We do not assume graduate-level machine learning expertise. Each pattern uses a layered format: a usable summary first, theoretical depth available below.

## Companion artifacts

- A research vault (private) holds the upstream literature review and principle-extraction work that feeds this catalog.
- A forthcoming white paper presents the full theoretical argument behind the catalog.

## Contributing

Contribution gate is documented in [`docs/methodology.md`](docs/methodology.md). New entries require multi-source evidence and a falsifiable architectural hypothesis.
