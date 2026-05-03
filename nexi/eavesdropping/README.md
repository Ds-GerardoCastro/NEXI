# Eavesdropping

> **NEXI status:** template · **Formats available:** architecture, skill · **Audience:** builder
>
> _A multi-agent design pattern in which agents extract information from observed third-party interactions, not just from messages addressed to them._

---

## At a glance

In a typical multi-agent system, each agent receives only messages addressed to it. The **eavesdropping pattern** changes that: agents also process _messages they observe between other agents_ under a defined visibility policy. Used well, this lets an agent build a model of others (their goals, knowledge, relationships) without paying the cost of direct interaction with each one.

It is one of the cheapest, most general primitives nature uses for social cognition — and it is **not** the default in current AI agent designs.

| Question          | Short answer                                                                                           |
| ----------------- | ------------------------------------------------------------------------------------------------------ |
| **Use this when** | Multiple agents share an environment, observability is partial, and inferring others' state is useful. |
| **Skip it when**  | Single-agent, privacy-sensitive, compute-constrained, or direct experience already suffices.           |
| **What it adds**  | A richer model of peers, built from observation rather than from explicit interaction.                 |
| **What it costs** | Larger input streams; attention compute scales with observable population.                             |

---

## The natural exemplar

In wild zebra finch colonies (_Taeniopygia castanotis_) in the Australian arid zone, individuals do not just sing to or listen for direct partners — they **eavesdrop** on the songs and exchanges around them. From observed third-party interactions, a finch can infer:

- Who is paired with whom
- Where breeding is active
- Where information-rich social hotspots are forming
- Who is healthy and well-conditioned enough to sing

This information shapes mate choice, territory decisions, and breeding synchronisation — _without the eavesdropper having any direct interaction with the observed individuals._ See [`references.md`](references.md) for the full literature.

The architectural insight: **information about an agent is partly accessible from observing that agent's interactions with others, not just from interacting with it directly.** Eavesdropping is how nature makes social-state inference cheap.

---

## The pattern

**Standard multi-agent design:**

```
[Agent A] ←──── direct ────→ [Agent B]      [Agent C]
                                           (Agent C is unaware
                                            of A↔B exchange)
```

**With eavesdropping enabled:**

```
[Agent A] ←──── direct ────→ [Agent B]
       ↑                           ↑
       └─── observed by ─── [Agent C]
                              │
                              ↓
                    Agent C updates internal
                    beliefs about A and B
```

Agent C receives no message addressed to it, but updates its model of both A and B based on the exchange it witnessed.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — components, interfaces, and pseudocode for both LLM-agent and reinforcement-learning flavours.

In summary, three components:

- **Observation bus.** Every agent subscribes to a stream that includes messages it sent, received, _and observed_.
- **Visibility policy.** A function that determines which agents can observe which messages (broadcast, proximity-based, role-based, stochastic).
- **Belief updater.** A function that, given an observed third-party message, updates the agent's internal model of the participants.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for an LLM-based agent:

- **System-prompt fragment** that instructs the agent to attend to observed third-party interactions as evidence about the participants.
- **Tool / function** `get_observed_interactions(time_window, participants_filter)` that exposes the eavesdropping stream.
- **Memory pattern** in which observed interactions persist with a discriminator field, separate from direct messages.

The skill spec includes translation notes for Claude skills, OpenAI function calling, MCP, and LangChain / LlamaIndex.

---

## When to use it

- ✅ Multi-agent settings with shared, partially observable environment.
- ✅ Tasks that benefit from inferring others' goals, knowledge, or relationships (cooperative coordination, opponent modelling, social inference).
- ✅ Direct interaction is costly, infrequent, or noisy.
- ✅ Population size is moderate — small enough that observation is tractable, large enough that eavesdropping adds signal beyond direct interaction.

## When not to use it

- ❌ Single-agent settings — there is nothing to eavesdrop on.
- ❌ Privacy-preserving or adversarial settings — observed agents may signal deceptively, or eavesdroppers may exfiltrate sensitive context.
- ❌ Strict compute constraints — eavesdropping multiplies the input stream by approximately the number of observable agents; attention-based architectures pay extra.
- ❌ Tasks where direct experience suffices and inferring others adds no useful signal.

---

## Tradeoffs

- **Information richness vs. compute cost.** Eavesdropping multiplies the observation stream by approximately the number of observable agents. Architectures with quadratic attention pay extra unless mitigated by sparse attention or message summarisation.
- **Privacy and robustness.** Third-party observability creates attack surface (deceptive signalling, inference attacks). Eavesdroppers may also exfiltrate sensitive context.
- **Memory pressure.** Observed-interaction history can grow unbounded; long-running deployments need summarisation or compression.

---

## Theoretical background & evidence

The pattern is described in animal-communication ecology under the term _communication networks_ — networks of potential information flow among individuals, in which signalling interactions are observable to non-target receivers. The foundational reference is **McGregor & Dabelsteen (1996)**. Recent work in wild zebra finches documents the role of eavesdropping in social hotspots and breeding-colony coordination (**Hagedoorn et al., bioRxiv preprint 2026-04-27**).

In computational AI literature, eavesdropping has analogs in:

- **Graph attention networks (GATs)** (Veličković et al., 2018) — agents attend over edges in which they don't directly participate.
- **Decentralised POMDPs with shared observability** (Oliehoek & Amato, 2016) — agents update local beliefs from joint observation streams.
- **Multi-agent reinforcement learning with broadcast observability** — opponent and teammate modelling from observed transitions.

NEXI's contribution is to package this as a **named, deliberate design choice** for AI engineers — not as an emergent property of attention architectures. Most LLM-agent stacks today restrict each agent to its own message history; eavesdropping has to be _enabled_ by an architectural decision.

Full citation list: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H₁ (Eavesdropping).** Multi-agent reinforcement-learning systems with attention over observed third-party interactions achieve higher sample efficiency on partially-observable cooperative tasks than identical systems restricted to self-directed observation.
>
> **Operationalisation.** At equal training compute on a benchmark of N ≥ 3-agent partially-observable cooperative tasks (e.g. Overcooked-AI multi-agent variants, Hanabi, or comparable social-inference benchmarks), eavesdropping-enabled agents reach a target performance threshold in fewer training episodes by a measurable margin (≥10% reduction in episode count to threshold).
>
> **Refutation.** If, across an appropriate benchmark suite, eavesdropping-enabled agents do _not_ outperform self-directed-only agents at equal training compute by the specified margin, this NEXI is refuted as an architectural primitive (though the natural-system phenomenon obviously remains).

---

## Boundary conditions

This NEXI specifies **observation-based belief update**, not action policy. Building agents that _do something_ with what they overhear (e.g. intervene, alert, act on inferred goals) is a separate design problem downstream of this one. First the agent must be able to overhear; then it can decide how to use what it heard.

---

## Related

- **Vault provenance (private):** consolidation hub `Eavesdropping`; principle `P02 — Eavesdropping as Network Mechanism`; metamodel `MM1 — Distributed Information Substrate`.
- **Related NEXIs:** _(none yet — will populate as catalog grows)_
- **References:** [`references.md`](references.md)
