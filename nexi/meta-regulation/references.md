# References — Meta-Regulation

## Primary natural-system literature

- **Nesin, S. M., & Chandrankunnel, M. (2025).** _The need for a new perspective on decision-making in bacteria._ Communicative & Integrative Biology, **18**(1), 2463926. DOI: [10.1080/19420889.2025.2463926](https://doi.org/10.1080/19420889.2025.2463926). License CC BY 4.0. Peer-reviewed review article.
  _Documents the bacterial three-level regulatory hierarchy: anti-σ proteins control σ factors which control RNA polymerase which controls genes. Section: Multiple pathways in bacteria and their interconnectedness. Each strain has multiple types of σ factors AND multiple anti-σ types — diversity at the regulator-of-regulator level. Extracytoplasmic-function (ECF) σ-factors play a specific bridging role between environmental sensing and gene expression._

## Computational analogs

### Meta-learning (training-time, not the same primitive)

- **Hochreiter, S., Younger, A. S., & Conwell, P. R. (2001).** _Learning to Learn Using Gradient Descent._ International Conference on Artificial Neural Networks.
  _Foundational meta-learning paper. Bacterial meta-regulation differs in that it operates as a runtime architectural layer, not as a training-time gradient-of-gradient procedure._

- **Andrychowicz, M., et al. (2016).** _Learning to learn by gradient descent by gradient descent._ NeurIPS. arXiv: [1606.04474](https://arxiv.org/abs/1606.04474).
  _Learned optimisers as a meta-learning paradigm. Shows that the meta-layer can be learned, but it is then frozen at deployment. Bacterial meta-regulation is a runtime layer with its own ongoing dynamics._

### HyperNet-style architectures

- **Ha, D., Dai, A., & Le, Q. V. (2017).** _HyperNetworks._ ICLR. arXiv: [1609.09106](https://arxiv.org/abs/1609.09106).
  _Networks that generate parameters of other networks. Closer architectural analog to bacterial meta-regulation than vanilla meta-learning — at least the meta-layer is structurally explicit. Still typically static at inference; the bacterial pattern argues for runtime dynamics._

### Mixture-of-Experts routing

- **Shazeer, N., et al. (2017).** _Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer._ arXiv: [1701.06538](https://arxiv.org/abs/1701.06538).
- **Fedus, W., Zoph, B., & Shazeer, N. (2021).** _Switch Transformer: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity._ arXiv: [2101.03961](https://arxiv.org/abs/2101.03961).
  _Gating networks decide which experts to activate. Partial analog of meta-regulation — gates do control downstream activation. But MoE gates are flat / one-level, while bacterial regulation is hierarchical with explicit control-over-the-control as a separate layer._

### Dynamic neural networks

- **Han, Y., et al. (2021).** _Dynamic Neural Networks: A Survey._ IEEE Transactions on Pattern Analysis and Machine Intelligence. arXiv: [2102.04906](https://arxiv.org/abs/2102.04906).
  _Survey of dynamic neural networks — networks that adapt structure or parameters based on input. The bacterial pattern is a specific design within this space: adaptation via an explicit meta-regulator layer rather than via dataset-conditioning or input-routing alone._

## Hierarchical control in cognitive science and neuroscience

- **Botvinick, M. M. (2008).** _Hierarchical models of behavior and prefrontal function._ Trends in Cognitive Sciences 12(5), 201–208.
  _Hierarchical control in mammalian prefrontal cortex. The bacterial three-level regulatory hierarchy is a substrate-independent realisation of similar architectural principles, in a system without a nervous system._

## Avoiding the regress

- **Russell, S. (2019).** _Human Compatible: Artificial Intelligence and the Problem of Control._ Viking.
  _General argument for terminating control hierarchies at stable layers; relevant to the meta-regulation regress-termination design choice._

## Vault references (private)

- Source ingestion: `Decision-Making in Bacteria` (sources/)
- Atomic principles: `P38 — Meta-Regulation (Regulators of Regulators)`, `P31 — Sigma-Factor Frequency Modulation` (principles/)
- Metamodel: `MM7 — Meta-Regulation as a First-Class Architectural Layer` (in `Metamodels — Decision-Making in Bacteria` deep-read addendum)
- Consolidation hub: `Embodiment Without Cortex` (concepts/)
