# 4. Methodology

> **Status: stub.** Section to be developed in a subsequent revision.

## 4.1 The vault → NEXI pipeline

Planned coverage:

```
Scientific paper
   ↓ ingest into research vault
Atomic principles (graded for project relevance)
   ↓ accumulate evidence across sources
Consolidation hub (named pattern, multi-source evidence)
   ↓ promotion gate (falsifiable hypothesis required)
NEXI pattern entry
   ↓ aggregation
NEXI cluster (intelligence model, system-level hypothesis)
```

Each stage has explicit acceptance criteria and curation discipline.

## 4.2 Source selection bias

The catalog explicitly prefers peer-reviewed work on intelligence in non-mammalian, non-primate species. Rationale: the existing AI design template already over-represents mammalian / human cognition; the catalog grows the design space by sampling under-represented biological lineages. Mammalian and primate sources are admissible but evaluated for what makes them _distinct from_ human intelligence, not what makes them similar.

## 4.3 Project-relevance grading

Each atomic principle ingested from a source is graded for relevance to the program:

- **CORE** — directly load-bears the architectural pillar (world models, sample efficiency, sensory grounding) _or_ reveals an intelligence-design pattern that diverges from the human / mammalian template.
- **SUPPORTING** — useful framing or scaffolding, doesn't carry the thesis on its own.
- **TANGENTIAL** — paper-internal interest only.

Grading is judgment-laden and recorded with rationale (audit trail).

## 4.4 The falsifiability requirement

Every promoted NEXI must commit to a falsifiable architectural hypothesis. The standard is operational: the hypothesis must specify what is compared, under what conditions, with what metric, predicting what direction of effect, with what threshold for a meaningful effect. The methodology distinguishes three validation levels (literature-only, literature + falsifiable hypothesis, literature + toy implementation) and selects the middle level for v1 of the catalog as the deliberate balance between defensibility and growth velocity.

## 4.5 Tensions log and signal architecture

Cross-source contradictions are logged explicitly in a _tensions log_ — the highest-value scientific signal lives in disagreements, not in confirmations. The methodology mandates surfacing tensions rather than burying them.

## 4.6 Provenance chain

Every claim in NEXI traces back to peer-reviewed literature through an unbroken chain: NEXI entry → vault consolidation hub → atomic principle → source paper → DOI. The white paper cites NEXI entries and clusters; NEXI entries cite vault notes and source papers; vault notes cite the literature directly. No circular references; every claim grounds in peer-reviewed work.
