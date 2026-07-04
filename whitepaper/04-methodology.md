# 4. Methodology

The Nature Intelligence Project's contribution at the methodological level is not a new research finding but a _process_: a defensible, auditable pipeline that turns peer-reviewed comparative-cognition literature into engineering-ready architectural primitives. This section documents that pipeline. The discipline matters because the catalog's two audiences impose conflicting acceptance criteria — engineers want copy-paste utility, reviewers want peer-reviewable rigor — and only an explicit methodology can satisfy both without one bleeding into the other.

The methodology is structured around six commitments: (1) source selection bias toward under-represented biological lineages; (2) section-by-section reading of original sources; (3) atomic-principle extraction with project-relevance grading; (4) cross-source consolidation as the gate for pattern formation; (5) falsifiability as a non-negotiable promotion requirement; and (6) Real Citations Only as a citation discipline. Each is developed below.

## 4.1 The vault → NEXI pipeline

The vault → NEXI pipeline is a six-stage compression of peer-reviewed source material into architectural primitives:

```
Source paper (peer-reviewed, or a vetted preprint en route to peer review)
   ↓ section-by-section reading; atomic principles extracted
Atomic principles (one operationalisable claim per note; graded for project relevance)
   ↓ accumulate evidence across sources; track tensions
Consolidation hub (named pattern; multi-source evidence required)
   ↓ promotion gate (multi-source + falsifiable hypothesis + curation review)
NEXI pattern entry (layered card + machine-readable schema)
   ↓ aggregation by problem class; structural shape identified
NEXI collection (system-level falsifiable hypothesis + complementarity notes)
```

Each stage has explicit acceptance criteria and an audit trail. No claim moves downstream without provenance to the source paper preserved through every prior stage.

## 4.2 Source selection bias

The catalog explicitly prefers peer-reviewed work on intelligence in non-mammalian, non-primate species. The rationale is structural rather than ideological: the existing AI design template already over-represents mammalian and human cognition (Section 3.2), and the catalog's mission is to widen the design space by sampling under-represented biological lineages. The three sources active at the time of writing — wild zebra finches [Hagedoorn et al. 2026], cognitive-capacity research that draws on jellyfish, sea anemones, nematodes, flatworms, tardigrades, corvids, elephants, cetaceans, and great apes [Turner et al. 2026], and bacterial decision-making [Nesin & Chandrankunnel 2025] — exemplify the bias: birds, marine invertebrates, and prokaryotes outnumber primate-derived material by design. Mammalian and primate sources are admissible but evaluated for what makes them _distinct from_ human intelligence, not what makes them similar.

## 4.3 Section-by-section reading and atomic principles

Each source paper is read section by section, with attention concentrated on the architecturally-consequential portions: mechanism, pathway, regulation, signaling, control, dynamics, and network. Abstract, introduction, and conclusion are necessary context but rarely expose the architectural primitives that the pipeline targets — those primitives sit in the experimental sections, in the regulatory diagrams, and in the methods. A reading that stops at abstract-level claims systematically misses the level of detail that makes the resulting NEXI engineerable. The methodology has been refined to make this stage non-negotiable: paper-level summaries alone, however well-structured, do not produce defensible architectural primitives.

From each section, _atomic principles_ are extracted. An atomic principle is one operationalisable claim, written in one short note, with the citation chain back to the source section preserved. Atomic decomposition is necessary because the consolidation step (Section 4.5) requires that principles from different sources be matched on _what they each claim_, not on what their parent papers happen to be _about_. A paper-level summary is too coarse for that match.

## 4.4 Project-relevance grading

Each atomic principle is graded for relevance to the program at extraction time:

- **CORE** — the principle either (a) load-bears the architectural pillar (world models, sample efficiency, sensory grounding) _or_ (b) reveals an intelligence-design pattern that diverges meaningfully from the human / mammalian template. Either condition qualifies; both are common.
- **SUPPORTING** — useful framing or scaffolding, but the principle does not carry the thesis on its own.
- **TANGENTIAL** — paper-internal interest only; admitted to the vault for completeness but excluded from consolidation.

The expanded CORE rubric (with the (b) condition) is a deliberate choice: it allows the catalog to grow in two directions simultaneously, both of which are load-bearing for the program. Grading is judgement-laden and recorded with a one-paragraph rationale on the principle note. The audit trail is what allows a reviewer to disagree with a grade without losing the underlying claim.

## 4.5 Consolidation hubs and the multi-source rule

A _consolidation hub_ is a named pattern that emerges when atomic principles from multiple sources converge on the same architectural claim. The hub-formation rule is simple and strict: a hub materialises only when at least two atomic principles from at least two independent sources converge. Single-source evidence is logged but does not produce a hub.

This rule is the catalog's primary defence against single-paper artefacts. A pattern observed in one paper, no matter how striking, may reflect that source's experimental conditions, the paper's framing, or a coincidence of terminology. A pattern observed across two independent peer-reviewed sources, both extracted as atomic principles, is unlikely to be any of those things.

Hubs are named so that the consolidation produces a vocabulary for further reasoning: _Eavesdropping_, _Multi-Modal Integration_, _Multi-Level Social Structure_, _Sensor Coverage Limits_, _Context-Dependent Semantics_, _Non-Human Intelligence Patterns_, _Niche-Bound Cognition_, _Embodiment Without Cortex_ — each pulled directly from the consolidation work. The names are then tested by writing them into NEXI entries; names that fail to translate cleanly into engineering primitives are revisited rather than retained on the strength of their first appearance.

## 4.6 The falsifiability requirement

Every promoted NEXI must commit to a falsifiable architectural hypothesis. The standard is operational: the hypothesis must specify _what_ is being compared, _under what conditions_, _with what metric_, predicting _what direction of effect_, and _what threshold_ counts as a meaningful effect. A claim like _"this pattern helps multi-agent systems"_ is not falsifiable; a claim like _"this pattern reduces episode count to a target performance threshold by more than 10% on partially-observable cooperative benchmarks at equal training compute"_ is.

The methodology distinguishes three validation levels — (1) literature-only, (2) literature + falsifiable hypothesis, (3) literature + toy implementation — and selects level 2 for v1 of the catalog as the deliberate balance between defensibility and growth velocity. Level 3 admits empirical test but cannot scale at the rate required for a useful catalog; level 1 fails the reviewer-defensibility bar. Level 2 commits to falsifiability without requiring the test, while leaving the test as a downstream invitation.

A pattern whose hypothesis is later refuted is marked `deprecated` and retained for traceability — the catalog tracks negative results, not just positive ones.

## 4.7 Tensions log

Cross-source contradictions are logged explicitly in a _Tensions Log_. The premise is that the highest-value scientific signal lives in disagreements, not in confirmations. When two sources converge on a claim, the methodology records a hub; when they diverge, the methodology records a tension. Both are first-class outputs of the pipeline.

The tension between Turner et al.'s domain-general capacity-axis (the g-factor view) and the niche-bound specialisation evidence in the zebra finch communication-network literature is a worked example. Rather than picking a side, the catalog logs the tension and records the synthesis that the relevant NEXI (`niche-specification`) draws from it: domain-general substrate is real, but specialisation emerges via canalisation under niche pressure. The synthesis becomes part of the pattern's theoretical grounding; the disagreement is not pretended away.

## 4.8 Operating surfaces

The pipeline is supported by four operating surfaces that together provide navigation, audit, prospective tracking, and aggregate signal:

- **Map of Contents (MOC).** A hand-curated entry-point note that links to every active hub, every collection, and every per-source analysis. Used to onboard new readers and to verify graph connectivity across the vault.
- **Tensions Log.** As described in §4.7. Append-only; entries are not deleted when resolved, only annotated with the resolution.
- **Watch List.** A staged queue of candidate NEXIs at three pre-promotion tiers (single-source, multi-source-but-not-yet-hub, hub-but-not-yet-promoted). The Watch List is what makes future-work claims (Section 8) concrete rather than aspirational; at the time of writing it carries nine active candidates across the three tiers.
- **Signal Dashboard.** A Dataview-driven aggregate view that computes hub counts, multi-source coverage, status-field distribution, and citation-validation status across the vault and the repo simultaneously. Engineering hygiene for a research artefact.

Together, these four surfaces let the methodology operate at the scale required for a catalog without losing the discipline required at each individual entry.

## 4.9 Citation discipline (Real Citations Only)

The methodology adopts _Real Citations Only_ as a design constraint, not a quality goal. Every citation in any catalog artefact (NEXI entry, collection, white paper) must resolve to a verifiable record on CrossRef, PubMed, arXiv, or a recognised preprint server. DOIs are preferred over titles wherever a DOI exists. Author-year citations without a DOI are admissible only for pre-1995 references and for sources without registered DOIs (older monographs, philosophical works); these are quarantined in a no-DOI section of the references list and never mixed with verified entries.

A vendored verification toolkit (`tools/citation/`, MIT-licensed) provides deterministic resolution of DOIs, PubMed identifiers, and arXiv identifiers against the relevant API. Validation is run before any citation enters an artefact and again before any external publication. The validator's output is a _signal_, not just a check: a fresh preprint that has not yet been indexed by CrossRef returns a 404, which is a known caveat — the methodology requires that such cases be _documented as deferred-verification_ rather than silently included or silently dropped. This is what distinguishes citation discipline from citation theatre.

## 4.10 Provenance chain

Every claim in the catalog traces back to peer-reviewed literature through an unbroken chain:

```
NEXI entry / collection
   ↓ cites
Vault consolidation hub (named pattern)
   ↓ cites
Atomic principle (one note, one claim)
   ↓ cites
Source paper section (DOI + page reference)
```

The white paper cites NEXI entries and collections; NEXI entries cite vault notes and source papers; vault notes cite the literature directly. There are no circular references and no vault note that floats unanchored. This is the structural property that lets a reviewer audit the catalog without trusting any individual claim — every claim's chain back to a peer-reviewed paper is finite, traceable, and short.

The methodology in this section produces a stream of validated patterns. The framework in Section 5 is what those patterns enter — the catalog's structural shape, schema, application formats, and the collection-shape finding that emerged retrospectively from the construction of the first three collections.
