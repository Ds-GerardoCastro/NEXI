# Network Density Over Absolute Size

> **NEXI status:** draft · **Formats available:** architecture · **Audience:** builder · **Created:** 2026-07-04
>
> **Cluster:** [`convergent-intelligence-attractor`](../../clusters/convergent-intelligence-attractor/)
>
> The **metric layer** of the cluster: the correlates of high intelligence are network-quality metrics — neuron number, packing density, connection number and pattern, cell-type diversity — **not** absolute size. Larger is not smarter. This NEXI is how the cluster's invariant (a dense integration hub) is measured, and it is what makes the whole attractor claim falsifiable.

---

## At a glance

The intuitive story — bigger brain, more intelligence — does not survive comparison. Roth's synthesis states the anomaly plainly —

> "Despite their very large brains, elephants and cetaceans turn out to possess an intelligence definitely inferior to monkeys and apes and also possibly to corvid and psittacid birds."

And on the other end of the scale, insect associative tissue is extraordinarily dense: honeybee Kenyon-cell packing density is reported as roughly **15 times higher than the highest** found anywhere in the vertebrate brain. The lineages with the largest brains rank below lineages with denser, more connected networks; a tiny insect brain packs association more tightly than any vertebrate.

The load-bearing correlates are therefore quantitative and substrate-agnostic: neuron number, packing density, connectivity. For an artificial system the analogous claim is that capability tracks **effective connectivity and representational density**, not raw parameter or unit count — and that scaling size without scaling integration density yields diminishing cognitive return.

---

## The natural exemplar

Two facts anchor the metric:

- **Large brains rank below dense ones.** Elephants and cetaceans have far larger brains than corvids or primates yet display inferior intelligence. Absolute size is a poor predictor.
- **Insect density is extreme.** Honeybee Kenyon-cell packing density ~15× the highest vertebrate density — a small structure that is nonetheless a dense associative network.

Together they say: what correlates with intelligence is how many units there are, how tightly they pack, and how richly they connect — not how big the whole is. This is the measurable face of the cluster's invariant. The [`convergent-integration-hub`](../convergent-integration-hub/) says intelligence lives in a dense associative centre; this NEXI says *dense*, not *big*, is the operative word, and gives it a metric.

See [`references.md`](references.md) for the full citation chain.

---

## The pattern

**Scale-maximalist framing:**

```
capability ≈ f(absolute size)      →  add parameters / units
```

**Density-over-size framing:**

```
capability ≈ f(effective connectivity, representational density)
        │
        ├─ adding size without density → sub-proportional return
        └─ adding integration density at fixed size → the lever
```

The pattern does not say size never helps. It says size is the wrong *primary* variable: past the point where a task is integration-bound, additional units with no additional connectivity into and within the association substrate buy little. The lever is density.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — how to define an effective-density metric for an artificial substrate and the matched-size experiment that tests density-over-size.

In summary:

1. **A density metric.** An effective-connectivity / representational-density measure for the substrate (connections into and within the association substrate per unit), not parameter count.
2. **The matched-size comparison.** At equal total size, compare a denser-integration variant against a sparser one on cross-domain tasks.
3. **The scaling-curve test.** Hold density constant and grow size; the pattern predicts sub-proportional capability gains.

This is the metric that makes [`convergent-integration-hub`](../convergent-integration-hub/) operational (a "hub" must be dense, not merely large) and sits alongside [`capacity-first-scaling`](../capacity-first-scaling/) as the connectivity-side companion to capacity-side allocation.

---

## When to use

- When reasoning about scaling decisions and whether to add absolute size or add connectivity/integration density.
- As a comparative-biology-grounded counter to size-equals-capability arguments.
- When evaluating efficiency of a design at fixed capability.

## When not to use

- Regimes where scale is empirically the dominant driver for the target task and no integration bottleneck is observed.
- Settings where "density" cannot be meaningfully defined or measured for the substrate in question.

## Tradeoffs

Optimising for connectivity density rather than raw size can raise routing and wiring cost and complicate parallelism, in exchange for better capability per unit of scale. Where scale is cheap and density is expensive to engineer, the size route may still win on total cost even if it is less efficient per unit.

## Falsifiable hypothesis

> If capability tracks connectivity density rather than absolute scale, then at matched total size a system with higher effective integration density (richer connectivity into and within its association substrate) should outperform a sparser same-size system on cross-domain cognitive tasks — and increasing absolute size while holding integration density constant should produce sub-proportional capability gains. Refutation: if absolute size (raw parameter or unit count) predicts capability at least as well as any density metric across systems — i.e. the biggest reliably win regardless of connectivity structure — the density-over-size claim is falsified.

## References

See [`references.md`](references.md) — Roth (2015) is the sole primary source for this NEXI's specific quantitative claims (large-brained taxa ranking below denser ones; honeybee Kenyon-cell packing density).

## See also

- Cluster: [`convergent-intelligence-attractor`](../../clusters/convergent-intelligence-attractor/).
- Sibling NEXIs: [`convergent-integration-hub`](../convergent-integration-hub/) · [`convergence-fan-routes`](../convergence-fan-routes/).
- Companion: [`capacity-first-scaling`](../capacity-first-scaling/) — the capacity-side allocation pattern this metric complements.
