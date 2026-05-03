# Skill: Context-Bound Semantics (framework-neutral)

A drop-in agent skill that adds context-conditional interpretation and negative-evidence reasoning to an LLM-based agent.

---

## System-prompt fragment

```
You operate in environments where the same signal can mean different
things depending on context. When interpreting a message, observation,
or signal:

1. Identify the relevant context — where you are, who's involved, what
   role this signal plays in the current setting.
2. Interpret the signal *conditionally* on that context. Do not collapse
   to its most-frequent meaning if context suggests otherwise.
3. Reason about what is *not* there. Use the `check_for_absences` tool
   to identify expected signals that are missing. Absences are
   diagnostic information, not gaps in your perception.

When reporting your interpretation, surface the context you used and
flag if the signal would have a different meaning in another context
that's plausible here. Do not silently commit to one interpretation
when several are plausible across contexts.
```

---

## Tool specifications

```yaml
tools:
  - name: interpret_signal
    description: |
      Interpret a signal conditional on the current context. Returns
      the most likely meaning along with alternative interpretations
      that would be valid in adjacent contexts.
    parameters:
      signal:
        type: object
        required: true
        description: The signal to interpret (text, message, observation).
      context:
        type: object
        required: true
        description: Current state — location, participants, role, time, recent history.
    returns:
      type: object
      properties:
        meaning: string
        confidence: number
        context_used: object
        alternative_meanings: array # interpretations valid in adjacent contexts

  - name: check_for_absences
    description: |
      Given the current context, returns the set of signals or
      observations that would be expected but are not present.
      Absences are themselves diagnostic.
    parameters:
      context:
        type: object
        required: true
      observed_signals:
        type: array
        required: true
        description: List of signals actually observed.
    returns:
      type: object
      properties:
        missing_expected:
          type: array
          items:
            type: object
            properties:
              expected_signal: string
              implication_of_absence: string
              confidence: number
        unexpected_present:
          type: array
          description: Signals present that are not normally expected in this context.

  - name: list_context_alternatives
    description: |
      Given a signal whose meaning depends on context, returns the
      interpretations that would apply in the most likely alternative
      contexts. Useful when the agent is uncertain about the current
      context.
    parameters:
      signal:
        type: object
        required: true
      candidate_contexts:
        type: array
        items: { type: object }
    returns:
      type: array
      items:
        type: object
        properties:
          context: object
          meaning: string
          confidence: number
```

---

## Memory pattern

Context-conditional interpretation benefits from a memory of _how this signal has been interpreted in past contexts_. Suggested record:

```yaml
interpretation_record:
  signal_signature: string # fingerprint of the signal
  context_at_time: object
  interpretation: string
  confidence: number
  outcome: string? # whether the interpretation was confirmed downstream
```

Querying memory by `(signal_signature, context_similarity)` lets the agent recall how it interpreted similar signals in similar contexts before — a structured form of pragmatic learning.

---

## Translation notes

| Target stack                     | How to translate                                                                                                                                                                          |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude / OpenAI agent stacks** | The system-prompt fragment guides interpretation; tools above are wrapped as function-calls / MCP tools.                                                                                  |
| **MCP**                          | Define an MCP server that exposes `interpret_signal` and `check_for_absences` as tools, with the interpretation memory as a resource.                                                     |
| **LangChain / LlamaIndex**       | Wrap the tools as `BaseTool`; add the prompt fragment to the agent's prompt template; back the interpretation memory with a context-keyed retriever.                                      |
| **Multi-agent RL**               | Context-conditional policy implemented via FiLM modulation on the action head. Negative-evidence module emits an additional reward signal for spotting expected-but-missing observations. |
