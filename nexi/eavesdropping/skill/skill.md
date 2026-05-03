# Skill: Eavesdropping (framework-neutral)

A drop-in agent skill that adds eavesdropping behaviour to an LLM-based agent. This spec is **framework-neutral** — see translation notes at the bottom for mapping it to specific stacks (Claude skills, OpenAI function calling, MCP tools, LangChain / LlamaIndex agents).

---

## System-prompt fragment

Insert this into the system or developer prompt of any agent that should eavesdrop:

```
You are operating in a multi-agent environment. In addition to messages
addressed to you, you have access to messages exchanged between other
agents that occur within your observation range. Treat these *observed
third-party interactions* as evidence about the participants — their
goals, knowledge, capabilities, and relationships.

Use the `get_observed_interactions` tool to retrieve recent third-party
messages you witnessed. When forming a model of another agent, prefer
evidence from their observed interactions with others over direct
experience with you, when both are available — direct interactions can
be deliberately framed; observed interactions are less filtered.

Do not act on observed interactions as if they were addressed to you.
They inform your beliefs; they do not invite a reply.
```

---

## Tool specifications (framework-neutral)

```yaml
tools:
  - name: get_observed_interactions
    description: |
      Retrieves messages exchanged between other agents that this agent
      witnessed within the specified time window.
    parameters:
      time_window:
        type: object
        required: true
        description: Time range to query.
        schema:
          start: timestamp
          end: timestamp
      participants_filter:
        type: array
        required: false
        description: |
          If provided, return only interactions involving any of these
          agent IDs (as sender or recipient).
        items: { type: string }
    returns:
      type: array
      items:
        type: object
        properties:
          sender: string
          recipients: [string]
          content: string
          timestamp: timestamp
          context: string

  - name: update_belief_about_agent
    description: |
      Records an updated belief about a specific agent based on observed
      evidence. Use when inferring something about a peer from their
      observed third-party interactions.
    parameters:
      agent_id:
        type: string
        required: true
      belief:
        type: string
        required: true
        description: Free-form description of the updated belief.
      evidence_source:
        type: string
        required: true
        description: |
          Reference to the observed interactions that grounded this
          belief (e.g. message IDs or a time window).
```

---

## Memory pattern

Observed interactions should persist in a retrievable memory store with a discriminator field (e.g. `kind: "observed_interaction"`) separate from direct messages. This allows the agent to:

- Surface observed interactions selectively at retrieval time.
- Compare its own model of another agent against the observed evidence.
- Detect inconsistencies between an agent's direct presentation and its observed behaviour.

A reasonable default schema:

```yaml
memory_entry:
  id: string
  kind: 'observed_interaction'
  observed_at: timestamp
  sender: string # the agent we eavesdropped on
  recipients: [string] # who they were talking to
  content_summary: string # condensed; do not store full payloads at scale
  raw_content_ref: string? # optional pointer to full payload
  belief_updates: [string] # references to update_belief_about_agent calls
```

---

## Translation notes

| Target stack                     | How to translate                                                                                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude skills (Anthropic)**    | The system-prompt fragment becomes the skill's instructions. The two tools become MCP tools the skill exposes.                                                                                                |
| **OpenAI function calling**      | Tools translate directly to function-calling specs. The system-prompt fragment goes in the `system` message.                                                                                                  |
| **MCP (Model Context Protocol)** | Define an MCP server that exposes `get_observed_interactions` as a tool and the observed-interaction memory store as an MCP resource.                                                                         |
| **LangChain / LlamaIndex**       | Wrap the tools as `BaseTool` subclasses; insert the system-prompt fragment into the agent's prompt template. The observed-interactions memory becomes a separately-namespaced vector store or document store. |
| **Custom agent loop**            | Implement the perception step pseudocode from [`../architecture/overview.md`](../architecture/overview.md).                                                                                                   |

---

## Examples

Working examples in popular stacks will be added under [`examples/`](examples/) as the catalog matures. For now this skill spec is reference-grade; concrete implementations are an open invitation.
