# References — Expansion-Readout Circuit

## Primary natural-system literature

- **Roth, G. (2015).** _Convergent evolution of complex brains and high intelligence._ Philosophical Transactions of the Royal Society B: Biological Sciences, **370**(1684), 20150049. DOI: [10.1098/rstb.2015.0049](https://doi.org/10.1098/rstb.2015.0049). Peer-reviewed review article in a themed issue on the origins of intelligence.
  _The sole source for this NEXI's circuit-motif claim. Reviews convergent emergence of complex brains across five lineages — insect mushroom bodies, octopod vertical lobe, cichlid pallium, corvid/psittacid avian pallium, and mammalian isocortex — and identifies the same architectural motif (expand-then-readout via orthogonal crossbar) instantiated on non-homologous neural substrates. Quantitative cytoarchitecture in honeybee (300k Kenyon cells × 800 PN via 1M synapses) and octopus (1.8M × 26M × 65k via orthogonal crossbar)._

## Primary cytoarchitecture sources (cited by Roth)

- **Strausfeld, N. J. (2012).** _Arthropod Brains: Evolution, Functional Elegance, and Historical Significance._ Harvard University Press.
  _Foundational reference for insect mushroom-body cytoarchitecture. Source for the Kenyon-cell numbers (300 000, 15× packing density) Roth cites._

- **Hochner, B. (2012).** _An embodied view of octopus neurobiology._ Current Biology, **22**(20), R887–R892.
  _Review of octopus nervous system. Cited by Roth 2015 for vertical-lobe cytoarchitecture._

- **Shomrat, T., Zarrella, I., Fiorito, G., & Hochner, B. (2008).** _The octopus vertical lobe modulates short-term learning rate and uses LTP to acquire long-term memory._ Current Biology, **18**(5), 337–342. DOI: [10.1016/j.cub.2008.01.056](https://doi.org/10.1016/j.cub.2008.01.056).
  _Primary electrophysiological evidence for octopus vertical-lobe learning role. Establishes lesion-defined cognitive bottleneck (Fiorito & Chichery) and synaptic plasticity in the orthogonal crossbar._

## Computational analogs

### Cerebellum-like circuits — closest CS analog of the motif

- **Marr, D. (1969).** _A theory of cerebellar cortex._ Journal of Physiology, **202**(2), 437–470.
  _Foundational computational theory of the cerebellar circuit as expansion-readout. Marr's model: granule cells (millions, sparse activation) feed Purkinje cells (few, sparse readout) via parallel fibres in an orthogonal arrangement._

- **Albus, J. S. (1971).** _A theory of cerebellar function._ Mathematical Biosciences, **10**(1–2), 25–61. DOI: [10.1016/0025-5564(71)90051-4](https://doi.org/10.1016/0025-5564(71)90051-4).
  _Complementary computational theory of cerebellum. Together Marr + Albus form the foundational pair for cerebellum-as-expansion-readout._

- **Dean, P., Porrill, J., Ekerot, C.-F., & Jörntell, H. (2010).** _The cerebellar microcircuit as an adaptive filter: experimental and computational evidence._ Nature Reviews Neuroscience, **11**(1), 30–43. DOI: [10.1038/nrn2756](https://doi.org/10.1038/nrn2756).
  _Modern synthesis of cerebellar computational architecture. The expansion-readout-with-adaptive-readout view this NEXI inherits._

### Reservoir computing / liquid state machines — most direct AI analog

- **Jaeger, H. (2001).** _The "echo state" approach to analysing and training recurrent neural networks._ GMD Technical Report 148, German National Research Center for Information Technology.
  _Original echo-state-network proposal. Fixed/random high-dimensional projection (the reservoir) + trained sparse readout — the most direct AI implementation of the convergent-divergent fan motif._

- **Maass, W., Natschläger, T., & Markram, H. (2002).** _Real-time computing without stable states: A new framework for neural computation based on perturbations._ Neural Computation, **14**(11), 2531–2560. DOI: [10.1162/089976602760407955](https://doi.org/10.1162/089976602760407955).
  _Liquid State Machine. Same architectural commitment with spiking-neural-network instantiation._

### Sparse routing and mixture-of-experts

- **Fedus, W., Zoph, B., & Shazeer, N. (2022).** _Switch Transformer: Scaling to trillion parameter models with simple and efficient sparsity._ JMLR, **23**(120), 1–39. arXiv: [2101.03961](https://arxiv.org/abs/2101.03961).
  _Sparse mixture-of-experts as the closest mainstream-AI analog of the motif at the expansion-stage scale. Each forward pass selects a sparse subset of expert sub-networks; the routing layer is the readout._

- **Shazeer, N., et al. (2017).** _Outrageously large neural networks: The sparsely-gated mixture-of-experts layer._ ICLR 2017. arXiv: [1701.06538](https://arxiv.org/abs/1701.06538).
  _Original sparse MoE proposal._

### Random projection and kernel methods

- **Rahimi, A., & Recht, B. (2007).** _Random features for large-scale kernel machines._ NIPS 2007.
  _Random-feature-expansion approach to kernel methods. The algorithmic-level analog of the convergent-divergent fan: high-dimensional random projection + trained linear readout._

## Vault references (private)

- Source ingestion: `Convergent evolution of complex brains and high intelligence` (sources/, added 2026-05-17)
- Atomic principles: `P47 — Convergent-Divergent Fan Circuit Motif` · `P48 — Orthogonal Crossbar Substrate` · `P49 — Soma Miniaturisation as Capacity Scaling Axis` · `P50 — Polyphyletic Intelligence via Non-Homologous Modules`
- Consolidation hub: `Convergent-Divergent Fan` (new 2026-05-17)
- Metamodels: `MM1 — Expand-Then-Readout as Substrate-General Circuit Motif (Roth)` · `MM2 — Architectural Polyphyly as Substrate-Independence Evidence (Roth)`
- Internal-only vocabulary: *convergent-divergent fan* (the biological-origin name; public NEXI slug uses CS-functional name)
