# References — Exaptation Architectural Reuse

## Primary natural-system literature

- **Nordli, S. A., & Todd, P. M. (2022).** _Embodied and embedded ecological rationality: A common vertebrate mechanism for action selection underlies cognition and heuristic decision-making in humans._ Frontiers in Psychology, **13**, 841972. DOI: [10.3389/fpsyg.2022.841972](https://doi.org/10.3389/fpsyg.2022.841972). License CC BY. Peer-reviewed conceptual-analysis article.
  _Master architectural claim of the source: the cortico-basal ganglia-thalamo-cortical loop, originally evolved for sequential goal-directed motor control, was redeployed in human evolution to regulate cognitive control. Heuristic decision-making and motor habit formation are therefore the same mechanism operating on different repertoires. Provides the strongest existing case for exaptation as a first-class architectural design pressure._

## Internal-external search homology (Hills/Todd/Miller research programme)

- **Hills, T. T., Todd, P. M., & Goldstone, R. L. (2008).** _Search in external and internal spaces: Evidence for generalized cognitive search processes._ Psychological Science, **19**(8), 802–808. DOI: [10.1111/j.1467-9280.2008.02160.x](https://doi.org/10.1111/j.1467-9280.2008.02160.x).
  _Foundational paper of the internal-external search homology programme. Documents that search behaviour in physical and cognitive domains shares neural substrate; cognitive search is exaptive of physical search._

- **Hills, T. T., Todd, P. M., & Jones, M. N. (2015).** _Foraging in semantic fields: How we search through memory._ Topics in Cognitive Science, **7**(3), 513–534. DOI: [10.1111/tops.12151](https://doi.org/10.1111/tops.12151).
  _Continued empirical case for cognitive search as exapted physical search. Cited by Nordli & Todd 2022._

- **Hills, T. T., Todd, P. M., Lazer, D., Redish, A. D., Couzin, I. D., & The Cognitive Search Research Group. (2015).** _Exploration versus exploitation in space, mind, and society._ Trends in Cognitive Sciences, **19**(1), 46–54. DOI: [10.1016/j.tics.2014.10.004](https://doi.org/10.1016/j.tics.2014.10.004).
  _Cross-disciplinary synthesis of exploration-exploitation in physical and cognitive domains. Reinforces the shared-substrate claim._

- **Todd, P. M., & Hills, T. T. (2020).** _Foraging in mind._ Current Directions in Psychological Science, **29**(3), 309–315. DOI: [10.1177/0963721420915861](https://doi.org/10.1177/0963721420915861).
  _Recent synthesis of the foraging-as-search-substrate programme. Cited by Nordli & Todd 2022._

- **Todd, P. M., & Miller, G. F. (2018).** _The evolutionary psychology of extended cognition: Targeted heuristics for human-environment systems._ Behavioural Processes, **161**, 113–119. DOI: [10.1016/j.beproc.2018.07.014](https://doi.org/10.1016/j.beproc.2018.07.014).
  _General-discussion source on extended cognition and the niche-bound heuristics framework. Cited by Nordli & Todd 2022 as foundational for the heuristic-as-exapted-mechanism argument._

## Exaptation theory in evolutionary biology

- **Gould, S. J., & Vrba, E. S. (1982).** _Exaptation — a missing term in the science of form._ Paleobiology, **8**(1), 4–15. DOI: [10.1017/S0094837300004310](https://doi.org/10.1017/S0094837300004310).
  *Foundational paper introducing the term *exaptation* into evolutionary biology — a structure originally adapted for one function co-opted for another. The architectural-reuse NEXI imports this concept directly.*

## Computational analogs

### Multi-task learning and shared encoders

- **Caruana, R. (1997).** _Multitask learning._ Machine Learning, **28**(1), 41–75. DOI: [10.1023/A:1007379606734](https://doi.org/10.1023/A:1007379606734).
  _Foundational paper on multi-task learning. Closest existing AI analog of architectural reuse — shared parameters across tasks. The exaptation NEXI extends the multi-task paradigm with explicit lesion-test infrastructure to verify genuine reuse vs. shallow sharing._

- **Crawshaw, M. (2020).** _Multi-task learning with deep neural networks: A survey._ arXiv: [2009.09796](https://arxiv.org/abs/2009.09796).
  _Recent survey of multi-task learning architectures. Many "shared encoder" claims in this literature would benefit from the audit-reuse-pattern check this NEXI proposes._

### Transfer learning

- **Pan, S. J., & Yang, Q. (2010).** _A survey on transfer learning._ IEEE Transactions on Knowledge and Data Engineering, **22**(10), 1345–1359. DOI: [10.1109/TKDE.2009.191](https://doi.org/10.1109/TKDE.2009.191).
  _Foundational transfer-learning survey. Transfer learning shares features with exaptation but typically operates training-time rather than as a deployment-time architectural commitment._

### Mixture-of-experts as adapter pattern

- **Fedus, W., Zoph, B., & Shazeer, N. (2022).** _Switch Transformer: Scaling to trillion parameter models with simple and efficient sparsity._ JMLR, **23**(120), 1–39. arXiv: [2101.03961](https://arxiv.org/abs/2101.03961).
  _MoE routing as a partial analog of adapter-based dispatch. The MoE gates are routes; the experts are domain-specific. The exaptation NEXI proposes the inverse: shared core M with domain-specific adapters._

### Adapter-based fine-tuning

- **Houlsby, N., et al. (2019).** _Parameter-efficient transfer learning for NLP._ Proceedings of ICML, 2790–2799. arXiv: [1902.00751](https://arxiv.org/abs/1902.00751).
  _Adapter-based fine-tuning — small per-task adapters wrapped around a shared frozen core. Architecturally close to this NEXI's pattern, though typically operating on language tasks rather than across motor/cognitive domains._

## Vault references (private)

- Source ingestion: `Embodied and Embedded Ecological Rationality` (sources/)
- Atomic principles: `P41 — Exaptation of Motor Circuitry for Cognitive Control` · `P46 — Internal-External Search Homology`
- Metamodel: `MM2 — Generalised Implementation: Motor↔Cognitive Isomorphism` (in `Metamodels — Embodied and Embedded Ecological Rationality`)
- Consolidation hubs: `Non-Human Intelligence Patterns` · `Beyond Human-Centric Intelligence`
