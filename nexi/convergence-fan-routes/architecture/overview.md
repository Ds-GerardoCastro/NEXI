# Architecture: Substrate-Diverse Routes to One Function

This document specifies how to use the convergence-fan as a *method* — an ablation-over-substrates that treats a target capability as a convergent attractor and reads off the necessary invariant by varying the architecture.

## The fan as a method, not just an observation

The biological observation is that complex brains arose independently on non-homologous substrates. The architectural use is inverted: instead of assuming one blueprint is necessary, run several architecturally distinct systems toward the same function and see what all the successes share.

```
   ┌──────────────┐
   │ target       │
   │ function X   │
   └──────┬───────┘
          │ optimise independently toward X
   ┌──────┼───────┬───────────┬───────────┐
   ▼      ▼       ▼           ▼           ▼
 arch A  arch B  arch C     arch D      arch E
   │      │       │           │           │
   └──────┴───────┴───────────┴───────────┘
          │ compare successes
          ▼
   invariant across all successes = necessary feature
   route-specific structure         = contingent
```

## Procedure

```
def find_necessary_invariant(target_function, substrates):
    successes = []
    for arch in substrates:                      # deliberately diverse
        system = optimise(arch, target_function) # independent optimisation
        if reaches(system, target_function):
            successes.append(system)

    invariant = intersect_structural_features(successes)
    contingent = union_features(successes) - invariant
    return invariant, contingent
```

- `substrates` must be genuinely non-homologous — the point is to vary the blueprint, not to re-run one architecture with different seeds.
- `invariant` is the design target: the feature no successful route omits. In this cluster it resolves to the dense integration hub ([`convergent-integration-hub`](../../convergent-integration-hub/)), measured via [`network-density-over-size`](../../network-density-over-size/).
- `contingent` is what you are free to choose per deployment.

## Guard against the single-driver trap

A recurring failure is to notice that many routes reach the same destination and then attribute it to a single cause. The biology warns against this: elaborate mushroom bodies in insects track parasitoidism, not sociality (Farris & Schulmeister 2011) — the same associative-centre destination reached under a different selective pressure. Method consequence:

```
assert distinct(driving_pressure(a) for a in successes)  # expect diversity
# if all successes share one driver, you have a single-driver
# account, not a convergence fan — re-examine before generalising.
```

Route multiplicity must extend to the *drivers*, not only the anatomy, before the fan reading is safe.

## What refutes the fan

```
if any(feature required by ALL successes and absent in ALL failures):
    # a single structural homology is necessary after all
    -> collapses to single-architecture-necessity; fan is refuted
```

If exactly one structural feature is present in every success and absent in every failure, "many routes" was an illusion of superficial variation over one required core. The method is honest only if it can return this verdict.

## Relation to the AGI critique

The fan is this cluster's citable case against "only architecture A can achieve capability X." If a capability is a convergent attractor in biology — reached on five unrelated substrates — then a claim that one artificial architecture is uniquely necessary carries its own burden of proof. This is the `agi-critique` face of the pattern: substrate-independence of the target undercuts single-blueprint necessity claims.

## Interaction with the cluster

Within [`convergent-intelligence-attractor`](../../../clusters/convergent-intelligence-attractor/) this NEXI is the **shape layer**: it names the topology and supplies the independence evidence. It hands its output — the surviving invariant — to [`convergent-integration-hub`](../../convergent-integration-hub/) (what the routes converge on) and depends on [`network-density-over-size`](../../network-density-over-size/) to measure that invariant. Without the shape, the hub is a single-lineage observation rather than a substrate-general design target.
