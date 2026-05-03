# References — Cognitive Regime Selection

## Primary natural-system literature

- **Turner, C. R., Russek, E. M., Seed, A., McEwen, E. S., Vélez, N., Morgan, T. J. H., & Griffiths, T. L. (2026).** _Cognitive capacity and control in the evolution of intelligence._ bioRxiv preprint, posted 2026-03-09. DOI: [10.1101/2026.03.07.710317](https://doi.org/10.1101/2026.03.07.710317). License CC-BY 4.0.
  _Mathematical model deriving three discrete regimes (passive-storage, control-enhanced, capacity-heavy) from the interaction of capacity-control synergy non-monotonicity with metabolic-cost selection. Empirical validation via retro-cue task on humans and rhesus macaques shows both species fall in the control-enhanced regime — a notable null result against the information-capacity hypothesis._

## Phylogenetic placement literature (Turner et al. references)

### Passive-storage regime — basal nervous systems

- Comparative-cognition treatments of cnidarian (jellyfish, sea anemone) and basal-metazoan nervous systems supporting sensitisation-style storage without selective attention or interference shielding (see Turner et al. references 65, 66 for the specific citations).

### Transitional regime — nematodes, flatworms, tardigrades

- Comparative neuroscience documenting rudimentary brain-like ganglion structures in nematodes, flatworms, and tardigrades, with multi-cue context tracking and representation shielding (see Turner et al. references 67, 68).

### Control-enhanced regime — corvids, elephants, cetaceans, great apes

- Working-memory control literature documenting rehearsal, resistance to interference, and attention control in corvids (refs 26, 59, 69, 70 in Turner et al.).

## Comparative-cognition foundations

- **MacLean, E. L., et al. (2014).** _The evolution of self-control._ Proceedings of the National Academy of Sciences 111, E2140–E2148.
  _36-species study linking self-control, brain size, and dietary generality — an empirical anchor for cross-species cognitive comparison that Turner et al. extend._
- **Burkart, J. M., Schubiger, M. N., & van Schaik, C. P. (2017).** _The evolution of general intelligence._ Behavioral and Brain Sciences 40, e195.
  _Cross-species evidence for a single information-processing construct correlated with brain size — the g-factor framing the regime taxonomy partially refines._
- **Engle, R. W. (2018).** _Working memory and executive attention: A revisit._ Perspectives on Psychological Science 13, 190–193.
  _Working-memory and executive-attention framing in humans, useful as a calibration anchor for the control-enhanced regime._

## Computational analogs

### Phase transitions and discrete attractors

- Phase-transition models in optimisation landscapes provide formal language for the "discrete attractors with phase boundaries" claim. While no specific paper directly mirrors Turner et al.'s three regimes for AI architectures, the underlying mathematics (regime-switching dynamical systems, discrete-attractor models) is well-established and applicable.

### Deployment-tier reasoning in production ML

- Practical model-family scaling (Phi, Llama-2/3, GPT-3.5/4, Gemini, Claude) consistently shows qualitative architectural differences across tiers — not just hyperparameter changes — supporting the claim that regime structure is real even when not explicitly named. No single canonical citation; the pattern is observable across multiple model families' release notes and architecture descriptions.

### Architecture-as-niche-fit (NAS literature)

- **Tan, M., & Le, Q. V. (2019).** _EfficientNet: Rethinking Model Scaling for Convolutional Neural Networks._ arXiv:1905.11946.
  _Compound scaling — depth, width, resolution scaled together — is regime-classification at micro-scale. The discovered "compound scaling coefficient" is a regime-fit parameter._
- **Zoph, B., & Le, Q. V. (2017).** _Neural Architecture Search with Reinforcement Learning._ arXiv:1611.01578.
  _NAS in general searches for niche-fit architectures; the regime taxonomy is a high-level meta-NAS structure._

### Cognitive science treatments of regime structure

- **Cantlon, J. F., & Piantadosi, S. T. (2024).** _Uniquely human intelligence arose from expanded information capacity._ Nature Reviews Psychology 3, 275–293.
  _The information-capacity hypothesis the empirical retro-cue result modifies — a single capacity axis predicts capacity-heavy placement; Turner et al.'s data show humans + macaques in control-enhanced._

## No-Free-Lunch grounding

- **Wolpert, D. H., & Macready, W. G. (1997).** _No free lunch theorems for optimization._ IEEE Transactions on Evolutionary Computation 1, 67–82.
  _Formal statement that no algorithm performs best across all problem distributions. Provides theoretical grounding for why a single architecture cannot dominate across niches — a necessary precondition for regime-conditional architecture selection to be principled._

## Vault references (private)

- Source ingestion: `Cognitive Capacity and Control in the Evolution of Intelligence` (sources/)
- Atomic principles: `P18 — Three Cognitive Regimes Across Species`, `P21 — Phylogenetic Placement of Cognitive Regimes`, `P25 — Empirical Validation: Humans and Macaques in Control-Enhanced Regime`, `P22 — Information-Processing G-Factor Across Species` (principles/)
- Per-source analysis: `Analysis — Cognitive Capacity and Control in the Evolution of Intelligence` (analyses/)
- Metamodels analysis: `Metamodels — Cognitive Capacity and Control in the Evolution of Intelligence`, specifically MM4 (Discrete Regime Topology) (analyses/)
- Consolidation hub: `Non-Human Intelligence Patterns` (concepts/)
