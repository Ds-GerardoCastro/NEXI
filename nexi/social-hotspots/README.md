# Social Hotspots

> **NEXI status:** draft · **Formats available:** architecture, skill · **Audience:** builder
>
> **Member of collection:** [Distributed Social Cognition](../../collections/distributed-social-cognition/)
>
> _Information density concentrates at the locations (or virtual loci) where agents converge. Architectures that explicitly model these hotspots and weight by spatial-or-virtual proximity outperform uniform-attention baselines on spatially structured tasks._

---

## At a glance

In multi-agent settings with shared environments, information is **not uniformly distributed**. It collects at the places where bodies (or processes) converge — what biologists call **social hotspots**. A multi-agent system that treats all locations and all peers as equivalently informative ignores a structural property of its world.

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
- A set of functions the source paper frames tentatively (not an established bundle): hotspots **may** support foraging information and condition signalling directly, and — following the secondary literature the paper cites, rather than as direct findings of the finch study — **could** also aid predation dilution and breeding synchronisation.

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

The pattern connects to **collective behaviour in animal-communication ecology** (information centre hypothesis; Ward & Zahavi 1973), to **swarm robotics** (where agent-density is a first-class signal), and to **distributed cognition** more broadly (Hutchins 1995). The wild zebra finch study (Hagedoorn et al. 2025) documents hotspots as structured information hubs rather than anonymous aggregations; comparative, cross-species support that convergence-plus-colony-sound is functional comes from colonial seabirds (Waas et al. 2000, royal penguins) — an analog, not evidence in zebra finches.

Computational analogs:

- **Spatial attention mechanisms** in vision and robotics — weight inputs by spatial proximity to a query.
- **Multi-agent retrieval** — inverse-distance-weighted neighbour aggregation.
- **Topic clustering and trending detection** — the virtual-space analog of hotspot detection.

Full citations: [`references.md`](references.md).

### Relation to existing methods

This pattern's weighting mechanism overlaps substantially with **Prioritized Experience Replay** (PER; Schaul et al. 2016) combined with spatial attention and a density-clustering backend such as DBSCAN. Like PER, it weights stored experience non-uniformly by a salience signal rather than sampling uniformly, and it should not be read as a novel idea in isolation. The residual novelty is threefold: (1) the weighting is keyed to **shared cross-agent loci** — hotspots visible to the whole population — whereas PER prioritises a single agent's own replay buffer; (2) **density-of-convergence is promoted to a first-class signal** the architecture detects and maintains, not merely a byproduct of TD-error; and (3) the mechanism carries a **virtual/topical analog** (topic-clusters, channels) that extends it beyond physical space. Absent these, the pattern would reduce to re-labelled PER.

---

## Falsifiable hypothesis

> **H_hotspot.** Multi-agent systems with location-keyed memory and proximity-weighted retrieval outperform agents with uniform memory access on tasks where the distribution of relevant information is spatially structured, at equal training compute.
>
> **Operationalisation (pre-registered, compute-matched).** On the DeepMind Melting Pot 2.0 cooperative-foraging substrates **"Coins"** and **"Clean Up"** (fixed evaluation scenarios), hotspot-aware agents should reach the uniform-memory baseline's final mean episode return in **≥10% fewer training episodes**, at equal wall-clock compute and identical network capacity.
>
> **Refutation.** If uniform-memory baselines match or beat hotspot-aware agents on these Melting Pot substrates at equal compute — i.e. the ≥10% episode-efficiency gain does not appear — this pattern's claim is refuted.

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
