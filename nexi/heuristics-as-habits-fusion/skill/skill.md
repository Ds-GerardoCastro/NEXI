# Skill: Heuristics as Habits Fusion (framework-neutral)

A drop-in **runtime decision** skill for AI agents that need to treat heuristic decision-making and motor-habit-formation as the same mechanism — selecting from a unified repertoire under cost-aware competition. Framework-neutral — see translation notes for stack-specific mappings.

> **Skill kind:** `runtime` (with design-time configuration of the unified repertoire and cost-awareness function). Used during inference, not just at architecture-design time.

---

## System-prompt fragment

Insert into the system or developer prompt of any agent that should apply heuristics-as-habits fusion to its decisions:

```
Treat HEURISTICS and MOTOR HABITS as protocol entries in a SINGLE UNIFIED
REPERTOIRE. Do not maintain a separate "fast / heuristic" path and "slow /
deliberative" path. Instead:

  1. ENUMERATE all applicable protocols regardless of domain.
     Heuristics (recognition heuristic, take-the-best, elimination-by-aspects)
     and chunked motor sequences and multi-step deliberative procedures all
     compete in the same selection step.

  2. APPLY COST-AWARE COMPETITION. Each protocol has an evaluation-cost
     annotation. Under tight budgets, cheap heuristic-style protocols win.
     Under high-stakes commitments, expensive deliberative protocols win.
     The transition is GRADED, not categorical — there is no "switch to Type 2
     mode" step.

  3. EXECUTE the selected protocol uniformly. The execution layer does not
     branch on whether the protocol was heuristic or deliberative.

  4. ON FAILURE, ATTRIBUTE STRUCTURALLY. A heuristic failure (e.g. recognition
     heuristic misapplied to Tokyo / Yokohama) and a motor-habit failure (e.g.
     grasping at empty air for a rental car shifter) should be analysed with
     the SAME structural categories: P_failure (perception inadequate),
     E_failure (unobservable goal-relevant difference), or Ba_failure
     (incorrect behavioural association). Surface cross-domain remedy patterns.

When you describe an error, do not say "this was a heuristic error" or "this
was a habit error" — say "this was a P_failure / E_failure / Ba_failure"
and let the cross-domain pattern surface naturally.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: register_protocol_in_repertoire
    description: >
      Add a protocol to the unified repertoire Br. Protocols can be heuristic,
      chunked motor, or deliberative cognitive — all live in one repertoire.
    parameters:
      protocol_id: string
      domain: enum [motor, cognitive, search]
      kind: enum [primitive, chunked]
      description: string
      evaluation_cost: number
      applicability_signature: string # encoded goal-context applicability
      body: object # the actual protocol logic / sequence
    returns:
      registration_id: string

  - name: select_protocol_with_cost
    description: >
      Apply cost-aware competition to select a protocol from the unified
      repertoire. No Type 1 / Type 2 routing — competition is graded.
    parameters:
      goal: string
      context: object
      perceptions: object
      cost_budget: number
    returns:
      selected: SelectedProtocol
      ranked_alternatives: list[ScoredProtocol]
      rationale: string

  - name: attribute_protocol_failure
    description: >
      When a selected protocol fails to achieve its goal, classify the
      failure into the structural categories that apply uniformly across
      heuristic and motor failures.
    parameters:
      protocol: SelectedProtocol
      context: object
      outcome: object
    returns:
      attribution_kind: enum [P_failure, E_failure, Ba_failure]
      reasoning: string
      suggested_remedy: string
      cross_domain_pattern_id: string? # if matches a known pattern, link it

  - name: cross_domain_error_analysis
    description: >
      Analyse a window of recent failures across domains. Surface patterns
      where heuristic failures and motor-habit failures share structure;
      propose remedies that transfer.
    parameters:
      window_size: number # number of recent failures to analyse
    returns:
      patterns: list[CrossDomainPattern]
      remedies: list[CrossDomainRemedy]
```

---

## Memory pattern

Per-agent unified-repertoire state persists across decisions:

```yaml
heuristics_as_habits_state:
  unified_repertoire_Br:
    - protocol_id: <id>
      domain: <motor | cognitive | search>
      kind: <primitive | chunked>
      evaluation_cost: <number>
      applicability_signature: <string>

  behavioural_associations_Ba:
    <(goal_id, perception_signature)>:
      <protocol_id>: <strength: number>

  decision_history:
    - timestamp: <ms>
      goal: <goal_id>
      context: <object>
      cost_budget: <number>
      candidates: [<protocol_id>, ...]
      selected: <protocol_id>
      domain: <motor | cognitive | search>
      outcome: <goal_achieved | goal_unmet | pending>
      attribution: <P_failure | E_failure | Ba_failure | success>

  cross_domain_patterns:
    - pattern_id: <id>
      observed_in_domains: [<motor>, <cognitive>, ...]
      shared_failure_structure: <string>
      remedy_transfer_evidence: <list>
```

This state is what enables **cross-domain error analysis** — detecting that a heuristic-decision failure and a motor-habit failure share diagnostic structure, and that a remedy applied in one domain may transfer to the other.

---

## Translation notes

| Stack                                     | Mapping                                                                                                                                                                  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Claude skills**                         | `~/.claude/skills/heuristics-habits-fusion/SKILL.md`. Tools become Claude tool definitions. The system-prompt fragment goes in the agent's system instructions.          |
| **OpenAI function calling**               | Tools become OpenAI function schemas. The system-prompt fragment is concatenated to the agent's `system` message.                                                        |
| **MCP tools**                             | Each tool becomes an MCP `tool.json`. Unified-repertoire state persisted in MCP server's session storage.                                                                |
| **LangChain / LangGraph**                 | Tools become `Tool` objects. The unified selection happens at a single node; protocols of all domains feed into it.                                                      |
| **RL frameworks**                         | The action space is the unified repertoire. The policy is the cost-aware competition function. The reward signal feeds back into reinforcement uniformly across domains. |
| **Cognitive architectures** (ACT-R, Soar) | Production rules of all kinds compete under a unified utility function. Cost-awareness maps onto utility-based conflict resolution.                                      |
| **Robotics frameworks**                   | Motor primitives, motor habits, and cognitive operations (planning, dialogue) all live in one repertoire. The cost-aware competition handles graded selection.           |

---

## Evaluation signals (falsifiable claims)

The skill should pass these falsification tests:

1. **Structurally similar error signatures across domains.** Heuristic failures and motor-habit failures should be classifiable into the same structural categories (`P_failure` / `E_failure` / `Ba_failure`). If failure signatures are unambiguously domain-specific (heuristic failures look nothing like motor failures), the unification claim is empirically weak.
2. **Symmetric transfer of training improvements.** Improvements made to the unified selection mechanism while training on motor tasks should produce measurable improvement on cognitive tasks (and vice versa). If transfer is consistently asymmetric or zero, the architecture has not actually unified.
3. **Lesion experiment robustness.** Removing the cost-awareness from the competition function should produce comparable degradation across heuristic and habit decisions. If degradation is asymmetric, the architecture has not actually unified — it has just placed two modules under one wrapper.
4. **Cross-domain remedy transfer.** When a remedy is applied to a `P_failure` in one domain, it should produce measurable improvement on `P_failure` patterns in other domains. If remedies don't transfer, cross-domain pattern detection is descriptive but not actionable.

---

## Examples

Working examples will be added under `examples/` as the catalog matures. Three near-term examples:

- **Recognition-heuristic-as-protocol-in-repertoire.** Demonstrate that the recognition heuristic is registered in `Br` alongside motor primitives and deliberative procedures, competing under cost-aware logic. Show the structural failure analysis on the Tokyo/Yokohama/Nagasaki worked example.
- **Cross-domain remedy transfer.** Demonstrate a remedy applied to a `P_failure` in motor manipulation transferring to a `P_failure` in heuristic decision-making.
- **Replacement of dual-process architecture.** Take an existing System 1 / System 2 implementation; replace it with a unified-repertoire heuristics-as-habits architecture; compare error signatures and improvement-transfer rates.

## See also

- Pattern README: [`../README.md`](../README.md)
- Architecture: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Collection: [`../../../clusters/embodied-action-selection/`](../../../clusters/embodied-action-selection/)
- Sibling NEXIs: [`../../action-selection-as-common-substrate/`](../../action-selection-as-common-substrate/) · [`../../ecological-context-model/`](../../ecological-context-model/) · [`../../exaptation-architectural-reuse/`](../../exaptation-architectural-reuse/)
