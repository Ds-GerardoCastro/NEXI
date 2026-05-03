# Skill: Social Hotspots (framework-neutral)

A drop-in agent skill that adds spatial-or-virtual hotspot awareness to a multi-agent system.

---

## System-prompt fragment

```
You operate in an environment with shared structure — physical
locations, virtual rooms, topic-clusters, or other spatial-like loci.
Information is *not* uniformly distributed across this environment.
It concentrates at *hotspots* — places where many agents converge
repeatedly.

When forming beliefs or making decisions:

1. Use the `current_hotspots` tool to know where information is
   currently concentrated.
2. When querying memory, prefer the `query_spatial_memory` tool with
   proximity weighting — observations from your current vicinity (or
   from active hotspots) are typically more informative than those
   from sparse regions.
3. Do not assume uniform information distribution. If your task
   depends on rare or scattered information, hotspots may not help —
   note this explicitly.

Hotspots themselves are signals: their location, persistence, and
membership tell you something about what other agents are doing or
where resources are.
```

---

## Tool specifications

```yaml
tools:
  - name: query_spatial_memory
    description: |
      Retrieve observations from spatial memory, weighted by proximity
      to a query location.
    parameters:
      location:
        type: object
        required: true
        description: |
          The query location. For physical environments, coordinates;
          for virtual environments, an identifier (channel id, topic
          cluster id, etc.).
      radius:
        type: number
        required: true
        description: Maximum distance from the query location to include.
      time_window:
        type: object
        required: false
        description: Restrict to observations within this time range.
      weighting:
        type: string
        required: false
        default: proximity
        enum: [proximity, uniform]
    returns:
      type: array
      items:
        type: object
        properties:
          observation: object
          location: object
          distance: number
          weight: number
          timestamp: timestamp

  - name: current_hotspots
    description: |
      Returns the currently active hotspots known to the system —
      locations of persistently elevated agent / event density.
    parameters:
      time_window:
        type: object
        required: false
        description: |
          Look at hotspots active within this window. Defaults to recent.
      min_density:
        type: number
        required: false
        description: Minimum density threshold for inclusion.
    returns:
      type: array
      items:
        type: object
        properties:
          location: object
          radius: number
          density: number
          persistence: number # how long this hotspot has been active
          known_members: array # individuals frequently observed here

  - name: is_hotspot
    description: |
      Check whether a given location currently qualifies as a hotspot.
    parameters:
      location:
        type: object
        required: true
    returns:
      type: object
      properties:
        is_hotspot: boolean
        confidence: number
        density: number
```

---

## Memory pattern

Spatial memory is a separate store from general-purpose memory:

```yaml
spatial_memory_record:
  observation_id:   string
  location:         object         # spatial coordinates or virtual locus id
  observation:      object         # the actual content
  timestamp:        timestamp
  observer:         string?        # agent that recorded the observation
  participants:     [string]?      # other agents involved
```

Indexing strategy: spatial index (KD-tree, R-tree, geohash) keyed by location for fast proximity queries.

---

## Translation notes

| Target stack                     | How to translate                                                                                                                     |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **LLM agents in virtual spaces** | Map "location" to channel / thread / topic-cluster id. Hotspot detection runs over recent activity counts per channel.               |
| **Robotics / embodied**          | Use real spatial coordinates; spatial index is a KD-tree of recent observation positions.                                            |
| **MCP**                          | Define an MCP server exposing `query_spatial_memory` and `current_hotspots`; the spatial index is internal to the server.            |
| **Multi-agent RL**               | Add spatial memory as a parallel observation channel; the policy network can attend to hotspot-relevant observations preferentially. |
| **Market / foraging**            | "Location" maps to price/resource regions; hotspots indicate high-activity regions.                                                  |
