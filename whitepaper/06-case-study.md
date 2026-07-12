# 6. Case Studies: Three Collection Shapes

This section walks through the three demonstration collections as worked examples of the methodology of Section 4 and the framework of Section 5. Each sub-study follows the same structure: the source, the atomic principles that crossed the relevance gate, the resulting NEXI patterns, the collection's structural shape and system-level falsifiable hypothesis, the status of the collection and its members, and the collection-specific limitations honestly attached. Section 6.4 compares the three side-by-side; Section 6.5 reports limitations that span all three.

The three collections were not chosen to demonstrate three different shapes — that finding emerged from their construction. Each collection was extracted from one peer-reviewed source independently, following the methodology, and the shape difference (§5.6) became visible only after all three were structured.

## 6.1 Constellation — Distributed Social Cognition

### Source

Hagedoorn et al. 2026, _Communication Networks of Wild Zebra Finches (Taeniopygia castanotis)_, bioRxiv preprint posted 2026-04-27 (DOI 10.1101/2025.09.11.675577, license CC-BY-NC-ND 4.0). The paper documents communication-network behaviour in wild zebra finches in the Australian arid zone, with attention to the social hotspots where many individuals converge under unpredictable timing.

### Atomic principles and consolidation

Section-by-section reading of the source produced atomic principles in five collections of claims, each grounded in specific paper sections (Methods, Results on hotspot density, Discussion of multi-channel signalling): (a) eavesdropping on third-party song interactions; (b) individual identification from distinctive song motifs; (c) acoustic + spatial integration as mutually-confirming channels; (d) context-binding such that the same signal carries different meanings in different settings (breeding colony vs. hotspot); (e) the social hotspot itself as a structured aggregator rather than an anonymous gathering. Each claim was graded CORE under both rubric conditions: it load-bears the architectural pillar (sample-efficient inference about other agents under partial observability) _and_ reveals an intelligence-design pattern that diverges from the human / mammalian template (peer-modelling distributed across observation, identity, context, and spatial substrate).

The consolidation hubs `Eavesdropping`, `Multi-Modal Integration`, and `Context-Dependent Semantics` materialised within this single source — each hub backed by multiple atomic principles drawn from independent measurement contexts within the paper. Multi-source promotion at the pattern level has since reached one member (`multi-modal-integration`, below); the remaining members await additional independent sources.

Roth 2015 provides the cross-phyletic confirmation that promotes `multi-modal-integration` to canonical. The zebra finch source supplies behavioural evidence that acoustic and spatial channels are fused into mutually-confirming percepts; Roth's comparative neuroanatomy shows that a _dedicated multimodal-integration centre_ has been independently selected across five non-homologous lineages — insect mushroom bodies, the octopus vertical lobe, the cichlid pallium, the corvid and psittacid avian pallium, and the mammalian isocortex. Behavioural evidence from one lineage plus convergent structural evidence across five others converge on the same architectural claim, satisfying the canonical-promotion criterion (§5.7) with the strongest available form of that convergence — cross-phyletic. `multi-modal-integration` is accordingly the catalog's third canonical NEXI.

### Member NEXIs

| Slug                      | Role                                                                  | Status                |
| ------------------------- | --------------------------------------------------------------------- | --------------------- |
| `eavesdropping`           | Extract information from observed third-party interactions            | template              |
| `identity-by-pattern`     | Attribute observed behaviour to specific individuals from signatures  | draft                 |
| `multi-modal-integration` | Mutually confirm identity and observation through cross-channel pairs | **canonical** (1.0.0) |
| `context-bound-semantics` | Bind meaning to context, including reasoning from absence             | draft                 |
| `social-hotspots`         | Aggregate observation where interaction density is highest            | draft                 |

`eavesdropping` carries `status: template` rather than `draft` because it is the structural exemplar that propagates the per-pattern subfolder layout to the rest of the catalog (§5.7). The template designation is a methodological role, not an evidence claim — the underlying evidence is currently single-source and would otherwise be `draft`.

### The constellation shape

The five patterns form a graph of mutual dependencies rather than a sequence. Eavesdropping requires identity (to know whose interaction is being observed) and context-bound semantics (to interpret the interaction's meaning); identity benefits from multi-modal integration (to confirm whose voice this is); social hotspots are the spatial substrate that makes eavesdropping cheap (because observation density is highest where interactions concentrate). There is no privileged member and no temporal ordering: in a deployed agent, the patterns run concurrently during inference, each enabling the others.

This is what distinguishes the constellation shape from the pipeline shape (§6.2) and the composition shape (§6.3). A constellation collection's load-bearing claim is the _graph_ of mutual enablement, not an order or a layering.

### System-level falsifiable hypothesis

> Multi-agent systems that adopt the full distributed-social-cognition collection outperform systems that adopt any proper subset of its member patterns on cooperative social-inference benchmarks at equal training compute, by a margin larger than the sum of the individual-pattern gains.

Operationalisation: a benchmark suite of N ≥ 3-agent partially-observable cooperative tasks (Hanabi-family, Overcooked-AI multi-agent variants, social-inference benchmarks) is run for (a) baseline (no patterns), (b) each member pattern in isolation, (c) all proper subsets, (d) the full collection. The collection's gain over baseline must exceed the sum of single-pattern gains by ≥10% for the synergy claim to be supported; every subset-vs-collection comparison must show degradation when any member is removed. Refutation: if subsetting never produces degradation beyond additive loss, the synergy claim fails — the patterns may still be individually useful, but the collection does not constitute a coherent intelligence model.

### Limitations

Predominantly single-source collection: four of the five member NEXIs trace back to a single peer-reviewed source, with `multi-modal-integration` the exception (promoted to canonical on cross-phyletic co-sourcing with [Roth 2015]). The collection as a whole therefore still carries `status: template` (anchored in the eavesdropping exemplar) rather than `canonical`; collection-level promotion requires multi-source evidence for the collection as a coherent intelligence model, not for a single member. The honest reporting here is that the collection's _shape_ is well-evidenced by the source's network analysis, but the _generality_ of each pattern beyond zebra finches awaits multi-source corroboration. The collection also assumes _honest_ observation; adversarial robustness (peers actively deceiving observers) is out of scope and a known failure mode.

**New evidence — `eavesdropping` validated against AI needs.** The collection's exemplar member has since been validated to address documented needs of current AI systems. `eavesdropping` maps directly onto machine theory of mind (peer-belief modelling under the observer's own partial observability) and onto partial-observability coordination — inferring third-party latent state that a decentralised agent cannot directly observe — with partial contributions to multi-agent credit assignment and opponent modelling. This grounds the constellation's transfer claim in named, documented AI failure modes rather than biological analogy alone. See [`validation/eavesdropping.md`](../validation/eavesdropping.md) for the full record.

## 6.2 Pipeline — Bounded Cognitive Architecture

### Source

Turner, C. R., Russek, E. M., Seed, A., McEwen, E. S., Vélez, N., Morgan, T. J. H., & Griffiths, T. L. (2026), _Cognitive capacity and control in the evolution of intelligence_, bioRxiv preprint posted 2026-03-09 (DOI 10.1101/2026.03.07.710317, license CC-BY 4.0). The paper develops a mathematical model of working-memory selection under metabolic cost, derives three discrete cognitive regimes as evolutionary attractors, and cross-validates with retro-cue task data from humans and rhesus macaques. Phylogenetic placements span jellyfish, sea anemones, nematodes, flatworms, tardigrades, corvids, elephants, cetaceans, and great apes. The DOI's CrossRef indexing is pending at the time of writing; verification is deferred to the biorxiv resolver and re-validated before any external submission (§4.9).

### Atomic principles and consolidation

The mathematical core of the source produced three architecturally-consequential atomic principles: (a) cognition is allocation under cost — finite metabolic budget shapes optimal architecture; (b) the deployment niche shapes the optimum — three discrete regimes (passive-storage, control-enhanced, capacity-heavy) emerge as attractors of the optimisation, not as tier-labels on a single scaling curve; (c) storage capacity is prerequisite to regulation — capacity contributes linearly to recall efficacy while control contributes sublinearly. Each principle was graded CORE under condition (a) of the rubric (architectural-pillar load) and most also under condition (b) (the regime structure is a non-mammalian-template architectural claim).

Independent corroboration arrived from the Hagedoorn et al. 2026 source — niche-conditional cognitive design appears as a fission-fusion social architecture in zebra finches, with the same signal type carrying different functions in different niches. This is the cross-source convergence that promoted `niche-specification` to `canonical` (§5.7).

### Member NEXIs

| Slug                         | Role in the pipeline                                                                     | Status                |
| ---------------------------- | ---------------------------------------------------------------------------------------- | --------------------- |
| `niche-specification`        | Specify the deployment niche as a typed object (entry point of the pipeline)             | **canonical** (1.0.0) |
| `cognitive-regime-selection` | Map the niche to one of three regime attractors and recommend the regime's component mix | draft                 |
| `capacity-first-scaling`     | Within the regime, allocate budget to capacity components before control components      | draft                 |

### The pipeline shape

The three patterns form a strict design-time pipeline:

```
niche-specification → cognitive-regime-selection → capacity-first-scaling → in-niche evaluation
```

Each stage's output is the next stage's typed input. Skipping niche specification leaves regime selection without an input; skipping regime selection leaves allocation without an architectural target; skipping capacity-first leaves the regime as a tier-label without an allocation policy. Crucially, this is a _design-time_ pipeline — the three patterns run before the deployed system exists, in sequence, producing the architecture the system will then run. This is the structural difference from the constellation: a constellation is a graph of runtime mutual enablement; a pipeline is a sequence of design-time typed-input dependencies.

### System-level falsifiable hypothesis

> Architectures designed using the full pipeline (niche specification → regime classification → capacity-first allocation) outperform same-budget architectures designed via single-axis scaling on niche-specific evaluation, by a margin larger than the sum of individual-NEXI gains.

Refutation: if pipeline-designed systems perform no better than the best individual-NEXI baseline at matched compute, the collection's compositional claim is refuted (the patterns may still be individually useful as standalone NEXIs). The bet the collection makes is that _composition is load-bearing_ — that the design-time discipline of forcing niche-then-regime-then-allocation, in that order, produces architectures that single-pattern application does not.

### Tension resolution: g-factor versus niche-binding

The source's P22 (the domain-general capacity-axis hypothesis, sympathetic to a g-factor view) sits in tension with niche-bound specialisation evidence from the zebra finch source and from the comparative-cognition literature more broadly. The methodology's response (§4.7) is to log the tension rather than pick a side. The synthesis recorded inside the `niche-specification` entry is that domain-general substrate is real, but specialisation emerges via canalisation under niche pressure — a position the entry takes explicitly and defends in its theoretical-grounding section. The tension and its resolution are both first-class catalog content.

### Computational analogs

The pipeline has partial analogs in current AI practice that the collection's references survey explicitly: Chinchilla compute-optimal scaling [Hoffmann et al. 2022] is consistent with capacity-first when read as "data is a capacity expansion;" long-context architectures (RoPE, ALiBi, sparse attention, FlashAttention) and retrieval-augmented generation (REALM, RAG, RETRO) are capacity expansions at low marginal control cost; mixture-of-experts (Switch Transformer, Mixtral) scales capacity via expert pool size; the No Free Lunch theorems [Wolpert & Macready 1997] formally ground the niche-specification step. Each analog is partial — none implements the full design-time pipeline — and the collection's contribution is precisely the discipline of composing them in the right order.

### Limitations

Collection status is `draft` even though one member is canonical: collection-level promotion requires multi-source evidence for the collection as a coherent intelligence model, not for any single member. The pipeline-shape claim itself rests primarily on the Turner et al. mathematical derivation; corroborating empirical work for the regime-as-attractor structure across additional independent sources is preliminary. The pipeline assumes deployment-niche commitment is meaningful; foundation-model pretraining (substrate construction) and multi-niche services (router-of-niche-specialists) are out of scope by design.

## 6.3 Composition — Acerebrate Decision-Making

### Source

Nesin, S. M., & Chandrankunnel, M. (2025), _The need for a new perspective on decision-making in bacteria_, _Communicative & Integrative Biology_, 18(1), 2463926 (DOI 10.1080/19420889.2025.2463926, peer-reviewed review article, CC BY 4.0). Corroborating phylogenetic evidence comes from Turner et al. 2026, which places jellyfish and sea anemones (nerve net, no brain) in the passive-storage regime — independent support for the substrate-independence claim that motivates this collection.

### Atomic principles and consolidation

Section-by-section reading of the bacterial source produced three architecturally-consequential atomic principles, each documented in a specific paper section: (a) _Vibrio cholerae_ biofilm commitment requires multi-stream coincidence detection (LuxPQ AND CqsS — both must agree) before the major behavioural transition fires; (b) bacterial decision-making under environmental unpredictability pairs stochastic gene-expression switching (random state-population) with iron-based cellular memory (persistent retention of beneficial states), producing exploration-with-retention; (c) anti-σ proteins act as runtime regulators of the σ factors that themselves regulate gene expression — an explicit control-over-control layer. Each principle was graded CORE under condition (b) of the rubric (intelligence-design pattern divergent from the human / mammalian template, in this case strikingly so: organisms with no nervous system at all).

The corroborating jellyfish / sea anemone placements in Turner et al. produced a fourth atomic principle (_intelligent behaviour is implementable on nerve nets without a brain_) that, paired with the bacterial evidence, satisfies the multi-source rule for the upstream consolidation hub `Embodiment Without Cortex`.

### Member NEXIs

| Slug                           | Layer                                                                       | Status |
| ------------------------------ | --------------------------------------------------------------------------- | ------ |
| `coincidence-detection-gating` | Commitment-gate: major transitions require multi-stream alignment           | draft  |
| `stochastic-memory-coupling`   | Exploration-with-retention: random state-switching + persistent memory      | draft  |
| `meta-regulation`              | Control-over-control: explicit regulators of regulators, dynamic at runtime | draft  |

### The composition shape

The three patterns are layered, not sequenced — they run concurrently within a single agent at runtime:

```
   meta-regulation               (regulators of regulators)
         │  regulates
         ▼
   coincidence-detection-gating  (multi-stream AND-gates on transitions)
         │  informs commitment
         ▼
   stochastic-memory-coupling    (exploration with retention)
```

This is not a temporal pipeline — all three layers run continuously. It is also not a constellation in the §6.1 sense — the layers are differentiated by _function_, not by mutual reinforcement around a shared niche. The composition shape's load-bearing claim is that the three layers are _substrate-independent components_: any implementation that preserves the component logic (molecular regulation in bacteria, simulated regulation in software, hybrid implementations) reproduces the collection's adaptive behaviour. Substrate independence is the property that makes the bacterial pattern engineerable in AI substrates at all, and the collection's structural distinctness rests on it.

### System-level falsifiable hypothesis

> AI architectures that adopt the full acerebrate-decision-making collection (multi-stream coincidence-detection gating + stochastic-memory paired exploration + explicit meta-regulation) outperform same-budget single-axis architectures on decision-making tasks under unpredictability and partial observability, by margins larger than the sum of individual-pattern gains.

Refutation: if composition-designed systems perform no better than the best individual-NEXI baseline at matched compute on appropriately heterogeneous benchmarks (varying environmental predictability, multi-stream context availability, non-stationarity), the collection's compositional claim is refuted. The collection bets that _layered composition is load-bearing_ — that the three layers operating concurrently produce decision quality that none of them in isolation can produce.

### Computational analogs

Multi-stream attention and multi-modal fusion are partial analogs of coincidence-detection-gating, but typically not used as AND-gates on commitment decisions. Reinforcement learning with replay buffers (DQN, PPO with prioritised experience replay) is a partial analog of stochastic-memory-coupling, but treats stochasticity (exploration policy) and memory (replay) as separable engineering concerns rather than as a coupled architectural commitment. Meta-learning and learned optimisers [Hochreiter et al. 2001; Andrychowicz et al. 2016] are partial analogs of meta-regulation, but operate at training time rather than as a runtime architectural layer. Mixture-of-Experts gating is a partial flat (one-level) analog; the bacterial pattern is hierarchical. HyperNet-style architectures (networks generating parameters of other networks) are the closest existing architectural analog of meta-regulation, currently research-frontier rather than deployment-default.

### Limitations

Collection status is `draft`: although the upstream consolidation hub `Embodiment Without Cortex` clears the multi-source rule (Nesin & Chandrankunnel 2025 plus Turner et al. 2026), the individual member NEXIs are still single-source for their specific architectural primitives — Turner et al. provides phylogenetic placement, not atomic principles for coincidence detection, stochastic-memory coupling, or meta-regulation as named architectural patterns. Member-level promotion to canonical waits for additional independent sources at the pattern level. The biology-to-engineering transfer for prokaryotic regulatory networks is also farther from existing AI substrates than the other two collections; the engineering caveat is correspondingly larger.

## 6.4 Cross-collection comparison

The three collections can be compared on four axes that together describe what makes the shape difference architecturally meaningful:

| Collection                     | Shape         | Composition mode                                  | Time mode             | Direction      |
| ------------------------------ | ------------- | ------------------------------------------------- | --------------------- | -------------- |
| Distributed Social Cognition   | Constellation | Graph of mutual dependencies                      | Runtime               | Across agents  |
| Bounded Cognitive Architecture | Pipeline      | Sequenced typed inputs / outputs                  | Design-time           | Through time   |
| Acerebrate Decision-Making     | Composition   | Layered concurrent regulators                     | Runtime               | Across layers  |
| Embodied Action Selection      | Isomorphism   | Same mechanism redeployed via per-domain adapters | Runtime + design-time | Across domains |

The three demonstration shapes plus the fourth (isomorphism, ingested subsequently and summarised in §6.6) are not exhaustive — the framework anticipates that future sources may produce collection shapes the catalog has not yet encountered (lattice, hierarchy, swarm, market). What the four rows already establish is that _shape diversity is real_: nature does not assemble adaptive behaviour in one canonical way, and a catalog that recognises this can place architectural claims at the shape level, not only at the pattern level.

The shape difference also has practical implications for adoption. A constellation collection invites an engineer to instantiate all members concurrently in the deployed agent; a pipeline collection invites the engineer to walk through stages at design-time before any deployment exists; a composition collection invites concurrent layered runtime regulators. Misclassifying a collection's shape — for example, attempting to instantiate the bounded-cognitive-architecture pipeline at runtime as if it were a constellation — produces specific predictable failures, and the framework's `complementarity_notes` field exists to document those.

A further observation: the three demonstration collections span the runtime / design-time axis (two runtime collections and one design-time collection) and the within-agent / across-agent axis (one across-agent collection, two within-agent). The catalog is therefore not a stack of variations on a single problem class; it is a small but structurally diverse first sample of the design space. That diversity is part of the case for the program more broadly (Section 3) — the program predicts that comparative cognition contains structurally distinct intelligence models, and the first three collections bear out the prediction.

## 6.5 Limitations across the three case studies

Several limitations apply to all three collections and warrant explicit reporting before the discussion in Section 7:

**Single-source vs. multi-source asymmetry.** Distributed Social Cognition is single-source (Hagedoorn et al. 2026). Bounded Cognitive Architecture is two-source (Turner et al. 2026 plus Hagedoorn et al. 2026 corroboration on niche-conditional design). Acerebrate Decision-Making is two-source (Nesin & Chandrankunnel 2025 plus Turner et al. 2026 phylogenetic placement). Collection-level promotion to canonical requires multi-source evidence for the collection as a coherent intelligence model; the canonical promotions at the time of writing are all pattern-level (`niche-specification`, `action-selection-as-common-substrate`, and `multi-modal-integration`, each 1.0.0). No collection is yet at canonical status — exactly the visibility the methodology mandates.

**Pre-empirical falsifiability.** Every collection commits to a system-level falsifiable hypothesis stated in operational form (a metric, a benchmark family, a direction of effect, a threshold). None of the hypotheses has yet been empirically tested. The validation level (per §4.6) is _literature + falsifiable hypothesis_, not _literature + toy implementation_; this is the deliberate v1 trade-off between defensibility and growth velocity. A toy-implementation track is part of the future work in Section 8.

**Biology-to-engineering transfer caveats per shape.** Constellation transfer is the most direct: the zebra-finch patterns map onto multi-agent reinforcement learning with multi-modal observation, an active area of current AI research. Pipeline transfer is intermediate: the regime / capacity / niche pattern maps onto deployment-tier architecture decisions but requires the AI engineer to commit to deployment niche before training, which is not the dominant practice. Composition transfer is the farthest: prokaryotic regulatory networks are structurally distant from current AI substrates, and the engineering analogs (HyperNets, hierarchical MoE) are research-frontier. Each collection's `when not to adopt` section catalogs the corresponding caveat.

**Honest in-progress status.** The catalog is at version 1 of an extended program. The case studies in this section are presented as worked examples of methodology and framework, not as final canonical content. The Watch List (§4.8) carries nine active candidates that may produce additional collections and may produce additional shapes; the framework is open to both. The honesty of the in-progress reporting is itself a methodological commitment: a catalog that conceals its draft status fails the reviewer-defensibility bar that is otherwise the program's load-bearing constraint.

The three collections together exercise the framework against three distinct shapes, three sources, and three problem classes. The discussion in Section 7 returns to what they collectively support and what they leave open. Section 6.6 below summarises the fourth collection (Embodied Action Selection, isomorphism shape), ingested after the three case studies were structured, which extends the framework's collection-shape catalogue by one and provides the catalog's second canonical NEXI on cross-substrate evidence.

## 6.6 Addendum: Embodied Action Selection (isomorphism collection)

A fourth collection, **Embodied Action Selection**, was ingested after the three demonstration case studies were structured. It is presented here as an addendum rather than as a fourth co-equal case study because it was not part of the case-study selection that produced the §5.6 / §6.4 collection-shape findings — the shape findings emerged from the first three collections and the fourth confirmed and extended them. The addendum nonetheless documents the collection's contribution to the framework with the same evidentiary discipline applied to §6.1–§6.3.

**Source and provenance.** The collection is anchored to [Nordli & Todd 2022], a peer-reviewed conceptual-analysis article in _Frontiers in Psychology_ (vol. 13, art. 841972; CC BY) that argues the cortico-basal ganglia-thalamo-cortical (CBGTC) loop is the universal vertebrate mechanism for action selection — a recurrent neural circuit conserved virtually unchanged from lamprey (~560 Mya divergence) to modern human, with cognition and heuristic decision-making in humans implemented as exaptations of the same motor-control machinery. The article also introduces a **named formal framework** (the Ecological Context Model) with three numbered equations specifying context construction (`C = {A(g), E}`), behaviour selection (`B(C) = f(Br, Ba(g, P))`), and goal achievement (`g+(C) = f(B, E)`).

**Shape: isomorphism.** The collection's four members all describe the _same architectural function_ under different domain transformations rather than different functions composed together: `action-selection-as-common-substrate` (the substrate-invariant function), `ecological-context-model` (the formalism layer), `exaptation-architectural-reuse` (the generative principle by which one mechanism gets redeployed), and `heuristics-as-habits-fusion` (the concrete behavioural-instance demonstrating the collection's predictive content). The collection's distinctive contribution is structural: "different patterns" turn out to be the same pattern under domain shift. This is categorically distinct from constellation (mutual enabling), pipeline (sequenced stages), and composition (layered concurrent components), and the catalog's framework absorbs it as the fourth collection shape (§5.6).

**System-level falsifiable hypothesis.** AI architectures committing to the full collection — action selection as a first-class substrate-general primitive, formalised via the Ecological Context Model, with explicit exaptive reuse of the same selection mechanism across motor and cognitive domains, and heuristic decisions implemented as a subset of chunked-sequence habits — outperform same-budget architectures that treat action selection as implicit, that separate motor and cognitive control into distinct modules, and that treat heuristics as a categorically separate fast-path. The performance margin is expected on cross-domain benchmarks (embodied agents mixing motor and cognitive operations) and on tasks where the cost of premature commitment is high. Refutation: if isomorphism-designed systems perform no better than the best individual-NEXI baseline at matched compute on cross-domain benchmarks, the collection's isomorphism claim is refuted (the patterns may still be individually useful as standalone NEXIs).

**Catalog impact.** The collection's first member, `action-selection-as-common-substrate`, is the catalog's **second canonical NEXI** (alongside `niche-specification`). Its promotion was justified by cross-substrate triangulation rather than the more typical two-paper convergence: the same architectural function (default-inhibit / selective-disinhibit gating, goal-directed sequence construction, contextual reinforcement) is documented in vertebrate-CBGTC loops [Nordli & Todd 2022], in bacterial molecular regulatory networks [Nesin & Chandrankunnel 2025], and in cnidarian nerve nets via the phylogenetic placement of jellyfish and sea anemones in the passive-storage regime [Turner et al. 2026]. Three substrates; the same architectural pattern; conservation that spans the deepest divergences in animal evolution. The promotion sets a precedent the catalog had not previously needed: cross-substrate evidence — categorically different implementations converging on the same architectural claim — can lift a pattern to canonical status by demonstrating substrate-independence-of-architectural-pattern (§3.2 also discusses the substrate-independence-of-pattern stance the program adopts on this evidence).

**Limitations.** The collection's status is `draft` because three of its four members are still single-source from Nordli & Todd 2022 (the collection contains the catalog's second canonical NEXI but the collection as a whole has not yet accumulated multi-source evidence at the collection-shape level). A second source independently surfacing the isomorphism shape — e.g. cephalopod peripheral cognition extending the cross-substrate evidence to a fourth substrate — would lift the collection itself toward canonical. The Watch List (§4.8) flags candidate corroborating sources accordingly.

**What the addendum demonstrates about the framework.** The fourth collection's emergence after the three case studies were structured is itself a methodological signal: the framework absorbed a new shape without modification because §5.6's claim — that future sources may produce shapes the framework has not yet encountered — was load-bearing rather than rhetorical. The framework's openness to new shapes was tested in practice within weeks of the three-shape finding being articulated, and the extension was clean. This is the kind of confirmation the program prefers: not "the framework already covered it," but "the framework's openness was structural, and the new evidence flowed in without breaking the schema."
