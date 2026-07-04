# Open letter to the authors of _The need for a new perspective on decision-making in bacteria_

**To:** Dr. Sibin Mathew Nesin, Dr. Mathew Chandrankunnel — co-authors of _The need for a new perspective on decision-making in bacteria_ (Communicative & Integrative Biology, 2025)

**From:** Juan Gerardo Castro Sánchez · Nature Intelligence Project · ds.gerardocastro@gmail.com

**Date:** 9 May 2026

**Re:** Three engineerable patterns extracted from your bacterial decision-making review — and a methodological lesson your paper produced

---

Dear Dr. Nesin and Dr. Chandrankunnel,

I am writing to introduce the **Nature Intelligence Project**, an independent research initiative I am developing, and to explain what your 2025 review _The need for a new perspective on decision-making in bacteria_ (Communicative & Integrative Biology, vol. 18 no. 1, [DOI 10.1080/19420889.2025.2463926](https://doi.org/10.1080/19420889.2025.2463926)) has contributed to it. Your paper is the source of **13 principles**, **one new consolidation theme** in our research vault, and **one new collection of three named patterns** in the catalog that downstream AI engineers can draw on. I want you to know what we extracted, how it sits relative to your argument, and what we deliberately bracketed.

**The problem the project addresses, in plain terms.** AI systems today are built almost entirely on one biological template: a simplified mathematical caricature of cortical neurons in mammals, scaled up and trained on enormous text corpora. Two structural problems follow. First — as Yann LeCun has argued — these systems learn patterns in language but do not learn _how the world works_; they have no model of physical reality, so they fail at tasks requiring real-world planning. Second, and what motivates the project specifically, the biological inspiration has been only **one species deep**. The diversity of cognitive design across the tree of life — birds, cephalopods, plants, slime molds, and crucially bacteria — is treated by AI research as a curiosity rather than a design library. The project's working bet is that the most consequential next-generation architectures are sitting in the comparative-cognition and cell-biology literatures and need an engineering-facing translation to reach the people who build AI systems.

**The catalog: NEXI.** Each entry pairs a **natural exemplar** (the species and behaviour that motivates the pattern) with an **architectural primitive** (how an AI system would implement it) and a **drop-in skill specification** (how an AI agent would actually use it during a task). Every entry includes a **falsifiable hypothesis** — a specific, testable prediction. Patterns aggregate into **collections** — coherent intelligence models whose member patterns reinforce each other.

**What I extracted from your work, in plain language.** Your 2025 review surfaces three architectural primitives that an AI engineer can act on immediately. Together they form one collection — _Acerebrate Decision-Making_ — grouping patterns that produce flexible decision-making _without any centralised processing unit_. Each primitive has been published as a NEXI entry with a falsifiable engineering hypothesis testable on AI systems.

- **Coincidence-Detection Gating.** Drawn from your account of _Vibrio cholerae_ biofilm commitment, where **both** LuxPQ-AI-2 and CqsS-CAI-1 must be activated for the bacterium to switch into colony behaviour. Your paper itself uses the explicit phrase "coincidence detection." The engineering translation: AI assistants committing to costly or irreversible actions (an external API call with side effects, an automated transaction, an irreversible content edit) should require independent confirmation from _qualitatively different_ evidence channels before committing. A single signal is not enough. This is not how most AI assistants behave today.

- **Stochastic-Memory Coupling.** Drawn from your synthesis of bacterial behaviour under environmental unpredictability, where stochastic state-switching is paired with persistent cellular memory (with iron-based signal transduction as one substrate). Your paper makes the load-bearing claim explicit: _"the stochastic switching of gene expression requires cellular memory as a crucial component. Cellular memory produces more accurate and beneficial decision-making."_ Neither random switching alone nor memory alone is sufficient. The pairing is the design pattern. The engineering translation: AI agents handling unpredictable environments should _both_ explore randomly _and_ maintain a persistent record of which explorations paid off — and the memory should bias the next random transition. Current AI systems treat random exploration and memory as separate engineering features; your paper argues they must be coupled at the architectural level. This is the catalog's single biggest architectural-vocabulary gap to fill.

- **Meta-Regulation.** Drawn from your description of anti-σ proteins regulating σ factors which regulate RNA polymerase which regulates genes — a three-level hierarchy with explicit _control over the control_. The engineering translation: AI systems should carry an explicit runtime _regulator-of-the-regulator_ layer — components whose job is to watch how the system's controller is behaving and adjust it on the fly. The closest analog in AI today is "meta-learning," but meta-learning is a training-time technique that's frozen once a model is deployed; your bacterial example argues meta-regulation should be a _runtime_ architectural commitment.

**What we deliberately bracketed.** Your paper makes a substantive philosophical argument for the _Cellular Basis of Consciousness_ (CBC) framework. The project has chosen to bracket the consciousness question — to carry your empirical and architectural claims forward without endorsing or rejecting CBC, since the engineering translation does not depend on whether bacteria are conscious. We describe each principle in architectural terms (decision-making, memory, regulation) rather than in consciousness terms (sentience, awareness, valenced experience). We mention this transparently because outreach materials drawing on your work will not appear to endorse CBC; we did not want that to read as dismissal of the philosophical argument, which we read carefully and respectfully. The architectural evidence carries on its own.

**An invitation.** I would value any feedback you are willing to offer: disagreements with my reading of your results, stronger ways to formulate the falsifiable claims, additional caveats I should respect, primary sources I should cite alongside your synthesis, or pointers to the boundary between substrate-flexible architectural patterns and the consciousness framing. The catalog repository is currently private during initial population; once the threshold for public release is reached, it will live at [github.com/Ds-GerardoCastro/NEXI](https://github.com/Ds-GerardoCastro/NEXI). In the interim I am happy to share the relevant entries directly with either of you — please reply to this email or contact me at the address below.

With genuine appreciation for the rigour of your synthesis, the breadth of primary literature you draw together, and the boldness of your argument that decision-making mechanisms can be observed in organisms without nervous systems.

Sincerely,

**Juan Gerardo Castro Sánchez**
Nature Intelligence Project
ds.gerardocastro@gmail.com
[linkedin.com/in/juan-gerardo-castro-sánchez-7b85b21b6](https://www.linkedin.com/in/juan-gerardo-castro-s%C3%A1nchez-7b85b21b6/)
9 May 2026
