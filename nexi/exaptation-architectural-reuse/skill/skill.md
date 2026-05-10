# Skill: Exaptation Architectural Reuse (framework-neutral)

A drop-in **design-time and runtime** skill for AI engineers identifying candidate mechanisms for cross-domain redeployment and surfacing the reuse pattern explicitly. Framework-neutral — see translation notes for stack-specific mappings.

> **Skill kind:** `design-time` (architectural-review pattern; identifies redeployment candidates) and `runtime` (implements adapter-based dispatch with audit infrastructure).

---

## System-prompt fragment

Insert into the system or developer prompt of any agent applying this skill at design-time:

```
When evaluating an AI system's architecture for cross-domain capability,
identify candidates for ARCHITECTURAL REUSE VIA EXAPTATION:

  1. SCAN for candidate redeployable mechanisms M. A candidate is:
     - Well-developed in its current domain (mature, well-tuned)
     - Has a function that *could* apply to other domains
       (e.g. selection, search, attention, ranking, gating)
     - Currently deployed only in its source domain

  2. SCAN for additional domains that could share M:
     - Domains where the same function is currently implemented by
       a separate, less-mature module
     - Domains where the function is currently absent and is being
       implemented ad-hoc inline

  3. PROPOSE the redeployment as a deliberate architectural choice:
     - Specify what M's domain-agnostic input and output types should be
     - Specify the per-domain adapters (preprocess + postprocess)
     - Specify the audit infrastructure (parameter-overlap check,
       improvement-transfer test, lesion test)

  4. EVALUATE the proposal honestly:
     - Is M actually mature enough to redeploy? Premature exaptation
       performs worse than specialised modules.
     - Will adapters leak domain specificity into M? If M would have
       to branch on domain identity, the reuse is shallow.
     - What is the cross-domain transfer expectation? If improvements
       won't transfer, the reuse claim is empty.

The exaptation pattern works in nature because evolution doesn't easily
build new machinery; AI systems should adopt the same discipline by default,
because architectural duplication is the default cost — reuse is the saving.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: register_redeployable_mechanism
    description: >
      Register a mechanism M as a candidate for cross-domain redeployment.
      Specifies M's typed input and output, the source domain, and the
      candidate target domains.
    parameters:
      mechanism_id: string
      source_domain: string
      M_input_type: string
      M_output_type: string
      candidate_target_domains: list[string]
      maturity_assessment: enum [immature, mature, well-developed]
    returns:
      registration_id: string

  - name: wrap_domain_adapter
    description: >
      Create an adapter for a target domain that translates domain-specific
      input into M_input_type and M_output_type back into domain-specific
      action.
    parameters:
      mechanism_id: string
      target_domain: string
      preprocess_logic: string # specification of domain → M_input
      postprocess_logic: string # specification of M_output → domain action
    returns:
      adapter_id: string

  - name: audit_reuse_pattern
    description: >
      Audit a registered exaptation pattern for genuine reuse vs. shallow
      parameter-sharing. Checks parameter overlap, branching, and
      cross-domain improvement transfer.
    parameters:
      mechanism_id: string
    returns:
      report:
        parameter_overlap_pct: number
        branches_on_domain: boolean
        improvement_transfer_score: number # 0.0 to 1.0
        verdict: enum [genuine_reuse, shallow_sharing, domain_specific]

  - name: lesion_test_redeployed_mechanism
    description: >
      Run a lesion test on the registered mechanism. Disabling M should
      degrade all target domains comparably; disabling individual
      adapters should degrade only their own domain.
    parameters:
      mechanism_id: string
    returns:
      M_lesion_degradation_per_domain: dict[domain, number]
      adapter_lesion_degradation: dict[(adapter_id, domain), number]
      verdict: enum [reuse_confirmed, reuse_shallow, reuse_failed]
```

---

## Memory pattern

Per-system exaptation registry persists across decisions:

```yaml
exaptation_registry:
  mechanisms:
    - id: <mechanism_id>
      source_domain: <string>
      M_input_type: <string>
      M_output_type: <string>
      target_domains: [<string>, ...]
      maturity: <immature | mature | well-developed>

  adapters:
    - id: <adapter_id>
      mechanism_id: <mechanism_id>
      target_domain: <string>
      preprocess_logic: <string>
      postprocess_logic: <string>

  audit_history:
    - timestamp: <ms>
      mechanism_id: <mechanism_id>
      report:
        parameter_overlap_pct: <number>
        branches_on_domain: <boolean>
        improvement_transfer_score: <number>
        verdict: <string>

  lesion_test_history:
    - timestamp: <ms>
      mechanism_id: <mechanism_id>
      M_lesion_per_domain_degradation: <dict>
      adapter_lesion_degradation: <dict>
      verdict: <string>
```

This state is what allows **continuous monitoring** of the reuse pattern's integrity. As the system evolves, reuse can degrade silently (someone adds a domain-specific branch to `M`); the audit infrastructure catches this.

---

## Translation notes

| Stack                       | Mapping                                                                                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude skills**           | `~/.claude/skills/exaptation-reuse/SKILL.md`. Tools become Claude tool definitions. The system-prompt fragment goes in design-time architectural-review prompts. |
| **OpenAI function calling** | Tools become OpenAI function schemas. Used in design-time architectural-review chat sessions where engineers identify candidate mechanisms.                      |
| **MCP tools**               | Each tool becomes an MCP `tool.json`. Exaptation registry persisted in MCP server's session storage; survives across sessions for long-term audit.               |
| **LangChain / LangGraph**   | The pattern is a meta-architecture: the LangGraph itself can be structured around a single core node (M) with multiple adapter nodes wrapping it.                |
| **Multi-task transformers** | The shared encoder is M; task-specific heads are adapters. The audit tool reports parameter-overlap and improvement-transfer.                                    |
| **Robotics / embodied-AI**  | The motor controller's action-selection mechanism is a strong M candidate. Wrap dialogue, planning, and tool-use as additional domains.                          |

---

## Evaluation signals (falsifiable claims)

The skill should pass these falsification tests:

1. **Cross-domain transfer of improvements.** Improvements made to `M` while training on domain Aᵢ should produce measurable improvement on domain Aⱼ. If improvement transfer is consistently zero, `M` is effectively domain-specific despite the adapter framing.
2. **Lesion experiment robustness.** Lesioning `M` should degrade all target domains comparably; lesioning a single adapter should degrade only its own domain. If lesioning `M` only degrades one domain, the reuse pattern is shallow.
3. **Marginal-cost-per-new-domain reduction.** Adding a new domain should cost on the order of one adapter's complexity, not on the order of `M`'s complexity. If marginal cost scales linearly with `M`'s complexity, the reuse pattern is failing.
4. **Audit-infrastructure activity.** The audit and lesion tools should run regularly (CI-style if possible). Silent degradation of the reuse pattern over time is the principal risk; surface it explicitly.

---

## Examples

Working examples will be added under `examples/` as the catalog matures. Three near-term examples:

- **Action selection redeployed across motor and cognitive domains.** Demonstrate that a single action-selection module (anchored in the [`action-selection-as-common-substrate`](../../action-selection-as-common-substrate/) NEXI) handles both motor commitments (in a robotic embodied agent) and cognitive operations (tool-call selection in an agentic loop) with shared core and per-domain adapters.
- **Search redeployed across information and action spaces.** Following the Hills/Todd/Miller research programme, demonstrate that one search mechanism handles both information retrieval (RAG) and planning (MCTS) without architectural duplication.
- **Lesion test for a "shared encoder" claim.** Take a multi-task transformer claiming shared-encoder reuse; run the lesion test; report whether reuse is genuine or shallow.

## See also

- Pattern README: [`../README.md`](../README.md)
- Architecture: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Cluster: [`../../../clusters/embodied-action-selection/`](../../../clusters/embodied-action-selection/)
- Sibling NEXIs: [`../../action-selection-as-common-substrate/`](../../action-selection-as-common-substrate/) · [`../../ecological-context-model/`](../../ecological-context-model/) · [`../../heuristics-as-habits-fusion/`](../../heuristics-as-habits-fusion/)
