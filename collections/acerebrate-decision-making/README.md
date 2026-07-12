# Acerebrate Decision-Making

> **Collection status:** draft · **Members:** 3 · **Audience:** builder
>
> A coherent intelligence model for **decision-making without a centralised processing unit**. The collection groups three architectural layers that together produce flexible, adaptive, context-conditional behaviour using only substrate-flexible control primitives — observed in organisms with no nervous system at all (bacteria), and in organisms with only nerve nets (cnidarians).

> **Adopting this collection.** Its patterns are **independently adoptable** — take one, several, or mix them with patterns from other collections. This page groups them because they were read from the same biological system and reinforce each other; it is a **reading path and provenance record, not a required bundle**. The system-level hypothesis below is a **falsifiable research claim** — that the whole outperforms any proper subset — offered as something to test, not a guarantee to the adopting engineer. If it is refuted, the member patterns remain individually valid.

---

## Why this collection exists

Mainstream AI architecture assumes a centralised controller substrate — neurons (real or simulated) with attention, routing, and decision-gating concentrated in a single computational hierarchy. The empirical record from comparative cognition shows this assumption is contingent: bacteria, with no nervous system, implement decision-making via molecular regulatory networks that produce the same architectural patterns (anticipation, coincidence detection, multi-stream integration, frequency-coded control, meta-regulation) without any centralised controller.

If the architectural patterns are substrate-flexible — implementable in molecular networks, nerve nets, or computational substrates — then the perceptron lineage's centralised-controller assumption is a design choice, not a necessity. This collection catalogues three patterns that bacteria use to make decisions without a brain, in a form AI engineers can adopt directly.

[Nesin & Chandrankunnel (2025)](https://doi.org/10.1080/19420889.2025.2463926) is the primary source. [Turner et al. (2026)](https://doi.org/10.1101/2026.03.07.710317) provides a corroborating phylogenetic placement (jellyfish, sea anemones — nerve net, no brain). The vault consolidation hub `Embodiment Without Cortex` is the upstream of this collection.

## Member NEXIs

| Slug                                                                       | Name                         | Layer in the architecture                                                                                                                                                                                               |
| -------------------------------------------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`coincidence-detection-gating`](../../nexi/coincidence-detection-gating/) | Coincidence-Detection Gating | **Commitment-gate layer.** Major behavioural transitions require multiple independent context streams to align. Prevents premature commitment under noisy or partial single-stream input.                               |
| [`stochastic-memory-coupling`](../../nexi/stochastic-memory-coupling/)     | Stochastic-Memory Coupling   | **Exploration-with-retention layer.** Random state-switching populates the option space; persistent memory tracks which states proved beneficial. The pairing produces decision-making under unpredictability.          |
| [`meta-regulation`](../../nexi/meta-regulation/)                           | Meta-Regulation              | **Control-over-control layer.** Explicit regulators-of-regulators dynamically up- or down-regulate the regulators themselves at runtime. Allows the system to adapt its own control behaviour to changing environments. |

## How the patterns compose

```
   ┌───────────────────────────────────────────────────────┐
   │              meta-regulation                           │
   │   (anti-σ-style runtime regulators of regulators —    │
   │    dynamic up/down-regulation of the control system)   │
   └───────────────────────┬───────────────────────────────┘
                           │ regulates
                           ▼
   ┌───────────────────────────────────────────────────────┐
   │          coincidence-detection-gating                  │
   │   (multi-stream AND-gates on major behavioural         │
   │    transitions — e.g. V. cholerae's BOTH-LuxPQ-AND-    │
   │    CqsS biofilm commitment requirement)                │
   └───────────────────────┬───────────────────────────────┘
                           │ informs commitment
                           ▼
   ┌───────────────────────────────────────────────────────┐
   │        stochastic-memory-coupling                      │
   │   (random state-switching + persistent cellular        │
   │    memory — explores option space while retaining      │
   │    beneficial states)                                  │
   └───────────────────────────────────────────────────────┘
```

The composition is **layered**, not sequenced. All three layers run concurrently within a single agent at runtime. Removing any one degrades the others:

- Without coincidence-gating, stochastic exploration commits prematurely on single-channel evidence.
- Without stochastic-memory coupling, coincidence-gated decisions still operate on a fixed exploration policy.
- Without meta-regulation, the collection's parameters are fixed at deployment rather than adapted to changing conditions.

## What this collection claims (system falsifiable hypothesis)

> AI architectures that adopt the full acerebrate-decision-making collection (multi-stream coincidence-detection gating + stochastic-memory paired exploration + explicit meta-regulation) outperform same-budget single-axis architectures on decision-making tasks under unpredictability and partial observability, by margins larger than the sum of individual-pattern gains. Refutation: if pipeline-designed systems perform no better than the best individual-NEXI baseline at matched compute on appropriately heterogeneous benchmarks (varying environmental predictability, multi-stream context availability, and non-stationarity), the collection's compositional claim is refuted.

This is a stronger claim than "each pattern helps in isolation." The bet is that **layered composition is load-bearing** — the three layers operating concurrently produce decision quality that none of them in isolation can produce.

## Comparison with the other collections

| Collection                                                             | Shape                                                     | Layer                                    | Direction                      |
| ---------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------- | ------------------------------ |
| [`distributed-social-cognition`](../distributed-social-cognition/)     | Constellation (5 mutually-enabling runtime patterns)      | Multi-agent runtime                      | Across agents                  |
| [`bounded-cognitive-architecture`](../bounded-cognitive-architecture/) | Pipeline (3 sequenced design-time stages)                 | Single-agent design-time                 | Through time (sequenced)       |
| **`acerebrate-decision-making`** _(this collection)_                   | **Composition (3 layered concurrent runtime mechanisms)** | **Single-agent runtime decision-making** | **Across layers (concurrent)** |

The catalog now documents **three distinct collection shapes** — constellation, pipeline, and composition — each appropriate for a different problem class; a fourth collection (substrate-independent-cognition) is newly seeded and not yet assigned a shape. The shape difference is itself architecturally meaningful and reflects the diverse ways nature solves coordination problems.

## When to adopt

- Decision-making AI deployments under partial observability, environmental unpredictability, or non-stationarity.
- Multi-agent populations and decentralised systems where centralised-controller assumptions are weak.
- Embedded / edge deployments without central servers; distributed databases that need self-coordination.
- Settings where multi-stream context information is available and the cost of premature commitment is high (irreversible tool calls, agentic loops without rollback).

## When not to adopt

- Single-stream classification or regression tasks with stable input distributions.
- Deployments with reliable centralised controllers and strong observability.
- Tasks where computational cost asymmetry favours simple amplitude-coded representations over the collection's combined overhead.
- Research / exploratory architectures deliberately operating without decision-commitment requirements.

## Tradeoffs

The collection trades architectural-overhead cost (additional regulator components, persistent memory stores, multi-stream input wiring) against decision-quality under unpredictability. For deployments with stable inputs and strong centralised observability, the overhead is wasted. For deployments where unpredictability is the dominant cost driver, the collection pays. Engineers should explicitly assess deployment-niche unpredictability before adopting.

## Natural exemplars

| Source                                                                                                                                           | What it contributes                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Nesin & Chandrankunnel (2025)](https://doi.org/10.1080/19420889.2025.2463926) — _The need for a new perspective on decision-making in bacteria_ | Primary source. _Vibrio cholerae_ biofilm commitment via coincidence detection (LuxPQ + CqsS); stochastic gene-expression switching paired with iron-based cellular memory; anti-σ proteins as meta-regulators of σ factors. All three primitives operate in organisms with no nervous system at all. |
| [Turner et al. (2026)](https://doi.org/10.1101/2026.03.07.710317) — _Cognitive capacity and control in the evolution of intelligence_            | Corroborating phylogenetic placement. Jellyfish and sea anemones (nerve net, no brain) in the _passive-storage_ regime — second source for the substrate-independence claim that motivates this collection.                                                                                           |

## Related work in current AI

- **Multi-stream attention** (multi-head attention, cross-attention, multi-modal fusion) — partial analog of coincidence-detection-gating, but typically not used as an _AND-gate_ on commitment decisions.
- **Reinforcement learning with replay buffers** (DQN, PPO with prioritised experience replay) — partial analog of stochastic-memory-coupling, but treats stochasticity (exploration policy) and memory (replay buffer) as separable engineering concerns rather than as a coupled architectural commitment.
- **Meta-learning / learned optimisers** (Hochreiter et al. 2001; Andrychowicz et al. 2016, _Learning to learn by gradient descent by gradient descent_) — partial analog of meta-regulation, but operating at training time rather than as a runtime architectural layer.
- **Mixture-of-Experts routing** (Switch Transformer, Mixtral) — partial analog of meta-regulation: gates control downstream experts. But MoE gates are flat / one-level; the bacterial pattern is hierarchical.
- **HyperNet-style architectures** — networks generating parameters of other networks. Closer architectural analog of meta-regulation, but research-frontier rather than deployment-default.

## See also

- Collection cousins: [`distributed-social-cognition`](../distributed-social-cognition/) and [`bounded-cognitive-architecture`](../bounded-cognitive-architecture/).
- Catalog index: [`../../CATALOG.md`](../../CATALOG.md).
- Methodology: [`../../docs/methodology.md`](../../docs/methodology.md).
- What a NEXI is: [`../../docs/what-is-a-nexi.md`](../../docs/what-is-a-nexi.md).
