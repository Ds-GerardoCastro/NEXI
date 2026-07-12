# Architecture: Expansion-Readout Circuit

This document specifies the architectural primitive for the expand-then-read-out motif — components, interfaces, data flow, and the design decisions each stage forces — and its integration with the [`substrate-independent-cognition`](../../../collections/substrate-independent-cognition/) collection.

The motif separates two functions that dense scaling entangles: **representation** (a wide, sparse-coded expansion sheet) and **selection** (a narrow, sparse readout). The natural systems that inspired it — insect mushroom bodies, the octopod vertical lobe, cichlid and avian pallium, mammalian isocortex — implement exactly this two-stage separation on non-homologous substrates.

## Components

### 1. Convergent fan-in

A small number of high-fan-in projection units carry convergent (typically multimodal) afferents into the circuit. In the natural exemplars this is the ~800 projection neurons of the honeybee mushroom body or the ~65,000 large projection neurons the octopus vertical lobe reads back out onto.

```
fan_in(afferents: MultiModalInput) -> ProjectionVector   # small, dense
```

Design-time: choose the projection dimensionality (small relative to the expansion sheet) and whether it is shared with [`multi-modal-integration`](../../multi-modal-integration/) as the integration front-end.

### 2. High-dimensional expansion sheet

A wide, **fixed-or-random** projection expands the input into a vast sheet of tiny units whose activation is **sparse**. This is the representational core: the sheet's dimensionality is far larger than the fan-in, and its capacity is scaled by _density_ (how many small units are packed) rather than by absolute count. The natural analogue is the ~300,000 Kenyon cells or the ~26M vertical-lobe interneurons; the CS analogues are the granule-cell layer of cerebellum-like circuits, the reservoir of a reservoir computer, the random-feature map, or the expert bank of a sparse mixture-of-experts.

```
expand(x: ProjectionVector, W_exp: FixedOrRandom, k: SparsityBudget) -> SparseCode   # wide, sparse
```

Design-time: choose expansion width, the sparsity budget `k` (how many units may be active), and whether `W_exp` is fixed, random, or lightly learned. Runtime: the sheet emits a high-dimensional sparse code. The expansion is orthogonalising — the crossbar / en-passant connectivity of the natural motif spreads correlated inputs into near-orthogonal high-dimensional codes, which is what makes downstream associative read-out cheap.

### 3. Sparse projection readout

A narrow, **learned** projection reads the expansion sheet back out. This is the selection stage: only a small readout is trained, activation cost stays bounded, and associative generalisation is driven here.

```
readout(code: SparseCode, W_read: Learned) -> Output
```

Design-time: choose the readout width and the learning rule (the only stage that typically needs plasticity). Runtime: the readout maps the sparse code to the downstream target — an associative recall, a class, or a value handed to a selection layer.

## Data flow

```
   multimodal afferents
        │
        ▼
   ┌──────────────────────┐
   │  convergent fan-in   │   few large projection units (dense)
   └──────────┬───────────┘
              │ ProjectionVector
              ▼
   ┌──────────────────────────────────────┐
   │  high-dimensional expansion sheet     │   wide, sparse-coded, fixed/random
   │  (orthogonal crossbar / en-passant)   │   ← capacity scaled by density
   └──────────┬───────────────────────────┘
              │ SparseCode
              ▼
   ┌──────────────────────┐
   │  sparse readout       │   narrow, learned  (selection)
   └──────────┬───────────┘
              │ Output
              ▼
      downstream / associative target
```

## Pseudocode — forward pass

```python
def expansion_readout(afferents, W_exp, W_read, k):
    # 1. Convergent fan-in: multimodal afferents -> small dense projection
    x = fan_in(afferents)

    # 2. High-dimensional expansion into a sparse-coded sheet.
    #    W_exp is fixed or random (not the trained part); sparsity budget k
    #    keeps only the top-k units active -> near-orthogonal high-dim code.
    pre = W_exp @ x
    code = k_winners_take_all(pre, k)        # sparse expansion

    # 3. Sparse readout: only W_read is learned. Selection / associative
    #    recall happens here; activation cost is bounded by k.
    return W_read @ code


def train_step(afferents, target, W_read, W_exp, k):
    # Only the readout is trained in the canonical motif; the expansion
    # sheet stays fixed/random. This is what makes the circuit cheap to
    # adapt and is the source of its rapid associative generalisation.
    code = k_winners_take_all(W_exp @ fan_in(afferents), k)
    W_read += learning_rule(code, target)    # e.g. delta rule / local plasticity
    return W_read
```

## Integration notes

| Stack                                                                            | How to integrate                                                                                                                                                                                                       |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cerebellum-inspired models** (deep cerebellar nets, MLP-mixer-style expansion) | The granule-layer expansion + Purkinje readout is already this motif. Make the fixed/random expansion and the learned sparse readout explicit modules so the separation is testable.                                   |
| **Reservoir computing** (echo-state, liquid-state machines)                      | The reservoir is the expansion sheet; only the read-out weights are trained. This NEXI is the design justification for that split and prescribes sparse (not dense) reservoir read-out.                                |
| **Sparse mixture-of-experts** (routed transformers)                              | The expert bank is a discrete expansion; sparse routing is the readout bottleneck. Treat the router as the sparse-readout stage and the expert bank as the fixed/wide expansion.                                       |
| **Random-feature / kernel methods**                                              | Random Fourier / random-ReLU features are the fixed expansion; the linear head is the learned readout. The motif predicts this beats depth-only dense scaling for associative generalisation at equal parameter count. |
| **Associative-memory modules** (Hopfield-style, key-value memory)                | Use the expansion sheet as the high-dimensional key space and the sparse readout as retrieval. The orthogonalising expansion is what raises memory capacity per parameter.                                             |

## Performance and cost considerations

- **Cost sits in the expansion sheet's width/density.** The natural systems pay this with soma miniaturisation (smaller, more densely packed units); artificial systems pay it in the parameters or memory of `W_exp`. Because `W_exp` is fixed/random, it need not be stored as trained weights — it can be regenerated from a seed, which is the cheapest way to buy the width.
- **The sparse readout bounds activation cost.** Only `k` units are active and only `W_read` is trained, so both compute and adaptation cost are governed by the readout, not the sheet.
- **Fixed expansion, learned readout.** Keeping the expansion fixed is what gives the motif its rapid associative generalisation and its cheap adaptation — the expensive stage is not on the training path.

## Interaction with the collection

This NEXI is the **how-the-circuit-is-shaped** layer of the [`substrate-independent-cognition`](../../../collections/substrate-independent-cognition/) collection. It composes with:

- [`multi-modal-integration`](../../multi-modal-integration/) — the **what-is-integrated** layer. Integration specifies that multiple sensory streams meet in a shared latent space; this NEXI specifies the circuit shape (wide sparse expansion + sparse readout) that the source cytoarchitecture shows implements such integration centres across phyla. The fan-in stage here is the natural home for a joint multi-modal encoder.

**Framing caveat.** The collection's stance is substrate-independence _of the pattern_, not substrate-irrelevance. The source account is itself substrate-restrictive; this NEXI takes the weaker, defensible reading — that the expand-then-read-out _motif_ recurs across non-homologous neural substrates and is therefore a candidate for porting to artificial ones — without claiming any substrate will do.
