# Social Hotspots

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Member of collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
>
> _Information density concentrates at the locations (or virtual loci) where agents converge. Architectures that explicitly model these hotspots and weight by spatial-or-virtual proximity outperform uniform-attention baselines on spatially structured tasks._

---

## At a glance

In multi-agent settings with shared environments, information is **not uniformly distributed**. It collections at the places where bodies (or processes) converge — what biologists call **social hotspots**. A multi-agent system that treats all locations and all peers as equivalently informative ignores a structural property of its world.

| Question          | Short answer                                                                                                      |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Use this when** | Multi-agent setting with spatial or topical structure; information distribution is non-uniform.                   |
| **Skip it when**  | Single-agent, no spatial / topical structure, uniform information distribution, or privacy-sensitive convergence. |
| **What it adds**  | Spatial memory; proximity-weighted retrieval; hotspot detection.                                                  |
| **What it costs** | Spatial state to maintain; proximity queries more expensive than uniform retrievals.                              |

---

## The natural exemplar

Wild zebra finch **social hotspots** in the arid zone are not anonymous gathering points but **structured information hubs**. The source paper documents that they are characterised by:

- Repeated encounters between specific individuals (not strangers passing through).
- Mix of known and unknown individuals — both familiar peers and new arrivals.
- A bundle of co-occurring functions: foraging information, predation dilution, breeding synchronisation, condition signalling.

The architectural lesson: **convergence in space is itself information**. Where bodies aggregate, observations multiply, and the eavesdropping pattern becomes empirically valuable rather than incidental.

---

## The pattern

```
                    Environment
       ┌─────────────────────────────────────┐
       │                                     │
       │     ●               ●●●●            │
       │  ● ●●               ●●●●●           │   ← hotspot:
       │   ●                  ●●●            │     high agent density,
       │                                     │     repeated encounters
       │     ●                ●               │
       │                                     │
       │   ● low-density area                │
       │                                     │
       └─────────────────────────────────────┘
                       ▲                 ▲
                       │                 │
            uniform attention      hotspot-aware
            misses concentration   attention weights by
            of info                proximity to hotspot
```

The architectural commitment: **memory and retrieval are keyed by location** (or virtual analog like topic-cluster), and queries are weighted by proximity. The agent attends more to observations from high-density loci.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md).

- **Spatial memory** keyed by location / virtual locus.
- **Proximity-weighted retrieval** — agents query memory weighted by their current location.
- **Hotspot detector** — identifies and maintains a set of currently-active hotspots from agent-position observations.

## Skill specification

See [`skill/skill.md`](skill/skill.md).

- **System-prompt fragment** instructs the agent to attend more to observations from current-or-known hotspots.
- **Tool** `query_spatial_memory(location, radius)` retrieves observations weighted by proximity.
- **Tool** `current_hotspots()` returns the active hotspots the agent is aware of.

---

## When to use it

- ✅ Multi-agent systems in spatial environments (robotics, simulation, embodied agents).
- ✅ Virtual environments with topical structure (forum threads, conversation rooms, code-review channels) — the "spatial" analog.
- ✅ Tasks where information distribution is non-uniform (foraging, market-making, social inference under partial observability).
- ✅ Settings where convergence-to-density is itself a feature signal (swarm robotics, crowd-density inference).

## When not to use it

- ❌ Single-agent systems.
- ❌ Environments without spatial or topical structure (i.i.d. data, fully shuffled streams).
- ❌ Privacy-sensitive contexts where revealing convergence is a leak.

---

## Theoretical background & evidence

The pattern connects to **collective behaviour in animal-communication ecology** (information centre hypothesis; Ward & Zahavi 1973), to **swarm robotics** (where agent-density is a first-class signal), and to **distributed cognition** more broadly (Hutchins 1995). The zebra finch literature (Hagedoorn et al. 2026; Waas et al. 2005) provides direct empirical evidence that hotspots are structured information hubs, not anonymous aggregations.

Computational analogs:

- **Spatial attention mechanisms** in vision and robotics — weight inputs by spatial proximity to a query.
- **Multi-agent retrieval** — inverse-distance-weighted neighbour aggregation.
- **Topic clustering and trending detection** — the virtual-space analog of hotspot detection.

Full citations: [`references.md`](references.md).

---

## Falsifiable hypothesis

> **H_hotspot.** Multi-agent systems with location-keyed memory and proximity-weighted retrieval outperform agents with uniform memory access on tasks where the distribution of relevant information is spatially structured, at equal training compute.
>
> **Operationalisation.** On benchmarks of multi-agent navigation, foraging-with-information-sharing, and crowd-density inference, hotspot-aware agents should reach target performance in ≥10% fewer training episodes.
>
> **Refutation.** If uniform-memory baselines match hotspot-aware agents on spatially structured tasks at equal compute, this pattern's claim is refuted.

---

## Tradeoffs

- **Storage and retrieval cost.** Spatial memory + proximity queries cost more than uniform retrievals.
- **Detector noise.** Hotspot detection can yield false positives in sparse / noisy environments. Calibrate.
- **Privacy.** Convergence patterns reveal information about agents (where they go, what they care about). In sensitive deployments, hotspots can become an attack surface.

## Boundary conditions

This NEXI specifies _spatial information aggregation_. It does not specify what to _do_ with the aggregated information — that depends on downstream patterns (eavesdropping, identity-by-pattern). Hotspots are where the collection operates most efficiently; they do not by themselves constitute social inference.

---

## Related

- **Collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
- **Co-dependent NEXIs:** [`eavesdropping`](../eavesdropping/), [`identity-by-pattern`](../identity-by-pattern/), [`multi-modal-integration`](../multi-modal-integration/), [`context-bound-semantics`](../context-bound-semantics/)
- **Vault provenance (private):** principle `P10 — Social Hotspots as Information Hubs`; metamodel `MM1 — Distributed Information Substrate`.
- **References:** [`references.md`](references.md)
