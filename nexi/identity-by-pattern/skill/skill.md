# Skill: Identity by Pattern (framework-neutral)

A drop-in agent skill that adds individual-identity tracking to an LLM-based agent. Framework-neutral spec; translation notes at the bottom.

---

## System-prompt fragment

```
You are operating in a multi-agent environment with persistent peers.
When you receive a signal from another agent (a message, a voice clip,
a sensor reading), do not treat the signal as belonging to a generic
class. Use the `identify_agent` tool to recover the specific individual
who produced it. Track each peer over time as a persistent identity,
not as instances of a category.

Individual identification is harder than category recognition; the tool
returns confidence and uncertainty. If confidence is low, treat the
identification as provisional and seek confirmation from other channels
(spatial co-occurrence, context) before binding important beliefs to it.

When no confident match exists, treat the signal as coming from an
"unknown" peer and consider whether to enroll a new identity.
```

---

## Tool specifications

```yaml
tools:
  - name: identify_agent
    description: |
      Given a signal observed from a peer, return the most likely
      individual identity along with calibrated confidence.
    parameters:
      signal:
        type: object
        required: true
        description: The observation to identify (audio clip, message, embedding).
      modality:
        type: string
        required: false
        description: Hint about the signal's modality (audio, text, image).
      threshold:
        type: number
        required: false
        default: 0.7
        description: Confidence threshold below which the result is "unknown".
    returns:
      type: object
      properties:
        identity: string | null
        confidence: number # 0.0 to 1.0
        top_alternatives: array # other candidate identities
        is_known: boolean

  - name: enroll_agent
    description: |
      Register a new individual identity from one or more enrollment
      signals. Use when the agent encounters a peer who is not yet in
      memory and is expected to recur.
    parameters:
      individual_id:
        type: string
        required: true
      signals:
        type: array
        required: true
        items: { type: object }
```

---

## Memory pattern

Identity-keyed memory is separate from observation memory. Each individual gets a record:

```yaml
identity_record:
  individual_id: string
  embeddings: [vector] # one or more enrollment samples
  first_observed: timestamp
  last_observed: timestamp
  observation_count: int
  drift_history: [embedding_change_event]
  beliefs: ref # link to belief store keyed by this individual
```

When an identification succeeds, the agent updates `last_observed` and `observation_count`, and writes any new beliefs into the linked belief store (the eavesdropping pattern's observed-interaction memory typically lives here).

---

## Translation notes

| Target stack                  | How to translate                                                                                                 |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Claude skills (Anthropic)** | Wrap `identify_agent` and `enroll_agent` as MCP tools. The system-prompt fragment becomes the skill description. |
| **OpenAI function calling**   | Tools translate directly; system-prompt fragment goes in the system message.                                     |
| **MCP**                       | Define an MCP server exposing identification + enrollment + the identity memory as a resource.                   |
| **LangChain / LlamaIndex**    | Wrap tools as `BaseTool`; the identity memory becomes a separate vector store.                                   |
| **Robotics / RL**             | Use the encoder directly inside the perception stack; identity embeddings become part of the agent's state.      |
