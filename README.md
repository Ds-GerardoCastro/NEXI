# NEXI — Nature Expression of Intelligence

> A curated catalog of design patterns for AI systems, drawn from how intelligence is expressed across biological species.

**Live project overview → [ds-gerardocastro.github.io/NEXI](https://ds-gerardocastro.github.io/NEXI/)** — an interactive walkthrough of the two-pillar thesis, the four-asset pipeline, and an end-to-end worked example, with dedicated lenses for AI engineers and scientific researchers.

## What is this

NEXI is the application catalog produced by the **Nature Intelligence Project**, a research effort by [_Juan Gerardo Castro Sanchez_](https://www.linkedin.com/in/juan-gerardo-castro-s%C3%A1nchez-7b85b21b6/).

The Nature Intelligence Project addresses two converging problems in modern AI:

1. **Agentic systems built on Large Language Models lack a world model.** Without an internal representation of how actions change the environment, they cannot reliably plan multi-step behaviour. The gap is architectural — scaling token prediction does not close it.
2. **Modern AI's biological inspiration is narrow.** Deep learning architectures descend from a single template — the perceptron, modelled on a simplified mammalian cortical neuron — repeated through decades of architectural variation. Intelligence as it exists in biological species takes many forms, and AI has explored only a small slice of that design space.

The project mines peer-reviewed research on intelligence across biological species and extracts architectural primitives that the perceptron lineage has not yet borrowed. **NEXI is the curated catalog of those primitives** — each entry a named, documented design pattern with implementation guidance for AI engineers and builders.

## Status

**Public — early access.** The catalog is open for **early-adopter feedback**. It is pre-1.0: patterns are still being populated and reviewed, and the schemas may evolve. If you build AI systems, this is the moment your input shapes the catalog most — see [Contributing](#contributing), or open an issue with a critique, a request, or a pattern you would use.

## Authorship and AI transparency

NEXI is the **intellectual design of [Juan Gerardo Castro Sanchez](https://www.linkedin.com/in/juan-gerardo-castro-s%C3%A1nchez-7b85b21b6/)** — the research questions, the framework, the curation standards, and every editorial decision are his, and he stewards the direction and scholarly integrity of the inquiry. This is a research endeavour in the spirit of the scientific method: it explores a broad design space in search of nature's expressions of intelligence, building on the peer-reviewed work of the global research community. Its outputs are **interpretations and falsifiable hypotheses offered for scientific scrutiny and community validation — not assertions of settled fact.**

It is built **systematically with Claude (Anthropic) as an AI collaborator.** Following good practice on disclosing AI assistance in scholarly work, we state this plainly: Claude supports the literature processing, deep analysis and meta-modeling, principle and pattern identification, candidate NEXI drafting, and much of the prose. An AI cannot be an author — it is a tool operated under human direction, and each pattern is **reviewed for fidelity to its cited sources** before it enters the catalog. Responsibility for the findings of the primary research cited here rests with those studies' original authors.

This division of labor is not incidental — it _is_ the method, and the ladder below makes it explicit.

## How the catalog earns its claims: Baseline → Benchmark → Benchbreak

NEXI treats validation as a three-stage ladder. Each stage moves a pattern's authority from _proposed_ to _evidenced_ to _proven in use._

### Baseline — what AI can produce

The starting point: what Claude, under human direction, can generate — literature processing, deep analysis and meta-modeling, principle extraction, pattern identification, and candidate NEXI propositions. This is fast, broad, and generative — but on its own it is a **well-formed hypothesis, not evidence.** A baseline NEXI is a proposal awaiting corroboration.

### Benchmark — corroboration by independent evidence

A NEXI reaches **benchmark** when it is corroborated by **several independent scientific publications** — when principles drawn from different papers converge on the same mechanism. That cross-source agreement is the validation signal: the pattern is not an artifact of one study or one model's reasoning, but a repeatedly observed feature of biological intelligence. This is the promotion gate documented in [`docs/methodology.md`](docs/methodology.md).

### Benchbreak — validation by the community

The ultimate value proposition, and the reason this repository is now public. A **benchbreak** happens when the catalog is _consumed_: an AI engineer accesses a NEXI, uses it as a baseline in their own design process, tests it against a real problem, and returns feedback — or modifies the pattern and contributes the improvement back. That is the catalog doing real work in the world and being refined by it — an innovation, not just a citation.

**Early adopters: this is the invitation — use a NEXI, put it under load, break it, and tell us what happened.**

**[`eavesdropping`](nexi/eavesdropping/) is the first validated pattern** — it addresses documented AI needs (machine theory of mind, partial-observability third-party state inference); see [`VALIDATION.md`](VALIDATION.md).

## Patterns and collections

The catalog's unit is the **pattern (NEXI)**:

- **Patterns** (under `nexi/`) are individual NEXIs — architectural primitives you can adopt directly, one at a time or in combination. Start here.
- **Collections** (under `collections/`) group patterns by the biological system they were read from, and record how those patterns interlock. A collection is an optional lens and provenance record — a reading path, not a required bundle. A pattern can belong to more than one collection.

Browse patterns first; open a collection when you want the biological system a pattern came from and its sibling patterns.

See [`docs/collections.md`](docs/collections.md) for the collection framework and curation rules.

## How to use a collection or pattern

A **collection** under `collections/<collection-slug>/` contains:

- `README.md` — the layered collection card (system-level claim, member patterns, complementarity notes)
- `collection.yaml` — structured metadata, validated against [`schema/collection.schema.json`](schema/collection.schema.json)

A **pattern** under `nexi/<pattern-slug>/` contains:

- `README.md` — the layered pattern card (quick-start at top, theoretical depth below)
- `nexi.yaml` — structured metadata, validated against [`schema/nexi.schema.json`](schema/nexi.schema.json)
- `architecture/` — design pattern, components, pseudocode (when applicable)
- `skill/` — drop-in agent skill specification (when applicable)
- `references.md` — peer-reviewed citations

Browse [`CATALOG.md`](CATALOG.md) for the full index.

For methodology and curation rules, see [`docs/methodology.md`](docs/methodology.md) and [`docs/collections.md`](docs/collections.md).

## Audience

This catalog is written for **builders working on AI systems** — multi-agent systems, LLM-based agents, reinforcement learning, robotics. We do not assume graduate-level machine learning expertise. Each pattern uses a layered format: a usable summary first, theoretical depth available below.

## Where this fits in your stack

If you are building agentic systems and reaching for **context engineering**, **memory engineering**, or **harness engineering** patterns, NEXI is a design library that names what you are doing, cites peer-reviewed comparative cognition that supports it, and commits to falsifiable hypotheses you can test.

See [`docs/positioning.md`](docs/positioning.md) for the full mapping of NEXI patterns to each engineering discipline.

## Companion artifacts

- The [**project overview site**](https://ds-gerardocastro.github.io/NEXI/) presents this program visually — the thesis, the discovery-to-architecture pipeline, and a worked example — for AI engineers, researchers, and decision-makers.
- A research vault (private) holds the upstream literature review and principle-extraction work that feeds this catalog.
- A forthcoming white paper presents the full theoretical argument behind the catalog.

## Contributing

Contribution gate is documented in [`docs/methodology.md`](docs/methodology.md). New entries require multi-source evidence and a falsifiable architectural hypothesis.

## License

NEXI is dual-licensed to fit what it contains:

- **Code, schemas, and skill specifications** (`nexi.yaml`, `schema/`, pseudocode, `skill/`) — [MIT License](LICENSE).
- **Catalog content, documentation, and the white paper** (pattern cards, `docs/`, `whitepaper/`, prose) — [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE-CONTENT).

In practice: build on the patterns freely, including commercially — just **keep the attribution.** Credit _"NEXI — Nature Expression of Intelligence, by Juan Gerardo Castro Sanchez"_ and link back to this repository.

## Disclaimer

This is a research project, shared for research and educational purposes. Its contents are **falsifiable design hypotheses grounded in published science — not established facts, engineering guarantees, or professional advice** — and they summarise and interpret third-party peer-reviewed work whose findings remain the responsibility of those studies' original authors. The material is provided "as is", without warranty of any kind, under the terms of the repository's [MIT License](LICENSE); adopt, adapt, and test it at your own discretion and risk.
