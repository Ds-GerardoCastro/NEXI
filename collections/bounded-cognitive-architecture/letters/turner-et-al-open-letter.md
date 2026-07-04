# Open letter to Turner, Russek, Seed, McEwen, Vélez, Morgan & Griffiths

**To:** Dr. Cameron Rouse Turner, Dr. Evan M. Russek, Dr. Amanda Seed, Dr. Emma Suvi McEwen, Dr. Natalia Vélez, Dr. Thomas J. H. Morgan, Dr. Thomas L. Griffiths

**From:** Juan Gerardo Castro Sánchez · Nature Intelligence Project · ds.gerardocastro@gmail.com

**Date:** 3 May 2026

**Re:** Architectural primitives extracted from your 2026 working-memory evolution model — an invitation

---

Dear Dr. Turner, Dr. Russek, and colleagues,

I am writing to introduce the **Nature Intelligence Project**, an independent research initiative I am developing, and to share the specific contribution your 2026 paper _Cognitive capacity and control in the evolution of intelligence_ (bioRxiv preprint, [10.1101/2026.03.07.710317](https://doi.org/10.1101/2026.03.07.710317)) is making to it. The project distils peer-reviewed comparative cognition into engineerable architectural primitives for AI engineers. Three of those primitives — and a collection that composes them — derive directly from your work.

**The problem the project addresses.** Modern AI architectures inherit a narrow biological template: the perceptron lineage, scaled toward what amounts to a single mammalian-cortical idealisation. Yann LeCun's well-known critique — that LLM-based agents lack a world model and therefore cannot plan reliably in physical settings — names the _architectural_ failure. The project I am building names a second, deeper failure: AI's biological inspiration has been one species deep. The diversity of cognitive design across the tree of life is currently treated as a curiosity rather than a design library. The project's working bet is that the most consequential next-generation architectural primitives are sitting in the comparative-cognition and evolutionary-biology literatures, and that they need an engineering-facing catalog to become available to the people building AI systems.

**The catalog: NEXI (Nature Expression of Intelligence).** NEXI is a curated, schema-validated catalog of named patterns drawn from peer-reviewed sources. Each entry pairs a **natural exemplar** (the species and behaviour that motivates the pattern) with an **architectural primitive** (interfaces, data flow, pseudocode) and a **framework-neutral agent-skill specification**, plus a **falsifiable hypothesis** that distinguishes the pattern from a description. Real Citations Only is enforced as a project policy: every cited paper is verified against CrossRef / PubMed / arXiv before publication. Patterns aggregate into **collections** — coherent intelligence models whose member patterns are mutually load-bearing.

**What I have extracted from your work.** Your paper produces, in my reading, three architectural primitives that an AI engineer can act on. Each has been published in NEXI as an entry with a layered card (engineer quick-start above, theoretical grounding below) and a falsifiable hypothesis testable on AI systems:

- **Capacity-First Scaling** (NEXI `capacity-first-scaling`). Drawn from your evolutionary-optimality result that capacity contributes linearly to recall efficacy while control contributes sublinearly with severe diminishing returns. The engineering translation is a scaling discipline: when allocating marginal compute / memory / latency budget, expand capacity components (context window, retrieval store, memory tokens, MoE expert pool) before scaling control components (attention sophistication, agentic-loop depth, reasoning chain length). The falsifiable hypothesis claims a measurable margin (≥10%) at matched cost on memory-intensive evaluations — directly testable against current foundation-model deployment.

- **Cognitive Regime Selection** (NEXI `cognitive-regime-selection`). Drawn from your three-regime taxonomy and from the empirical finding that humans and rhesus macaques both fall in the _control-enhanced_ regime — a result I read as a quiet but consequential null against the information-capacity hypothesis's prediction of capacity-heavy human placement. The engineering translation is a design-space taxonomy: small-budget edge, mid-tier assistant, and flagship deployments are not points on the same scaling curve but structurally distinct architectures, and the deployment niche selects which regime is appropriate.

- **Niche Specification** (NEXI `niche-specification`). Drawn jointly from your "information-processing niches" framing and an independent ethological source on zebra finch fission-fusion social architecture. The pattern argues that specifying the deployment niche along typed axes (task structure, signal environment, resource envelope, error profile, social surround, evaluation protocol) is the most upstream architectural decision — and that generic-benchmark performance is not a substitute for in-niche evaluation. This is the catalog's first multi-source pattern, and the strongest near-term candidate for promotion to a fully canonical entry.

These compose into the collection **Bounded Cognitive Architecture** — a design-time pipeline (`niche-specification → cognitive-regime-selection → capacity-first-scaling`) whose system-level falsifiable hypothesis claims pipeline-designed architectures outperform same-budget single-axis-scaled architectures on niche-specific evaluation by margins larger than the sum of individual-pattern gains.

**Why this matters for AI.** The current pace of AI architecture evolution is dominated by intuitions that under-emphasise the structural constraints your paper formalises: that storage is prerequisite to regulation; that intelligence has discrete attractors rather than a continuous scaling axis; that deployment niche shapes what counts as a good architecture. Each of these is a statement an AI engineer can act on, derived not from intuition but from mathematical evolutionary modelling validated against human and macaque behavioural data. Translating your results into engineering primitives — with the scientific bar visibly preserved through citation traceability — is the project's contribution.

**An invitation.** I would value any feedback you are willing to offer: disagreements with my reading of your results, stronger ways to formulate the falsifiable claims, additional caveats I should respect, references I should cite alongside yours, or pointers to whether you see the regime taxonomy applying differently to AI architectures than to biological ones. The catalog repository is currently private during initial population; once the threshold for public release is reached, it will live at [github.com/Ds-GerardoCastro/NEXI](https://github.com/Ds-GerardoCastro/NEXI). In the interim I am very happy to share the relevant entries directly with any of you who wish to read them — please reply to this email or contact me at the address below.

With genuine appreciation for the clarity and rigour of your model, and hopes the engineering translation does it justice.

Sincerely,

**Juan Gerardo Castro Sánchez**
Nature Intelligence Project
ds.gerardocastro@gmail.com
[linkedin.com/in/juan-gerardo-castro-sánchez-7b85b21b6](https://www.linkedin.com/in/juan-gerardo-castro-s%C3%A1nchez-7b85b21b6/)
3 May 2026
