# Architecture: Identity by Pattern

Components, pseudocode, and integration notes for embedding individual identity from sensory signal patterns.

## Components

### 1. Identity encoder

A neural encoder trained with a **within-class discriminability** objective. Input: a sensory signal (audio clip, image, sequence). Output: a fixed-dimensional embedding intended to be uniquely associated with the producing individual.

The choice of training objective is the load-bearing decision, and it is **governed by the enrollment regime** — not a flat menu:

- **Open-world enrollment of unseen identities → triplet / contrastive-instance losses.** When new individuals appear at inference time and were never in the training class set, use metric-learning objectives that shape a distance space rather than a fixed classifier head:
  - **Triplet loss** — given (anchor, positive, negative) tuples, push anchor closer to positive than negative by a margin.
  - **Contrastive-instance losses** — pull together observations known to come from the same individual, push apart observations from different individuals.
- **Closed, labelled enrolled population → ArcFace / CosFace.** When the set of identities is fixed and labelled at train time, angular-margin classification losses give the tightest within-class clustering. They **require a labelled class set at training time** and do not, by construction, generalise to identities unseen at train time — so they suit closed enrollment, not open-world re-id.

> **Disambiguation — two different "instance discrimination".** SimCLR-style **augmentation-instance discrimination** treats different _augmented views of the same input_ as a positive pair; it is a self-supervised _proxy_ objective. That is **not** the same as **identity-instance discrimination**, which must treat genuinely different observations of the same individual (different songs, different sessions, different days) as a positive pair. SimCLR is an analogy that motivates the metric-learning framing — it is not a drop-in identity objective.

### 2. Identity memory

A keyed store mapping individual ID → embedding(s) + metadata.

```
IdentityMemory {
  enroll(individual_id, embedding) -> ()
  match(query_embedding, top_k=5) -> [(individual_id, similarity), ...]
  is_in_distribution(query_embedding, top_p, margin) -> bool   # open-set gate
  forget(individual_id, reason) -> ()    # reason distinguishes the two semantics below
}
```

Backends: vector index (FAISS, ScaNN) for fast similarity search; metadata store for individual-level annotations.

### 3. Calibrated confidence

Every identification returns a **calibrated** confidence, on the same scale as the accept/reject decision. Raw cosine similarity is _not_ a probability and is not comparable across queries, so the pipeline calibrates before it decides:

1. **Cosine similarity** `s = cos(q, c)` between the query embedding and a candidate centroid.
2. **Temperature-scaled logit** `z = (s - b) / T`, where `T` (temperature) and `b` (bias) are fit on a held-out verification set.
3. **Sigmoid** `p = σ(z)` — a calibrated probability that query and candidate are the _same_ individual.

The accept/reject threshold is then applied to the **calibrated** score `p` (e.g. accept if `p >= τ`), never to the raw similarity — otherwise the decision boundary and the reported confidence live on two different scales.

### 4. Open-set recognition (imposter rejection)

Deciding _which_ enrolled identity is closest is a different problem from deciding whether the query belongs to **any** enrolled individual at all. A single similarity threshold cannot do the second job: an imposter (a genuinely unknown individual) can still land above any fixed threshold, so a naive threshold silently accepts it.

Open-set recognition therefore uses a **calibrated out-of-distribution / novelty score**, separate from the closed-set ranking, to gate an explicit `is_known` output:

- Score novelty from the _distribution_ of match evidence, not a single similarity — e.g. the calibrated same-identity probability `p` of the top candidate combined with the margin to the runner-up, or a dedicated OOD score fit on held-out non-enrolled identities.
- If the novelty gate says out-of-distribution, return `is_known = false` and `identity = None` regardless of the closed-set ranking.
- Only when `is_known = true` does the closed-set winner become the returned identity.

This keeps "who is the nearest enrolled identity" (ranking) and "is this anyone we know" (open-set) as two decisions, each with its own calibrated gate.

---

## Pseudocode

```python
import math

class IdentityModule:
    def __init__(self, encoder, memory, temperature, bias):
        self.encoder = encoder          # within-class-discriminative
        self.memory = memory            # keyed by individual ID
        self.T = temperature            # fit on held-out verification set
        self.b = bias                   # decision bias, fit alongside T

    def enroll(self, individual_id, signals):
        for s in signals:
            emb = self.encoder(s)
            self.memory.enroll(individual_id, emb)

    def _calibrate(self, similarity):
        # raw cosine similarity -> temperature-scaled logit -> probability
        z = (similarity - self.b) / self.T
        return 1.0 / (1.0 + math.exp(-z))     # calibrated P(same individual)

    def identify(self, signal, threshold=0.5):
        emb = self.encoder(signal)
        matches = self.memory.match(emb, top_k=5)          # ranked by raw similarity
        if not matches:
            return {"identity": None, "confidence": 0.0,
                    "top_alternatives": [], "is_known": False}

        # calibrate every candidate onto a comparable probability scale
        scored = [(m.individual_id, self._calibrate(m.similarity)) for m in matches]
        top_id, top_p = scored[0]
        runner_p = scored[1][1] if len(scored) > 1 else 0.0

        # open-set gate: separate from the accept threshold, rejects imposters
        # even when they rank first. Combines calibrated confidence with the
        # margin to the runner-up (or a dedicated OOD score).
        is_known = self.memory.is_in_distribution(emb, top_p, top_p - runner_p)

        # accept/reject applies to the CALIBRATED score, not raw similarity
        if not is_known or top_p < threshold:
            return {"identity": None, "confidence": top_p,
                    "top_alternatives": scored, "is_known": False}

        return {"identity": top_id, "confidence": top_p,
                "top_alternatives": scored[1:], "is_known": True}
```

---

## Integration notes

| Stack                            | How to integrate                                                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **LLM agent frameworks**         | Wrap as a tool the agent can call when receiving signals from peers. The tool returns identity + confidence.                          |
| **Multi-agent RL**               | Add an identity-embedding head to each agent's observation encoder; expose embeddings as part of the inter-agent observation channel. |
| **Robotics / perception stacks** | Plug in as a separate model alongside the standard category classifier. The two outputs are complementary, not redundant.             |

---

## Performance considerations

- **Embedding dimension** is a tunable: larger preserves more particularity but costs more memory and compute. 128–512 dims is typical.
- **Memory growth** with population: O(N × embeddings_per_individual). Periodic compression (collecting an individual's samples into one centroid) is useful at large scale — but note the trade-off: collapsing samples to a centroid discards **intra-individual variance**, which is exactly the signal that makes re-identification robust to natural variation (different songs, sessions, conditions). Compress for memory only where that variance is not load-bearing, or keep a small variance estimate alongside the centroid.
- **Cold-start** on new individuals requires at least one enrollment signal; few-shot adaptation is a research frontier.

## Edge cases and failure modes

- **Imposter signals** — adversarial or accidental signal collisions. Pair with anomaly detection.
- **Drift** — an individual's signal pattern can change over time (in animals: seasonal vocal change; in agents: model fine-tuning shifts behaviour). Re-enroll periodically.
- **Population scale** — at very large N, the within-class margin shrinks; expect graceful degradation with calibrated uncertainty rather than hard failure.
- **`forget` has two distinct semantics** — do not conflate them. **Privacy / right-to-be-forgotten** is an external, deliberate deletion of a specific individual's records (and must be complete and auditable). **Drift eviction** is an internal maintenance operation that retires stale embeddings when an individual's signal pattern has moved (often paired with re-enrollment). They differ in trigger, completeness guarantees, and whether the identity persists — hence `forget(individual_id, reason)` carries the reason.
