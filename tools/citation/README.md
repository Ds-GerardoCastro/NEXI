# `tools/citation/` — Deterministic citation verification

A small toolkit for **verifying that every citation in NEXI artefacts (NEXI entries, cluster entries, white paper) refers to a paper that actually exists**, with the metadata we claim. The scripts make external API calls to CrossRef, PubMed, arXiv, and Google Scholar. They are deterministic — they catch the kind of plausible-looking-but-slightly-wrong citation that an LLM can generate confidently.

> **Provenance:** vendored from [K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer) under MIT License (upstream commit `5bf6b59`, version 2.13.0). See [`UPSTREAM.md`](UPSTREAM.md) for credits, license, and rationale.

## What's here

| File                       | Purpose                                                                                                          |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `doi_to_bibtex.py`         | Convert a DOI (or list of DOIs) into BibTeX entries via CrossRef.                                                |
| `extract_metadata.py`      | Extract paper metadata from any of: DOI / PubMed ID / arXiv ID / URL.                                            |
| `format_bibtex.py`         | Clean up a BibTeX file — sort, deduplicate, normalise field formatting.                                          |
| `search_google_scholar.py` | Search Google Scholar by query, author, title. Produces BibTeX.                                                  |
| `search_pubmed.py`         | Search PubMed via NCBI E-utilities. Returns rich metadata.                                                       |
| `validate_citations.py`    | Validate a BibTeX file against API-resolved truth: existence, author match, year match, missing required fields. |
| `bibtex_template.bib`      | Reference templates for each entry type (article, book, inproceedings, etc.).                                    |
| `citation_checklist.md`    | Pre-flight checklist for verifying a manuscript's bibliography.                                                  |

## When to invoke them in the NEXI workflow

The discipline (per `whitepaper/README.md`'s **Real Citations Only** policy):

1. **Before** any citation is added to:
   - A NEXI entry's `references.md`
   - A NEXI entry's `nexi.yaml` `natural_exemplars[].paper.doi`
   - A cluster's `references` or `cluster.yaml`
   - A white-paper chapter or `whitepaper/REFERENCES.md`

   → run `extract_metadata.py` or `doi_to_bibtex.py` to confirm the paper exists with the metadata claimed.

2. **Before any commit** that touches a `references.md` or the white paper's bibliography:
   → run `validate_citations.py` against the modified BibTeX or the references file converted to BibTeX.

3. **Before any white-paper chapter is marked draft-complete:**
   → walk through `citation_checklist.md` and verify every item.

This is the closest the catalog has to a citation-level CI gate. It runs locally for now; later it should run in GitHub Actions on PRs that touch references.

## Setup

Requirements: Python 3.10+ and the `requests` library.

```bash
cd tools/citation
pip install -r requirements.txt
```

The scripts use `python` shebangs; on Windows where the Microsoft Store stub may intercept `python3`, invoke `python` directly.

## Usage examples

### Verify a DOI exists and produce its BibTeX entry

```bash
python doi_to_bibtex.py 10.48550/arXiv.2203.15556
# → @misc{...} BibTeX block, or "Error: DOI not found" if unresolvable.
```

A "DOI not found" result is **signal**, not error. It means the citation as written cannot be verified through CrossRef — investigate whether the DOI is wrong, whether the paper is too new to be indexed (common for fresh preprints), or whether the source uses a non-CrossRef DOI registry (e.g., DataCite for datasets).

### Resolve metadata from any identifier

```bash
python extract_metadata.py --doi 10.1101/2024.06.10.598315
python extract_metadata.py --pmid 12345678
python extract_metadata.py --arxiv 2203.15556
python extract_metadata.py --url https://arxiv.org/abs/2203.15556
```

### Validate a BibTeX file end-to-end

```bash
python validate_citations.py path/to/references.bib
# Checks: required-field completeness, format compliance, optionally
# verifies entries via API lookups.
```

### Search PubMed for niche-specific literature

```bash
python search_pubmed.py "working memory capacity rhesus macaque" --max-results 20
```

## Known caveats

- **Preprints often aren't in CrossRef yet.** A 2026 biorxiv preprint may return "DOI not found" for a few weeks after posting. This is a CrossRef indexing lag, not a citation error. For preprints, prefer `--arxiv` or biorxiv's own resolver where applicable.
- **Google Scholar rate-limits aggressively.** `search_google_scholar.py` includes random delay handling, but expect occasional failures. Don't run it in tight loops.
- **PubMed coverage is biomedical.** Computer-science / cognitive-science papers may not be indexed; prefer arXiv or DOI lookup for those.
- **No project-specific configuration.** The scripts use the upstream defaults — `User-Agent` strings still reference the upstream `support@example.com`. Acceptable for a small private repo; if we go public and start hitting rate limits, customise the User-Agent strings.

## How to re-sync with upstream

If upstream releases new versions of the scripts:

```bash
# From the repo root, with $UPSTREAM checked out alongside
diff -ur tools/citation/<script>.py $UPSTREAM/.claude/skills/citation-management/scripts/<script>.py
```

If the diff is clean (no NEXI-specific modifications), copy the new versions over and update the upstream-commit reference in `UPSTREAM.md`. If we have local modifications, document them in `UPSTREAM.md` first so the merge is informed.
