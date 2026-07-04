# Skill: Ecological Context Model (framework-neutral)

A drop-in **runtime formalism** skill for AI agents that need to surface context construction, behaviour selection, and goal-achievement evaluation as explicit relational steps with typed terms. Framework-neutral — see translation notes for stack-specific mappings.

> **Skill kind:** `runtime` (with design-time configuration of the unified state schema and perception-signature function). Used during inference, not just at architecture-design time.

---

## System-prompt fragment

Insert into the system or developer prompt of any agent that should apply ECM formalism to its decisions:

```
For every action you take, surface FOUR EXPLICIT STEPS with typed terms,
following the Ecological Context Model:

  1. CONSTRUCT CONTEXT (eq. 1: C = { A(g), E }).
     Identify: the current goal g, the environment E, and your own
     perceptible subset E(A). Note that your own internal state —
     working memory, recent reasoning, internal cycles — is part of E,
     not separate from it.

  2. SELECT BEHAVIOUR (eq. 2: B(C) = f(Br, Ba(g, P))).
     Identify: candidates from your repertoire Br relevant to goal g;
     your behavioural associations Ba indexed by (g, P); rank
     candidates by strength of association. Select the winning
     candidate via the action-selection mechanism.

  3. EVALUATE GOAL ACHIEVEMENT (eq. 3: g+(C) = f(B, E)).
     After acting, check whether goal g was achieved given the full
     environment E (not just your perceptible subset E(A)).

  4. IF FAILED, ATTRIBUTE.
     Distinguish three failure modes:
     - P-failure: your perceptions P were inadequate (a feature in
       E(A) was observable but you missed it). Remedy: improve perception.
     - E-failure: the environment E differed from training in
       goal-relevant ways outside E(A) — i.e. structurally relevant
       but unobservable to you. Remedy: handle unobservability.
     - Ba-failure: your behavioural association was wrong for the new
       context even though P/E were fine. Remedy: weaken Ba(g, P) for
       the failed action.

These distinctions matter because they imply different remedies. Do not
collapse them into a single "the action failed" signal.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: construct_context
    description: >
      Construct an Ecological Context Model context object given the
      current goal, environment state, and agent's perceptual apparatus.
      Implements equation (1): C = { A(g), E }.
    parameters:
      goal: string
      environment_state: object # the unified E
      agent_id: string
    returns:
      context: Context
      perceptible_features: list[Feature] # E(A)
      perceptions: list[Feature] # P (subset of E(A) actually attended)

  - name: lookup_behavioural_association
    description: >
      Look up the behavioural associations Ba(g, P) for a given goal and
      perception signature. Returns ranked candidate actions for use in
      equation (2).
    parameters:
      goal: string
      perception_signature: string
    returns:
      ranked_candidates: list[ScoredCandidate]

  - name: evaluate_goal_achievement
    description: >
      Evaluate whether the goal was achieved given the executed behaviour
      and full environment state. Implements equation (3).
    parameters:
      context: Context
      behaviour: Behaviour
      outcome_state: object
    returns:
      achieved: boolean
      g_plus_result: GoalAchievementResult

  - name: attribute_failure
    description: >
      When goal achievement fails, attribute the failure to one of:
      P-failure (perception inadequate), E-failure (unobservable
      goal-relevant difference), or Ba-failure (incorrect association).
    parameters:
      context: Context
      behaviour: Behaviour
      outcome_state: object
    returns:
      attribution: enum [P_failure, E_failure, Ba_failure, unknown]
      reasoning: string
      suggested_remedy: string
```

---

## Memory pattern

Per-agent ECM state persists across decisions:

```yaml
ecm_state:
  unified_state_schema:    # design-time definition of E
    feature_types:
      - id: <string>
        source: <external | agent_internal>
        kind: <observable_to_agent | observable_to_human_only | structural_only>

  behavioural_associations_Ba:    # learnable component
    <(goal_id, perception_signature)>:
      <action_id>: <strength: number>

  context_history:
    - timestamp: <ms>
      C: { goal, environment_snapshot, perceptible_features, perceptions }
      B: <selected_behaviour>
      g_plus: <achievement_result>
      attribution: <P_failure | E_failure | Ba_failure | success>
```

This state enables transfer-failure-attribution analysis (when failures collection, what is their attribution distribution? P-failures suggest perception improvements; E-failures suggest training-distribution gaps; Ba-failures suggest reinforcement-update bugs).

---

## Translation notes

| Stack                                  | Mapping                                                                                                                                                                                                                                             |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude skills**                      | `~/.claude/skills/ecm-formalism/SKILL.md`. Tools become Claude tool definitions. The system-prompt fragment goes in the agent's system instructions.                                                                                                |
| **OpenAI function calling**            | Tools become OpenAI function schemas. The system-prompt fragment is concatenated to the agent's `system` message.                                                                                                                                   |
| **MCP tools**                          | Each tool becomes an MCP `tool.json`. ECM state is persisted in the MCP server's session storage.                                                                                                                                                   |
| **LangChain / LangGraph**              | Tools become `Tool` objects. The four ECM steps map onto explicit nodes in the graph.                                                                                                                                                               |
| **RL frameworks**                      | The state-action-reward-policy quadruple maps onto ECM with extension. State → `E` / `E(A)` / `P`; policy → `f(Br, Ba(g, P))`; reward → `g+`; the extension is the failure-attribution layer.                                                       |
| **Robotics frameworks** (ROS, Habitat) | World state and proprioception both feed `E`. Sensor stack defines `E(A)`. `g+` is the task-success classifier. Failure attribution distinguishes "sensor missed it" from "world wasn't what we trained on" from "policy was wrong for this state." |

---

## Evaluation signals (falsifiable claims)

The skill should pass these falsification tests:

1. **Provenance auditability.** For every commitment, the skill should produce a complete trace: `C` (with `E`/`E(A)`/`P`), `B`, `g+`, attribution. If any link is missing, the formalism is not actually being applied.
2. **Failure-attribution diagnosticity.** Given a controlled distribution shift, the skill should distinguish `P_failure` (which fails when sensors are degraded), `E_failure` (which fails when training distribution gaps are introduced), and `Ba_failure` (which fails when reinforcement updates are corrupted). Each kind should be detectable independently.
3. **Transfer attribution accuracy.** When transfer to a new context succeeds, success-attribution should identify which features in `P` overlapped sufficiently with prior successful contexts. When transfer fails, failure-attribution should identify whether the relevant overlap was in `P` (perceptual overlap) or in unobservable structural features in `E`.
4. **Lesion experiment robustness.** Removing the formalism (replacing the four steps with informal generation) should produce measurable degradation on tasks where the formalism's payoff is hypothesised. If not, the formalism is not load-bearing for this deployment.

---

## Examples

Working examples will be added under `examples/` as the catalog matures. Two near-term examples:

- **Tool-using agent with ECM-formalism prompt.** Demonstrate decision-provenance audit on a multi-tool agentic flow with explicit `C` / `B` / `g+` / attribution surfaced for each tool call.
- **Robotic manipulation with failure attribution.** Demonstrate the three-way failure attribution on controlled distribution shifts (sensor occlusion = `P_failure`; novel object material = `E_failure`; degraded policy = `Ba_failure`).

## See also

- Pattern README: [`../README.md`](../README.md)
- Architecture: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Collection: [`../../../collections/embodied-action-selection/`](../../../collections/embodied-action-selection/)
- Sibling NEXIs: [`../../action-selection-as-common-substrate/`](../../action-selection-as-common-substrate/) · [`../../exaptation-architectural-reuse/`](../../exaptation-architectural-reuse/) · [`../../heuristics-as-habits-fusion/`](../../heuristics-as-habits-fusion/)
