# Architecture: Heuristics as Habits Fusion

This document specifies the architectural primitive for unifying heuristic decision-making and motor-habit-formation under a single mechanism — components, interfaces, data flow, and integration with the rest of the [`embodied-action-selection`](../../../clusters/embodied-action-selection/) collection.

## Components

### 1. Unified repertoire `Br`

A typed structure containing both motor actions and cognitive operations as protocol entries. Each entry has an evaluation-cost annotation; the structure is otherwise domain-agnostic.

```
Br := list of:
    Protocol:
        id: string
        domain: enum [motor, cognitive, search]
        kind: enum [primitive, chunked]
        description: string
        evaluation_cost: number    # how expensive to run this protocol
        applicability: GoalContextSignature
        body: ProtocolBody          # the actual logic / sequence
```

Design-time: register protocols in `Br` regardless of domain. The recognition heuristic is just a protocol with `domain=cognitive`, `kind=chunked`, low `evaluation_cost`, applicability matching "two-option decision under recognition asymmetry." Motor habits are protocols with `domain=motor`, `kind=chunked`, varying `evaluation_cost`, applicability matching specific motor-context signatures.

### 2. Cost-aware competition

Equation (2) extended to account for evaluation cost. The selection function takes both behavioural-association strength and evaluation cost into account, with a cost-budget parameter that depends on the deployment context.

```
select_protocol(
    candidates: ranked_by_strength,
    cost_budget: number,
) -> SelectedProtocol
```

The cost-awareness is implemented within the competition function, not as a Type 1 / Type 2 routing layer. Under tight budget, cheap heuristic-style protocols win. Under high-stakes commitments, expensive deliberative protocols win. The transition is graded, not categorical.

### 3. Cross-domain error-analysis layer

Failure attribution from the [`ecological-context-model`](../../../nexi/ecological-context-model/) NEXI applied uniformly to heuristic and motor failures. Reports the same structure regardless of domain:

```
attribute_protocol_failure(
    protocol: SelectedProtocol,
    context: Context,
    outcome: GoalAchievementResult,
) -> FailureAttribution

FailureAttribution:
    kind: enum [P_failure, E_failure, Ba_failure]
    domain: enum [motor, cognitive, search]
    cross_domain_pattern_id: string?    # if same-shape failures observed in
                                        # other domains, link them
```

The cross-domain pattern detection is what extracts the architectural payoff: when heuristic failures and motor-habit failures show the same diagnostic structure, the system surfaces this as a cross-domain pattern, and remedies transfer.

## Data flow

```
       goal g, context C, perceptions P, cost_budget
                        │
                        ▼
              ┌─────────────────────┐
              │ Look up applicable  │ ◄── unified repertoire Br
              │ protocols in Br     │
              └─────────┬───────────┘
                        │ ranked candidates (heuristic + chunked + primitive)
                        ▼
              ┌─────────────────────┐
              │ Cost-aware compete  │ ◄── cost_budget
              └─────────┬───────────┘
                        │ selected protocol
                        ▼
                 execute and commit
                        │
                        ▼
              ┌─────────────────────┐
              │ Evaluate goal       │   eq. (3) from ECM
              │ achievement g+(C)   │
              └─────────┬───────────┘
                        │
              ┌─────────┴───────────┐
              ▼                     ▼
          achieved              not achieved
              │                     │
              ▼                     ▼
       reinforce Ba         attribute failure
       (chunking if       (kind: P / E / Ba)
        threshold)              │
                                ▼
                       ┌─────────────────────┐
                       │ Cross-domain pattern│
                       │ detection           │
                       └─────────────────────┘
                                │
                                ▼
                  surface remedy that may
                  transfer across domains
```

## Pseudocode — runtime decision with unified repertoire

```python
def decide(goal, context, perceptions, cost_budget, repertoire, associations):
    # Step 1: look up applicable protocols across all domains
    candidates = repertoire.lookup_applicable(
        goal=goal,
        perception_signature=signature_of(perceptions),
        # No domain filter — heuristic and motor protocols compete together
    )

    # Step 2: rank by behavioural-association strength
    ranked = associations.rank(candidates, goal, perceptions)

    # Step 3: cost-aware competition (graded, not Type 1 / Type 2 routing)
    selected = compete_with_cost(
        ranked,
        cost_budget=cost_budget,
        cost_extractor=lambda p: p.evaluation_cost,
    )

    # Step 4: execute the selected protocol regardless of domain
    outcome = execute(selected, context)

    # Step 5: evaluate via ECM equation (3)
    g_plus = evaluate_goal_achievement(context, selected, outcome)

    # Step 6: reinforce or attribute failure (uniform across domains)
    if g_plus.achieved:
        associations.reinforce(goal, perceptions, selected)
        if associations.strength(selected) > CHUNKING_THRESHOLD:
            repertoire.chunk(selected.body)
    else:
        attribution = attribute_protocol_failure(selected, context, g_plus)
        # Cross-domain pattern detection
        if attribution.matches_existing_pattern_in_other_domains():
            surface_cross_domain_remedy(attribution)

    return selected, outcome
```

## Integration notes

| Stack                                        | How to integrate                                                                                                                                                                                                                                      |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LLM agent frameworks** (LangGraph, CrewAI) | Tool calls, reasoning steps, and inline computations are all protocols in `Br`. The recognition-style heuristic for tool selection competes alongside multi-step deliberative plans under the same mechanism. Cost-awareness via token budget.        |
| **Embodied agents**                          | Motor primitives, motor habits, cognitive operations, and reasoning protocols are all entries in `Br`. The same selection mechanism handles "grasp the cup" and "decide which path to take" via different protocols competing under cost-aware logic. |
| **RL agents**                                | The action space is extended to include both motor primitives and cognitive operations. The policy is the cost-aware competition function. Reward attribution feeds back into both heuristic and habit reinforcement uniformly.                       |
| **Cognitive architectures** (ACT-R, Soar)    | Production rules of all kinds (motor, cognitive, declarative-retrieval) compete under a unified utility function. The cost-awareness maps onto ACT-R's utility-based conflict resolution.                                                             |
| **Dual-process architectures**               | The pattern is the _replacement_ for dual-process. Audit existing dual-process architectures for cases where the Type 1 / Type 2 distinction is descriptive rather than architecturally load-bearing — those are candidates for unification.          |

## Performance and cost considerations

- **Repertoire-management complexity.** A unified `Br` containing motor and cognitive protocols is larger than a single-domain repertoire. Lookup-by-applicability becomes more important; indexing structures may be needed for large `Br`.
- **Cost-awareness implementation difficulty.** Encoding evaluation cost without devolving into a Type 1 / Type 2 router requires care. The cost should be a _property of the protocol_, not of a routing layer above the protocols.
- **Cross-domain pattern detection overhead.** Comparing failure structures across domains adds analysis cost. For tight-loop deployments, defer to post-hoc analysis.
- **Loss of dual-process descriptive convenience.** Some users / debuggers will find it harder to reason about a unified architecture. Documentation should explicitly map common dual-process language onto the unified-mechanism vocabulary.

## Interaction with the collection

This NEXI is the **behavioural-instance layer** of the [`embodied-action-selection`](../../../clusters/embodied-action-selection/) collection — the concrete demonstration that the collection's other three NEXIs (formalism / substrate-invariant / reuse) compose to produce a useful unified architecture. It composes with:

- [`action-selection-as-common-substrate`](../../action-selection-as-common-substrate/) — provides the unified selection mechanism. Heuristics-as-habits is what that mechanism does at the behavioural level when given a unified `Br` spanning domains.
- [`ecological-context-model`](../../ecological-context-model/) — provides the formalism (equations 1–3) that expresses the heuristic / habit equivalence. Both are instances of `B(C) = f(Br, Ba(g, P))`; both fail via `g+(C) = f(B, E)` when `E` differs from training.
- [`exaptation-architectural-reuse`](../../exaptation-architectural-reuse/) — explains _why_ the unified mechanism works: cognitive heuristics are exaptive of motor habit-formation; the same mechanism redeployed across domains.
