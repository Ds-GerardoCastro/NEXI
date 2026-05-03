# What is a NEXI?

A **NEXI** (_Nature Expression of Intelligence_) is a curated design pattern for AI systems, drawn from how a non-human species solves a cognitive problem and translated into a reusable architectural primitive or agent skill.

## What it is not

- **Not a metaphor.** A NEXI is a concrete engineering pattern with interfaces, pseudocode, and a falsifiable claim about its effect — not a "lessons from biology" essay.
- **Not a benchmark.** NEXI does not provide tasks or evaluations. It provides patterns; testing them is downstream.
- **Not platform-locked.** Skills and architectures are specified in framework-neutral form; translation notes show how to map them to specific stacks (LangChain, MCP, OpenAI, custom RL, etc.).

## What every NEXI gives you

1. **A natural exemplar.** The species and behaviour that motivates the pattern.
2. **A pattern description.** What the pattern _is_, in plain language with a diagram.
3. **An architectural primitive.** Interfaces, data flow, pseudocode (when the entry has the `architecture` format).
4. **A skill specification.** Drop-in components for an LLM-based agent (when the entry has the `skill` format).
5. **When to use / not use.** Boundary conditions.
6. **Theoretical grounding.** Citations to peer-reviewed work supporting the claim.
7. **A falsifiable hypothesis.** A specific, testable architectural prediction.

## Layered format

Every NEXI's `README.md` is **layered for two reading depths**:

- **Top of the document** — quick-start, plain-language summary, when-to-use. A builder can stop reading here and have enough to apply the pattern.
- **Lower sections** — theoretical background, citations, falsifiable hypothesis, computational analogs. A reviewer or researcher can verify the pattern is grounded in peer-reviewed work.

Same file, two reading depths. The two audiences are not served by writing two separate documents.

## How to navigate

- [`../CATALOG.md`](../CATALOG.md) — full index of all NEXIs.
- [`methodology.md`](methodology.md) — how patterns enter the catalog and the curation gate.
- Each `nexi/<slug>/` folder — one NEXI, with `README.md` as the layered card.
