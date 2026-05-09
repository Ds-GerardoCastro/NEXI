# References — Stochastic-Memory Coupling

## Primary natural-system literature

- **Nesin, S. M., & Chandrankunnel, M. (2025).** _The need for a new perspective on decision-making in bacteria._ Communicative & Integrative Biology, **18**(1), 2463926. DOI: [10.1080/19420889.2025.2463926](https://doi.org/10.1080/19420889.2025.2463926). License CC BY 4.0. Peer-reviewed review article.
  _Documents the paired stochastic-memory primitive in bacterial decision-making under unpredictability. Section: Bacterial interaction with the environment. Cites Landmann et al. 2021 as the theoretical model. Iron-based signal transduction documented as the molecular substrate of cellular memory; ~4-generation swarming memory as a multi-generational example._

## Theoretical model for the pairing

- **Landmann, S., et al. (2021).** _Dynamic regulatory architecture for environmental learning._ eLife.
  _Cited as ref [12] in Nesin & Chandrankunnel 2025. Theoretical demonstration that phenotypic heterogenicity depends on stochastic switching across different states, AND that the switching requires cellular memory as a crucial component. Independent corroboration of the pairing-as-primitive claim._

  > Note: Specific paper title and authors per Nesin & Chandrankunnel's reference list. Verify full author list and DOI before promoting this NEXI from `draft` to `canonical`.

## Computational analogs

### Reinforcement learning — stochasticity and memory as separable techniques

- **Mnih, V., et al. (2015).** _Human-level control through deep reinforcement learning._ Nature 518, 529–533.
  _Deep Q-Networks pair ε-greedy exploration with replay buffers — a partial computational analog. The bacterial pattern argues these should be coupled at the architectural level (memory shapes which transitions persist; transitions populate memory) rather than as parallel engineering techniques._

- **Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2016).** _Prioritized Experience Replay._ ICLR. arXiv: [1511.05952](https://arxiv.org/abs/1511.05952).
  _Replay buffer with prioritisation moves toward the coupled architecture by biasing replay sampling. Closer to the bacterial pattern, but still treats stochasticity (action selection) and memory (replay) as separable._

### Options framework

- **Sutton, R. S., Precup, D., & Singh, S. (1999).** _Between MDPs and semi-MDPs: A framework for temporal abstraction in reinforcement learning._ Artificial Intelligence 112(1-2), 181–211.
  _Options framework provides discrete behavioural states with their own policies. The architectural extension this NEXI proposes is explicit memory-biased stochastic transition between options, with the memory integrating multiple stimuli rather than a single reward channel._

### Bayesian non-stationarity handling

- **Fortunato, M., et al. (2018).** _Noisy Networks for Exploration._ ICLR. arXiv: [1706.10295](https://arxiv.org/abs/1706.10295).
  _Parametric noise in network weights as a structured exploration mechanism. Complementary to the bacterial pattern; could be combined with persistent memory in the coupled architecture._

## Multi-generational memory

- **Lambert, G., & Kussell, E. (2014).** _Memory and fitness optimization of bacteria under fluctuating environments._ PLoS Genetics 10(9), e1004556.
  _Empirical demonstration of bacterial memory and its fitness consequences under environmental fluctuation. Independent biological evidence supporting the cellular-memory side of the paired primitive._

## Vault references (private)

- Source ingestion: `Decision-Making in Bacteria` (sources/)
- Atomic principles: `P37 — Stochastic-Memory Coupling`, `P29 — Bacterial Anticipatory Behavior and Cellular Memory`, `P36 — Clone Individuality` (principles/)
- Metamodel: paired primitive emerging from MM4 + MM5 in `Metamodels — Decision-Making in Bacteria`
- Consolidation hub: `Embodiment Without Cortex`, `Niche-Bound Cognition` (concepts/)
