# White Paper: Nature Intelligence Project

> A research program proposing that AI's design space can be expanded by mining peer-reviewed comparative cognition for architectural primitives the perceptron lineage has not yet borrowed. NEXI (Nature Expression of Intelligence) is the catalog that operationalises the program.

**Author:** Juan Gerardo Castro Sanchez
**Status:** Working draft. Sections in active development. Not for distribution.
**Format:** Multi-file markdown, intended for pandoc conversion to LaTeX / PDF when stable.

## Files

| File                                                     | Section                        | Status           |
| -------------------------------------------------------- | ------------------------------ | ---------------- |
| [`OUTLINE.md`](OUTLINE.md)                               | Full section plan              | Active           |
| [`00-abstract.md`](00-abstract.md)                       | Abstract                       | Drafted          |
| [`01-introduction.md`](01-introduction.md)               | 1. Introduction                | Drafted          |
| [`02-background.md`](02-background.md)                   | 2. Background and Related Work | Stub             |
| [`03-two-pillar-critique.md`](03-two-pillar-critique.md) | 3. The Two-Pillar Critique     | Drafted          |
| [`04-methodology.md`](04-methodology.md)                 | 4. Methodology                 | Stub             |
| [`05-nexi-framework.md`](05-nexi-framework.md)           | 5. The NEXI Framework          | Stub             |
| [`06-case-study.md`](06-case-study.md)                   | 6. Case Study                  | Stub             |
| [`07-discussion.md`](07-discussion.md)                   | 7. Discussion                  | Stub             |
| [`08-future-work.md`](08-future-work.md)                 | 8. Future Work                 | Stub             |
| [`09-conclusion.md`](09-conclusion.md)                   | 9. Conclusion                  | Stub             |
| [`REFERENCES.md`](REFERENCES.md)                         | Bibliography                   | Active (growing) |

## Reading order

For a reviewer: read in numerical order. Section 3 is the conceptual core; Sections 5–6 are the operational core; Section 7 is the falsifiability discussion.

For a collaborator: start with [`OUTLINE.md`](OUTLINE.md) for the overall argument shape, then the sections marked Active or Drafted.

## Real Citations Only — citation discipline

This white paper enforces a **Real Citations Only** policy. The rule and the enforcement mechanism:

### The rule

Every citation in any chapter, in [`REFERENCES.md`](REFERENCES.md), and in any cross-referenced NEXI / cluster `references.md` or `nexi.yaml` must be a **real, verifiable paper found in CrossRef, PubMed, arXiv, or a recognised preprint server**. Specifically:

- **Zero tolerance for placeholder citations.** No "Smith et al. 2023" unless `Smith et al. 2023` resolves to a real paper with the cited title and authors.
- **DOIs preferred over titles** wherever a DOI exists. Author-year-only citations are acceptable for pre-1995 references and for sources without registered DOIs (e.g., older monographs, philosophical works); these are tracked separately in [`REFERENCES.md`](REFERENCES.md) under a clearly-marked "no-DOI" section.
- **Preprint citations include the preprint server and posting date.** A bioRxiv preprint citation must include the bioRxiv DOI and the posting date even when no peer-reviewed version exists.
- **Metadata must match the cited claim.** Year, authors, title, and venue as cited must match the paper actually retrieved by the verification toolkit. A 2024 paper cited as 2023 fails the policy.

### The verification mechanism

The deterministic verifiers live in [`tools/citation/`](../tools/citation/) — a vendored slice of the MIT-licensed [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) plugin. See [`tools/citation/README.md`](../tools/citation/README.md) for full usage.

The discipline:

1. **Before any citation is added** to a chapter or to `REFERENCES.md`, run `python tools/citation/extract_metadata.py --doi <DOI>` (or `--arxiv`, `--pmid`, `--url`) and confirm the returned metadata matches the citation as written.
2. **Before any commit** that touches `REFERENCES.md` or any chapter's bibliography, run `python tools/citation/validate_citations.py path/to/references.bib`. The commit gate is failing if any required-field check fails or any API-resolved metadata mismatches the claim.
3. **Before any chapter is marked draft-complete**, walk through [`tools/citation/citation_checklist.md`](../tools/citation/citation_checklist.md) and verify every item.
4. **Before any external publication** (arXiv preprint upload, peer-review submission), re-run the validator against the final BibTeX. No exceptions.

### Why this matters

The white paper is one of three artefacts that constitute the PhD-ticket strategy (vault → NEXI repo → white paper). For the white paper to function as a credible application artefact, every claim must be traceable to a real, verifiable source. The verifier catches the kind of error a careful human reviewer would catch — a slightly-wrong year, a missing author, a misattributed venue — that an LLM can confidently produce.

### Known caveats

- **Fresh preprints often aren't in CrossRef yet.** A bioRxiv preprint posted in the last few weeks may return "DOI not found" from `doi_to_bibtex.py`. This is CrossRef indexing lag, not a citation error. For very fresh preprints, verify via the preprint server's own resolver and document the deferred CrossRef-verification status in `REFERENCES.md`.
- **No-DOI references are acceptable but quarantined.** Brunswik 1956, Neisser 1976, and similar pre-DOI references stay in a clearly-marked "no-DOI section" of `REFERENCES.md`. They cannot be API-verified; they are accepted on the strength of their canonical-text status.
- **The User-Agent strings in the upstream scripts default to a placeholder email.** Acceptable for low-volume private use; if we go public, customise as documented in [`tools/citation/README.md`](../tools/citation/README.md).
