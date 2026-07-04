# Architecture: Convergent Integration Hub

This document specifies the architectural primitive for the convergent-integration-hub pattern — the hub interface, the density requirement that distinguishes a hub from a merely large module, the cross-domain routing, and the ablation that tests hub-invariance.

## What the hub is

A **convergent integration hub** is a named module where multiple modality encoders and internal-state signals converge and associate, and from which downstream domains read. It is the artificial analogue of the invariant Roth reads off every independent route to intelligence: a discrete multimodal associative centre.

The hub is defined by three properties, in order of importance:

1. **Convergence.** Multiple modality/state streams terminate in it. If only one stream enters, it is not a hub.
2. **Association density.** Connection density *within* the hub is high relative to the surrounding substrate. A large module with sparse internal connectivity is not a hub (see `network-density-over-size`).
3. **Broadcast.** Downstream domains read from the hub, so binding achieved once is reused everywhere.

## Hub interface

```
hub.integrate(streams: list[Stream]) -> HubState
hub.read(domain: DomainId)          -> DomainView(HubState)
```

```
   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
   │ modality A   │   │ modality B   │   │ internal     │
   │ encoder      │   │ encoder      │   │ state signal │
   └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
          │                  │                  │
          └───────► integrate(streams) ◄────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │   HubState        │  (dense associative
                 │   (associative)   │   network — high internal
                 └────────┬──────────┘   connection density)
                          │ read(domain)
             ┌────────────┼────────────┐
             ▼            ▼            ▼
        domain 1     domain 2     domain 3
```

## The density requirement

The distinguishing property is **not** hub size. A hub the same size as its substrate but with uniform connectivity is not a hub. The requirement is measured as association density:

```
hub_association_density = internal_connections(hub) / units(hub)^2
```

and the pattern requires `hub_association_density` to be materially higher than the substrate baseline. This is the hand-off point to [`network-density-over-size`](../../network-density-over-size/): the hub is characterised by connectivity and packing, not by parameter count. A large sparse module fails the test.

## Cross-domain routing

Every downstream domain reads a view of the same `HubState`:

```
for domain in downstream_domains:
    view = hub.read(domain)
    domain.step(view)
```

The point of the single hub is reuse: cross-modal binding computed once is available to every domain, rather than each domain recomputing its own late association. This is what buys cross-domain coherence — and what makes the hub a single point of failure.

## Ablation — testing hub-invariance

The falsifiable claim is that a dedicated dense hub beats uniform association at matched budget. The ablation:

```
A. hub_model     : dedicated dense integration hub, cross-domain read
B. uniform_model : same total capacity + connectivity budget, association
                   spread uniformly, no dense convergence locus
```

Train both at matched compute and connectivity budget; evaluate on cross-domain generalisation. The pattern predicts `A > B`. If `A ≈ B`, or if a strong cross-domain system can be shown to have no localisable hub, the hub-invariance claim is refuted.

## Distinction from within-system multimodal fusion

This architecture is the substrate-general *justification* for a dedicated fusion locus, derived from cross-system convergence. The concrete engineering of fusing channels inside one system belongs to [`multi-modal-integration`](../../multi-modal-integration/). Kept apart:

| Concern | `multi-modal-integration` | `convergent-integration-hub` (this NEXI) |
| ------- | -------------------------- | ------------------------------------------ |
| Scope | Within one system | Across independent systems |
| Question | *How* do I fuse channels? | *Why* is a dedicated dense fusion locus necessary? |
| Evidence | Fusion mechanisms | Convergent recurrence of a hub across non-homologous lineages |

Use `multi-modal-integration` to build the fusion; cite `convergent-integration-hub` for why the fusion deserves a dedicated, dense home.

## Interaction with the cluster

Within [`convergent-intelligence-attractor`](../../../clusters/convergent-intelligence-attractor/) this NEXI is the **invariant layer**. [`convergence-fan-routes`](../../convergence-fan-routes/) supplies the shape (many independent routes) that makes the hub read as necessary rather than incidental; [`network-density-over-size`](../../network-density-over-size/) supplies the metric that makes "dense hub" measurable and the ablation above runnable.
