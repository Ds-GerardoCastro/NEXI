# Architecture Overview — Expansion-Readout Circuit

> Substrate-architectural pattern: high-dimensional expansion stage feeding a sparse projection readout via fixed-or-random orthogonal-crossbar connectivity. Implementation-agnostic; the biological convergent evidence (Roth 2015) supports multiple substrate realisations.

## Components

### 1. Multi-modal input encoder

- **Role.** Convert raw input from one or more modalities into a fixed-dimensional dense vector. This stage is *not* the expansion; it is the upstream encoder that prepares the input for the convergent-divergent fan.
- **Constraint.** Must produce vectors of a fixed dimension `d_in` regardless of input variation; multi-modal inputs may pass through modality-specific encoders before concatenation, or through a shared multi-modal encoder ([`multi-modal-integration`](../../multi-modal-integration/)).
- **Typical implementation.** Transformer encoder, CNN, ResNet, modality-specific small networks with cross-modal attention. Whatever produces a dense input vector.

### 2. Orthogonal-crossbar projection

- **Role.** Project the dense input vector into a high-dimensional sparse representation in the expansion sheet. The projection matrix is **fixed or randomly initialised** (not learned dense), preserving topographic structure where it exists.
- **Constraint.** Projection dimension `d_exp >> d_in` (typical: 10–100× expansion). The projection should preserve some topographic structure of the input — naive fully-random projection works but loses cross-modal alignment.
- **Typical implementation.** Random Gaussian projection; locality-sensitive hashing; biologically-inspired sparse random connectivity (Marr's cerebellum theory); learned but frozen projection layer.

### 3. Expansion sheet (sparse activation)

- **Role.** A high-dimensional layer of units that activate sparsely under any single input. The sheet is dense in *connectivity* (every input fibre crosses every interneuron process) but sparse in *activation* (any single input drives only a small subset of units).
- **Constraint.** Sparsity is enforced — either by top-k activation, by competitive lateral inhibition, or by a learned sparse-coding objective. Without sparsity the expansion collapses into a wide dense layer.
- **Typical implementation.** Reservoir computing readout state with explicit sparsity; mixture-of-experts where the expansion sheet is the expert pool; cerebellum-inspired granule-cell layer with top-k activation.

### 4. Sparse readout

- **Role.** A small population of large readout units that integrate over the active subset of the expansion sheet. The readout is the *trained* component — plasticity operates here, not in the expansion projection.
- **Constraint.** Readout population is small (`d_out << d_exp`, typical: 100–10000× compression). Routing or selection mechanism determines which expansion units contribute.
- **Typical implementation.** Trained linear layer with sparse input; mixture-of-experts router; cerebellum-inspired Purkinje-cell-like integration.

### 5. Plasticity layer (optional but typical)

- **Role.** Adapt the readout weights based on task feedback. Plasticity operates *on top of* the substrate — the expansion projection is fixed; the readout adapts.
- **Constraint.** Plasticity should be local to the readout. Plasticity in the expansion stage breaks the fixed-projection assumption that makes the architecture work.
- **Typical implementation.** Hebbian update on readout; gradient descent on readout weights only; reinforcement-learning credit assignment limited to readout.

## Pseudocode

```python
class ExpansionReadoutCircuit(nn.Module):
    def __init__(self, d_in: int, d_exp: int, d_out: int, expansion_ratio: int = 50, top_k: int = 32):
        super().__init__()
        assert d_exp >= d_in * expansion_ratio, "Expansion ratio insufficient"

        # Fixed/random projection — NOT trained
        self.expansion_projection = nn.Linear(d_in, d_exp, bias=False)
        nn.init.orthogonal_(self.expansion_projection.weight)
        for p in self.expansion_projection.parameters():
            p.requires_grad = False  # Substrate, not weights

        # Top-k sparsity
        self.top_k = top_k

        # Trained readout
        self.readout = nn.Linear(d_exp, d_out)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: (batch, d_in) — dense input vector from upstream encoder
        returns: (batch, d_out) — sparse-projection readout output
        """
        # Step 2: Orthogonal-crossbar projection
        expanded = self.expansion_projection(x)  # (batch, d_exp)

        # Step 3: Sparse activation via top-k
        topk_vals, topk_idx = expanded.topk(self.top_k, dim=-1)
        sparse_expanded = torch.zeros_like(expanded)
        sparse_expanded.scatter_(-1, topk_idx, topk_vals)

        # Step 4: Sparse readout
        out = self.readout(sparse_expanded)  # (batch, d_out)
        return out
```

## Wrapping pattern for existing architectures

For architectures that lack an explicit expansion-readout layer, the wrapping pattern:

1. **Identify the bottleneck** where dense compositional features feed a downstream task head.
2. **Insert an `ExpansionReadoutCircuit` module** between the dense backbone and the task head, with `d_in` = backbone output dimension, `d_exp` = 50× `d_in`, `d_out` = task-head input dimension.
3. **Freeze the expansion projection** during training; train only the readout and the backbone.
4. **Compare against the unwrapped baseline** on associative-generalisation benchmarks (few-shot, novel-stimulus, pattern completion).

The wrapping does not require modifying the backbone or the task head; it inserts a substrate-architectural commitment between them. This is the cheapest path from "depth-scaled dense feedforward" to "expansion-readout substrate" and is the recommended starting experiment for evaluating the falsifiable hypothesis.

## Inspection / lesion protocols

Per the [`action-selection-as-common-substrate`](../../action-selection-as-common-substrate/) methodology export from Roth 2015 (lesion-defined cognitive bottleneck): the expansion-readout architecture should be evaluated by ablation against cognitive-flexibility tasks, not training-distribution accuracy.

- **Inspect:** for each input, log which subset of the expansion sheet was active (top-k indices). Look for stable subsets across inputs that vary in irrelevant dimensions.
- **Lesion:** ablate fractions of the expansion sheet (force `expanded[i] = 0` for random subsets). Plot task accuracy vs. ablation fraction. A graceful degradation curve confirms the expansion sheet is the substrate of representational richness, not a redundant layer.
- **Compare:** run the same ablation on a depth-equivalent dense baseline. The dense baseline should degrade more sharply (no redundant capacity in the bottleneck).

## Connection to other NEXIs

- [`multi-modal-integration`](../../multi-modal-integration/) — the *functional* claim (joint multi-modal encoders > late fusion). This NEXI provides the *circuit-level* implementation. Multi-modal integration centres in mushroom body / vertical lobe / pallium are *instances* of the expansion-readout circuit handling multi-modal input.
- [`action-selection-as-common-substrate`](../../action-selection-as-common-substrate/) — Roth's evidence adds a fourth substrate vertex to that canonical NEXI; this NEXI is the substrate-architectural detail of how that fourth vertex implements its action-selection function.
- [`ecological-context-model`](../../ecological-context-model/) — Roth's emphasis on spatial-learning / navigation as the evolutionary driver of the architecture aligns with Nordli & Todd's `E` schema (agent + environment unified state).
