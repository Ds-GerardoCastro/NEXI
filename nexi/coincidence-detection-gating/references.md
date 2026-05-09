# References — Coincidence-Detection Gating

## Primary natural-system literature

- **Nesin, S. M., & Chandrankunnel, M. (2025).** _The need for a new perspective on decision-making in bacteria._ Communicative & Integrative Biology, **18**(1), 2463926. DOI: [10.1080/19420889.2025.2463926](https://doi.org/10.1080/19420889.2025.2463926). License CC BY 4.0. Peer-reviewed review article.
  _Documents the bacterial coincidence-detection mechanism: V. cholerae biofilm formation requires BOTH LuxPQ (responding to AI-2) AND CqsS (responding to CAI-1) to be activated. Uses the explicit phrase "coincidence detection" for the gating logic. Section: Multiple pathways in bacteria and their interconnectedness._

## Computational analogs

### Multi-modal fusion and AND-gating

- **Baltrušaitis, T., Ahuja, C., & Morency, L.-P. (2019).** _Multimodal Machine Learning: A Survey and Taxonomy._ IEEE Transactions on Pattern Analysis and Machine Intelligence 41(2), 423–443. DOI: [10.1109/TPAMI.2018.2798607](https://doi.org/10.1109/TPAMI.2018.2798607).
  _Multi-modal fusion strategies in current AI. Most are average / late-fusion; coincidence-detection-gating is the AND-gate variant operating at the commitment-decision layer rather than the input layer._

### Evidence accumulation in decision-making

- **Ratcliff, R., & McKoon, G. (2008).** _The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks._ Neural Computation 20(4), 873–922.
  _Drift-diffusion models accumulate noisy evidence to threshold; closely related to per-stream evidence accumulation in this NEXI's design. The architectural extension is multi-stream AND-gating across qualitatively different evidence sources._

### Safety-critical AND-gating in robotics and control

- **Leveson, N. (2011).** _Engineering a Safer World: Systems Thinking Applied to Safety._ MIT Press.
  _Safety engineering's classical use of AND-gating across redundant sensor channels for fail-safe commitment. Coincidence-detection-gating extends the pattern to AI agentic decision-making._

## Broader cognitive-science context

- **Gold, J. I., & Shadlen, M. N. (2007).** _The Neural Basis of Decision Making._ Annual Review of Neuroscience 30, 535–574.
  _Multi-area integration in primate decision-making. Premotor and parietal cortex coincidence-detection patterns; biological grounding for the AND-gating primitive in mammalian brains._

## Vault references (private)

- Source ingestion: `Decision-Making in Bacteria` (sources/)
- Atomic principle: `P28 — Cell-Density Switched Behavior` (principles/) — including the secondary analysis that surfaces the author's explicit "coincidence detection" terminology
- Metamodel: `MM6 — Multi-Stream Coincidence Detection as Decision Gating` (in `Metamodels — Decision-Making in Bacteria`)
- Consolidation hub: `Embodiment Without Cortex` (concepts/)
