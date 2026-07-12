# References — Eavesdropping

## Primary natural-system literature

- **Hagedoorn, K., Tschirren, N., ter Avest, E., Tyson, C., Snijders, L., Griffith, S. C., Naguib, M., & Loning, H. (2025).** _Communication Networks of Wild Zebra Finches (Taeniopygia castanotis)._ bioRxiv preprint (non-peer-reviewed), posted 2025-09-11. DOI: [10.1101/2025.09.11.675577](https://doi.org/10.1101/2025.09.11.675577). License CC-BY-NC-ND 4.0.
  _Correlational field study reconstructing low-strength zebra-finch communication networks from co-singing proximity in arid-zone Australia. The authors report overall low network strength ("birds mostly move around"); the study measures co-singing proximity and does not itself test eavesdropping or third-party inference._

- **McGregor, P. K., & Dabelsteen, T. (1996).** _Communication networks._ In: Kroodsma, D. E., & Miller, E. H. (Eds.), _Ecology and Evolution of Acoustic Communication in Birds_ (pp. 409–425). Cornell University Press.
  _Foundational reference establishing the concept of "communication networks" — networks of potential information flow among individuals — in animal-communication ecology._

- **Snijders, L., & Naguib, M. (2017).** _Communication in animal social networks: a missing link?_ Advances in the Study of Behavior, 49, 297–359.
  _Theoretical synthesis linking communication networks to spatial / movement networks; provides the theoretical basis for treating song-based and proximity-based social networks as related observables._

- **Waas, J. R., Caulfield, M., Colgan, P. W., & Boag, P. T. (2005).** _Colony sound facilitates sexual reproduction in wild zebra finches._ Animal Behaviour, 70(6), 1265–1272.
  _Empirical evidence for a synchronising function of colony soundscape — relevant to the inference that observed third-party interactions carry information beyond their explicit content._

## Computational analogs

- **Veličković, P., Cucurull, G., Casanova, A., Romero, A., Liò, P., & Bengio, Y. (2018).** _Graph Attention Networks._ International Conference on Learning Representations.
  _Partial architectural analog. Standard GAT attends over a node's neighbour **nodes**. Eavesdropping's object is instead a dyadic **edge/interaction** (A↔B) observed by a third party C who does not participate in it. The homology therefore holds only for an **edge-featured / relational (line-graph) attention** variant — attention whose keys and values are the observed dyadic edges (or line-graph nodes), not the participant nodes of vanilla GAT._

- **Foerster, J. N., Song, F., Hughes, E., Burch, N., Dunning, I., Whiteson, S., Botvinick, M., & Bowling, M. (2019).** _Bayesian Action Decoder for Deep Multi-Agent Reinforcement Learning._ International Conference on Machine Learning.
  _Related, not identical. BAD is **self-directed partner observation**: cooperating agents reason about a partner's private information via a **public belief** over observed actions. Eavesdropping differs in that the observer is a **third party** to the interaction it witnesses (not a participant) and the observed channel need not be public. Useful framing for the cooperative case, not a drop-in method for third-party observation._

- **Oliehoek, F. A., & Amato, C. (2016).** _A Concise Introduction to Decentralized POMDPs._ Springer Briefs in Intelligent Systems.
  _Theoretical framing for partially observable multi-agent decision making. Provides the formal substrate for analyzing what eavesdropping changes: an enlargement of each agent's observation set Oᵢ to include witnessed third-party interactions._

## Vault references (private)

- Source ingestion: `Wild Zebra Finch Communication Networks` (sources/)
- Atomic principle: `P02 — Eavesdropping as Network Mechanism` (principles/)
- Consolidation hub: `Eavesdropping` (concepts/)
- Metamodel: `MM1 — Distributed Information Substrate` (analyses/)
- Per-source synthesis: `Analysis — Zebra Finch Communication Networks` (analyses/)
