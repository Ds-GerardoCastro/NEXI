# Skill: Multi-Modal Integration (framework-neutral)

A drop-in agent skill that exposes joint multi-modal observations to an LLM-based agent. Framework-neutral; translation notes at the bottom.

---

## System-prompt fragment

```
You are operating in an environment with multiple information channels —
text messages, structured data, sensory observations, spatial signals,
or others. When forming beliefs about the world, treat observations
across these channels as views onto a single underlying state, not as
parallel independent inputs. When two channels confirm each other, the
joint signal is stronger than either alone; when they conflict, that
contradiction is itself information about the world or about your
sensors.

Use the `get_cross_modal_observations` tool to retrieve aligned
multi-channel observations for a given time window. Reason explicitly
about whether the channels confirm or contradict each other, and what
that implies.

Do not silently average or override one channel with another. Surface
the alignment (or its absence) in your reasoning.
```

---

## Tool specifications

```yaml
tools:
  - name: get_cross_modal_observations
    description: |
      Returns observations across multiple channels for a given time
      window, aligned where possible. Each result tuple contains
      contemporaneous observations from each requested modality.
    parameters:
      time_window:
        type: object
        required: true
        schema:
          start: timestamp
          end: timestamp
      modalities:
        type: array
        required: true
        items: { type: string }
        description: List of modality names to retrieve (e.g. ["audio", "spatial"]).
      alignment:
        type: string
        required: false
        default: 'strict'
        enum: ['strict', 'loose']
        description: |
          strict: only return tuples where all requested modalities have
          contemporaneous observations.
          loose: return tuples even if some modalities are missing for
          that timestamp; missing channels are null.
    returns:
      type: array
      items:
        type: object
        properties:
          timestamp: timestamp
          observations: object # keys are modality names, values are observations
          alignment_quality: number # 0.0 to 1.0

  - name: check_cross_modal_consistency
    description: |
      Given two or more observations across modalities, returns a
      consistency score and an explanation if the channels conflict.
      Use this when you suspect channels disagree about the world.
    parameters:
      observations:
        type: object
        required: true
        description: Map of modality -> observation.
    returns:
      type: object
      properties:
        consistent: boolean
        score: number
        conflict_summary: string # natural-language explanation if inconsistent
```

---

## Memory pattern

Multi-modal observations should be stored with explicit modality tagging and timestamp alignment metadata, so cross-channel queries are efficient:

```yaml
observation_record:
  timestamp: timestamp
  modality: string
  observation: object
  alignment_id: string? # shared id for tuples that are paired across modalities
  joint_embedding: vector? # optional shared-latent embedding if the system supports one
```

When the system can compute joint embeddings, store them as well — they enable retrieval by _concept_ rather than by _modality_.

---

## Translation notes

| Target stack                     | How to translate                                                                                                                                                                                                              |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude / OpenAI agent stacks** | Pre-process multi-modal inputs into a shared embedding space (CLIP, ImageBind, or custom) before invoking the agent; the agent reasons over the joint embedding. The tools above retrieve from a multi-modal observation log. |
| **MCP**                          | Expose `get_cross_modal_observations` as an MCP tool backed by a multi-modal observation server.                                                                                                                              |
| **LangChain / LlamaIndex**       | The observation memory becomes a multi-modal vector store; the joint embedding is the index key.                                                                                                                              |
| **Robotics / RL**                | Replace late-fusion observation processing with a joint encoder upstream of the policy network.                                                                                                                               |
