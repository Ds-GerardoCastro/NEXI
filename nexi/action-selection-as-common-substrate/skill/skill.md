# Skill: Action Selection as Common Substrate (framework-neutral)

A drop-in **runtime action-selection** skill for AI agents that need to make their selection step inspectable, lesionable, and reusable across domains. Framework-neutral — see translation notes for stack-specific mappings.

> **Skill kind:** `runtime` (with design-time configuration of the candidate space and competition policy). Used during inference, not just at architecture-design time.

---

## System-prompt fragment

Insert into the system or developer prompt of any agent that should expose action selection as a first-class step:

```
For every action you commit to — tool call, output sequence, mode change,
plan step — make your action-selection step EXPLICIT. Do not let action
selection be implicit in your generation. Specifically:

  1. ENUMERATE candidate actions. Given the current goal and context,
     list the candidate actions you are choosing among. Do not collapse
     this step into "I will do X."
  2. COMPETE candidates against the goal. For each candidate, articulate
     why it might or might not contribute to goal achievement, drawing
     on prior context, prior outcomes, and current perceptions.
  3. SELECT via DEFAULT-INHIBIT / SELECTIVE-DISINHIBIT. The default state
     is "no action committed." A specific candidate is RELEASED only when
     it clearly outranks alternatives by goal-conditioned strength. If
     no candidate clearly wins, hold for more evidence rather than
     committing arbitrarily.
  4. AFTER OUTCOME, REINFORCE. When a selected action achieves its goal,
     remember the goal-context-action association so similar future
     selections benefit. When it fails, weaken the association.
  5. Make every step inspectable: the candidate list, the competition
     reasoning, the selection rationale, and the post-outcome update
     should all be surfaced rather than hidden.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: enumerate_candidate_actions
    description: >
      Enumerate the candidate actions for the current goal and context,
      drawn from the agent's behavioural repertoire.
    parameters:
      goal: string
      context: object
      perceptions: object
    returns:
      candidates: list[Action]

  - name: score_candidates_against_goal
    description: >
      Compete candidates against the goal using accumulated behavioural
      associations Ba(g, P). Returns ranked candidates.
    parameters:
      goal: string
      perceptions: object
      candidates: list[Action]
    returns:
      ranked: list[ScoredCandidate]

  - name: select_action
    description: >
      Apply default-inhibit / selective-disinhibit gating. Releases the
      winning candidate if it clearly outranks alternatives; otherwise
      returns no-selection (hold for more evidence).
    parameters:
      ranked: list[ScoredCandidate]
      threshold: number
      high_stakes: boolean # if true, delegates to coincidence-gate
    returns:
      decision: enum [release, hold, abort]
      selected_action: Action | null
      rationale: string

  - name: reinforce_selection_post_outcome
    description: >
      Update the goal-context-action association based on the outcome of
      a previously-selected action. Successful selections strengthen the
      association; failed selections weaken it.
    parameters:
      goal: string
      context: object
      action: Action
      outcome: enum [goal_achieved, goal_unmet, partial]
    returns:
      updated_association_strength: number
      chunking_triggered: boolean
```

---

## Memory pattern

Per-agent action-selection state persists across decisions within a session:

```yaml
selection_state:
  repertoire:
    - action_id: <id>
      domain: <motor | cognitive | search>
      origin: <innate | learned | chunked>
  associations:
    Ba_g_P:
      <goal_id>:
        <perception_signature>:
          <action_id>: <strength: number>
  selection_history:
    - timestamp: <ms>
      goal: <goal_id>
      candidates: [<action_id>, ...]
      ranked: [{action_id, score}, ...]
      decision: <release | hold | abort>
      selected: <action_id | null>
      rationale: <string>
      outcome: <goal_achieved | goal_unmet | pending>
```

This state is what enables **lesion experiments** (remove the selection module; observe degradation) and **decision-provenance auditing** (which action did the agent select, given which goal and context, on which evidence?).

---

## Translation notes

| Stack                                  | Mapping                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude skills**                      | `~/.claude/skills/action-selection/SKILL.md`. Tools become Claude tool definitions. The system-prompt fragment goes in the agent's system instructions.                                                                                                                                                                      |
| **OpenAI function calling**            | Tools become OpenAI function schemas. The system-prompt fragment is concatenated to the agent's `system` message.                                                                                                                                                                                                            |
| **MCP tools**                          | Each tool becomes an MCP `tool.json`. Selection state persistence is handled by the MCP server's session storage.                                                                                                                                                                                                            |
| **LangChain / LangGraph**              | Tools become `Tool` objects. The selection module sits as a conditional node before any side-effect-producing edge.                                                                                                                                                                                                          |
| **RL frameworks** (PPO, DQN, SAC)      | Wrap the existing action head in the four-component structure. Action enumeration is the policy's candidate output; competition is the policy's scoring; gating is the explicit threshold check; reinforcement is the existing TD-learning update — but now all four are first-class modules rather than substrate-implicit. |
| **Robotics frameworks** (ROS, Habitat) | Motor commands are the candidates. Selection module sits between motion-planner output and motor controllers.                                                                                                                                                                                                                |

---

## Evaluation signals (falsifiable claims)

The skill's gates should pass these falsification tests:

1. **Explicit-selection systems outperform substrate-implicit baselines on long-horizon goal pursuit.** At matched cost, agents using the explicit selection module should outperform substrate-implicit baselines on tasks requiring long-horizon goal pursuit, chunked-sequence reuse, and recovery from premature commitment.
2. **Lesion experiment robustness.** Removing the explicit selection module should produce measurable degradation. If not, the module was not load-bearing and the system was effectively substrate-implicit.
3. **Cross-domain reuse efficiency.** Paired with the [`exaptation-architectural-reuse`](../../exaptation-architectural-reuse/) NEXI, one selection module should handle motor and cognitive domains at lower marginal cost than duplicate-module architectures.
4. **Decision-provenance auditability.** Every commitment should be traceable to a candidate list, a competition rationale, and a selection threshold check. If decisions cannot be audited, the system is substrate-implicit even if it nominally exposes the four components.

---

## Examples

Working examples will be added under `examples/` as the catalog matures. Three near-term examples:

- **Tool-using agent with explicit selection.** Demonstrate decision-provenance audit on a multi-tool agentic flow.
- **RL agent with wrapped action head.** Demonstrate lesion experiments on the four-component structure.
- **Embodied agent with motor-cognitive sharing.** Demonstrate the cross-domain reuse claim by sharing one selection module across manipulation and reasoning, and showing reduced marginal cost vs. duplicate-module baseline.

## See also

- Pattern README: [`../README.md`](../README.md)
- Architecture: [`../architecture/overview.md`](../architecture/overview.md)
- References: [`../references.md`](../references.md)
- Collection: [`../../../collections/embodied-action-selection/`](../../../collections/embodied-action-selection/)
- Sibling NEXIs: [`../../ecological-context-model/`](../../ecological-context-model/) · [`../../exaptation-architectural-reuse/`](../../exaptation-architectural-reuse/) · [`../../heuristics-as-habits-fusion/`](../../heuristics-as-habits-fusion/)
