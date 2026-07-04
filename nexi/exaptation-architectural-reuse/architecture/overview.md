# Architecture: Exaptation Architectural Reuse

This document specifies the architectural primitive for explicit exaptation-based component reuse — components, interfaces, data flow, and integration with the rest of the [`embodied-action-selection`](../../../collections/embodied-action-selection/) collection.

## Components

### 1. The redeployable core mechanism `M`

A well-developed module designed in one domain (e.g. action selection, search, attention) but typed to be **domain-agnostic at its interface**. The core's internal logic is specific to its function (e.g. selection); the input and output types are abstracted so that domain-specific data can be wrapped to match.

```
core_mechanism(
    typed_input: M_Input,        # domain-agnostic input type
    config: M_Config,
) -> typed_output: M_Output      # domain-agnostic output type
```

Design-time: implement `M` once, in its source domain (e.g. motor action selection). Tune it well. Expose its interface as typed values rather than as domain-specific structures.

### 2. Per-domain adapters `Aᵢ`

Thin wrappers that translate domain-specific input into `M_Input` and translate `M_Output` back into domain-specific actions. Adapters are cheap and domain-aware; the core is expensive and domain-agnostic.

```
adapter_motor(
    motor_state: MotorState,
    motor_goal: MotorGoal,
) -> M_Input

adapter_motor_postprocess(
    M_output: M_Output,
) -> MotorAction

# Same shape for adapter_cognitive, adapter_search, adapter_dialogue, ...
```

Critical: adapters must not leak domain specificity into `M_Input` such that `M` ends up branching on domain identity. If `M` has `if domain == "motor": ...`, the reuse claim is false — `M` is effectively a multi-modal switch rather than a redeployed mechanism.

### 3. Reuse audit / lesion infrastructure

Tooling that confirms the reuse pattern is genuine. Two principal checks:

```
audit_reuse(M, adapters: list[Aᵢ]) -> ReuseAuditReport
    - parameter overlap: % of M's parameters used by all adapters
    - branching audit: does M branch on domain identity?
    - improvement transfer test: does training on adapter Aᵢ improve performance through Aⱼ?

lesion_test(M, adapters) -> LesionReport
    - lesion M completely → all domains should degrade comparably
    - lesion individual adapter Aᵢ → only domain i should degrade
    - if pattern matches → reuse is genuine
    - if not → reuse is shallow (M is effectively domain-specific)
```

## Data flow

```
   Domain 1 input ──► Adapter A₁ ──┐
   Domain 2 input ──► Adapter A₂ ──┤
   Domain 3 input ──► Adapter A₃ ──┼──► [ M_Input typed ]
   ...                              │
   Domain N input ──► Adapter Aₙ ──┘
                                    ▼
                       ┌─────────────────────────┐
                       │  Core mechanism M       │
                       │  (domain-agnostic core) │
                       └────────────┬────────────┘
                                    │ M_Output typed
                                    ▼
                       ┌─────────────────────────┐
                       │  Output dispatch by     │
                       │  originating domain     │
                       └────────────┬────────────┘
                                    │
              ┌─────────┬───────────┼───────────┬─────────┐
              ▼         ▼           ▼           ▼         ▼
          Domain 1   Domain 2    Domain 3    ...      Domain N
          adapter    adapter     adapter              adapter
          postproc   postproc    postproc             postproc
              │         │           │                   │
              ▼         ▼           ▼                   ▼
          Domain 1  Domain 2    Domain 3             Domain N
          action    action      action                action
```

## Pseudocode — runtime cross-domain redeployment

```python
class ExaptationCore:
    def __init__(self, M_implementation, adapters: dict[str, Adapter]):
        self.M = M_implementation
        self.adapters = adapters
        self.audit_log = []

    def handle(self, domain: str, domain_input: Any) -> Any:
        if domain not in self.adapters:
            raise NoAdapterForDomain(domain)

        # Phase 1: adapter wraps domain input into typed M_Input
        M_input = self.adapters[domain].preprocess(domain_input)

        # Phase 2: core mechanism processes typed input — DOMAIN-AGNOSTIC
        M_output = self.M.process(M_input)

        # Phase 3: adapter unwraps typed M_Output into domain-specific action
        domain_action = self.adapters[domain].postprocess(M_output)

        # Audit log — used by lesion-test infrastructure
        self.audit_log.append({
            "domain": domain,
            "M_input_type": type(M_input).__name__,
            "M_output_type": type(M_output).__name__,
            "adapter_id": self.adapters[domain].id,
        })

        return domain_action

    def audit_reuse(self) -> ReuseAuditReport:
        # Verify M does not branch on domain identity
        # Verify all adapters used the same M parameter subset
        # Verify improvement transfer across adapters
        ...

    def lesion_test_M(self) -> LesionReport:
        # Disable M; all domains should degrade comparably
        ...

    def lesion_test_adapter(self, domain: str) -> LesionReport:
        # Disable one adapter; only that domain should degrade
        ...
```

## Integration notes

| Stack                                     | How to integrate                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Embodied-AI deployments**               | The motor controller's action-selection mechanism (already well-developed in robotics) is a strong candidate `M`. Add adapters for cognitive operations (planning, dialogue, tool selection) so the same selection logic handles all. Audit that improvements to the motor selection (latency reduction, sample efficiency) transfer to cognitive selection. |
| **Tool-using LLM agents**                 | The agent's tool-selection mechanism is a candidate `M`. Adapters wrap reasoning steps, dialogue turns, and external tool calls into the same selection interface. Cross-domain transfer: improvements to selection from observability instrumentation in one domain (e.g. tool calling) transfer to others (e.g. dialogue planning).                        |
| **RL agents**                             | The action head is `M`. Domain adapters: motor action wrap, dialogue action wrap, planning-step wrap. Lesion test: disabling the action head should degrade all domains comparably.                                                                                                                                                                          |
| **Multi-task transformer architectures**  | The shared encoder is `M`; task-specific heads are adapters. The audit-reuse check on parameter overlap is critical — many "shared encoder" architectures branch heavily on task identity, undermining the reuse claim.                                                                                                                                      |
| **Cognitive architectures** (ACT-R, Soar) | The procedural-memory firing mechanism is `M`. Adapters wrap motor production rules, cognitive production rules, and goal-management production rules into the same firing interface.                                                                                                                                                                        |

## Performance and cost considerations

- **Adapter overhead.** Per-domain adapters add I/O cost. For tight-loop deployments, this overhead may be non-trivial; design adapters as zero-copy where possible.
- **Domain-leakage risk.** Naive adapters can leak domain-specific structure into `M_Input` such that `M` ends up branching on domain identity. The audit-reuse infrastructure exists specifically to catch this.
- **Substrate maturity prerequisite.** Exaptation pays only when the source mechanism is well-developed. For early-stage AI deployments where the candidate `M` is itself immature, specialise first; redeploy only when `M` is mature.
- **Cross-domain transfer of improvements.** This is the primary architectural payoff. Track it explicitly: when training on domain Aᵢ, measure performance on Aⱼ. If transfer is consistently zero, `M` is effectively domain-specific.

## Interaction with the collection

This NEXI is the **generative-reuse layer** of the [`embodied-action-selection`](../../../collections/embodied-action-selection/) collection. It composes with:

- [`action-selection-as-common-substrate`](../../action-selection-as-common-substrate/) — the substrate-invariant selection mechanism is the canonical candidate for `M`. Exaptation is _how_ the same selection module handles motor and cognitive domains; action-selection is _what_ it does.
- [`ecological-context-model`](../../ecological-context-model/) — the formalism's domain-agnostic typing of `B` (motor or cognitive) is what makes exaptive reuse feasible. Without the formalism, `M_Input` and `M_Output` types are ad-hoc; with it, they are the formal terms `Br`, `Ba(g, P)`, and `B`.
- [`heuristics-as-habits-fusion`](../../heuristics-as-habits-fusion/) — the specific behavioural-instance NEXI that demonstrates this NEXI's claim. Heuristic decision-making and motor habit formation share the same `M` (action selection) via different adapters (cognitive vs. motor).
