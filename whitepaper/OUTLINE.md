# Outline

> The full section plan with status. Each section has a target length, a stated argument, and dependencies.

## Abstract — `00-abstract.md`

**Status:** Drafted.
**Target:** ~250 words.
**Argument:** Two converging critiques of modern AI (architectural and template) jointly motivate a research program (Nature Intelligence Project) that mines comparative cognition for architectural primitives. NEXI is the operationalising catalog.

## 1. Introduction — `01-introduction.md`

**Status:** Drafted.
**Target:** ~1,500 words.
**Argument:** Sets up the structural failure of LLM-based agentic AI, motivates the architectural critique (LeCun), then introduces the template critique as the missing companion claim. Concludes with the proposal: mine comparative cognition for design primitives. Roadmaps the rest of the paper.

## 2. Background and Related Work — `02-background.md`

**Status:** Drafted.
**Target:** ~2,500 words.
**Planned coverage:**

- World models in AI: from Schmidhuber's early world-model proposals through JEPA / V-JEPA.
- Scaling-law debates: Sutton's "Bitter Lesson", Kaplan et al., the LeCun / Marcus critiques.
- Comparative cognition and animal-cognition literature relevant to AI design.
- Existing pattern-catalog approaches in software engineering and AI.
- Why a curated, falsifiability-disciplined catalog of _biology-derived_ architectural primitives does not yet exist in a form usable by AI engineers.

## 3. The Two-Pillar Critique — `03-two-pillar-critique.md`

**Status:** Drafted.
**Target:** ~2,500 words.
**Argument:** The conceptual core of the paper. Develops the architectural pillar (LeCun's world-model argument) and the template pillar (perceptron-lineage narrowness) in detail. Shows how they converge on a single research direction. Establishes the falsifiability of the program at the program level (individual NEXIs and collections carry their own sub-claims).

## 4. Methodology — `04-methodology.md`

**Status:** Drafted.
**Target:** ~1,500 words.
**Planned coverage:**

- The vault → NEXI pipeline: how peer-reviewed sources are processed into design primitives.
- The provenance chain: paper → atomic principle → consolidation hub → NEXI / collection.
- Curation discipline: project-relevance grading, multi-source evidence, falsifiable hypothesis requirement.
- The signal/noise architecture: tensions log, dashboard, layered cards.

## 5. The NEXI Framework — `05-nexi-framework.md`

**Status:** Drafted.
**Target:** ~2,000 words.
**Planned coverage:**

- The two-layer catalog: collections and patterns.
- NEXI metadata schema, layered card structure, application formats.
- The collection-as-intelligence-model concept: why complementarity is first-class.
- The status field as audit trail.
- The repository structure as a contribution-friendly artifact.

## 6. Case Studies: Three Collection Shapes — `06-case-study.md`

**Status:** Drafted (~3,200 words at first draft; below the original 5,500 target because collection READMEs in the repo carry full implementation depth and the chapter focuses on what the white paper specifically must show — methodology exercise + shape-diversity finding).
**Target:** ~5,500 words.
**Planned coverage:**

- **6.1 Constellation — Distributed Social Cognition** (zebra finch source). Source paper, principles extracted, the five resulting NEXIs and their constellation collection, the collection's system-level falsifiable hypothesis, the complementarity story (why subsetting degrades referential robustness), honest single-source-of-evidence caveats and draft status of member NEXIs.
- **6.2 Pipeline — Bounded Cognitive Architecture** (cognitive-capacity-limits source). Source paper, principles extracted, the resulting NEXIs and their pipeline collection, the collection's system-level falsifiable hypothesis (downstream stages depend on upstream capacity limits being honoured), and the multi-source promotion of `niche-specification` to canonical status across this collection and 6.1.
- **6.3 Composition — Acerebrate Decision-Making** (bacterial-community source). Source paper, principles extracted, the resulting NEXIs and their composition collection, the collection's system-level falsifiable hypothesis (substrate-independent components reproduce adaptive bacterial collective behaviour), and the substantive contribution this collection makes to the template pillar (intelligence without neurons, sometimes without multicellularity).
- **6.4 Cross-collection comparison.** What the three shapes (constellation, pipeline, composition) reveal about the geometry of natural intelligence designs; why a single canonical shape would have been the more suspicious finding.
- Honest reporting of limitations across all three: single-source vs. multi-source evidence by collection; draft vs. canonical status of individual NEXIs; the transfer-to-engineering caveats specific to each shape.

## 7. Discussion — `07-discussion.md`

**Status:** Drafted.
**Target:** ~1,500 words.
**Planned coverage:**

- Limitations of the approach (single-source caveats, biology-to-engineering translation gaps).
- Falsifiability of the overall program (architectural pillar, template pillar, individual NEXI hypotheses).
- Relationship to mainstream AI research: what the program complements, what it challenges.
- Counter-arguments: scaling-law optimism, the bitter lesson, "biology is not engineering".

## 8. Future Work — `08-future-work.md`

**Status:** Drafted.
**Target:** ~1,000 words.
**Planned coverage:**

- The catalog growth roadmap (longer arc, multi-clade, eventual public release).
- Empirical-validation track: which NEXIs admit toy implementations soonest.
- Community contribution model.
- Open-question track for the PhD thesis itself.

## 9. Conclusion — `09-conclusion.md`

**Status:** Drafted.
**Target:** ~600 words.
**Argument:** Restates the two pillars, summarises the contribution (catalog + methodology + first collection as demonstration), and positions the work within the broader research conversation.

## References — `REFERENCES.md`

**Status:** Active, growing as sections are drafted.

---

**Total target length:** ~19,000 words across all sections (a substantial conference / arxiv-grade white paper, not a journal-length monograph). The expansion from a prior ~16,000-word target reflects chapter 6's restructuring into three collection-shape case studies rather than a single demonstration.

**Ordering of work:** introduction and Section 3 first (conceptual scaffolding); Section 5 (NEXI framework) and Section 6 (case study) second (operational core); Sections 2, 4, 7 third (situating, methodology, falsifiability); Sections 8, 9 last (forward-looking and concluding).
