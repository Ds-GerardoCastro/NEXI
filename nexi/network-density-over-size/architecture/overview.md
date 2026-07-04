# Architecture: Network Density Over Absolute Size

This document specifies the metric primitive for the density-over-size pattern — how to define an effective-density measure for an artificial substrate, the matched-size experiment that tests the claim, and the scaling-curve test that separates size gains from density gains.

## Why a metric layer

The cluster's invariant is a dense associative integration hub. "Dense" is meaningless without a measure. This NEXI supplies the operationalisation: it turns "bigger is not smarter" into a quantity you can compute for a candidate architecture and an experiment you can run.

The biological calibration is stark. Absolute size mis-predicts: elephants and cetaceans, with the largest brains, rank below corvids and primates. Density predicts better: honeybee Kenyon-cell packing runs ~15× the highest vertebrate density. So the metric must reward packing and connectivity, and must *not* reward raw size.

## The effective-density metric

For an artificial substrate, define density over the association substrate rather than the whole model:

```
effective_density = active_connections(association_substrate)
                    ─────────────────────────────────────────
                    units(association_substrate)

# complemented by a packing/participation term:
participation = active_units(association_substrate) / total_units
```

- Count connectivity *into and within* the association substrate, not parameters at large.
- Reward participation (units actually engaged in association), penalise dead capacity.
- Crucially, `effective_density` is scale-normalised: doubling size with proportionally sparser wiring does **not** raise it.

This is deliberately the inverse of a parameter-count metric. Two systems of equal parameter count can have very different `effective_density`; the pattern predicts the denser one is more capable on integration-bound tasks.

## The matched-size experiment

```
A. dense_model  : high effective_density, size S
B. sparse_model : low  effective_density, size S   (same total size)
```

Train both at matched total size and compute; evaluate on cross-domain cognitive tasks. Prediction: `A > B`. This isolates density from size — any advantage cannot be attributed to A being bigger, because it is not.

## The scaling-curve test

```
for S in increasing_sizes:
    fix effective_density = d0
    grow total size to S
    measure capability(S)
# prediction: capability(S) grows sub-proportionally in S
#             when density is held constant.
```

If capability rises proportionally (or faster) with size at fixed density, the "density is the lever" claim weakens. The pattern stakes itself on diminishing returns to size-without-density.

## What refutes the pattern

```
if absolute_size predicts capability >= any density metric, across systems:
    -> the biggest reliably win regardless of connectivity structure
    -> density-over-size is falsified
```

Concretely: if a parameter-count regression explains cross-system capability at least as well as `effective_density`, the metric layer carries no design content and the cluster's attractor claim collapses into a scale claim.

## Relation to hub and to capacity-first-scaling

- **Makes the hub operational.** [`convergent-integration-hub`](../../convergent-integration-hub/) requires its hub to be *dense*, not merely large. `effective_density` is the test a candidate hub must pass; a large sparse module fails it.
- **Complements capacity allocation.** [`capacity-first-scaling`](../../capacity-first-scaling/) reasons about how much capacity to allocate; this NEXI reasons about the *connectivity structure* of that capacity. They are the two sides of "spend the budget well": capacity-side and connectivity-side.

## Interaction with the cluster

Within [`convergent-intelligence-attractor`](../../../clusters/convergent-intelligence-attractor/) this NEXI is the **metric layer**. It measures the invariant that [`convergent-integration-hub`](../../convergent-integration-hub/) names and that [`convergence-fan-routes`](../../convergence-fan-routes/) reads off independent routes. Without the metric, the invariant cannot be operationalised or falsified — there is no way to say whether a system has a dense integration hub or merely a large one. The metric is what keeps the whole attractor claim from collapsing into "make it bigger."
