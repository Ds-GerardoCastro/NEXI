# Open letter to the authors of *Communication networks of wild zebra finches*

**To:** Dr. Marc Naguib (corresponding author), Dr. K. Hagedoorn, Dr. H. Loning, and colleagues — co-authors of *Communication networks of wild zebra finches (Taeniopygia castanotis)*

**From:** Juan Gerardo Castro Sánchez · Nature Intelligence Project · ds.gerardocastro@gmail.com

**Date:** 3 May 2026

**Re:** Five engineerable patterns extracted from your zebra finch study — an invitation

---

Dear Dr. Naguib, Dr. Hagedoorn, Dr. Loning, and colleagues,

I am writing to introduce the **Nature Intelligence Project**, an independent research initiative I am developing, and to explain what your 2026 paper *Communication networks of wild zebra finches (Taeniopygia castanotis)* (bioRxiv, [10.1101/2025.09.11.675577](https://doi.org/10.1101/2025.09.11.675577)) contributes to it. Your study is the source of **five named patterns** in the project's catalog and the basis of one of its two intelligence-model clusters. The translation aims at engineers building artificial intelligence systems, but I want to be sure you can see how I read your work and where the engineering claims sit relative to your findings.

**The problem the project addresses, in plain terms.** AI systems today are built almost entirely on one biological inspiration: a simplified mathematical caricature of cortical neurons in mammals, scaled up and trained on text. Two structural problems follow. First — as Yann LeCun has argued — these systems learn patterns in language but do not learn *how the world works*; they have no model of physical reality, so they fail at planning in real environments. Second, and what motivates this project specifically, the biological inspiration has been only one species deep. The diversity of cognitive design across the tree of life is treated as a curiosity rather than a design library. The project's working bet is that the most consequential next-generation architectures are sitting in the comparative-cognition and behavioural-ecology literatures and need an engineering-facing translation to reach the people who build AI systems.

**The catalog: NEXI (Nature Expression of Intelligence).** Each entry pairs a **natural exemplar** (the species and behaviour that motivates the pattern) with an **architectural primitive** (how an AI system would implement it) and a **drop-in skill specification** (how an AI agent would use it during a task). Every entry includes a **falsifiable hypothesis** — a specific, testable claim. Citations are verified against external bibliographic databases before publication. Patterns aggregate into **clusters** — coherent intelligence models whose member patterns reinforce each other.

**The five patterns I extracted from your work.** Together they form the cluster *Distributed Social Cognition*. Each is summarised below in plain language, with the AI translation written for someone whose expertise is in animal behaviour, not machine learning.

- **Eavesdropping** — Your finding that finches build a model of the social world by listening to interactions among *other* finches, not just by participating directly. *AI translation:* imagine several AI assistants working together on a task — one drafting code, another reviewing it, another running tests. Today, each one only "hears" messages sent directly to it. This pattern says each should also attend to what the others say *to each other*, because those exchanges carry information about each assistant's strengths, recent decisions, and trust relationships. That is structurally what your finches extract from third-party song.

- **Identity by Pattern** — Your demonstration that individual finches can be identified by song motifs, alongside your honest caveat that BirdNET's individual-level reliability is not yet robust. *AI translation:* AI is good at recognising *categories* ("this is a cat") and considerably worse at recognising *particulars* ("this is *my* cat, not the neighbour's"). The wall you describe at the individual-finch level is the same wall AI hits when it tries to reliably track specific people, patients, or accounts in noisy data. Your work points toward AI representations that preserve individual identity, not just category.

- **Multi-Modal Integration** — Your study showed that combining acoustic information (song) with spatial information (where the birds were) revealed structure that neither channel alone showed; sub-colonies and hotspots emerged only in the joint analysis. *AI translation:* most AI systems specialise in one type of input — text, OR images, OR sound. Your work is a clean demonstration that the meaningful pattern often lives in the *combination* of channels observed jointly. This directs AI architects to fuse modalities deeply (treating them as joint observations of one underlying state) rather than running separate pipelines and stitching results together at the end.

- **Context-Bound Semantics** — Your observation that the same song type takes different functional meaning in different contexts: at a breeding sub-colony versus at a social hotspot. *AI translation:* current language models bind meaning largely to *which words appear together in text*. Your finches bind meaning to *which signal occurs in which context* — same song, different function depending on where, when, and with whom. This argues for AI architectures where context (location, time, social surround) is treated as a first-class part of meaning, not as separate metadata applied afterward.

- **Social Hotspots** — Your finding that information flow concentrates at specific spatial locations rather than distributing evenly. *AI translation:* in any system with many interacting agents, information does not flow evenly; it concentrates in specific nodes (shared databases, particular agents that everyone routes through). Most AI architectures treat all interactions as equally important. Your finches show that natural systems do not — they evolve hotspot structure deliberately because that is where signal density is highest.

The five patterns reinforce each other: eavesdropping is meaningless without identity-by-pattern (you cannot attribute what you hear), multi-modal integration needs context (where you hear it matters), hotspots are where eavesdropping pays off. Removing any one weakens the others. This is the integrated picture your paper paints, and it is largely missing in current AI — these capabilities, when present at all, exist as separate features rather than a tightly-coupled system.

**Why this matters for AI.** Modern AI architectures are dominated by one assumption: that intelligence scales with size, more or less smoothly. Your work suggests that what is missing is *not size* but *structural primitives*: extracting information from observed (not direct) interactions, maintaining individual identity, deeply fusing signals, binding meaning to context, and being aware of where information concentrates. Each is something wild finches do routinely and current AI does not.

**An invitation.** I would value any feedback you are willing to offer: disagreements with my reading of your results, stronger ways to formulate the falsifiable claims, additional caveats I should respect, references I should cite alongside yours, or pointers to whether you see the eavesdropping / identity / hotspot framings applying differently to AI than to wild finches. The catalog repository is currently private during initial population; once the threshold for public release is reached, it will live at [github.com/Ds-GerardoCastro/NEXI](https://github.com/Ds-GerardoCastro/NEXI). In the interim I am happy to share the relevant entries directly with any of you who wish to read them — please reply to this email or contact me at the address below.

With genuine appreciation for the rigour and honesty of your study — the BirdNET caveat in particular set the standard I am trying to keep across the catalog — and with hopes the engineering translation does it justice.

Sincerely,

**Juan Gerardo Castro Sánchez**
Nature Intelligence Project
ds.gerardocastro@gmail.com
[linkedin.com/in/juan-gerardo-castro-sánchez-7b85b21b6](https://www.linkedin.com/in/juan-gerardo-castro-s%C3%A1nchez-7b85b21b6/)
3 May 2026
