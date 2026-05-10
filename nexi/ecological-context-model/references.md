# References — Ecological Context Model

## Primary natural-system literature

- **Nordli, S. A., & Todd, P. M. (2022).** _Embodied and embedded ecological rationality: A common vertebrate mechanism for action selection underlies cognition and heuristic decision-making in humans._ Frontiers in Psychology, **13**, 841972. DOI: [10.3389/fpsyg.2022.841972](https://doi.org/10.3389/fpsyg.2022.841972). License CC BY. Peer-reviewed conceptual-analysis article.
  _Develops the Ecological Context Model in §4 of the article, with three numbered equations (eq. 1: C = {A(g), E}; eq. 2: B(C) = f(Br, Ba(g, P)); eq. 3: g+(C) = f(B, E)) and explicit symbolic notation for environment, agent-perceptible features, behavioural repertoire, perceptions, and behavioural associations. The state-merger commitment — that agent-internal features are part of E rather than a separate inner stage — is in §5._

## Foundational antecedent

- **Lewin, K. (1936).** _Principles of topological psychology._ McGraw-Hill.
  _Lewin's field-theory equation B = f(A, E) — behaviour as a function of agent and environment — is the antecedent the Ecological Context Model generalises. Cited explicitly by Nordli & Todd in §4. Pre-DOI publication; cited by canonical bibliographic record per the catalog's no-DOI quarantine rule._

## Computational analogs

### Cognitive architectures

- **Anderson, J. R., Bothell, D., Byrne, M. D., Douglass, S., Lebiere, C., & Qin, Y. (2004).** _An integrated theory of the mind._ Psychological Review, **111**(4), 1036–1060. DOI: [10.1037/0033-295X.111.4.1036](https://doi.org/10.1037/0033-295X.111.4.1036).
  _ACT-R cognitive architecture — declarative-procedural memory split with chunk-based retrieval. Behavioural associations Ba(g, P) in this NEXI map closely onto ACT-R's procedural-memory chunks, with explicit goal-perception-action structure. ECM extends ACT-R-style architecture with explicit failure-attribution and unified state-merger commitment._

- **Laird, J. E., Newell, A., & Rosenbloom, P. S. (1987).** _Soar: An architecture for general intelligence._ Artificial Intelligence, **33**(1), 1–64. DOI: [10.1016/0004-3702(87)90050-6](<https://doi.org/10.1016/0004-3702(87)90050-6>).
  _Soar architecture — production-system-based cognitive model with operator selection mechanism. Action selection in Soar's operator-elaboration phase is structurally similar to ECM's eq. (2) but does not formalise the unified state E or the failure-attribution distinction._

### Embodied AI and situated cognition

- **Brooks, R. A. (1991).** _Intelligence without representation._ Artificial Intelligence, **47**(1–3), 139–159. DOI: [10.1016/0004-3702(91)90053-M](<https://doi.org/10.1016/0004-3702(91)90053-M>).
  _Subsumption architecture and the situated-cognition critique of representational AI. The state-merger commitment in ECM (agent-internal features as part of E) is consonant with situated-cognition's rejection of separable inner representations, but ECM additionally formalises the relational structure that situated-cognition typically describes informally._

- **Clark, A. (2008).** _Supersizing the mind: Embodiment, action, and cognitive extension._ Oxford University Press.
  _Embodied-cognition framework. ECM's unified-state schema operationalises the embodied-cognition claim that the agent-environment boundary is a modelling convenience rather than an ontological commitment._

### Reinforcement learning with goal-context-action structure

- **Schaul, T., Horgan, D., Gregor, K., & Silver, D. (2015).** _Universal value function approximators._ Proceedings of ICML, 1312–1320.
  _Universal value functions parameterised by goal — partial analog of ECM's goal-conditional behaviour-association structure. ECM extends the framework with explicit context-construction and failure-attribution layers._

## Broader cognitive-science context

- **von Uexküll, J. (1957).** _A stroll through the worlds of animals and men: A picture book of invisible worlds._ In _Instinctive Behavior: The Development of a Modern Concept_ (C. H. Schiller, ed.), pp. 5–80. International Universities Press.
  _Origin of the Umwelt concept — that each species inhabits a perceptual world specific to its sensory apparatus. The E(A) filter in ECM is a direct formalisation of Umwelt. Cited by Nordli & Todd in §1. Pre-DOI translation; cited by canonical bibliographic record per the catalog's no-DOI quarantine rule._

- **Todd, P. M., & Gigerenzer, G. (eds.) (2012).** _Ecological Rationality: Intelligence in the World._ Oxford University Press. DOI: [10.1093/acprof:oso/9780195315448.001.0001](https://doi.org/10.1093/acprof:oso/9780195315448.001.0001).
  _Foundational volume of the ecological rationality research programme. The ECM is a formalisation of ER's core claim that cognition is shaped by environment-task structure. Co-author Todd is also a co-author of this NEXI's primary source._

## Vault references (private)

- Source ingestion: `Embodied and Embedded Ecological Rationality` (sources/)
- Atomic principles: `P42 — Goal-Cyclic Recurrence as Organizational Primary` · `P43 — Agent-Environment Ontological Continuity` · `P45 — Context-Overlap-Driven Behavior Transfer`
- Metamodels: `MM1 — The Ecological Context Model formalism` · `MM4 — Embodiment-as-State-Merger` (both in `Metamodels — Embodied and Embedded Ecological Rationality`)
- Consolidation hubs: `Context-Dependent Semantics` · `Niche-Bound Cognition`
