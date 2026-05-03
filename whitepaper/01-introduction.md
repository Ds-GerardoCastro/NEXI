# 1. Introduction

## 1.1 The structural failure of agentic AI

Large Language Models, optimised to predict the next token in a sequence, have proven to be remarkably general tools. By 2026 they write code, summarise documents, classify images, and converse fluently in dozens of languages. The natural extrapolation is to make them _agentic_ — to give them the power to plan and execute multi-step actions autonomously across digital and physical environments. This is the direction the AI industry has aggressively pursued.

This direction is structurally limited.

The argument has been made most clearly by Yann LeCun [LeCun 2022, 2023, 2024]: a system cannot plan a sequence of actions if it cannot predict the _consequences_ of those actions. LLMs are trained to predict the next _token_ — a linguistic continuation. They are not trained to predict the next _state of the world_ — a causal continuation. The two are different objectives; mastering the first does not yield the second. Without an internal model of how its actions change the environment — what LeCun calls a _world model_ — an agentic system cannot reliably anticipate outcomes, cannot reliably plan, and is dangerous when given execution authority over multi-step plans in the physical world.

The empirical signature of this gap is _sample inefficiency_. A teenager learns to drive a car in roughly twenty hours of practice. Current AI systems applied to comparable tasks require many orders of magnitude more data, and even then fail at basic spatial reasoning, object permanence, and counterfactual prediction [LeCun 2022; Lake et al. 2017; Garnelo & Shanahan 2019]. The five-order-of-magnitude gap is not a function of dataset size; it is a function of architecture. Scaling token prediction will not close it.

## 1.2 The architectural critique is incomplete

LeCun's argument identifies _what is missing_ (world models grounded in sensory data) but does not, by itself, tell us _what to build differently_. Building world models from video — the direction Meta FAIR has pursued through architectures like JEPA, V-JEPA, and I-JEPA [Assran et al. 2023; Bardes et al. 2024] — is a meaningful architectural commitment. But this work operates within a recognisable design space: deep neural networks composed of perceptron-derived units, optimised end-to-end via gradient descent. The architectural variation within that space is real and substantial. The _biological lineage_ of the substrate is unchanged.

This paper argues that the biological lineage itself is too narrow.

## 1.3 The template critique

Modern deep learning descends from a single biological template. The McCulloch-Pitts neuron [McCulloch & Pitts 1943] abstracted a mammalian cortical neuron into a logical computing unit. Rosenblatt's perceptron [Rosenblatt 1958] made that unit _learnable_. Every major architectural development since — multi-layer networks, backpropagation [Rumelhart et al. 1986], convolutional networks [LeCun et al. 1989], recurrent networks and LSTMs [Hochreiter & Schmidhuber 1997], transformer attention [Vaswani et al. 2017] — has elaborated _the same biological reference unit_: a weighted-sum-and-non-linearity, modelled on the abstracted point-neuron of the mammalian cerebral cortex.

The architectural creativity within this lineage has been spectacular. The _biological diversity_ sampled has been minimal.

Nature has produced many other implementations of intelligence:

- **Decentralised cognition.** Cephalopods compute partly in peripheral arm ganglia [Hochner 2012]; the octopus is not centrally controlled in the way mammalian cognition is.
- **Acerebrate computation.** Slime molds [Nakagaki et al. 2000] and plants [Trewavas 2014] solve real optimisation problems with no neurons at all.
- **Network-level intelligence.** Eusocial insects [Seeley 2010] and flocking birds exhibit cognition that is _irreducibly multi-agent_; no single individual contains the system's intelligence.
- **Phase-coded dynamics.** Many invertebrate brains encode information in synchrony and timing rather than in firing rates [Buzsáki 2006].
- **Closed sensorimotor loops without central planners.** Insect navigation produces complex adaptive behaviour without a controller in the perceptron-lineage sense [Webb 2002].

Each of these is a candidate architectural primitive that the deep learning community has barely tried. Each is documented in a substantial peer-reviewed literature that AI research has largely not engaged with as a _design source_.

The _template critique_ is that AI's narrow biological inspiration is itself a design constraint, and a substantial portion of the intelligence-design space is unvisited. Just as the architectural critique tells us scaling current architectures will not produce reliability, the template critique tells us scaling current architectures will not produce _diversity_. Both constraints are structural; both require addressing.

## 1.4 The proposal

This paper proposes a research program that addresses both critiques jointly: **mine peer-reviewed research on intelligence across biological species for architectural primitives the perceptron lineage has not yet borrowed, and translate those primitives into engineering-ready design patterns for AI systems.**

The two critiques converge on a single direction. The architectural critique identifies _what is missing_ (world models). The template critique identifies _where to find candidate designs_ (comparative cognition across species). World models _should be informed by_ the plurality of natural intelligence designs, not by scaling up a single cortical template.

This is the central thesis of the **Nature Intelligence Project**.

The operational instrument of the project is **NEXI (Nature Expression of Intelligence)** — a curated, public catalog of architectural primitives derived from peer-reviewed comparative-cognition research. NEXI is organised at two layers: individual _patterns_ (single architectural primitives) and _clusters_ (coherent intelligence models composed of co-dependent patterns). Each entry is grounded in peer-reviewed literature, presented in a layered format readable by both engineers and academic reviewers, and commits to a falsifiable architectural hypothesis. NEXI is built at <https://github.com/Ds-GerardoCastro/NEXI>; this paper presents its foundation and first demonstration case.

## 1.5 Roadmap

Section 2 surveys related work in world models, scaling debates, comparative cognition, and pattern-catalog approaches in AI. Section 3 develops the two-pillar critique in detail and establishes the falsifiability of the program. Section 4 describes the methodology — how peer-reviewed sources are processed into design primitives, with curation discipline that preserves provenance and enforces falsifiability. Section 5 introduces the NEXI catalog framework: schema, layered cards, the cluster concept, status fields. Section 6 presents the first demonstration: the Distributed Social Cognition cluster, derived from research on wild zebra finch communication networks, with its five member patterns and its system-level falsifiable hypothesis. Section 7 discusses limitations, falsifiability of the overall program, relationship to mainstream AI research, and engagement with counter-arguments. Section 8 outlines future work. Section 9 concludes.
