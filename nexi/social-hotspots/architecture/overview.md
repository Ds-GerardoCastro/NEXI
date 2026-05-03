# Architecture: Social Hotspots

Components, pseudocode, integration notes for spatial information aggregation and hotspot-aware retrieval.

## Components

### 1. Spatial memory

A keyed store mapping locations (or virtual loci) to observations. Locations can be:

- **Geographic coordinates** (robotics, embodied agents).
- **Discretised cells** in a grid.
- **Virtual loci** (forum threads, channels, topic-clusters) — the same architecture applies if the "space" is non-physical.

```
SpatialMemory {
  store(location, observation, timestamp) -> ()
  query(location, radius, time_window) -> [(observation, distance, age)]
  density(location, radius, time_window) -> count
}
```

### 2. Proximity-weighted retrieval

Queries are weighted by inverse distance from the query location:

```
weight(observation, query_location) = f(distance(observation.location, query_location))
```

with `f` typically inverse-square or inverse-Gaussian. The agent's attention or retrieval is biased toward observations from locations close to where it currently is.

### 3. Hotspot detector

A module that maintains the set of currently-active hotspots in the environment by clustering recent observations:

```
HotspotDetector {
  update(recent_observations) -> ()
  current_hotspots() -> [Hotspot]
  is_hotspot(location) -> (bool, confidence)
}
```

A hotspot is a location with persistently elevated density of observation events. Implementations:

- **Spatial clustering** — DBSCAN, kernel-density estimation over recent positions.
- **Temporal persistence threshold** — a cluster becomes a hotspot only after sustained density.
- **Decay** — hotspots fade if density drops; they are not permanent.

---

## Pseudocode

```python
class HotspotAwareMemory:
    def __init__(self, spatial_memory, detector):
        self.memory = spatial_memory
        self.detector = detector

    def observe(self, location, observation, t):
        self.memory.store(location, observation, t)
        self.detector.update([(location, t)])

    def query(self, location, radius, time_window, weighting="proximity"):
        results = self.memory.query(location, radius, time_window)
        if weighting == "proximity":
            return self._proximity_weight(location, results)
        return results

    def attention_focus(self, current_location):
        # If we're in or near a hotspot, attend more to its observations
        for hotspot in self.detector.current_hotspots():
            if dist(current_location, hotspot.location) < hotspot.radius:
                return self.memory.query(
                    hotspot.location, hotspot.radius,
                    time_window=recent
                )
        return []  # not in a hotspot, default attention applies

    def _proximity_weight(self, query_loc, observations):
        return [
            (obs, weight=1.0 / (1.0 + dist(query_loc, obs.location)**2))
            for obs in observations
        ]
```

---

## Integration notes

| Stack                               | How to integrate                                                                                                                         |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Robotics / embodied multi-agent** | Each agent maintains a local spatial memory; the hotspot detector runs over recent perceived positions (own + other agents).             |
| **LLM agents in virtual spaces**    | Map "location" to thread / channel / topic. The hotspot detector finds active topic-clusters; queries are weighted by topical proximity. |
| **Multi-agent RL**                  | Add a spatial memory module as part of the observation; policy network can attend to hotspot-relevant observations preferentially.       |
| **Foraging / market-making**        | Hotspots = high-activity regions of the resource / price space. Agents bias exploration toward hotspots, with explore-exploit tradeoff.  |

---

## Performance considerations

- **Spatial index** (KD-tree, R-tree, or grid hashing) is essential for fast proximity queries; naïve linear scan is O(N) per query.
- **Memory growth** — without pruning, spatial memory grows unbounded. Implement age-based decay or fixed-size sliding windows.
- **Detector latency** — hotspot updates need not run every step; batch over short time windows.

## Edge cases and failure modes

- **False-positive hotspots** in noisy environments — calibrate the persistence threshold.
- **Hotspot drift** — real hotspots can shift location over time; the detector should track this rather than treat each new location as a new hotspot.
- **Privacy / adversarial leakage** — exposing hotspot information reveals where agents converge. In sensitive contexts, the hotspot map itself is sensitive data.
- **Cold start** — early in deployment, the detector has insufficient data to identify hotspots. Default to uniform retrieval until enough density is observed.
