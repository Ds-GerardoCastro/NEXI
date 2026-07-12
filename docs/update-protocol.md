# Update Protocol — Coherence Propagation Order

Any change to NEXI content propagates in a fixed order to keep the project's artifacts coherent: **vault → GitHub repo → whitepaper**. A change originates in the research vault, where the upstream literature review and principle-extraction work lives. Once settled there, it flows into the public GitHub repository (the catalog, `VALIDATION.md`, `CATALOG.md`, `docs/`), and only then into the whitepaper, which presents the full theoretical argument last. Working in this order ensures the whitepaper never asserts something the catalog and vault do not yet support.

Every note edited along that path stamps an `updated:` date in its front matter. The stamp records when the note last moved, making the propagation auditable: a reader can see whether a given artifact reflects the latest state or is still awaiting its turn in the chain. When a change lands, walk the order and stamp each note you touch.

Public artifacts present **new information only**. They report the current state — what a pattern is, what it addresses, that it is validated — not the history of how it got there. Revision trails, internal correction notes, and version churn stay in the vault; the repo and whitepaper read as a clean, present-tense record of what the project now holds to be true.
