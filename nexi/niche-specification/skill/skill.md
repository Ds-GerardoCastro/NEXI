# Skill: Niche Specification (framework-neutral)

A drop-in **design-time specification** skill for an engineering agent (or human-in-the-loop architecture-design assistant) that elicits a typed niche object from a deployment description and refuses to proceed until the niche is complete. Framework-neutral — see translation notes for stack-specific mappings.

> **Skill kind:** `design-time-specification`. The most upstream skill in the [`bounded-cognitive-architecture`](../../../collections/bounded-cognitive-architecture/) collection. Produces the typed input that downstream design-time skills (regime selection, capacity-first allocation) consume.

---

## System-prompt fragment

Insert this into the system or developer prompt of any agent that should specify a niche before architecture decisions:

```
You are specifying the deployment niche for an AI architecture. A niche
is NOT an aspirational use case — it is the operational context the
system will be optimised for and evaluated in.

Reject vague specifications. "Help users with general questions" is not
a niche. "An AI assistant for everyone" is not a niche. Push back: what
tasks, what users, what cost budget, what signal reliability, what
failure tolerance?

Required axes (refuse to produce a niche object until each is specified
or explicitly marked unknown with a confidence note):

  - task_structure       — primary task family, complexity in bits if
                            estimable, hierarchical structure,
                            multi-modal requirements
  - signal_environment   — cue reliability, distribution stability,
                            adversariality, noise profile
  - resource_envelope    — cost per response, latency budget, memory
                            budget, energetic-constraint tier,
                            inference concurrency
  - error_profile        — correctness premium, failure-mode tolerance,
                            recovery path
  - social_surround      — multi-agent presence, other-agent
                            observability, human-in-loop, oversight
                            frequency
  - evaluation_protocol  — in-niche benchmark (NOT a generic
                            benchmark), success threshold, out-of-niche
                            behaviour, re-evaluation cadence

For each axis, ask the engineer for either a value or a confidence-
annotated estimate. Do NOT synthesise plausible-sounding defaults.

If the deployment is being asked to serve multiple distinct niches,
detect this and recommend a router-of-niche-specialists pattern
instead of a single niche commitment.

Produce a typed, versioned niche object. Persist it. Downstream
architecture decisions reference this object by version, not by
transient values.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: detect_multi_niche_request
    description: >
      Detect whether a deployment is being asked to serve multiple
      distinct niches. Recommends a router-of-niche-specialists pattern
      if so, with one specifier invocation per sub-niche.
    parameters:
      deployment_description: { type: string }
    returns:
      is_multi_niche: { type: boolean }
      sub_niches:
        type: array
        items:
          type: object
          properties:
            description: { type: string }
            distinguishing_axis: { type: string }
      recommended_pattern: { enum: [single-niche, router-of-specialists, refuse] }
      router_spec: { type: object, description: 'If router-of-specialists, the routing schema' }

  - name: elicit_niche_field
    description: >
      Ask one targeted question to fill one niche axis. The questions
      are pre-authored per axis and should NOT be synthesised
      generically — they push toward specificity.
    parameters:
      axis:
        enum:
          [
            task_structure,
            signal_environment,
            resource_envelope,
            error_profile,
            social_surround,
            evaluation_protocol,
          ]
      deployment_description: { type: string }
      prior_partial_niche: { type: object }
    returns:
      value: { type: object, description: 'Filled axis values' }
      confidence: { enum: [low, medium, high] }
      notes: { type: string }
      vagueness_pushback:
        type: array
        items: { type: string }
        description: "If the engineer's answers were vague, the specific pushback questions asked"

  - name: validate_niche_completeness
    description: >
      Check whether a partial niche has enough information to allow
      downstream architecture decisions. Flag missing or incoherent
      fields.
    parameters:
      partial_niche: { type: object }
    returns:
      complete: { type: boolean }
      missing_fields: { type: array, items: { type: string } }
      incoherent_fields:
        type: array
        items:
          type: object
          properties:
            field: { type: string }
            issue: { type: string }
      recommendation: { type: string }

  - name: persist_niche
    description: >
      Save the completed niche as a versioned artefact and return its
      reference for downstream consumption.
    parameters:
      niche: { type: object }
      deployment_id: { type: string }
    returns:
      niche_version: { type: string, description: 'Semver' }
      artefact_path: { type: string }
      previous_version: { type: string, description: 'If this updates an existing niche' }

  - name: declare_out_of_niche_behaviour
    description: >
      Force an explicit declaration of what the deployed system does
      when an input falls outside the specified niche. Refuses to
      accept "undefined" as the answer.
    parameters:
      niche: { type: object }
    returns:
      declaration: { enum: [graceful_decline, refuse, route_to_alternative] }
      implementation_note: { type: string, description: 'How the architecture must support this' }
```

---

## Memory pattern

Niche objects persist as **versioned artefacts** scoped to the deployment, not the conversation:

```yaml
deployment_niches:
  - deployment_id: <id>
    versions:
      - version: <semver>
        created_at: <iso8601>
        created_by: <agent-or-human-id>
        niche_object: <full typed niche>
        elicitation_dialogue:
          - axis: <axis>
            questions_asked: <array>
            answers_received: <array>
            pushbacks: <array>
        validation_status: complete | incomplete | incoherent
    current: <semver-of-current-version>

    # Multi-niche router metadata (if applicable)
    router_spec:
      sub_niches: <array of niche refs>
      routing_logic: <object>
```

The elicitation dialogue is preserved with the niche so future re-specifications can reference _why_ particular values were chosen. This matters for the canalisation framing — niche values are not arbitrary; they reflect specific deployment constraints, and those constraints may evolve.

---

## Translation notes

| Stack                                 | Mapping                                                                                                                                                                  |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Claude skills**                     | `~/.claude/skills/niche-specifier/SKILL.md`. The elicitation tools become Claude tool definitions. The pushback discipline is enforced via the system_prompt_addition.   |
| **OpenAI function calling**           | Tools become OpenAI function schemas. The elicitation can be staged across multiple turns of an agent loop.                                                              |
| **MCP tools**                         | Each tool becomes an MCP `tool.json`. The persistence layer can be backed by an MCP-exposed deployment registry.                                                         |
| **LangChain / LlamaIndex agents**     | Tools become `Tool` objects. The elicitation dialogue maps cleanly onto a multi-turn agent that walks the engineer through each axis.                                    |
| **Model card / data sheet pipelines** | The niche object is a structured supplement to the model card. Persistence backends (Hugging Face Model Cards, MLflow registry) can store the niche alongside the model. |

---

## Evaluation signals (falsifiable claims)

The skill's specifications should pass these falsification tests:

1. **Niche-specified architectures outperform general-purpose architectures on matched in-niche evaluation.** When the skill produces a complete niche object and downstream design follows the collection pipeline, the resulting architecture should outperform a same-budget general-purpose architecture on the niche's in-niche benchmark. Failure: weakens the niche-binding claim.
2. **Vague specifications get rejected.** When the deployment description is genuinely vague, the skill refuses to produce a niche object rather than synthesising plausible values. Failure: the pushback discipline is not load-bearing — and the resulting "niche" is worth no more than the implicit assumptions it papers over.
3. **Multi-niche detection triggers router pattern.** Deployments with genuinely heterogeneous use cases get routed-of-specialists recommendations, not single-architecture recommendations. Failure: the multi-niche detector is misclassifying genuine heterogeneity as a single niche.
4. **Out-of-niche behaviour is operationally implemented.** Architectures shipped with explicit niche specifications support the declared out-of-niche behaviour at inference time (graceful decline, refusal, or routing actually happens when inputs cross the boundary). Failure: niche specifications are descriptive but not actionable.

---

## Examples

Working examples will be added under [`examples/`](examples/) as the catalog matures.

---

## See also

- Pattern README: [`../README.md`](../README.md)
- Architectural primitive: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Collection: [`../../collections/bounded-cognitive-architecture/`](../../../collections/bounded-cognitive-architecture/)
- Downstream skill: [`cognitive-regime-selection`](../../cognitive-regime-selection/)
- Downstream skill: [`capacity-first-scaling`](../../capacity-first-scaling/)
