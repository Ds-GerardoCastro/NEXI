# Architecture: Eavesdropping

This document specifies the architectural primitive for the eavesdropping pattern — components, interfaces, data flow, and integration notes for both LLM-agent and reinforcement-learning settings.

## Components

### 1. Observation bus

A shared message channel that every agent subscribes to. Each message carries metadata about its sender, intended recipients, and the agents that can witness it under the visibility policy.

```
Message {
  id:         string
  sender:     AgentID
  recipients: [AgentID]   # explicit addressees
  observers:  [AgentID]   # agents that can witness, per visibility policy
  payload:    <agent-defined>
  timestamp:  int
}
```

### 2. Visibility policy

A pure function `visible_to(message, agent) -> bool` that determines whether `agent` can observe `message`. Common implementations:

- **Broadcast** — every agent observes every message. Simplest; expensive at scale.
- **Proximity-based** — agents observe messages within a spatial radius. Closest to the zebra-finch case; suits robotics and embodied multi-agent settings.
- **Role-based** — agents observe messages within their group, role, or organisational unit. Suits enterprise multi-agent stacks.
- **Stochastic** — observability is probabilistic, controlled by a parameter. Useful for noisy / partial-observability research.

Visibility policies are pluggable; the rest of the architecture does not depend on which policy is in effect.

### 3. Belief updater

A function the agent invokes when it observes a third-party message:

```
update_beliefs(observer_agent, observed_message) -> ()
  # Updates observer_agent's internal model of message.sender and
  # message.recipients based on the content of message.payload.
```

For LLM-based agents, the belief updater is typically a memory write at perception time and an attention-time read at response time. For RL agents, it is a representation update — either explicit (additional input channel) or implicit (augmented observation embedding).

---

## Data flow

```
                       ┌──────────────────────┐
   [Agent A: sender] ──→  Observation Bus      │
                       │  + visibility policy  │
                       └──────────────────────┘
                          │              │
                  to recipient        to observers
                          ↓              ↓
                [Agent B: receiver]  [Agent C: observer]
                                          │
                                          ↓
                                update_beliefs(C, msg)
```

---

## Pseudocode — LLM-agent flavour

Each agent's perception step:

```python
def perceive(agent, bus, t):
    incoming = bus.deliver(agent, t)        # messages addressed to agent
    observed = bus.observable(agent, t)     # messages agent can eavesdrop on

    for msg in incoming:
        agent.handle_direct_message(msg)

    for msg in observed:
        if msg.sender != agent.id and agent.id not in msg.recipients:
            agent.memory.append({
                "kind":       "observed_interaction",
                "sender":     msg.sender,
                "recipients": msg.recipients,
                "content":    msg.payload,
                "timestamp":  msg.timestamp,
            })
            agent.beliefs.update_about(msg.sender, msg.payload)
            for r in msg.recipients:
                agent.beliefs.update_about(r, msg.payload)
```

At response time, the agent retrieves both direct and observed interactions from memory, with the discriminator field allowing the prompt template to surface them as separate sections.

## Pseudocode — RL-agent flavour

In a multi-agent RL setup with shared observability:

```python
class EavesdroppingObservationWrapper(gym.Wrapper):
    """Augments each agent's observation with witnessed third-party transitions."""

    def step(self, action):
        obs, reward, done, info = self.env.step(action)
        for agent_id in self.agents:
            obs[agent_id]["eavesdropped"] = [
                t for t in info["all_transitions"]
                if visible_to(t, agent_id) and t["actor"] != agent_id
            ]
        return obs, reward, done, info
```

The agent's policy network receives the eavesdropped transitions as an additional input channel. Encode them with a separate encoder (often a transformer or graph attention) before fusing into the main state representation.

---

## Integration notes

| Stack                               | How to integrate                                                                                                                                                                         |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **LangChain / LlamaIndex**          | Add observed messages to each agent's memory store with a `kind` discriminator. Surface them at retrieval time alongside direct messages, distinguishing the two in the prompt template. |
| **MCP (Model Context Protocol)**    | Expose `get_observed_interactions` as an MCP tool; the eavesdropping stream lives in an MCP server.                                                                                      |
| **OpenAI / Anthropic agent stacks** | Define a function-calling tool for the eavesdropping stream; pass observed interactions in the system or developer message under a labelled section.                                     |
| **PettingZoo / OpenSpiel (RL)**     | Wrap the environment to expose third-party transitions in each agent's observation dict.                                                                                                 |
| **Robotics**                        | Implement visibility as proximity; messages decay with distance. Use ROS topics or equivalent pub-sub.                                                                                   |

---

## Performance considerations

- **Compute cost** scales roughly as `O(N × M)` where `N` is the population size and `M` is the message rate. With attention-based architectures, this becomes a quadratic blowup unless mitigated by:
  - Sparse attention (top-k observed messages by relevance).
  - Message summarisation (consolidate observed interactions into compressed beliefs).
  - Visibility-policy tightening (proximity-based, role-based filters).
- **Memory cost** grows with retained observation history. For long-running agents, implement periodic summarisation: every N steps, consolidate observed interactions about each peer into a single belief update, then prune the raw history.
- **Latency** is generally not affected at perception time but can be at retrieval time if the observation memory is large. Index observed interactions by participant.

---

## Edge cases and failure modes

- **Observation cycles** — if the bus broadcasts an agent's own messages back to it as "observations", filter them at perception time (`msg.sender != agent.id`).
- **Observed-of-observed** — does Agent C's observation of A↔B itself become observable to D? The reference design says _no_ — only first-order interactions are observable. Higher-order observability is a separate design choice with its own tradeoffs.
- **Stale beliefs** — observed interactions can become outdated. Pair this NEXI with explicit recency-weighting in the belief updater.
- **Adversarial signalling** — observed agents may behave deceptively _because_ they know they are being observed. This is a known failure mode; pair with skepticism heuristics or do not deploy in adversarial settings.
