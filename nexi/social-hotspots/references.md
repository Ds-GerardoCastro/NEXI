# References — Social Hotspots

## Primary natural-system literature

- **Hagedoorn, K., Tschirren, N., ter Avest, E., Tyson, C., Snijders, L., Griffith, S. C., Naguib, M., & Loning, H. (2025).** _Communication Networks of Wild Zebra Finches (Taeniopygia castanotis)._ bioRxiv preprint, posted 2025-09-11. DOI: [10.1101/2025.09.11.675577](https://doi.org/10.1101/2025.09.11.675577). License CC-BY-NC-ND 4.0.
  _Documents social hotspots in arid-zone zebra finch populations as structured information hubs (not anonymous gathering points), with repeated encounters mixing known and unknown individuals. Frames the possible functions of these hotspots in hedged terms (foraging information and condition signalling directly; predation dilution and breeding synchronisation by reference to the secondary literature it cites)._

- **Waas, J. R., Caulfield, M., Colgan, P. W., & Boag, P. T. (2000).** _Colony sound facilitates sexual and agonistic activities in royal penguins._ Animal Behaviour, 60, 77–84.
  _Cross-species evidence that colony-level sound aggregation facilitates reproductive and agonistic activity (in royal penguins, Eudyptes schlegeli). Supports the general principle that convergence-plus-colony-sound is functional, but is not evidence in zebra finches; cited here as a comparative analog for hotspots as functional aggregations._

- **Ward, P., & Zahavi, A. (1973).** _The importance of certain assemblages of birds as "information-centres" for food-finding._ Ibis, 115(4), 517–534.
  _Foundational "information centre" hypothesis — bird roosts and gatherings as places where individuals gain foraging information from others. Directly relevant to the hotspot framing._

## Distributed cognition and collective behaviour

- **Hutchins, E. (1995).** _Cognition in the Wild._ MIT Press.
  _Foundational treatment of distributed cognition — cognition as residing in networks of agents and artefacts in shared environments, not in any single head. Theoretical anchor for the hotspot pattern._

- **Couzin, I. D. (2009).** _Collective cognition in animal groups._ Trends in Cognitive Sciences, 13(1), 36–43.
  _Synthesis of how groups of animals process information collectively, with explicit attention to spatial structure and density-dependent dynamics._

## Computational analogs

- **Spatial attention mechanisms** in computer vision and robotics — proximity-weighted attention is the standard architectural primitive that this NEXI generalises.

- **Schaul, T., Quan, J., Antonoglou, I., & Silver, D. (2016).** _Prioritized Experience Replay._ ICLR 2016.
  _The closest existing method: non-uniform weighting of stored experience by a salience signal. This NEXI's proximity-weighted retrieval is a spatial cousin of PER's priority-weighted sampling. The residual novelty is that the weighting is keyed to shared cross-agent loci (PER prioritises a single agent's own replay buffer), treats density-of-convergence as a first-class signal, and admits a virtual/topical analog. See "Relation to existing methods" in [`README.md`](README.md)._

- **Density-Based Spatial Clustering of Applications with Noise (DBSCAN)** — Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). KDD 1996.
  _Foundational clustering algorithm that scales to dynamic spatial data; suitable backend for hotspot detection._

- **DeepMind Melting Pot 2.0** — Agapiou, J. P., et al. (2022). _Melting Pot 2.0._ arXiv:2211.13746.
  _Suite of multi-agent reinforcement-learning substrates with fixed evaluation scenarios. The "Coins" and "Clean Up" cooperative-foraging substrates provide the named, compute-matched benchmark against which this pattern's >=10% episode-efficiency target is pre-registered (see falsifiable hypothesis)._

- **Trending detection on social platforms** — the virtual-space analog of physical hotspot detection. Not a single canonical reference but a well-developed engineering practice.

## Vault references (private)

- Atomic principle: `P10 — Social Hotspots as Information Hubs`
- Consolidation hub: `Eavesdropping` (related; hotspots are where eavesdropping pays off)
- Metamodel: `MM1 — Distributed Information Substrate`
- Source ingestion: `Wild Zebra Finch Communication Networks`
