# References — Capacity-First Scaling

## Primary natural-system literature

- **Turner, C. R., Russek, E. M., Seed, A., McEwen, E. S., Vélez, N., Morgan, T. J. H., & Griffiths, T. L. (2026).** _Cognitive capacity and control in the evolution of intelligence._ bioRxiv preprint, posted 2026-03-09. DOI: [10.1101/2026.03.07.710317](https://doi.org/10.1101/2026.03.07.710317). License CC-BY 4.0.
  _Mathematical evolutionary-optimality model of working memory in which capacity contributes linearly to recall efficacy and control contributes sublinearly with severe diminishing returns. Empirical validation via retro-cue task fits to humans and rhesus macaques._

## Comparative-cognition / brain-evolution context

- **Sterelny, K. (2003).** _Thought in a Hostile World: The Evolution of Human Cognition._ Blackwell Publishing.
  _General framing for the evolution of cognition under environmental constraint._
- **Cantlon, J. F., & Piantadosi, S. T. (2024).** _Uniquely human intelligence arose from expanded information capacity._ Nature Reviews Psychology 3, 275–293.
  _The information-capacity hypothesis the Turner et al. results modify — single-axis capacity-as-everything-driver framing._
- **Halford, G. S., Wilson, W. H., & Phillips, S. (1998).** _Processing capacity defined by relational complexity: implications for comparative, developmental, and cognitive psychology._ Behavioral and Brain Sciences 21, 803–831.
  _Capacity as the upper bound on relational-complexity tasks across species and developmental stages._
- **Musslick, S., & Cohen, J. D. (2021).** _Rationalizing constraints on the capacity for cognitive control._ Trends in Cognitive Sciences 25, 757–775.
  _Modern computational treatment of why control is bounded; complementary to Turner et al.'s synergy framing._

## Computational analogs

### Compute-optimal scaling

- **Hoffmann, J., et al. (2022).** _Training Compute-Optimal Large Language Models._ arXiv:2203.15556.
  _The Chinchilla result: compute-optimal allocation between parameters and data is more data-heavy than prior practice. Data is a capacity expansion (more representations the model absorbs); pure parameter scaling without matching data is a control-axis bias._

### Long-context architectures

- **Su, J., Lu, Y., Pan, S., Murtadha, A., Wen, B., & Liu, Y. (2021).** _RoFormer: Enhanced Transformer with Rotary Position Embedding._ arXiv:2104.09864.
- **Press, O., Smith, N. A., & Lewis, M. (2021).** _Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation._ arXiv:2108.12409.
- **Beltagy, I., Peters, M. E., & Cohan, A. (2020).** _Longformer: The Long-Document Transformer._ arXiv:2004.05150.
- **Dao, T., Fu, D. Y., Ermon, S., Rudra, A., & Ré, C. (2022).** _FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness._ arXiv:2205.14135.

  _Capacity expansion (longer context window) at low marginal control cost. Empirical wins on long-document tasks are predicted by the rule._

### Retrieval-augmented generation

- **Guu, K., Lee, K., Tung, Z., Pasupat, P., & Chang, M.-W. (2020).** _REALM: Retrieval-Augmented Language Model Pre-Training._ arXiv:2002.08909.
- **Lewis, P., et al. (2020).** _Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks._ NeurIPS 2020. arXiv:2005.11401.
- **Borgeaud, S., et al. (2022).** _Improving language models by retrieving from trillions of tokens (RETRO)._ ICML 2022. arXiv:2112.04426.

  _External retrieval store as a capacity primitive. The rule predicts retrieval should outperform same-budget control-side scaling on memory-bound tasks._

### Memory-augmented neural networks

- **Graves, A., Wayne, G., & Danihelka, I. (2014).** _Neural Turing Machines._ arXiv:1410.5401.
- **Graves, A., et al. (2016).** _Hybrid computing using a neural network with dynamic external memory (Differentiable Neural Computer)._ Nature 538, 471–476.

  _Explicit external storage as capacity primitive in deep learning, with attention over memory as the control component._

### Mixture-of-Experts

- **Shazeer, N., et al. (2017).** _Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer._ arXiv:1701.06538.
- **Fedus, W., Zoph, B., & Shazeer, N. (2021).** _Switch Transformer: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity._ arXiv:2101.03961.

  _Expert-pool size = capacity dimension; routing sophistication = control dimension. The empirical pattern that MoE scales best when expert count grows faster than routing sophistication is consistent with the rule._

### Information theory and complexity

- **Papadimitriou, C. H. (1994).** _Computational Complexity._ Addison-Wesley, Reading, MA.
  _The space hierarchy theorem — formal result that systems with strictly more storage can solve strictly more problems. Foundational for the capacity-as-storage-bound framing._

## Vault references (private)

- Source ingestion: `Cognitive Capacity and Control in the Evolution of Intelligence` (sources/)
- Atomic principles: `P17 — Capacity Prioritized in Joint Evolution`, `P20 — Capacity-First Evolutionary Sequence`, `P15 — Capacity-Control Synergy (No Trade-off)`, `P16 — Strongest Synergy at Intermediate Values`, `P13 — Capacity as Storage Bound on Problem Solving` (principles/)
- Per-source analysis: `Analysis — Cognitive Capacity and Control in the Evolution of Intelligence` (analyses/)
- Metamodels analysis: `Metamodels — Cognitive Capacity and Control in the Evolution of Intelligence`, specifically MM3 (Prerequisite Ordering of Primitives) (analyses/)
- Consolidation hub: `Non-Human Intelligence Patterns` (concepts/)
