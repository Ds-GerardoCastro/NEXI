# 5. The NEXI Framework

The methodology in Section 4 produces a stream of validated patterns. The framework in this section is what those patterns enter — the catalog's structural shape, schema, application formats, and promotion model. The framework is itself an empirical artefact: it was not designed in advance and applied; it emerged from the construction of the first patterns and was formalised retrospectively. Several of its load-bearing properties — most notably the three collection shapes documented in §5.6 — could not have been anticipated before the catalog was built.

## 5.1 The two-layer catalog

NEXI is organised at two layers. The _pattern_ layer is the unit of adoption: each NEXI is a single named architectural primitive with concrete interfaces, when-to-use guidance, and a falsifiable hypothesis, independently adoptable on its own. The _collection_ layer is the architecture-and-theory lens: each collection groups two or more patterns read from the same biological system and advances a system-level falsifiable hypothesis — that the patterns reinforce one another beyond their individual effects. That synergy is a prediction to be tested, not a precondition for using any single pattern.

The two-layer choice is not cosmetic. The framework's central empirical conjecture is that patterns read from the same biological system are _co-dependent_ — that eavesdropping reaches full effect alongside referential semantics, niche specification alongside multi-modal integration, capacity-first scaling alongside cognitive-regime selection. This co-dependence is stated as a falsifiable hypothesis, not a demonstrated result: each pattern remains independently adoptable, and the collection layer exists to make the conjectured synergy explicit and testable rather than to forbid partial adoption.

## 5.2 NEXI schema and required fields

Each NEXI is validated against a JSON Schema 2020-12 contract (`schema/nexi.schema.json`) with `additionalProperties: false`. The required fields are:

| Field                    | Constraint                                                                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------- |
| `id`                     | kebab-case slug; must match the folder name                                                       |
| `name`                   | human-readable form                                                                               |
| `status`                 | one of `template`, `draft`, `canonical`, `deprecated`                                             |
| `version`                | semantic version                                                                                  |
| `natural_exemplars[]`    | at least one entry; each carries species, paper metadata (title, authors, venue, DOI, URL), notes |
| `abstract_claim`         | at least 50 characters                                                                            |
| `falsifiable_hypothesis` | at least 80 characters; specific and testable per the standard in Section 4.6                     |
| `formats[]`              | at least one of `architecture`, `skill`, `communication`, `coordination`                          |
| `when_to_use`            | at least 20 characters                                                                            |
| `when_not_to_use`        | at least 20 characters                                                                            |

Optional but encouraged fields capture audit trail: `created`, `updated`, `audience_voice`, `applies_to`, `tradeoffs`, `related_nexi[]`, `collections[]`, `tags[]`, and `provenance` pointing back into the vault.

The character-length minima are a deliberate guard against template-only entries: a falsifiable hypothesis that fits in fewer than 80 characters is almost certainly under-specified. The schema does not test whether a hypothesis is _good_; it tests whether it is _present_ at the level of detail the methodology requires.

## 5.3 Layered cards

Every NEXI's `README.md` is a _layered document_ — same file, two reading depths. The structure progresses from top to bottom:

1. **Quick-start / TL;DR.** A builder can stop reading here and have enough to apply the pattern.
2. **Pattern description.** Plain-language with a diagram and pseudocode.
3. **Implementation guidance.** Skill specification, architectural blueprint, or both — depending on which application formats the entry populates.
4. **Theoretical grounding.** Citations to peer-reviewed work, the falsifiable hypothesis stated in operational form, computational analogs from existing AI literature, and the natural-system evidence in detail.
5. **When-not-to-use.** Boundary conditions, known failure modes, and the conditions under which the pattern misleads.

The layering reconciles the two-audience problem (engineer + reviewer) without writing two separate documents. A builder who never reads past §1 still gets value; a reviewer who reads §4 still gets peer-reviewable depth. The voice across the layers is stable — plain language at the top, technical depth lower — but the audience never has to be guessed at because the layers are explicit.

## 5.4 Application formats

A NEXI may populate one or more of four application formats:

- `architecture` — interfaces, data flow, pseudocode, integration points. The pattern is offered as an architectural primitive ready to compose into a larger system design.
- `skill` — a framework-neutral agent-skill specification (system-prompt fragment plus tool/function definitions in a neutral schema), with translation notes for Claude skills, OpenAI function calling, MCP, LangChain, and LlamaIndex.
- `communication` — protocols and message contracts for inter-agent or human-agent interaction.
- `coordination` — multi-agent coordination patterns (decentralised consensus, leader election, role specialisation).

Catalog version 1 populates only `architecture` and `skill`; `communication` and `coordination` are valid format values but no entry yet exercises them. The deferred formats are not aspirational — they are guarded by the same schema constraints and admitted only when an entry can populate them with the same evidence and falsifiability discipline as the v1 formats.

The framework-neutral skill specification is itself a contribution beyond convenience: catalogs that lock to one stack (Claude-only, MCP-only) lose long-tail utility as the platform landscape shifts. The translation notes are therefore part of the entry's content, not an afterthought.

## 5.5 Collection definition and schema

A NEXI _collection_ is a grouping of two or more patterns read from one biological system, plus a system-level falsifiable hypothesis about their conjectured synergy. Collections are validated against `schema/collection.schema.json` (filename retained for now), with required fields:

| Field                             | Constraint                                               |
| --------------------------------- | -------------------------------------------------------- |
| `id`, `name`, `status`, `version` | as for NEXIs                                             |
| `problem_class`                   | the cognitive-design problem the collection addresses       |
| `member_nexis[]`                  | at least two                                             |
| `system_falsifiable_hypothesis`   | the collection-level claim about how the patterns synergise |

Optional `complementarity_notes` and per-member rationale are encouraged. The minimum-of-two member rule enforces the collection definition at the schema level: a collection is, by construction, a multi-pattern entity, and a "collection of one" is a category error caught by the validator.

## 5.6 The four collection shapes

The catalog's strongest structural finding is that collections do not all have the same shape. Three distinct shapes emerged from the construction of the first three collections, each carrying a different system-level claim, a different complementarity story, and a different relationship between its member patterns. A fourth shape — _isomorphism_ — emerged from the subsequent ingestion of a vertebrate-action-selection source [Nordli & Todd 2022] and is documented at the end of this section.

**Constellation.** The Distributed Social Cognition collection (anchored to wild zebra finch communication, [Hagedoorn et al. 2026]) is a constellation: the member patterns mutually reinforce each other around a shared niche. Removing any one pattern degrades referential robustness across the others. There is no temporal ordering and no privileged member; the collection is a graph of mutual dependencies, not a sequence. The system-level hypothesis predicts that subsetting the constellation produces non-linear capability loss — degradation beyond the additive sum of individual-pattern losses.

**Pipeline.** The Bounded Cognitive Architecture collection (anchored to capacity-limit research, [Turner et al. 2026]) is a pipeline: downstream pattern stages depend on upstream capacity limits being honoured rather than circumvented. Capacity-first scaling, cognitive-regime selection, and niche specification compose in a specific order; reordering them produces a different and provably weaker system. The system-level hypothesis predicts that pipeline violations produce specific, predictable architectural failures rather than generic degradation.

**Composition.** The Acerebrate Decision-Making collection (anchored to bacterial decision-making, [Nesin & Chandrankunnel 2025]) is a composition: substrate-independent components combine to produce adaptive collective behaviour, with no requirement that the components share a substrate or operate at the same level. Coincidence-detection gating, stochastic memory coupling, and meta-regulation can be implemented in molecular, computational, or hybrid substrates; the collection's claim is about the components, not the substrate. The system-level hypothesis predicts that adaptive bacterial-style decision-making is recoverable from any implementation that preserves the component logic.

**Isomorphism.** The Embodied Action Selection collection (anchored to the cortico-basal ganglia-thalamo-cortical loop as a vertebrate-conserved action-selection mechanism, [Nordli & Todd 2022]) is an isomorphism: the same architectural mechanism is redeployed across distinct domains via _exaptation_. The collection's four members — `action-selection-as-common-substrate` (the substrate-invariant function), `ecological-context-model` (the formalism layer with three numbered equations specifying context construction, behaviour selection, and goal achievement), `exaptation-architectural-reuse` (the generative principle by which one well-developed mechanism gets redeployed to new domains), and `heuristics-as-habits-fusion` (the concrete behavioural-instance demonstrating the collection's predictive content) — all describe the same architectural function under different domain transformations rather than different functions composed together. The system-level hypothesis predicts that an architecture committing to the collection (action selection as a first-class substrate-general primitive, formalised via the Ecological Context Model, with explicit exaptive reuse of the same selection mechanism across motor and cognitive domains, and heuristic decisions implemented as a subset of chunked-sequence habits) outperforms duplicate-module architectures on cross-domain benchmarks at lower marginal cost per added domain. The collection's distinctive contribution is that "different patterns" turn out to be the same pattern under domain shift — a structurally distinct shape from constellation (mutual enabling), pipeline (sequenced stages), or composition (layered concurrent components).

The four shapes are not exhaustive. They are what the present catalog has produced; future sources may produce shapes the framework has not yet encountered (lattice, hierarchy, swarm), and the framework is open to that. What the four shapes already establish is a stronger structural claim than any single collection carries on its own: nature does not assemble adaptive behaviour in one canonical way, and the perceptron lineage's implicit assumption that all intelligence resolves to a homogeneous network of perceptrons is a templating bias the catalog can now put pressure on with concrete, peer-reviewable cases of four distinct shapes.

## 5.7 Status taxonomy and the canonical promotion criterion

NEXI entries carry an explicit `status` field that functions as an audit trail:

| Status       | Meaning                                                                                                                                            |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `template`   | An exemplar that propagates structure; admitted with single-source evidence so that the catalog has a structural reference (e.g. `eavesdropping`). |
| `draft`      | Single-source evidence; the entry is included for visibility but has not yet accumulated the multi-source evidence required for promotion.         |
| `canonical`  | Multi-source evidence; falsifiable hypothesis stated; passed curation review.                                                                      |
| `deprecated` | Replaced, refuted, or superseded; retained for traceability so that the catalog tracks what _did not work_ alongside what did.                     |

The canonical promotion criterion is the catalog's load-bearing quality gate. A draft entry promotes to canonical only when (a) at least two independent peer-reviewed sources support the pattern at the level of atomic principles, (b) a falsifiable architectural hypothesis is stated in the operational form (Section 4.6), and (c) curation review confirms both conditions and the layered card's clarity for the broader-builder audience.

The first canonical promotion is `niche-specification` (version 1.0.0), which crossed the threshold when atomic principles from the wild zebra finch literature [Hagedoorn et al. 2026] and the cognitive-capacity literature [Turner et al. 2026] converged on the same architectural claim about niche-conditional cognitive design. The promotion is logged in the entry, with provenance to both source collections and the resolution of the g-factor / niche-binding tension recorded as part of the theoretical grounding.

The second canonical promotion is `action-selection-as-common-substrate` (version 1.0.0), which crossed the threshold on **cross-substrate triangulation**: vertebrate-CBGTC evidence from the action-selection literature [Nordli & Todd 2022], bacterial-molecular evidence from the acerebrate-decision-making literature [Nesin & Chandrankunnel 2025], and cnidarian-nerve-net evidence from the cognitive-capacity literature [Turner et al. 2026] converge on the same architectural function (default-inhibit / selective-disinhibit gating, goal-directed sequence construction, contextual reinforcement) implemented in three categorically different substrates. The promotion sets a precedent the catalog had not previously needed: cross-substrate evidence — the same architectural pattern observed in molecular regulatory networks, nerve nets, and centralised neural circuitry — can lift a pattern to canonical status by demonstrating substrate-independence-of-architectural-pattern.

The third canonical promotion is `multi-modal-integration` (version 1.0.0), which crossed the threshold on **cross-phyletic co-sourcing**: the zebra finch communication-network evidence for acoustic-plus-spatial channel fusion [Hagedoorn et al. 2026] is joined by comparative-neuroanatomy evidence that a dedicated multimodal-integration centre has been independently selected across five non-homologous lineages — insect mushroom bodies, the octopus vertical lobe, the cichlid pallium, the corvid and psittacid avian pallium, and the mammalian isocortex [Roth 2015]. Behavioural evidence from one lineage and convergent structural evidence across five others meet at the same architectural claim: that mutually-confirming cross-channel integration is a recurrently-selected primitive rather than a lineage-specific accident. The three canonical NEXIs together establish that the catalog's promotion threshold is not merely "two papers" but rather "two structurally-distinct sources converging on the same architectural claim," with the strongest forms of that convergence being cross-substrate and cross-phyletic.

## 5.8 The repository as catalog artefact

The catalog is a public artefact, not a paper supplement. Each NEXI sits in a per-pattern subfolder (`nexi/<slug>/`) containing a layered `README.md`, a machine-validatable `nexi.yaml`, application-format files where populated (`architecture/overview.md`, `skill/skill.md`), and a `references.md` with citations grounded in the discipline of Section 4.9. Each collection sits in `collections/<slug>/` with a `collection.yaml` and a layered `README.md`. Schemas are first-class repository content (`schema/`), not buried in tool configuration.

The repository structure is contribution-friendly by design: a new pattern is one new folder, validated against an existing schema, with a clear path through the methodology of Section 4. The catalog grows by addition rather than by central editing — but every addition crosses the canonical-promotion criterion before the entry can claim canonical status, so growth does not dilute. This is the engineering form of selectivity-over-volume: a small catalog of well-grounded patterns is more useful than a sprawling one.

The artefact lives at <https://github.com/Ds-GerardoCastro/NEXI>. Section 6 walks through the three demonstration case studies — one per collection shape (constellation, pipeline, composition) — that exercise the framework defined here against the methodology defined in Section 4. Section 6.6 then summarises the fourth collection (Embodied Action Selection, isomorphism shape) which was ingested subsequently and exercises the framework's openness to new shapes.
