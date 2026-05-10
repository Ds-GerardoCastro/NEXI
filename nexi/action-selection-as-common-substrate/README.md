# Action Selection as Common Substrate

> **NEXI status:** canonical · **Formats:** architecture, skill · **Audience:** builder
>
> **Cluster:** [`embodied-action-selection`](../../clusters/embodied-action-selection/)
>
> A design-time and runtime pattern for **treating action selection as a first-class architectural commitment** — implementing default-inhibit / selective-disinhibit gating, goal-directed sequence construction, and contextual reinforcement as an explicit module rather than as an emergent property of an opaque substrate. Documented across three substrates as different as bacterial molecular regulatory networks, cnidarian nerve nets, and vertebrate CBGTC loops — establishing action selection as a substrate-general invariant.

---

## At a glance

The default mental model in AI is that action selection is something that _emerges_ — from attention scores, from output sampling, from MoE routing, from RL action heads. It is rarely a named, inspectable, lesionable architectural commitment. The empirical record from comparative cognition contradicts this default: action selection is a substrate-general architectural pattern that nature implements _explicitly_ across substrates as different as molecular networks and CBGTC loops.

The vertebrate version: the basal ganglia inhibit most candidate behaviours by default and _selectively release_ the chosen action — selection is a release operation, not a positive activation. This circuit has remained virtually unchanged from lamprey (~560 million years ago) to modern humans. The bacterial version: convergent-divergent molecular pathways perform the equivalent default-inhibit / selective-disinhibit gating without any neural substrate. The cnidarian version: nerve-net sensitisation produces selection without a brain.

The architectural translation: AI systems committing to behavioural sequences should treat action selection as a first-class module — inspectable (which action did you select, and on what evidence?), lesionable (ablate selection pressure to test its load-bearing role), and reusable across domains (when paired with [`exaptation-architectural-reuse`](../exaptation-architectural-reuse/), the same module handles motor and cognitive selection).

---

## The natural exemplars

This is the catalog's second canonical NEXI (alongside [`niche-specification`](../niche-specification/)). Promotion to canonical was justified by **cross-substrate evidence across three independent sources**:

[Nordli & Todd (2022)](https://doi.org/10.3389/fpsyg.2022.841972) — peer-reviewed conceptual-analysis article, _Frontiers in Psychology_ — develops the case that the CBGTC loop is the universal vertebrate action-selection mechanism. The basal ganglia perform the same role in lamprey brains as in modern human brains: inhibiting most behaviour and selectively disinhibiting actions in sequence to achieve specific motor goals. This functional architecture is virtually unchanged across all living vertebrate species — fish, reptiles, birds, mammals — over half a billion years.

[Nesin & Chandrankunnel (2025)](https://doi.org/10.1080/19420889.2025.2463926) — peer-reviewed review article, _Communicative & Integrative Biology_ — documents the same architectural pattern in bacteria. Convergent-divergent molecular pathways implement default-inhibit / selective-disinhibit gating; cell-density-switched behaviour produces sequence construction; operon-regulon-module hierarchy produces contextual reinforcement. All three pattern elements operate without any nervous system.

[Turner et al. (2026)](https://doi.org/10.1101/2026.03.07.710317) — preprint, _bioRxiv_ — places jellyfish and sea anemones in the passive-storage cognitive regime. Cnidarians have nerve nets but no brain; they nonetheless perform documented action selection via sensitisation. The cnidarian nerve-net case completes the cross-substrate triangulation.

Three substrates (molecular regulatory networks / cnidarian nerve nets / vertebrate CBGTC loops); the same architectural pattern; conservation that spans the deepest divergences in animal evolution. See [`references.md`](references.md) for full citation chain and computational analogs.

---

## The pattern

**Default substrate-implicit action selection (current AI):**

```
   Substrate (transformer, RL agent, ...)
      │
      ▼
   Implicit selection (autoregressive decoding,
   attention weights, sampling, action head)
      │
      ▼
   Output / commitment
```

**Action selection as a first-class module:**

```
   Inputs (goal g, context C, perceptions P)
      │
      ▼
   Action-selection module
   ├── Default inhibition: most candidate actions blocked
   ├── Goal-directed gating: candidates compete given g
   ├── Selective disinhibition: chosen action released
   └── Contextual reinforcement: successful sequences reinforced
      │
      ▼
   Output / commitment
```

The non-trivial design choice is **which substrate-implicit selection to _expose_ as an explicit module**. In a transformer-class system, candidate actions might be tool calls or output sequences; the action-selection module sits between the substrate's logits and the side-effect-producing layer. In an RL system, the action head already exists but is rarely treated as a lesionable, inspectable module.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — components, interfaces, data flow, and integration with the rest of the [`embodied-action-selection`](../../clusters/embodied-action-selection/) cluster.

In summary, four components:

1. **Candidate-action enumeration.** A typed list of possible actions, generated from the agent's repertoire `Br` given the current goal `g`. Default state: all candidates inhibited.
2. **Goal-conditioned competition.** Candidates compete based on their predicted contribution to `g+` (goal achievement). Competition uses behavioural associations `Ba(g, P)` learned from prior reinforcement.
3. **Selective disinhibition gate.** The winning candidate is released; others remain inhibited. The gate's logic must specify what counts as "winning" and what happens under tied or absent winners (delegate to [`coincidence-detection-gating`](../coincidence-detection-gating/) for high-stakes commitments).
4. **Contextual reinforcement loop.** Successful selections (those that achieve `g+`) reinforce the goal-context-action association in `Ba(g, P)`, increasing the likelihood of similar selections in similar future contexts.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for an engineering-agent or runtime decision system:

- **System-prompt fragment** that instructs the agent to surface its action-selection step explicitly (which action, given which goal and context, and why this action over alternatives).
- **Tool definitions** for `enumerate_candidate_actions`, `score_candidates_against_goal`, `select_action`, `reinforce_selection_post_outcome`.
- **Translation notes** for stack-specific mappings (Claude tool definitions, OpenAI function calling, MCP tools, LangChain agents, RL frameworks).

---

## When to use

- Agentic systems with long-horizon goal pursuit where opaque substrate-implicit selection is failing in observable ways (premature commitment, untracked decision provenance, inability to ablate the selection step).
- Embodied AI deployments where the same selection mechanism should handle both motor actions and cognitive operations under a shared goal stack.
- Hierarchical control systems where lower-order goals chunk into higher-order behavioural sequences — explicit action selection makes the chunk-boundary visible.
- Tool-using agents where the choice of tool call is high-stakes and decision provenance is important for debugging or audit.
- Research / engineering contexts where mechanism-interpretability of the selection step is a deliverable.

## When not to use

- Pure-perception or pure-classification systems with no commitment among alternatives.
- Deployments where opaque substrate-implicit selection is performing well at low cost and exposing the mechanism would add overhead without payoff.
- Pre-training / foundation-model substrate construction (the NEXI operates at deployment-time architecture, not at substrate-construction layer).
- Single-shot retrieval / single-shot classification tasks with no goal-directed sequence to construct.

## Tradeoffs

- **Module-boundary discipline.** Exposing action selection as a first-class module costs upfront design effort and ongoing boundary maintenance.
- **Inspectability vs. opacity.** Substrate-implicit selection is opaque but cheap; explicit selection is inspectable but adds an addressable layer that must be maintained.
- **Cross-domain reuse opportunity.** When paired with [`exaptation-architectural-reuse`](../exaptation-architectural-reuse/), one selection module handles many domains. Without that pairing, the discipline cost may not pay off.

In return: lesion experiment ability (ablate selection pressure to confirm its load-bearing role), decision-provenance auditing, cross-domain reuse, and explicit support for the [`heuristics-as-habits-fusion`](../heuristics-as-habits-fusion/) NEXI's claim that fast-heuristic and deliberative-habit decisions share substrate.

## Falsifiable hypothesis

> At matched compute and identical task budgets, AI architectures with an explicit action-selection module — implementing default-inhibit / selective-disinhibit gating, goal-directed sequence construction, and contextual reinforcement of successful sequences as an architectural commitment — outperform substrate-implicit architectures on tasks involving long-horizon goal pursuit, chunked-sequence reuse across contexts, and recovery from premature commitment. A second testable claim: explicit action-selection architectures should generalise across motor and cognitive domains (when paired with the exaptation NEXI) at lower marginal cost than duplicate-module architectures. Refutation: if substrate-implicit architectures perform indistinguishably on long-horizon goal-pursuit benchmarks at matched compute, the substrate-general invariant claim is empirically weak and the NEXI's promotion to canonical should be reconsidered.

A third claim worth tracking: **lesion experiment robustness.** Removing the explicit action-selection module from a system that uses it should produce measurable degradation; if removing it leaves performance unchanged, the module was not load-bearing and the system was effectively substrate-implicit.

## References

See [`references.md`](references.md) — three primary natural-system sources (Nordli & Todd 2022; Nesin & Chandrankunnel 2025; Turner et al. 2026) plus computational analogs in current AI (action-conditioned video prediction, RL action heads, MoE routing as implicit selection, autoregressive decoding as implicit selection).
