# Skill Specification — Expansion-Readout Circuit

> Design-time skill for AI architects: when reviewing an AI architecture, audit whether it has an expansion-then-readout layer. If the task requires associative generalisation and the architecture is depth-scaled dense, propose adding an expansion-readout circuit at the bottleneck.

## When to invoke this skill

- During architecture design or review for systems pursuing:
  - Few-shot novel-stimulus generalisation
  - Multi-modal binding under partial input
  - Pattern completion under noise
  - Rapid associative learning from sparse examples
- When the candidate architecture is dominantly depth-scaled dense feedforward (transformer-class without MoE, ResNet-class, MLP-class).
- When the system fails the "expand-then-readout audit" below.

## When NOT to invoke

- When the architecture already employs reservoir computing, sparse mixture-of-experts in the expansion direction, or explicit cerebellum-inspired modules.
- When the task is dominantly dense feature compositionality with abundant training data (high-resolution image classification, language modeling with abundant per-token supervision).
- When the parameter budget is severely constrained — expansion adds width, and width has parameter cost.

## The audit (system-prompt fragment)

```
You are reviewing a proposed AI architecture for tasks involving
associative generalisation. Audit for the expand-then-readout pattern:

1. Identify the dense-feature bottleneck — the layer where compositional
   features are integrated before being passed to the task head.
2. Check whether this bottleneck has:
   a. An expansion stage (output dimension >> input dimension)
   b. Sparse activation (top-k, competitive inhibition, or sparse-coding
      objective enforced)
   c. A sparse readout (small projection population reading from the
      sparse-active expansion sheet)
3. If any of (a), (b), (c) is missing, the architecture is depth-scaled
   dense at the critical bottleneck. Propose an expansion-readout circuit
   per the wrapping pattern in architecture/overview.md §"Wrapping pattern".
4. Specify the falsifiable comparison: the proposed architecture should
   outperform the depth-equivalent dense baseline by ≥10% relative on
   few-shot associative-generalisation benchmarks at matched compute.
5. Document the inspection / lesion protocol the system should support
   to test the expansion-sheet's load-bearing role.

The five-phyla convergent-evolution evidence (Roth 2015 — mushroom body,
vertical lobe, cichlid pallium, avian pallium, mammalian isocortex)
supports treating expand-then-readout as a substrate-general design
commitment, not a niche choice.
```

## Tools

### `audit_architecture_for_expand_readout(architecture_spec: dict) -> AuditReport`

- **Input:** A structured description of the architecture's layer sequence (per-layer type, dimensions, activation function, plasticity scope).
- **Output:** `AuditReport` with fields:
  - `bottleneck_layer`: the identified dense-feature bottleneck.
  - `expansion_present`: bool — does the bottleneck have an expansion stage?
  - `sparsity_enforced`: bool — is sparse activation enforced?
  - `sparse_readout_present`: bool — is the readout a small projection population?
  - `recommendation`: 'no_action' | 'add_expansion' | 'add_sparsity' | 'add_sparse_readout' | 'wrap_with_expansion_readout_circuit'.
  - `falsifiable_comparison`: a concrete benchmark + expected outcome that would refute or confirm the recommendation.

### `propose_wrapping(bottleneck_dim: int, target_expansion_ratio: int = 50, top_k: int = 32) -> ArchitectureDelta`

- **Input:** The bottleneck dimension and target expansion parameters.
- **Output:** `ArchitectureDelta` specifying the wrapping module (per the pseudocode in architecture/overview.md), including:
  - Module class signature
  - Where to insert in the existing architecture
  - Training-time freezing protocol for the expansion projection
  - Inspection / lesion protocol to validate the load-bearing role

## Example invocation

> **Architect:** I'm building a multi-modal grounded-language agent that needs to bind new objects after one or two exposures. Architecture: ViT vision encoder + transformer language encoder + cross-modal attention + task head. Should I add an expansion-readout layer?

> **Skill response:** Audit your architecture against the expand-then-readout pattern:
>
> - **Bottleneck identified:** The cross-modal attention output → task head. This is your dense-feature bottleneck where multi-modal features are integrated.
> - **Expansion present:** No — cross-modal attention preserves dimensionality.
> - **Sparsity enforced:** No — attention is dense.
> - **Sparse readout present:** No — task head reads from dense attention output.
> - **Recommendation:** Wrap with an expansion-readout circuit between cross-modal attention and task head. Use `expansion_ratio = 50`, `top_k = 32`. Freeze the orthogonal projection; train only the readout.
> - **Falsifiable comparison:** On few-shot novel-object binding benchmarks (e.g. one-shot CLEVR variants, omniglot-extended cross-modal), the wrapped architecture should outperform the unwrapped baseline by ≥10% relative at matched compute. If parity, refuted.
> - **Inspection protocol:** Log top-k indices per input. Look for stable subsets across exemplars of the same novel object class. Lesion the expansion sheet at 50% / 25% / 12.5% to confirm graceful degradation.

The five-phyla convergent evidence supports this as a default architectural commitment for associative-generalisation tasks; the depth-scaled dense baseline is the niche choice.
