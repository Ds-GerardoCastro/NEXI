# Upstream credit and license

These citation-management scripts are imported, unmodified, from
[K-Dense-AI/claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer)
under the upstream MIT License. The originals live at
`.claude/skills/citation-management/scripts/` and `.claude/skills/citation-management/assets/`
in that repository.

## What was imported

| File                       | Source path                                                           |
| -------------------------- | --------------------------------------------------------------------- |
| `doi_to_bibtex.py`         | `.claude/skills/citation-management/scripts/doi_to_bibtex.py`         |
| `extract_metadata.py`      | `.claude/skills/citation-management/scripts/extract_metadata.py`      |
| `format_bibtex.py`         | `.claude/skills/citation-management/scripts/format_bibtex.py`         |
| `search_google_scholar.py` | `.claude/skills/citation-management/scripts/search_google_scholar.py` |
| `search_pubmed.py`         | `.claude/skills/citation-management/scripts/search_pubmed.py`         |
| `validate_citations.py`    | `.claude/skills/citation-management/scripts/validate_citations.py`    |
| `bibtex_template.bib`      | `.claude/skills/citation-management/assets/bibtex_template.bib`       |
| `citation_checklist.md`    | `.claude/skills/citation-management/assets/citation_checklist.md`     |

Imported at upstream commit `5bf6b59` (2026-04-20, version 2.13.0).

## Why we vendored rather than installing the full plugin

The full `claude-scientific-writer` plugin (24 skills) is heavily clinical/medical-biased and ships an opinionated workflow (LaTeX-first, IMRaD default, Parallel Web Systems lock-in) that does not fit the NEXI white-paper context. The citation-management scripts in isolation are deterministic verifiers — they make CrossRef / PubMed / Google Scholar API calls and check that cited papers actually exist as cited — and that is the strongest single value the upstream plugin offers for our use case. Importing only this slice avoids the workflow lock-in while preserving the verification capability.

See the upstream `LICENSE` file (also vendored as `UPSTREAM_LICENSE` in this directory) for the full MIT license text.

## Modifications

None at import time. If the scripts diverge from upstream in the future, document the diffs here so that re-syncing with upstream remains straightforward.
