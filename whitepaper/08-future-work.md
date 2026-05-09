# 8. Future Work

The catalog is at version 1 of an extended research program. This section outlines five tracks of future work: catalog growth, empirical-validation tracks per cluster, the community contribution model, the connection to the longer-term doctoral research program, and the open research questions surfaced by the case studies.

## 8.1 Catalog growth roadmap

Near-term ingestion priorities follow the source-selection bias of §4.2: peer-reviewed work on intelligence in non-mammalian, non-primate species. The Watch List (§4.8) currently carries nine active candidates across three pre-promotion tiers — single-source, multi-source-but-not-yet-hub, and hub-but-not-yet-promoted. Specific lineages prioritised for next ingestion include cephalopods (extending [Hochner 2012]), eusocial insects [Seeley 2010], corvids, electric fish, slime molds (extending [Nakagaki et al. 2000]), and additional plant-signalling literature beyond the model species already represented [Trewavas 2014].

The growth pattern is two-directional. As additional independent sources support patterns currently in `draft` status, those patterns promote toward `canonical`. As new sources produce atomic principles that converge on architectural claims not yet in the catalog, new patterns and new clusters emerge. Public release of the repository is gated on a critical mass of canonical patterns plus reviewer-defensible breadth across the lineages above; the gate is intentionally slow to keep curation discipline ahead of population pressure.

A specific near-term promotion target is the upstream consolidation hub `Embodiment Without Cortex`, which already clears the multi-source rule (Nesin & Chandrankunnel 2025 + Turner et al. 2026 phylogenetic placement). Closing the loop from hub to NEXI requires articulating substrate-independence as a falsifiable architectural primitive in its own right rather than only as a property of the Acerebrate Decision-Making cluster's members.

## 8.2 Empirical-validation track

The validation level (§4.6) is _literature + falsifiable hypothesis_, deliberately lower than full empirical validation per pattern. The empirical-validation track maps how individual patterns can be promoted through validation in subsequent work.

The pattern most likely to admit a near-term toy implementation is `niche-specification`: the typed niche object can be implemented in a deployment-design tool, the regime-classification step is computationally cheap, and the capacity-first allocation is testable against existing scaling-curve benchmarks. The constellation-cluster patterns admit toy implementations within multi-agent reinforcement learning environments (Hanabi-family, Overcooked-AI variants) where the falsifiable hypothesis predicts measurable subsetting effects at matched training compute. The composition-cluster patterns are the farthest from a near-term toy implementation, requiring a substrate that supports concurrent meta-regulation; HyperNet-style architectures are the most plausible analog and are an active area of research-frontier work.

When empirical evidence is produced for a NEXI, it is linked back to the entry's `evaluation/` subfolder, and the entry's `status` advances if and only if the evidence supports the falsifiable hypothesis at the threshold the hypothesis specifies. Negative results trigger `deprecated` rather than removal; the catalog tracks failed transfers so they cannot be silently retried.

## 8.3 Community contribution model

The contribution gate documented in `docs/methodology.md` is the same gate applied to the in-house entries: multi-source evidence plus a falsifiable architectural hypothesis stated in operational form. The methodology is intended to be reproducible by other researchers ingesting their own source literature into compatible structures. A short ingestion-protocol guide (the section-by-section reading practice, the atomic-principle template, the project-relevance rubric, the multi-source consolidation rule) accompanies the contribution gate.

The contribution model's load-bearing requirement is that submitters validate their citations through the same toolkit the catalog itself uses (`tools/citation/`, MIT-licensed; §4.9), and submit alongside their entries a BibTeX file referencing the validated entries. This keeps the Real Citations Only discipline intact across contributors; it also produces an organic test of whether the methodology travels — a methodology that only its originators can apply is a methodology with limited reach.

## 8.4 Connection to the longer-term doctoral research program

The white paper and catalog are the foundation for an extended doctoral research program. Three strands of open work define the program's likely shape: (a) the empirical-evaluation venue for cluster-level hypotheses; (b) the relationship between NEXI and existing world-model research programs (V-JEPA-family, predictive-coding, latent-dynamics); (c) whether the niche-bound cognition framing should be developed into a substantive critique of domain-general AGI as a research target.

The relationship of the white paper to the program is intentional: the paper presents the foundation in publishable form while leaving the larger questions explicitly open. This is the structural choice motivating §7.4's surfacing of the AGI-as-target question rather than a commitment to its answer. A doctoral thesis would commit; the white paper does not, by design.

## 8.5 Open research questions surfaced by the case studies

Each cluster surfaces research questions the catalog cannot itself answer.

The Distributed Social Cognition cluster raises the question of how individual identity stability is maintained under network reorganisation — the patterns rely on identity from distinctive signal patterns, but in real social networks the signals themselves drift. The corresponding open research question is the dynamics of identity-pattern persistence across structural network change, and what minimum amount of pattern stability is required for the cluster's synergy claim to hold.

The Bounded Cognitive Architecture cluster raises the tension between domain-general capacity (Turner et al.'s P22) and niche-bound specialisation (the zebra-finch and broader comparative-cognition evidence). The synthesis recorded in `niche-specification` — that domain-general substrate is real but specialisation emerges via canalisation under niche pressure — is one resolution, but the tension as a research programme remains open: under what conditions does each side of the synthesis dominate, and how should an AI engineer detect which side their deployment falls on?

The Acerebrate Decision-Making cluster raises the deeper substrate-independence question. If adaptive collective behaviour is recoverable from a small set of substrate-independent components, what is the minimal component set, and is the bacterial particular set the optimal one or just an evolutionarily-converged-upon one? The answer matters for AI architecture: a minimal substrate-independent set is the most engineerable; the bacterial set may be sub-optimal but historically converged. This is precisely the place where evolutionary-design and engineering-design questions diverge in a way the catalog can frame but not yet answer.

These questions are productive starting points for independent research. The catalog provides the named patterns and the falsifiable hypotheses; the questions are what comes after.
