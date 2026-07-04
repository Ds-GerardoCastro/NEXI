# References — Action Selection as Common Substrate

## Primary natural-system literature

- **Nordli, S. A., & Todd, P. M. (2022).** _Embodied and embedded ecological rationality: A common vertebrate mechanism for action selection underlies cognition and heuristic decision-making in humans._ Frontiers in Psychology, **13**, 841972. DOI: [10.3389/fpsyg.2022.841972](https://doi.org/10.3389/fpsyg.2022.841972). License CC BY. Peer-reviewed conceptual-analysis article.
  _Develops the case that the cortico-basal ganglia-thalamo-cortical (CBGTC) loop is the universal vertebrate mechanism for action selection, conserved virtually unchanged from lamprey (~560 Mya) to modern humans. Provides the vertebrate-substrate exemplar for this NEXI's substrate-general claim. Also develops the Ecological Context Model formalism that anchors the rest of the embodied-action-selection collection._

- **Nesin, S. M., & Chandrankunnel, M. (2025).** _The need for a new perspective on decision-making in bacteria._ Communicative & Integrative Biology, **18**(1), 2463926. DOI: [10.1080/19420889.2025.2463926](https://doi.org/10.1080/19420889.2025.2463926). License CC BY 4.0. Peer-reviewed review article.
  _Documents action-selection-like architecture in bacteria — convergent-divergent molecular pathways implementing the equivalent of default-inhibit / selective-disinhibit gating, cell-density-switched behaviour producing sequence construction, and operon-regulon-module hierarchy producing contextual reinforcement. Provides the bacterial-substrate exemplar; establishes that action-selection architecture appears in organisms with no nervous system at all._

- **Turner, C. R., Russek, E. M., Seed, A., McEwen, E. S., Vélez, N., Morgan, T. J. H., & Griffiths, T. L. (2026).** _Cognitive capacity and control in the evolution of intelligence._ bioRxiv preprint. DOI: [10.1101/2026.03.07.710317](https://doi.org/10.1101/2026.03.07.710317).
  _Phylogenetic placement of jellyfish and sea anemones (cnidarians, nerve net, no brain) in the passive-storage cognitive regime — documented action selection via sensitisation. Provides the cnidarian-substrate exemplar; completes the cross-substrate triangulation (molecular / nerve-net / vertebrate-CBGTC) that lifts this NEXI to canonical status._

## Supporting vertebrate-neuroscience literature

- **Grillner, S., & Robertson, B. (2016).** _The basal ganglia over 500 million years._ Current Biology, **26**(20), R1088–R1100. DOI: [10.1016/j.cub.2016.06.041](https://doi.org/10.1016/j.cub.2016.06.041).
  _Review of basal-ganglia conservation across vertebrates. Cited extensively by Nordli & Todd 2022 for the lamprey-to-human conservation claim._

- **Stephenson-Jones, M., Samuelsson, E., Ericsson, J., Robertson, B., & Grillner, S. (2011).** _Evolutionary conservation of the basal ganglia as a common vertebrate mechanism for action selection._ Current Biology, **21**(13), 1081–1091. DOI: [10.1016/j.cub.2011.05.001](https://doi.org/10.1016/j.cub.2011.05.001).
  _Primary empirical paper establishing the lamprey basal-ganglia / human basal-ganglia structural and functional homology. Foundational citation for Nordli & Todd's claim._

- **Reiner, A. (2010).** _The conservative evolution of the vertebrate basal ganglia._ Handbook of Behavioral Neuroscience, **20**, 29–62. DOI: [10.1016/B978-0-12-374767-9.00002-0](https://doi.org/10.1016/B978-0-12-374767-9.00002-0).
  _Comprehensive review of basal-ganglia conservation. Cited by Nordli & Todd 2022._

## Computational analogs

### Action heads in reinforcement learning

- **Mnih, V., et al. (2015).** _Human-level control through deep reinforcement learning._ Nature, **518**, 529–533. DOI: [10.1038/nature14236](https://doi.org/10.1038/nature14236).
  _DQN's action-head architecture — partial analog of explicit action selection, but typically not treated as a lesionable, inspectable module. The wrapping pattern proposed in this NEXI's architecture overview applies directly._

- **Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017).** _Proximal policy optimization algorithms._ arXiv: [1707.06347](https://arxiv.org/abs/1707.06347).
  _PPO policy networks produce candidate distributions over actions; the architectural pattern is closest to candidate enumeration + competition, but lacks explicit default-inhibit / selective-disinhibit gating._

### Tool selection in LLM agentic systems

- **Schick, T., et al. (2023).** _Toolformer: Language models can teach themselves to use tools._ arXiv: [2302.04761](https://arxiv.org/abs/2302.04761).
  _Tool selection as a special case of action selection. Decision provenance is implicit; the architecture proposed in this NEXI would expose it as a first-class module._

### MoE routing as implicit selection

- **Fedus, W., Zoph, B., & Shazeer, N. (2022).** _Switch Transformer: Scaling to trillion parameter models with simple and efficient sparsity._ JMLR, **23**(120), 1–39. arXiv: [2101.03961](https://arxiv.org/abs/2101.03961).
  _MoE routing performs implicit selection over experts. Partial analog of the gate component, but lacks default-inhibit semantics and contextual-reinforcement loop._

## Broader cognitive-science context

- **Redgrave, P., Prescott, T. J., & Gurney, K. (1999).** _The basal ganglia: a vertebrate solution to the selection problem?_ Neuroscience, **89**(4), 1009–1023. DOI: [10.1016/S0306-4522(98)00319-4](<https://doi.org/10.1016/S0306-4522(98)00319-4>).
  _Influential proposal that vertebrate basal-ganglia architecture exists specifically to solve the action-selection problem. Cited by Nordli & Todd 2022 and central to the framing this NEXI inherits._

- **Houk, J. C., Adams, J. L., & Barto, A. G. (1995).** _A model of how the basal ganglia generate and use neural signals that predict reinforcement._ In _Models of Information Processing in the Basal Ganglia_ (J. C. Houk, J. L. Davis, & D. G. Beiser, eds.), pp. 249–270. MIT Press.
  _Foundational link between basal-ganglia function and reinforcement-learning theory. The contextual-reinforcement-loop component of this NEXI's architecture inherits this connection._

## Vault references (private)

- Source ingestion: `Embodied and Embedded Ecological Rationality` (sources/) · `Decision-Making in Bacteria` (sources/) · `Cognitive Capacity and Control in the Evolution of Intelligence` (sources/)
- Atomic principles: `P39 — CBGTC Loop as Universal Vertebrate Action-Selection Substrate` · `P21 — Phylogenetic Placement of Cognitive Regimes` · `P26 — Convergent-Divergent Molecular Pathways` · `P28 — Cell-Density Switched Behavior` · `P30 — Modular Regulatory Hierarchy (Operon-Regulon-Module)`
- Metamodels: `MM2 — Generalised Implementation: Motor↔Cognitive Isomorphism` (Nordli & Todd) · `MM1 — Substrate-Independent Architectural Primitives` (Nesin & Chandrankunnel)
- Consolidation hubs: `Non-Human Intelligence Patterns` · `Embodiment Without Cortex`
