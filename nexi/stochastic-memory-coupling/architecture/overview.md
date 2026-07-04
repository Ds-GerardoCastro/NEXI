# Architecture: Stochastic-Memory Coupling

This document specifies the architectural primitive for the stochastic-memory-coupling pattern — components, interfaces, data flow, and integration notes.

## Components

### 1. Discrete state space

The system has explicit qualitatively-different behavioural states (not a continuous parameter space). States are _named_: each has an identifier, a characterising behavioural-output policy, and an outcome-history slot.

```
states: list[State]
state.id, state.policy, state.history
```

Design-time decision: how many states, what each state's policy is. Runtime: the system is in exactly one state at any time.

### 2. Stochastic transition policy

Random transitions between states with a controllable temperature parameter. The transition probability from state s_i to state s_j is biased by the persistent-memory layer:

```
P(s_i → s_j) ∝ exp(β · memory_score(s_j)) · transition_kernel(s_i, s_j)
```

Where `memory_score(s_j)` is the persistent memory's estimate of state s_j's accumulated benefit, and `β` is an inverse-temperature parameter (high β → more memory-biased; low β → more uniform exploration).

### 3. Persistent state-memory store

Records outcomes of past state visits. Two roles:

- **Accumulator:** updates `memory_score(s)` based on outcomes observed when the system was in state `s`.
- **Bias source:** provides the score to the transition policy at decision time.

```
memory.record_outcome(state_id, outcome)
memory.score(state_id) -> float
memory.decay()  # optional time-based decay
```

The memory must integrate **multiple stimuli** at the decision moment — the iron-based signal-transduction analog. Each state's score is a function of multiple input streams, not a single reward channel.

## Data flow

```
   Outcome o ──► memory.record_outcome(current_state, o)
                       │
                       ▼
              memory_score(s) for all s
                       │
                       ▼
   Stochastic policy ──► P(next_state | current_state, memory_scores)
                       │
                       ▼
              Sampled next_state
                       │
                       ▼
              Transition: state := next_state
                       │
                       ▼
              Apply state.policy to produce action / behavioural output
```

## Pseudocode — runtime decision step

```python
def decision_step(state, memory, observations):
    # Apply current state's policy to get action
    action = state.policy(observations)

    # Execute action; observe outcome
    outcome = environment.step(action)

    # Record outcome in persistent memory
    memory.record_outcome(state.id, outcome)

    # Optionally decay memory (time-based forgetting)
    memory.decay(now)

    # Sample next state — stochastic, biased by memory
    transition_logits = {
        s.id: math.log(transition_kernel(state, s)) + BETA * memory.score(s.id)
        for s in state_space
    }
    next_state_id = stochastic_sample(transition_logits)

    return next_state_id, action, outcome
```

## Two failure modes the architecture must avoid

- **Memory domination** (β too high): all transitions become deterministic toward the historically-best state. Exploration eliminated. Detection: monitor entropy of transition distribution; if it collapses, raise `β` cap or temperature floor.
- **Stochasticity domination** (β too low): memory has insufficient weight; transitions stay uniformly random. Detection: monitor whether memory_score correlates with future outcomes; if not, raise `β`.

The architecture must include a **balance monitor** that adjusts `β` (or other coupling parameters) at runtime to keep both components active. This balance monitor is a natural place for the [`meta-regulation`](../../meta-regulation/) NEXI's meta-regulator to operate.

## Integration notes

| Stack                                 | How to integrate                                                                                                                                                                                         |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Reinforcement learning**            | The state space + memory store maps to options frameworks (Sutton, Precup, Singh 1999) but with explicit stochastic-memory coupling rather than separate exploration and value estimation.               |
| **LLM agent frameworks**              | States = behavioural modes (e.g. `gathering-info`, `proposing`, `verifying`, `committing`). Memory = persistent task-outcome store. Coupling = bias the agent's mode-transition prompt by memory scores. |
| **Multi-agent populations**           | Each agent maintains its own (state, memory). The coupling produces population-level diversity ([[clone-individuality\|P36]]) — same agent template, divergent trajectories.                             |
| **Production ML with online updates** | Memory = feature-importance estimates updated by online feedback. Stochastic transition = policy randomisation between feature-set configurations.                                                       |

## Interaction with the collection

This NEXI is the **exploration-with-retention layer** of the [`acerebrate-decision-making`](../../../collections/acerebrate-decision-making/) collection. It composes with:

- [`coincidence-detection-gating`](../../coincidence-detection-gating/) — the coincidence-gate decides which proposed stochastic transitions actually commit.
- [`meta-regulation`](../../meta-regulation/) — the meta-regulator dynamically adjusts the coupling parameter `β` and the memory's decay rate in response to deployment conditions.
