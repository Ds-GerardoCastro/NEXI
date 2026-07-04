# Coincidence-Detection Gating

> **NEXI status:** draft · **Formats:** architecture, skill · **Audience:** builder
>
> **Collection:** [`acerebrate-decision-making`](../../collections/acerebrate-decision-making/)
>
> A design-time and runtime pattern for **gating major behavioural transitions on alignment of multiple independent context streams**. Single-channel evidence is insufficient; coincidence detection across qualitatively different streams prevents premature commitment under noisy or partial input. Originally documented in _Vibrio cholerae_ biofilm commitment, where BOTH LuxPQ (responding to AI-2) AND CqsS (responding to CAI-1) must activate before colony behaviour engages.

---

## At a glance

The default mental model in AI is single-channel decision-gating: one threshold, one attention score, one router decision. The bacterial pattern says that for major behavioural transitions — irreversible tool calls, regime switches, modal commitments — a single signal is the wrong primitive. Multiple independent context streams must align.

_V. cholerae_ doesn't enter biofilm mode just because population density is high. It requires evidence from **two independent sensors** (LuxPQ + CqsS) reading **two independent autoinducers** (AI-2 + CAI-1). Either signal alone leaves the bacterium in individualistic behaviour. Both together commit it. That's coincidence-detection gating.

The architectural translation: AI systems committing to costly, irreversible actions should require AND-gated agreement across qualitatively different evidence channels — not just majority vote on the same channel.

---

## The natural exemplar

[Nesin & Chandrankunnel (2025)](https://doi.org/10.1080/19420889.2025.2463926) — peer-reviewed review article, _Communicative & Integrative Biology_ — synthesises the molecular biology of bacterial decision-making. The _V. cholerae_ coincidence detection example appears in the section _Multiple pathways in bacteria and their interconnectedness_. The paper itself uses the explicit phrase "coincidence detection" for the gating mechanism, validating the architectural primitive's name in the source's own vocabulary.

The mechanism: at low cell density, LuxPQ acts as a kinase and CqsS receives no CAI-1; both receptors output the "individualistic-behaviour" signal. As density rises, AI-2 binds LuxPQ (switching it from kinase to phosphatase) and CAI-1 binds CqsS. Only when both signals are present does the cell commit to biofilm formation — a costly, partially-irreversible architectural transition. Either signal alone is insufficient.

See [`references.md`](references.md) for full citation chain and computational analogs.

---

## The pattern

**Default single-channel gating:**

```
Input signal s
      │
      ▼
threshold(s) > τ ──► commit
                  └──► don't commit
```

**Coincidence-detection gating:**

```
Input signals s₁, s₂, ..., sₙ  (qualitatively different streams)
      │
      ▼
AND-gate( threshold(s₁), threshold(s₂), ..., threshold(sₙ) )
      │
      ├──► all aligned   → commit
      └──► any missing   → don't commit
```

The non-trivial design choice is **what counts as a "qualitatively different" stream**. Two attention heads on the same modality are not different streams. Two channels of the same physical input are not different streams. Genuinely different streams are: visual + audio, syntactic + semantic, recent context + retrieved context, agent-local + population-level.

---

## Architectural primitive

See [`architecture/overview.md`](architecture/overview.md) for the full design — components, interfaces, data flow, integration with downstream commitment logic.

In summary, three components:

1. **Multi-stream input mux.** Wires qualitatively different evidence channels to the gating layer. Channel selection is design-time; the mux is runtime.
2. **Per-stream evidence accumulator.** Each stream gets its own thresholding logic. Streams may have different noise characteristics, different latency, different reliability.
3. **AND-gate logic with degraded-stream handling.** The gate fires when all required streams cross threshold within a coincidence window. Critical: must degrade gracefully if a stream becomes consistently unavailable, rather than blocking forever.

---

## Skill specification

See [`skill/skill.md`](skill/skill.md) for the framework-neutral specification.

Drop-in components for an engineering-agent or runtime decision-gate:

- **System-prompt fragment** that instructs the agent to require multi-stream evidence alignment before irreversible commitments.
- **Tool definitions** for `register_evidence_stream`, `accumulate_evidence`, `check_coincidence_gate`, `degraded_stream_handler`.
- **Translation notes** for stack-specific mappings (Claude tool definitions, OpenAI function calling, MCP tools, LangChain agents, MARL frameworks).

---

## When to use

- Any deployment where a behavioural mode commits the system to costly, irreversible, or hard-to-reverse actions.
- Multi-agent settings where commitment to a coordinated behaviour requires multi-channel evidence alignment.
- Systems with multiple genuinely independent context streams (multi-modal inputs, multi-source retrieval, multi-tool agentic flows).
- Cases where premature commitment is the dominant failure mode and the fix is "wait for more evidence."

## When not to use

- Deployments where commitments are cheap to reverse (chat turns with no external side effects, classification tasks, retrieval-only systems).
- Settings where only one context stream is meaningfully available — adding artificial coincidence-gates adds no signal.
- Compute-budget-constrained deployments where multi-stream wiring is too expensive relative to its decision-quality return.
- Tasks where premature commitment is _not_ the primary failure mode.

## Tradeoffs

- **Multi-stream wiring overhead.** Maintaining N independent input streams costs more than maintaining 1.
- **Latency from coincidence-window logic.** Waiting for evidence alignment introduces decision latency.
- **Degraded-stream risk.** If one required stream becomes unavailable, naive AND-gate logic blocks forever. Architectures must specify graceful-degradation behaviour up-front.

In return: lower premature-commitment rate; higher decision quality after commitment; structural defence against single-channel adversarial perturbation.

## Falsifiable hypothesis

> At matched compute and identical task budgets, AI architectures with explicit multi-stream coincidence-detection gating on major behavioural transitions outperform single-channel-gated architectures on tasks where decision regret is high and single-stream evidence is noisy. Specifically, on benchmarks where the cost of premature commitment is high (irreversible tool calls, write actions to external systems, multi-step agentic loops without rollback), coincidence-gated systems should show a measurably lower premature-commitment rate (≥20% reduction) and a measurably higher average decision quality after commitment, compared to single-channel baselines. Refutation: if no such margin appears across an appropriate task suite, this NEXI is refuted.

A second testable claim: **lesion experiment robustness.** Removing any one required stream from a coincidence-gated system should produce a measurable degradation; if removing a stream leaves performance unchanged, that stream was not load-bearing and the gate was effectively single-channel.

## References

See [`references.md`](references.md) — Nesin & Chandrankunnel 2025 as primary source, plus computational analogs in multi-modal fusion, evidence-accumulation models in decision-making (drift-diffusion, Bayesian updating), and AND-gating in safety-critical robotics.
