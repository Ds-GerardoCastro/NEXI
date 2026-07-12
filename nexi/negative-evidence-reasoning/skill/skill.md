# Skill: Negative-Evidence Reasoning (framework-neutral)

A drop-in agent skill that adds reasoning-from-absence and negation handling to an LLM-based agent. Framework-neutral spec; translation notes at the bottom.

---

## System-prompt fragment

```
You operate in environments where the most important observation is
often the one that is missing — the expected signal that did not
arrive, the step that was skipped, the finding that is absent. When
interpreting a situation:

1. Form explicit expectations. Before reading the observations, ask:
   given this context, what signals *should* be present? Name them.
2. Diff expectations against reality. Use the `check_for_absences`
   tool to find expected-but-missing signals and unexpected-present
   signals. Treat a confidently missing signal as evidence, not as a
   gap in your perception. The absence of an expected signal can be as
   informative as the presence of an unexpected one.
3. Handle negation as truth-reversing. "X is not true", "not
   permitted", "no Y observed" REVERSE the claim — they are not near-
   synonyms of the un-negated statement. Never let a "not" quietly
   collapse into the affirmative.
4. Do not fabricate absences. Only treat a signal as meaningfully
   missing if it was genuinely expected here AND the channel that would
   carry it was actually observed. If you did not look, "not observed"
   is not "absent" — say so instead of inventing meaning.

When you report a conclusion, state which absences (if any) it rests on
and how confident you are that each is a true absence rather than an
unobserved one.
```

---

## Tool specifications

```yaml
tools:
  - name: check_for_absences
    description: |
      Given the current context and the signals actually observed,
      return the signals that were expected but are missing, the
      signals present that were not expected, and an interpretation of
      what the confidently-missing signals imply. Absences are
      first-class evidence. Only signals whose expected-presence
      probability clears the calibrated threshold are returned as
      missing; gaps below threshold, or on unmonitored channels, are
      withheld rather than over-interpreted.
    parameters:
      expected_signals:
        type: array
        required: true
        description: |
          The signals that should be present in this context, each
          optionally with an expected-presence probability. If omitted,
          the tool derives them from context.
        items:
          type: object
          properties:
            signal: string
            p_present: number # optional; calibrated expected-presence probability
      actual_observations:
        type: array
        required: true
        description: The signals actually observed.
    returns:
      type: object
      properties:
        missing:
          type: array
          items:
            type: object
            properties:
              expected_signal: string
              implication_of_absence: string
              confidence: number # confidence this is a true absence, not unobserved
        unexpected:
          type: array
          description: Signals present that were not expected in this context.
        interpretation:
          type: string # what the confidently-missing signals mean, taken together
```

---

## Memory pattern

Reasoning-from-absence benefits from a memory of _which absences were diagnostic in past contexts_ — so the agent learns which gaps matter and which are noise. Suggested record:

```yaml
absence_record:
  context_signature: string # fingerprint of the context
  expected_signal: string
  was_absent: boolean
  interpreted_as: string
  outcome: string? # whether the absence-based inference was confirmed
```

Querying by `(context_signature, expected_signal)` lets the agent recall whether a given absence has proven informative before — a structured way to tune, from experience, which missing signals to trust and to keep the expectation set calibrated.

---

## Translation notes

| Target stack                     | How to translate                                                                                                                                                                       |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude / OpenAI agent stacks** | The system-prompt fragment guides reasoning; `check_for_absences` is wrapped as a function-call / MCP tool. Negation handling lives in the prompt rule.                                |
| **MCP**                          | Define an MCP server exposing `check_for_absences`, backed by the expectation model, with the absence memory as a resource.                                                            |
| **LangChain / LlamaIndex**       | Wrap `check_for_absences` as a `BaseTool`; add the prompt fragment to the agent template; back the absence memory with a context-keyed retriever.                                      |
| **Anomaly / monitoring stacks**  | The expectation model is the normal-behaviour baseline; `check_for_absences` runs continuously and emits alerts on confidently-missing signals (missing heartbeats, absent log lines). |
| **Multi-agent RL**               | Expected observations come from the world model; a confidently-missing expected observation emits an auxiliary prediction-error signal into the policy/value head.                     |
