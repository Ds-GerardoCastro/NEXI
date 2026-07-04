# Substrate-Diverse Routes to One Function

> **NEXI status:** draft · **Formats available:** architecture · **Audience:** builder · **Created:** 2026-07-04
>
> **Cluster:** [`convergent-intelligence-attractor`](../../clusters/convergent-intelligence-attractor/)
>
> The **shape layer** of the cluster: high-level cognitive function is a convergent attractor reachable by multiple independent, non-homologous architectures. The same outcome — behavioural flexibility, problem-solving — is arrived at from starting points that share no common complex-brain ancestor and no common tissue plan. Function, not substrate provenance, defines the destination.

---

## At a glance

The strongest evidence that a capability is substrate-general is that nature built it more than once, on unrelated hardware, from ancestors that had it not at all. Roth's synthesis makes the independence explicit —

> "The highly complex brains found in insects and in cephalopods must have evolved independently, and with them high intelligence."

Each major taxon surveyed — insects, cephalopods, teleost fish, birds, mammals — descends from ancestors that "revealed neither complex brains nor intelligent behaviour." So the capability was not inherited down a single line; it was reached, separately, by anatomically and developmentally divergent machinery (everted vs. evaginated pallium; nuclear vs. laminar telencephalon). That is the convergence-fan: many routes, one destination.

For AI architecture the reading is direct. If a target function is a genuine convergent attractor, then "only this architecture can achieve X" is a claim in tension with the biology. The diversity of viable routes is itself the evidence that the capability is substrate-general rather than tied to one privileged blueprint.

---

## The natural exemplar

The independence is the whole point. Across Ecdysozoa (insects), Lophotrochozoa (cephalopods) and Vertebrata (teleosts, birds, mammals), complex brains and intelligence arose on separate lineages whose common ancestors had neither. The machinery differs at every level — cell types, layering, developmental origin — yet the functional outcome (flexible, problem-solving behaviour) recurs.

A pointed test of the "same function, therefore same driver" temptation comes from [Farris & Schulmeister (2011)](https://doi.org/10.1098/rspb.2010.2161): among insects, elaborate mushroom bodies track **parasitoidism**, not sociality — falsifying the tidy single-driver account and reinforcing the fan reading. The same destination (an elaborate associative centre) is reached under different selective pressures. Route multiplicity extends to the driving forces, not just the anatomy.

See [`references.md`](references.md) for the full citation chain.

---

## The pattern

**Single-architecture-necessity framing:**

```
"Capability X requires architecture A."
        │
        ▼
one blueprint, one route, everything else presumed incapable
```

**Convergence-fan framing:**

```
architecture A ─┐
architecture B ─┤
architecture C ─┼──►  function X   (the attractor)
architecture D ─┤
architecture E ─┘
        │
        ▼
X is substrate-general; no single blueprint is necessary.
Route selection is a separate (open) question.
```

The fan does two jobs. It licenses architectural exploration — many routes are viable, so search the space. And it reframes AGI-style "only-this-can" claims: if the biology reaches the same function on five unrelated substrates, a strong claim that one artificial architecture is uniquely necessary needs its own evidence.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — how to run the convergence as an ablation-over-substrates and read off the necessary invariant.

In summary, the fan is used as a *method*:

1. **Vary the substrate deliberately.** Optimise architecturally distinct systems independently toward the same target function.
2. **Read off what all successes share.** The invariant that survives across routes is the necessary feature; everything route-specific is contingent. (In this cluster, the surviving invariant is the dense integration hub — see [`convergent-integration-hub`](../convergent-integration-hub/).)
3. **Leave route selection explicit and open.** Convergence says many routes exist; it does not say which is cheapest.

---

## When to use

- When arguing or testing whether a capability is tied to a specific architecture or is substrate-general.
- When justifying architectural diversity or an ablation programme that seeks the necessary invariant by varying the substrate.
- As a framing against "only this architecture can achieve X" claims.

## When not to use

- When the engineering goal is to optimise one fixed substrate rather than to ask what is necessary across substrates.
- When only a single architecture is available or affordable, making the multiplicity-of-routes framing moot.

## Tradeoffs

Treating a function as a convergent attractor licenses architectural exploration but offers no shortcut to which route is cheapest or best for a given budget — convergence says many routes exist, not that they are equally economical. The pattern buys substrate-independence of the design target at the cost of leaving route selection underdetermined.

## Falsifiable hypothesis

> If a target cognitive function is a genuine convergent attractor, then multiple architecturally distinct systems, optimised independently toward that function, should reach comparable capability without sharing a common structural blueprint — and no single structural homology should be necessary across all successful systems. Refutation: if every high-capability system is found to require one specific shared structural feature (a particular layer plan, cell type, or connectivity motif present in all and absent in all failures), the convergence claim collapses into a single-architecture necessity claim, and "many routes" is an illusion of superficial variation over one required core.

## References

See [`references.md`](references.md) — Roth (2015) as the primary source, with Farris & Schulmeister (2011) as the falsifier of the single-driver account.

## See also

- Cluster: [`convergent-intelligence-attractor`](../../clusters/convergent-intelligence-attractor/).
- Sibling NEXIs: [`convergent-integration-hub`](../convergent-integration-hub/) · [`network-density-over-size`](../network-density-over-size/).
- Contrast: [`action-selection-as-common-substrate`](../action-selection-as-common-substrate/) — one conserved machine across substrates (isomorphism), the inverse of this NEXI's many-machines-one-function fan.
