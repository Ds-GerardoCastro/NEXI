# Niche Specification

> **NEXI status:** canonical · **Formats available:** architecture, skill · **Audience:** builder · **Promoted:** 2026-05-09
>
> **Collection:** [`bounded-cognitive-architecture`](../../clusters/bounded-cognitive-architecture/)
>
> The most upstream design-time pattern in the collection: **before any architecture decision, specify the niche**. The niche is a typed bundle of deployment parameters — task structure, signal environment, resource envelope, error profile, social surround, evaluation protocol — that downstream patterns consume as input. There is no architecture without a niche.
>
> **First `canonical` NEXI in the catalog.** Multi-source evidence: 7 supporting principles spanning two independent sources (Hagedoorn et al. 2026 zebra finch + Turner et al. 2026 mathematical model). Schema has been stable across three subsequent ingestions (Turner collection, methodology refinement, bacteria collection). Falsifiable hypothesis is sharply stated and operationally testable. The promotion meets all three `canonical`-status criteria per `docs/methodology.md`.

---

## At a glance

"Build a general-purpose AI assistant" is not a niche. "Help users with their questions" is not a niche. "Achieve human-level performance" is not a niche. These are absences of niche specification — the architecture decisions that follow are unanchored, the evaluation that follows is generic, and the result is benchmark-tuned rather than deployment-fit.

The niche-specification pattern forces the upstream step: produce a typed niche object before architecture, regime, or scaling decisions are made. The typed object covers six axes:

1. **Task structure** — primary task family, complexity in bits if estimable, hierarchical structure, multi-modal requirements.
2. **Signal environment** — cue reliability, distribution stability, adversariality.
3. **Resource envelope** — cost per response, latency budget, memory budget, energetic-constraint tier (edge / mid / server / datacenter).
4. **Error profile** — correctness premium, failure-mode tolerance.
5. **Social surround** — multi-agent presence, other-agent observability, human-in-loop.
6. **Evaluation protocol** — in-niche benchmark, out-of-niche behaviour declaration.

The pattern is also the project's strongest critique of AGI as currently framed. If cognition is irreducibly niche-bound, "general intelligence abstracted from environment" is structurally incoherent. The right targets are **families of niche-specific intelligences** with explicit specifications, plus router-of-niche-specialists architectures when heterogeneity is genuine.

---

## The natural exemplar

Two independent biological sources converge on niche-conditional cognitive design:

1. **Turner et al. (2026)** — formal mathematical model with explicit "information-processing niches" framing. Niche conditions (task complexity, cue reliability, metabolic-energy availability) translate into the metabolic-cost-to-recall-benefit ratio that places a species in a regime. Specialisation emerges via canalisation of an initially domain-general substrate under niche pressure.

2. **Hagedoorn et al. (2026, _Communication Networks of Wild Zebra Finches_)** — wild ethological documentation. Fission-fusion social architecture as a niche-conditional response to arid-zone non-stationarity. Same signal type (song) takes different functions in different contexts (breeding-colony vs. social-hotspot vs. dawn). Cognition is shaped by the ecological niche, not abstracted from it.

The convergence between an evolutionary-modelling paper and an ethological field study on the same architectural claim is non-trivial. They approach niche-binding from opposite methodological poles and arrive at compatible structural commitments.

This makes Niche Specification the catalog's **first multi-source pattern**. It draws evidence from 7 vault principles spanning two source publications and is a candidate for early `canonical` promotion once the collection's schema settles.

See [`references.md`](references.md) for the full citation chain.

---

## The pattern

**Standard architecture-design conversation:**

```
"Let's build [system X]."
        │
        ▼
"Pick an architecture / model / framework."
        │
        ▼
Architecture commitments made on
implicit niche assumptions
        │
        ▼
Generic-benchmark evaluation
        │
        ▼
Surprise distribution shift on real deployment
```

**Niche-specified design:**

```
"Let's build [system X]."
        │
        ▼
Niche specification (forced upstream step)
   ┌─ task_structure
   ├─ signal_environment
   ├─ resource_envelope
   ├─ error_profile
   ├─ social_surround
   └─ evaluation_protocol
        │
        ▼
Typed, versioned niche object (persisted artefact)
        │
        ├──► consumed by cognitive-regime-selection
        ├──► consumed by capacity-first-scaling
        └──► used as evaluation context (NOT a generic benchmark)
        │
        ▼
Out-of-niche behaviour: declared, not discovered
```

The niche is a **persisted, versioned artefact** — like a model card but typed and machine-readable. It governs the architecture's lifecycle: re-specifying the niche triggers re-design, not just re-tuning.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — the typed niche schema, persistence pattern, and downstream consumption interfaces.

In summary, three components:

1. **Niche schema (typed object).** Six axes covering task, signal, resource, error, social, evaluation parameters. Validates against an explicit JSON Schema.
2. **Specification dialogue.** Elicits values for each axis from a deployment description; refuses to synthesise plausible-sounding defaults; flags incomplete specifications.
3. **Persistence and versioning.** Niche objects are stored as versioned artefacts; downstream architectures reference them by version, not by transient values.

The pattern composes upstream of [`cognitive-regime-selection`](../cognitive-regime-selection/) and [`capacity-first-scaling`](../capacity-first-scaling/) — both are blocked until a niche object exists.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for the most upstream design-time skill:

- **System-prompt fragment** that instructs the agent to refuse to synthesise plausible niche values and to push back on vague specifications.
- **Tool definitions** for `elicit_niche_field`, `validate_niche_completeness`, `persist_niche`, `detect_multi_niche_request`.
- **Multi-niche detection** — when a deployment is being asked to serve multiple distinct niches, the skill recommends a router-of-specialists pattern instead of a single-architecture commitment.
- **Translation notes** for Claude skills, OpenAI function calling, MCP tools, LangChain / LlamaIndex.

---

## When to use

- At the very start of any architecture-design conversation, before regime classification or scaling decisions.
- Whenever a deployment context is being specified or revised — e.g. promoting a research prototype to production, expanding an assistant to a new user segment, deploying a model to a new geography.
- When evaluation rigour matters (PhD reviewers, regulatory contexts, safety-critical deployments). Niche-specified evaluation is what makes "this model is good for X" a defensible claim rather than a benchmark-leaderboard one.
- When the implicit answer to "what's this for?" is "general purpose for everyone" — that's exactly the situation the pattern is designed to push back on.

## When not to use

- Foundation-model pretraining. That is substrate construction, not niche-bound design — the canalisation that produces niche specialisation happens at fine-tuning / adaptation / deployment, not pretraining.
- Single-architecture services that genuinely must serve many distinct niches — use the **router-of-niche-specialists** pattern instead, where each specialist is niche-bound and the router classifies incoming requests.
- Research / exploratory architectures deliberately operating without deployment commitments. Specification is reserved for production-bound architectures.
- Compute-budget-constrained settings where the niche-specification overhead is large relative to the architecture-development budget. The pattern is most valuable for non-trivial deployments.

## Tradeoffs

- **Specification cost** — niches are typed, complete, and persisted. That costs upfront effort. The reward is downstream principled-ness.
- **Tension with foundation-model practice** — pretrained models are deployed across many niches without re-specification. The pattern argues this should change at the fine-tuning / adaptation stage; foundation-model pretraining itself is exempt.
- **Tension with the g-factor view** ([Turner et al.'s P22](https://doi.org/10.1101/2026.03.07.710317) supports a single shared information-processing axis correlating with brain size). The reconciliation Turner et al. offer is that domain-general substrate is real, but specialisation emerges via canalisation under niche pressure. This NEXI takes the niche-binding side of that synthesis. See the collection's `complementarity_notes` for the full framing.

## Falsifiable hypothesis

> Niche-specified architectures outperform same-budget general-purpose architectures on niche-specific evaluation, when the niche is genuinely specified along the canonical axes (task structure, signal environment, resource envelope, error profile, social surround) and evaluation is in-niche. Refutation: if niche-specific and general-purpose architectures perform indistinguishably on in-niche evaluation at matched cost, the niche-binding claim is structurally weak.

A second testable claim: **a model that wins on a generic benchmark should not, on average, win on niche-specific benchmarks for niches it was not optimised for**. If generic-benchmark winners transfer at the same rate as niche-specific competitors, niche binding is weaker than the claim asserts.

A third claim about implementability: **out-of-niche graceful-decline behaviour is achievable when the niche is explicit**. Architectures shipped with explicit niche specifications can implement principled out-of-niche behaviour (graceful decline, refusal). If they cannot, niche specifications are descriptive but not actionable.

## References

See [`references.md`](references.md) for the full citation chain — Turner et al. 2026 + Hagedoorn et al. 2026 as primary biological sources, plus computational analogs in No-Free-Lunch theorems (Wolpert & Macready 1997), domain adaptation, ecological-validity literature in cognitive science, and benchmark-design work (BIG-Bench, HELM).
