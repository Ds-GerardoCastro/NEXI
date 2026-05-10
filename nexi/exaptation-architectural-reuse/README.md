# Exaptation Architectural Reuse

> **NEXI status:** draft · **Formats:** architecture, skill · **Audience:** builder
>
> **Cluster:** [`embodied-action-selection`](../../clusters/embodied-action-selection/)
>
> A design-time architectural commitment to **reuse a single well-developed mechanism across multiple domains via explicit exaptation**, rather than building duplicate domain-specific modules. The pattern argues that architectural reuse is a first-class deployment-time design pressure, observable in nature wherever a mechanism originally evolved for one purpose gets redeployed to serve another.

---

## At a glance

The default mental model in modern AI is that capability surfaces grow by adding modules: a new domain gets a new model, a new task gets a new fine-tune, a new modality gets a new encoder. The empirical record from comparative neuroscience contradicts this default: nature repeatedly takes a single well-developed mechanism and _redeploys it_ into a new domain without building new machinery.

The strongest documented case: the cortico-basal ganglia-thalamo-cortical (CBGTC) loop in vertebrates. Originally evolved for sequential goal-directed motor control (~560 million years ago), the same circuit was redeployed in human evolution to regulate cognitive control — sequences of cognitive operations in pursuit of cognitive goals. Heuristic decision-making, working-memory operations, and abstract reasoning all run on the same machinery that handles motor sequencing in any vertebrate. The redeployment is **exaptation** — a structure originally adapted for one function is co-opted for another without rebuild.

A second documented case: the internal/external search homology (Hills, Todd, Miller research programme). Physical search through external space is phylogenetically ancient and ubiquitous in the animal kingdom. Cognitive search through internal information space is plausibly unique to humans and arose much later — via exaptation of the physical-search machinery. The architectural translation: AI systems that redeploy one search component for both information retrieval and action-space planning, without architectural duplication, are implementing this primitive.

The architectural translation: AI systems should treat exaptation — runtime redeployment of one mechanism across multiple domains — as a first-class design pressure. One well-tuned mechanism handles N domains; improvements in one domain transfer to all. Marginal cost per new domain drops sharply.

---

## The natural exemplar

[Nordli & Todd (2022)](https://doi.org/10.3389/fpsyg.2022.841972) — peer-reviewed conceptual-analysis article, _Frontiers in Psychology_ — argues for exaptation as the central architectural design lesson of vertebrate cognitive evolution. The master claim (§7): _"the evolutionarily conserved circuitry that underlies vertebrate motor control has been coopted to facilitate the use of cognitive control to pursue and achieve cognitive goals analogously to how motor goals are pursued and achieved via motor control."_

The internal/external search corollary: _"search behaviour in both physical and cognitive domains likely relies on a shared set of underlying neural mechanisms,"_ with cognitive search arising via exaptation of the older physical-search machinery (Hills et al. 2008, 2015a, 2015b; Todd & Hills, 2020; Todd & Miller, 2018). Cognitive search is "newer hardware on older substrate."

The methodological corollary the source raises: physical search is observable from outside (animal foraging trajectories); cognitive search is "obscured by our skulls." If physical search is the evolutionary substrate of cognitive search, then studying physical search in non-human species — observable, ubiquitous, easier to instrument — _is_ studying the architectural pattern that underlies human cognitive search.

See [`references.md`](references.md) for full citation chain and computational analogs.

---

## The pattern

**Default duplicate-module specialisation:**

```
   Domain A ──► Module A (specialised)
   Domain B ──► Module B (specialised)
   Domain C ──► Module C (specialised)
   ...
   Domain N ──► Module N (specialised)

   Cost per new domain: O(N)
   Cross-domain transfer of improvements: low
```

**Exaptation architectural reuse:**

```
   Domain A ─┐
   Domain B ─┤
   Domain C ─┼─► Single well-developed mechanism M
   ...       │   (originally built for one domain;
   Domain N ─┘    redeployed across all via thin domain adapters)

   Cost per new domain: O(adapter), << O(M)
   Cross-domain transfer of improvements: high (improvement to M lifts all)
```

The non-trivial design choice is **which mechanism is "well-developed enough" to redeploy**. A poorly-tuned mechanism redeployed across N domains performs worse than N specialised modules; a well-tuned mechanism redeployed across N domains performs comparably or better with vastly lower marginal cost. The exaptation pressure pays only when the source mechanism is mature.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — components, interfaces, data flow, and integration with the rest of the cluster.

In summary, three components:

1. **The redeployable core mechanism `M`.** A well-developed module designed in one domain (e.g. action selection, search, attention) — typed to be domain-agnostic at its interface even though originally tuned for a specific domain.
2. **Per-domain adapters `Aᵢ`.** Thin wrappers that translate domain-specific input into the core mechanism's typed interface and translate the core's output back into domain-specific actions. Adapters are cheap; the core is expensive.
3. **Reuse audit / lesion infrastructure.** Tooling that confirms the reuse pattern is genuine — improvements to `M` should transfer across all `Aᵢ`, and lesioning `M` should degrade all domains equally. Without this, "exaptation" can devolve into shallow parameter-sharing.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for an engineering-agent or runtime decision system:

- **System-prompt fragment** that instructs the agent to identify candidate mechanisms for cross-domain redeployment and to surface the reuse pattern explicitly.
- **Tool definitions** for `register_redeployable_mechanism`, `wrap_domain_adapter`, `audit_reuse_pattern`, `lesion_test_redeployed_mechanism`.
- **Translation notes** for stack-specific mappings.

---

## When to use

- Cross-domain agentic systems where the same underlying mechanism could benefit multiple domains if shared.
- Embodied-AI deployments where motor and cognitive control are currently separate but share goal-context-action structure.
- Multi-task systems growing capability surfaces over time — exaptation amortises substrate development across an expanding domain set.
- Research / engineering work explicitly testing whether the same mechanism can serve N domains as opposed to N copies of similar mechanisms.
- Mechanism-interpretability projects where exposing the reuse pattern across domains is itself a deliverable.

## When not to use

- Single-domain deployments where there is no second domain to redeploy to.
- Deployments where candidate mechanisms are domain-specifically optimised in ways that make reuse counterproductive.
- Pre-training / foundation-model substrate construction (the NEXI operates at deployment-time architecture, not at substrate-construction layer).
- Cases where the source mechanism is not yet well-developed — exaptation pressure on an immature mechanism produces worse outcomes than specialised baselines.

## Tradeoffs

- **Specialisation vs. reuse efficiency.** A domain-specific module can be tuned to its domain alone; a redeployed mechanism amortises across N domains but is general-purpose at its core.
- **Adapter complexity.** Per-domain adapters add their own surface area. Naive adapters can leak domain specificity into the core, undermining the reuse claim.
- **Audit infrastructure overhead.** Without lesion-test infrastructure confirming genuine reuse, "exaptation" can devolve into shallow parameter-sharing that doesn't actually transfer improvements across domains.

In return: vastly lower marginal cost per new domain; cross-domain transfer of improvements; mechanism-interpretability that exposes the same machinery in multiple guises; alignment with one of nature's most robust architectural design patterns.

## Falsifiable hypothesis

> At matched compute and identical task budgets, AI architectures that redeploy a single well-developed mechanism across multiple domains via explicit exaptation outperform same-budget architectures with duplicate domain-specific modules on cross-domain tasks, with measurably lower marginal cost per new domain added. A second testable claim: improvements made to the redeployed mechanism in one domain should transfer at measurably higher rates to other redeployment domains than improvements made to one of N duplicate modules transfer to its siblings. Refutation: if exaptation-architecture systems perform indistinguishably from duplicate-module architectures on cross-domain benchmarks at matched compute and matched added-domain marginal cost, the architectural-reuse claim is empirically weak.

The internal-external search analog (Hills/Todd/Miller programme) provides the strongest existing evidence pattern; AI replications — e.g. demonstrating that one search mechanism redeployed across information retrieval and action-space planning outperforms separate search modules at matched compute — would corroborate.

A third testable claim: **lesion experiment robustness.** Lesioning the redeployed core mechanism `M` should degrade all `Aᵢ` domains comparably; lesioning a single adapter should degrade only its own domain. If lesioning `M` only degrades one domain, the reuse pattern is shallow (the core is effectively domain-specific despite the adapter framing).

## References

See [`references.md`](references.md) — Nordli & Todd (2022) as primary source, plus the Hills/Todd/Miller research programme on internal-external search homology, and computational analogs in multi-task learning, transfer learning, and shared-encoder architectures.
