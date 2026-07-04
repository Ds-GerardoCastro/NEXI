# Embodied Action Selection

> **Cluster status:** draft · **Members:** 4 · **Audience:** builder
>
> A coherent intelligence model for **action selection as a substrate-general invariant, redeployed across motor and cognitive domains via exaptation**. The cluster groups four architectural layers — a formal framework, a cross-substrate invariant, a generative reuse principle, and a specific behavioural-level fusion — that together specify how a single action-selection mechanism produces both motor habits and cognitive heuristics within an embodied, ecologically-situated agent.

---

## Why this cluster exists

Mainstream AI architecture treats action selection implicitly — as something that emerges from attention scores, output sampling, MoE routing, or RL action heads — and treats motor control and cognitive reasoning as separate modules implemented by separate machinery. The empirical record from comparative cognition and vertebrate neuroanatomy contradicts both assumptions:

- The cortico-basal ganglia-thalamo-cortical (CBGTC) loop has remained virtually unchanged across all living vertebrates for ~560 million years (lamprey-to-human conservation), implementing action selection as a first-class architectural commitment with explicit default-inhibit / selective-disinhibit gating.
- The same action-selection function appears across substrates as different as bacterial molecular regulatory networks (no nervous system at all) and cnidarian nerve nets (no brain) — implying the architectural pattern is substrate-flexible.
- In humans, the same vertebrate CBGTC machinery that handles motor control was redeployed in evolution to handle cognitive control — heuristic decision-making is structurally a redeployment of habit formation, not a separate cognitive faculty.

If action selection is a substrate-general architectural invariant, redeployable across domains via exaptation, then the perceptron lineage's implicit-and-modular treatment is a design choice, not a necessity. This cluster catalogues the pattern's formal framework (Ecological Context Model), its cross-substrate occurrence (action-selection-as-common-substrate), its generative reuse principle (exaptation), and its concrete behavioural-level instance (heuristics-as-habits-fusion) in a form AI engineers can adopt directly.

[Nordli & Todd (2022)](https://doi.org/10.3389/fpsyg.2022.841972) is the primary source — a conceptual-analysis article in _Frontiers in Psychology_ that develops the Ecological Context Model and argues for the CBGTC-as-universal-vertebrate-substrate claim. [Nesin & Chandrankunnel (2025)](https://doi.org/10.1080/19420889.2025.2463926) provides the bacterial molecular-network second source, and [Turner et al. (2026)](https://doi.org/10.1101/2026.03.07.710317) provides the cnidarian nerve-net third source. The vault consolidation hubs `Non-Human Intelligence Patterns`, `Niche-Bound Cognition`, and `Context-Dependent Semantics` are the upstream of this cluster.

## Member NEXIs

| Slug                                                                                       | Name                                 | Layer in the architecture                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------ | ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`action-selection-as-common-substrate`](../../nexi/action-selection-as-common-substrate/) | Action Selection as Common Substrate | **Substrate-invariant layer.** Action selection (default-inhibit / selective-disinhibit gating, goal-directed sequence construction, contextual reinforcement) recurs across substrates as different as bacterial molecular networks, cnidarian nerve nets, and vertebrate CBGTC loops. **Status: canonical** — multi-source. |
| [`ecological-context-model`](../../nexi/ecological-context-model/)                         | Ecological Context Model             | **Formalism layer.** Three numbered equations specify context, behaviour, and goal-achievement as relational structures: `C = {A(g), E}`; `B(C) = f(Br, Ba(g, P))`; `g+(C) = f(B, E)`. Citable formal framework underpinning the other three NEXIs.                                                                           |
| [`exaptation-architectural-reuse`](../../nexi/exaptation-architectural-reuse/)             | Exaptation Architectural Reuse       | **Generative-reuse layer.** A single action-selection mechanism, originally evolved for motor control, is redeployed at runtime to operate on cognitive operations (and on internal-space search). Architectural reuse via exaptation as a first-class deployment-time design pressure.                                       |
| [`heuristics-as-habits-fusion`](../../nexi/heuristics-as-habits-fusion/)                   | Heuristics as Habits Fusion          | **Behavioural-instance layer.** Heuristic decision-making (e.g. recognition heuristic, elimination-by-aspects) is formally indistinguishable from motor-habit-style chunked-sequence execution. The same context-overlap-driven mechanism produces both.                                                                      |

## How the patterns compose (isomorphism shape)

```
   ┌─────────────────────────────────────────────────────────┐
   │            ecological-context-model                       │
   │   (the formalism — equations 1–3 specify what context,    │
   │    behaviour, and goal-achievement mean as relations)     │
   └─────────────────────────────┬───────────────────────────┘
                                 │ formalises
                                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │      action-selection-as-common-substrate                 │
   │   (the substrate-general architectural invariant —        │
   │    default-inhibit / selective-disinhibit, goal-directed  │
   │    sequence construction, contextual reinforcement)       │
   └─────────────────────────────┬───────────────────────────┘
                                 │ generated-via reuse
                                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │       exaptation-architectural-reuse                      │
   │   (the generative principle — same mechanism redeployed   │
   │    across domains; motor → cognitive; physical search →   │
   │    information search)                                    │
   └─────────────────────────────┬───────────────────────────┘
                                 │ instantiated as
                                 ▼
   ┌─────────────────────────────────────────────────────────┐
   │        heuristics-as-habits-fusion                        │
   │   (concrete behavioural manifestation — heuristic         │
   │    decisions are habit-style chunked sequences operating  │
   │    on cognitive contexts via the same equations)          │
   └─────────────────────────────────────────────────────────┘
```

The composition is **isomorphism**, not sequenced (pipeline), constellation (mutually-enabling), or layered concurrent (composition). The four NEXIs document the same architectural function under different domain transformations — the cluster's distinctive shape is that "different patterns" turn out to be the same pattern under domain shift.

Removing any one component degrades the others:

- Without the formalism, the substrate-invariant claim loses its citable formal expression and downstream pattern derivations lose grounding.
- Without action-selection-as-common-substrate, the formalism describes a structure with no documented cross-substrate occurrence; exaptation becomes a vertebrate-only claim.
- Without exaptation, the substrate-invariant pattern is a parallel-evolution coincidence rather than a usable design pressure.
- Without heuristics-as-habits-fusion, the cluster has formalism + invariant + reuse but no concrete behavioural-level instance demonstrating predictive content.

## What this cluster claims (system falsifiable hypothesis)

> AI architectures that adopt the full embodied-action-selection cluster (action selection as a first-class substrate-general primitive, formalised via the Ecological Context Model, with explicit exaptive reuse across motor and cognitive domains, and heuristic decisions implemented as a subset of chunked-sequence habits) outperform same-budget architectures that treat action selection as implicit, separate motor and cognitive control into distinct modules, and treat heuristics as a categorically separate fast-path. Refutation: if isomorphism-designed systems perform no better than the best individual-NEXI baseline at matched compute on cross-domain benchmarks (embodied agents mixing motor and cognitive operations, agentic loops with both irreversible-action and decision-heuristic components), the cluster's isomorphism claim is refuted.

This is a stronger claim than "each pattern helps in isolation." The bet is that **architectural reuse is load-bearing** — when the same selection mechanism handles both motor and cognitive domains under a shared formalism, the resulting system extracts efficiency the modular alternatives cannot.

## Comparison with the other clusters

| Cluster                                                                | Shape                                                                  | Layer                     | Direction                                       |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------- | ----------------------------------------------- |
| [`distributed-social-cognition`](../distributed-social-cognition/)     | Constellation (5 mutually-enabling runtime patterns)                   | Multi-agent runtime       | Across agents                                   |
| [`bounded-cognitive-architecture`](../bounded-cognitive-architecture/) | Pipeline (3 sequenced design-time stages)                              | Single-agent design-time  | Through time (sequenced)                        |
| [`acerebrate-decision-making`](../acerebrate-decision-making/)         | Composition (3 layered concurrent runtime mechanisms)                  | Single-agent runtime      | Across layers (concurrent)                      |
| **`embodied-action-selection`** _(this cluster)_                       | **Isomorphism (4 instances of the same machinery under domain shift)** | **Single-agent embodied** | **Across domains (motor / cognitive / search)** |

The catalog now documents **four distinct cluster shapes** — constellation, pipeline, composition, isomorphism — each appropriate for a different problem class. The shape difference is itself architecturally meaningful and reflects the diverse ways nature solves coordination and selection problems.

## When to adopt

- Embodied-AI deployments where a single agent selects across motor actions and cognitive operations under a shared goal-context schema.
- Cross-domain agentic systems where the same underlying selection machinery would benefit motor and cognitive subsystems if shared rather than duplicated.
- Systems where heuristic / habit-style fast decisions and deliberative-style chunked sequences are both needed and currently implemented as separate modules.
- Research / engineering work where a citable formal framework for action-selection (with verbatim equations) is preferable to ad-hoc pattern descriptions.

## When not to adopt

- Pure-perception or pure-classification systems with no commitment to action.
- Deployments where centralised, opaque action-selection (autoregressive decoding) is performing well and exposing the selection mechanism would add cost without payoff.
- Pre-training / foundation-model substrate construction — the cluster operates at deployment-time architecture and design, not at the substrate-construction layer.

## Tradeoffs

The cluster trades architectural-discipline cost (committing to a single action-selection module shared across domains, formalising context as agent-goal-environment-behaviour, treating exaptation as a deployment-time reuse pattern) against modularity and separation-of-concerns. For deployments where motor and cognitive domains are genuinely separable, the discipline is wasted. For embodied-agent deployments where motor and cognitive control share the agent's goal stack and perceptual state, the cluster pays.

## Natural exemplars

| Source                                                                                                                                           | What it contributes                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Nordli & Todd (2022)](https://doi.org/10.3389/fpsyg.2022.841972) — _Embodied and embedded ecological rationality_                               | Primary source. Develops the Ecological Context Model with three numbered equations; argues CBGTC-as-universal-vertebrate-substrate (~560 Mya conservation, lamprey-to-human); develops the heuristics-as-habits formal equivalence and the exaptation thesis. Anchors all four cluster member NEXIs.      |
| [Nesin & Chandrankunnel (2025)](https://doi.org/10.1080/19420889.2025.2463926) — _The need for a new perspective on decision-making in bacteria_ | Second-substrate exemplar. Documents action-selection-like architecture in bacteria — convergent-divergent molecular pathways, cell-density-switched behaviour, modular regulatory hierarchy — establishing action-selection-as-common-substrate as multi-source via the bacterial molecular-network case. |
| [Turner et al. (2026)](https://doi.org/10.1101/2026.03.07.710317) — _Cognitive capacity and control in the evolution of intelligence_            | Third-substrate exemplar. Phylogenetic placement of jellyfish and sea anemones (nerve net, no brain) in the passive-storage regime — completes the cross-substrate triangulation (molecular / nerve-net / vertebrate-CBGTC) that lifts action-selection-as-common-substrate to canonical status.           |

## Related work in current AI

- **Action-conditioned video prediction** (e.g. world-model agents with explicit action-selection heads) — closest current-AI analog of action-selection-as-common-substrate, but typically domain-bound (motor only) and rarely shared with cognitive operations.
- **Chain-of-thought reasoning + tool use as action selection** — partial analog of exaptation: the same autoregressive decoding mechanism is "redeployed" from text generation to tool calling, but the redeployment is not architecturally explicit.
- **Dual-process theories in AI** (System 1 / System 2 architectures) — partial analog of heuristics-as-habits-fusion, but typically frames the two as _separate_ modules rather than as the same mechanism in different operating regimes.
- **Multi-task learning and shared encoders** — partial analog of exaptive architectural reuse, but operates at training-time parameter sharing rather than deployment-time mechanism redeployment.
- **Embodied AI and situated cognition** — the broader research programme that _would_ implement the Ecological Context Model formalism; this cluster is one operationalisation.

## See also

- Cluster cousins: [`distributed-social-cognition`](../distributed-social-cognition/) · [`bounded-cognitive-architecture`](../bounded-cognitive-architecture/) · [`acerebrate-decision-making`](../acerebrate-decision-making/).
- Catalog index: [`../../CATALOG.md`](../../CATALOG.md).
- Methodology: [`../../docs/methodology.md`](../../docs/methodology.md).
- What a NEXI is: [`../../docs/what-is-a-nexi.md`](../../docs/what-is-a-nexi.md).
