# Open letter to the authors of _Embodied and embedded ecological rationality_

**To:** Dr. Samuel A. Nordli, Dr. Peter M. Todd — co-authors of _Embodied and embedded ecological rationality: A common vertebrate mechanism for action selection underlies cognition and heuristic decision-making in humans_ (Frontiers in Psychology, 2022)

**From:** Juan Gerardo Castro Sánchez · Nature Intelligence Project · ds.gerardocastro@gmail.com

**Date:** 10 May 2026

**Re:** Four engineerable patterns from your 2022 conceptual analysis — including the catalog's first citable formal framework and second canonical pattern

---

Dear Dr. Nordli and Dr. Todd,

I am writing to introduce the **Nature Intelligence Project** and to explain what your 2022 article _Embodied and embedded ecological rationality_ ([DOI 10.3389/fpsyg.2022.841972](https://doi.org/10.3389/fpsyg.2022.841972)) has contributed to it. Your paper is the source of **8 principles**, **one new collection of four named patterns**, the catalog's **second canonical pattern** (promoted on cross-substrate evidence), and the catalog's **first citable formal framework**. I want you to know what we extracted, how it sits relative to your argument, and one specific interpretive claim we carry with explicit confidence-flagging.

**The problem the project addresses.** AI systems today are built almost entirely on one biological template: a simplified caricature of cortical neurons in mammals, scaled up on text. Two structural problems follow. First — as Yann LeCun has argued — these systems learn patterns in language but do not learn _how the world works_, so they fail at tasks requiring real-world planning. Second, the biological inspiration has been only one species deep. The diversity of cognitive design across the tree of life — birds, bacteria, cephalopods, slime molds, and the half-billion-year-old vertebrate substrate your paper anchors — is treated as curiosity rather than design library. The project's bet is that the most consequential next-generation architectures need an engineering-facing translation from comparative cognition and neuroscience to reach the people who build AI systems.

**The catalog: NEXI.** Each entry pairs a **natural exemplar** with an **architectural primitive** and a **drop-in skill specification**. Every entry includes a **falsifiable hypothesis**. Patterns aggregate into **collections** — coherent intelligence models whose member patterns reinforce each other.

**What I extracted from your work.** Your 2022 conceptual analysis surfaces four architectural primitives. Together they form one collection — _Embodied Action Selection_ — describing the same architectural function under different domain transformations. This _isomorphism_ shape is the catalog's fourth collection shape, distinct from the constellation, pipeline, and composition shapes the prior three sources had produced.

- **Action Selection as Common Substrate.** Drawn from your argument that the CBGTC loop performs the same role in lamprey brains as in modern human brains — virtually unchanged across all living vertebrate species over half a billion years. This is the catalog's **second canonical pattern** (alongside `niche-specification`). Its promotion was justified by **cross-substrate triangulation**: the same architectural function (default-inhibit / selective-disinhibit gating, goal-directed sequence construction, contextual reinforcement) is documented in vertebrate-CBGTC loops (your work), bacterial molecular regulatory networks (Nesin & Chandrankunnel 2025), and cnidarian nerve nets via Turner et al. 2026's phylogenetic placement of jellyfish and sea anemones. Three substrates; one architectural pattern; conservation across the deepest divergences in animal evolution. The engineering translation: AI architectures should treat action selection as a first-class architectural commitment — inspectable, lesionable, shareable across domains — rather than as an emergent property of an opaque substrate.

- **Ecological Context Model (formalism layer).** Drawn directly from §4: the symbolic framework with three numbered equations (`C = {A(g), E}`; `B(C) = f(Br, Ba(g, P))`; `g+(C) = f(B, E)`) generalising Lewin's 1936 field-theory equation, plus the §5 state-merger commitment that agent-internal features are part of the environment `E`. This is the **catalog's first named formal framework**: prior sources contributed observations the project synthesised after the fact; your paper contributes equations the catalog can adopt directly. The engineering translation: AI systems committing to the formalism gain decision-provenance auditability and transfer-failure attribution that distinguishes perception failure from environment-unobservability failure.

- **Exaptation Architectural Reuse.** Drawn from your master claim (§7): the same machinery vertebrates use for sequential goal-directed motor control was redeployed in human evolution to regulate cognitive control. The internal-external search homology you cite (Hills et al. 2008, 2015a, 2015b; Todd & Hills 2020; Todd & Miller 2018) extends the case to a second exaptive instance. The engineering translation: AI architectures should treat **architectural reuse via exaptation** as a first-class deployment-time design pressure — one well-developed mechanism redeployed across domains via thin per-domain adapters, with cross-domain transfer of improvements as the architectural payoff. The perceptron lineage has overwhelmingly favoured the opposite (specialisation per task).

- **Heuristics as Habits Fusion.** Drawn from your formal equivalence in §6 and §7, including the recognition-heuristic worked example (Tokyo / Yokohama / Nagasaki, citing Goldstein & Gigerenzer 2002). The engineering translation: AI architectures that currently implement Type 1 / Type 2 reasoning as separate modules can unify them under a single context-overlap-driven selection mechanism drawing from a shared repertoire spanning motor and cognitive operations — heuristic failures and motor-habit failures gain the same diagnostic structure, and remedies transfer across domains.

**What we deliberately flag for confidence-grading.** Your heuristics-as-habits formal equivalence is the catalog's most consequential interpretive move from this source — and we have graded it `core × medium` rather than `core × high` to flag this transparently. _Core_ because it load-bears the exaptation-of-CBGTC-for-cognition argument. _Medium_ because the equivalence is interpretive synthesis rather than fresh empirical demonstration — a careful reader could accept every neuroscience point and still reject the formal mapping between recognition-heuristic errors and motor-habit errors. The grading is an _audit hook_ rather than a critique: a corroborating source (e.g. CBGTC fMRI activation during structurally-induced heuristic errors) would justify a re-grade to `high`. We mention this transparently because honest grading is itself a methodological commitment, and we did not want quiet confidence-marking on what is, in our reading, the paper's sharpest interpretive contribution. The single-goal simplification you note in footnote 6 is logged as an open extension point in the collection's complementarity notes.

**An invitation.** I would value any feedback you are willing to offer: disagreements with my reading, stronger formulations of the falsifiable claims, additional caveats, primary sources I should cite alongside your synthesis, or pointers from the broader Hills / Todd / Miller research programme that would strengthen the exaptation collection's evidence base. The catalog repository is currently private during initial population; once the threshold for public release is reached, it will live at [github.com/Ds-GerardoCastro/NEXI](https://github.com/Ds-GerardoCastro/NEXI). In the interim I am happy to share the relevant entries directly — please reply to this email.

With genuine appreciation for the structural clarity of your formal model, the depth of the phylogenetic argument, and the architectural ambition of the exaptation thesis — which has given the catalog its first citable formal framework, its second canonical pattern, and a fourth collection shape.

Sincerely,

**Juan Gerardo Castro Sánchez**
Nature Intelligence Project
ds.gerardocastro@gmail.com
[linkedin.com/in/juan-gerardo-castro-sánchez-7b85b21b6](https://www.linkedin.com/in/juan-gerardo-castro-s%C3%A1nchez-7b85b21b6/)
10 May 2026
