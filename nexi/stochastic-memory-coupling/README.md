# Stochastic-Memory Coupling

> **NEXI status:** draft · **Formats:** architecture, skill · **Audience:** builder
>
> **Collection:** [`acerebrate-decision-making`](../../collections/acerebrate-decision-making/)
>
> A pattern for **decision-making under environmental unpredictability** via the load-bearing pairing of (a) stochastic state-switching and (b) persistent memory of which states proved beneficial. The catalog's biggest architectural-vocabulary gap to fill: AI design treats stochasticity and memory as separate concerns; bacteria treat them as a single coupled primitive.

---

## At a glance

Current AI design vocabulary treats stochasticity and memory as separable engineering concerns:

- **Stochasticity** = sampling temperature, exploration policies, dropout, noise injection, random seeds. An _inference-time / training-time technique_.
- **Memory** = KV-cache, RAG retrieval store, replay buffers, episodic memory. A _storage technique_.

Bacterial decision-making under environmental unpredictability says: **neither alone produces decision-making.** Stochasticity alone is noise. Memory alone is rigid behaviour. The **coupling** — random transitions selected and retained by accumulated state — is the load-bearing design pattern.

The paper makes this explicit, citing a theoretical model (Landmann et al. 2021, _eLife_): _"phenotypic heterogenicity depends on stochastic switching across different states... The stochastic switching of gene expression requires cellular memory as a crucial component. Cellular memory produces more accurate and beneficial decision-making."_

The architectural translation: AI agents that explore stochastically AND retain persistent state about which explorations paid off — with the memory selecting which transitions to continue — outperform agents with either alone, on tasks involving partial-observability and unpredictability.

---

## The natural exemplar

[Nesin & Chandrankunnel (2025)](https://doi.org/10.1080/19420889.2025.2463926) — peer-reviewed review article — synthesises bacterial decision-making under environmental unpredictability. Section _Bacterial interaction with the environment_ documents the paired primitive:

- **Stochastic state-switching:** σB-factor pulsing in _Bacillus subtilis_ (>150 stress-response genes); flagellar individuality in clonal _E. coli_; phenotypic heterogenicity across genetically identical populations.
- **Persistent cellular memory:** iron-based signal transduction integrating multiple stimuli; ~4-generation swarming memory in _E. coli_; multi-pathway state retention.

The pairing is what produces decision-making. The paper cites Landmann et al. 2021 as the theoretical model. Removing either component breaks the function.

See [`references.md`](references.md) for the full citation chain.

---

## The pattern

**Default uncoupled approach (current AI):**

```
Stochastic exploration ─────► next action
        ▲
        │
        (sampling temperature; no memory of past)

Memory ─────────────────────► retrieval at decision time
        ▲
        │
        (retrieves examples; doesn't shape exploration)
```

**Coupled (stochastic-memory):**

```
       ┌────────────────────────────────┐
       │   Stochastic state-switching    │
       │  (random transitions across     │
       │   discrete behavioural states)  │
       └─────────────┬──────────────────┘
                     │ selects new state
                     ▼
       ┌────────────────────────────────┐
       │      Persistent memory          │
       │  (which states have proven      │
       │   beneficial; iron-style        │
       │   multi-stimulus integration)   │
       └─────────────┬──────────────────┘
                     │ biases next stochastic transition
                     ▼
       ┌────────────────────────────────┐
       │   Behavioural state at time t   │
       │   (action / mode / commitment)  │
       └────────────────────────────────┘
```

The architectural commitment: stochastic transitions and persistent memory are **wired together at the architectural level**, not bolted on as separate features. Memory shapes which transitions persist; transitions populate the memory with novel options.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design.

In summary, three components:

1. **Discrete state space.** The system has explicit qualitatively-different behavioural states (not a continuous parameter space). Stochastic transitions happen between named states.
2. **Stochastic transition policy.** Random switching with controllable temperature/noise, _biased by_ the persistent-memory layer.
3. **Persistent state-memory store.** Records outcomes of past transitions; biases future transitions; integrates multiple stimuli at the decision moment.

The two failure modes the architecture must avoid:

- **Memory domination:** all transitions become deterministic; exploration is eliminated.
- **Stochasticity domination:** memory has insufficient weight; decisions stay random.

The architecture must keep both components active and balance their relative contribution.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for a runtime decision-making agent:

- **System-prompt fragment** that instructs the agent to maintain both stochastic exploration and persistent state-memory, with explicit biasing.
- **Tool definitions** for `record_state_outcome`, `bias_next_transition`, `sample_state_transition`, `decay_memory`.
- **Translation notes** for stack-specific mappings (RL frameworks, agentic frameworks, custom decision systems).

---

## When to use

- Decision-making under genuine environmental unpredictability where the system must balance exploration with exploitation.
- Non-stationary environments where the optimal policy changes across deployment lifetime.
- Multi-step agentic tasks where retaining state across decisions is feasible.
- Heterogeneous task distributions where no single fixed policy will perform well across all sub-tasks.

## When not to use

- Stable / stationary single-task deployments where the optimal policy is knowable in advance.
- Memoryless protocols (strict stateless service interfaces) where persistent memory is structurally unavailable.
- Tasks where stochastic exploration has unbounded cost (irreversible production side effects without rollback). The pattern presupposes that stochastic switching is bounded in cost.

## Tradeoffs

- **Stochastic-exploration overhead** — sampling cost; potentially worse short-term outcomes.
- **Memory-storage overhead** — persistent state; retrieval costs at decision time.
- **Coupling-balance complexity** — must avoid both memory-domination and stochasticity-domination.

In return: robust decision-making under unpredictability; sample-efficient adaptation to new contexts; emergent population-level diversity ([[P36]] clone-individuality) when deployed in multi-instance configurations.

## Falsifiable hypothesis

> At matched compute and equivalent task budgets, AI agents combining stochastic state-transition with persistent state-memory (where memory tracks which transitions proved beneficial and biases future stochastic switching toward those) outperform agents with either component alone on tasks involving partial-observability and environmental unpredictability. On benchmarks varying environmental predictability, the stochastic-memory-coupled architecture should show a measurable advantage (≥15% improvement in average task success or sample efficiency) over pure-stochastic and pure-memory baselines, with the advantage _scaling with the unpredictability of the environment_. Refutation: if either pure-stochastic or pure-memory baselines match the coupled architecture across the predictability spectrum, the pairing claim is refuted.

The scaling-with-unpredictability sub-claim is the load-bearing one — if the coupled architecture only wins when unpredictability is high, the pairing is doing the work it's claimed to do.

## References

See [`references.md`](references.md) — Nesin & Chandrankunnel 2025 as primary source, Landmann et al. 2021 as the theoretical model for the pairing, plus computational analogs in reinforcement learning (replay buffers + exploration policies — but as decoupled techniques), Bayesian non-stationarity-handling, and stochastic-decision-process literature.
