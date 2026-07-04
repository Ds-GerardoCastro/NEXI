# 3. The Two-Pillar Critique

The argument of this paper rests on two converging critiques of modern AI: an _architectural_ critique (what current systems lack) and a _template_ critique (what current systems have not tried). Section 3.1 develops the architectural pillar; Section 3.2 develops the template pillar; Section 3.3 shows their convergence; Section 3.4 establishes the falsifiability of the resulting research program.

## 3.1 The architectural pillar

The architectural pillar makes a sharp claim: agentic systems built on Large Language Models cannot plan reliably because they lack a _world model_.

A world model, in the technical sense developed by [Schmidhuber 1990; Ha & Schmidhuber 2018; LeCun 2022], is an internal representation that allows a system to:

1. **Anticipate** what is going to happen in its environment.
2. **Predict** the consequences of its own actions.
3. **Plan** a sequence of actions toward a defined objective.

LLMs trained on text predict the next token. Token sequences are lossy compressions of the world; most causal structure (gravity, persistence, inertia, intent, consequence) is implicit in the texts that mention them, but the texts themselves are not the structure. A model that has learned the statistical regularities of _descriptions of the world_ is not, by virtue of that learning, a model _of the world_.

The empirical signature of this gap is _sample inefficiency_. Humans (and many other animals) acquire useful causal models of their environments from very limited observation. A teenager learning to drive needs roughly twenty hours of practice before being licensed. Current AI systems applied to comparable tasks require many orders of magnitude more data, and even then fail at basic spatial reasoning, object permanence, and counterfactual prediction [LeCun 2022; Lake et al. 2017; Garnelo & Shanahan 2019]. The five-order-of-magnitude gap is not a function of dataset size; it is a function of architecture.

Two responses to this gap are common in the field.

The first is **scaling-law optimism**: the claim that with sufficient parameters and data, current architectures will eventually close the gap [Kaplan et al. 2020; Hoffmann et al. 2022]. The historical track record of LLMs through 2020–2025 — capability emerging from scale in ways many predicted impossible — gives this view weight. Sutton's "Bitter Lesson" [Sutton 2019] generalises the point: in AI history, general methods leveraging compute have repeatedly defeated approaches that build in human-derived structure.

The architectural critique does not deny these observations. It argues that the empirical signature of the world-model gap is not in any single capability that scaling has not yet reached; it is in the _kind_ of failure modes that persist _regardless_ of scale: hallucination of causal structure, brittleness when deployed in physical environments, inability to plan over horizons that exceed training-context patterns [Marcus 2022; LeCun 2024]. The bitter-lesson observation applies _within_ a substrate; it does not show that _any_ substrate is equally capable. A system whose training objective is linguistic continuation will, at every scale, optimise for that objective.

The second response is **world-model architectures**: building systems explicitly trained to predict future states of their environments from sensory input. The Joint Embedding Predictive Architecture family — JEPA, V-JEPA, I-JEPA [Assran et al. 2023; Bardes et al. 2024] — represents the most prominent technical instantiation of this response. Rather than predicting raw pixels or tokens, JEPA predicts _future embeddings_ of sensory input, learning the structure of how the world evolves at a level of abstraction stripped of pixel-level noise.

The architectural pillar of the present paper accepts the world-model framing without modification. Where it builds further is on the question that the world-model framing alone does not answer: _what should world models look like?_

## 3.2 The template pillar

The template pillar argues that the architectural creativity of modern deep learning is constrained by an unacknowledged narrow biological inspiration.

The lineage in one paragraph: the McCulloch-Pitts neuron [McCulloch & Pitts 1943] abstracted a mammalian cortical neuron into a logical computing unit — a weighted sum of inputs, passed through a threshold non-linearity. Rosenblatt's perceptron [Rosenblatt 1958] made that unit _learnable_ via supervised gradient updates. Every subsequent major architectural advance — multi-layer networks, backpropagation [Rumelhart et al. 1986], convolutional networks [LeCun et al. 1989], recurrent networks and LSTMs [Hochreiter & Schmidhuber 1997], transformer attention [Vaswani et al. 2017] — has elaborated the same biological reference unit: a weighted-sum-and-non-linearity, modelled on the abstracted point-neuron of the mammalian cerebral cortex.

The architectural creativity within this lineage has been spectacular: dropout, batch normalisation, residual connections, attention, mixture-of-experts, neural ODEs, diffusion. The biological diversity sampled has been minimal. The intelligence-design space implicit in the perceptron lineage is approximately: _combinations of point-neuron-derived units optimised end-to-end against human-relevant tasks_.

The biological reality from which intelligence has actually emerged is far broader. Five non-exhaustive examples:

| Implementation                                     | Found in                                                                                                        | What the perceptron template misses                                                |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Decentralised peripheral cognition                 | Cephalopods (octopus arms) [Hochner 2012]                                                                       | Computation in peripheral ganglia rather than a central cortex                     |
| Acerebrate computation                             | Slime molds [Nakagaki et al. 2000], plants [Trewavas 2014], bacterial communities [Nesin & Chandrankunnel 2025] | Information processing without neurons at all — sometimes without multicellularity |
| Network-level cognition                            | Eusocial insects [Seeley 2010], flocking birds                                                                  | Cognition that is irreducibly multi-agent — no single perceptron computes it       |
| Phase-coded dynamics                               | Many invertebrate brains [Buzsáki 2006]                                                                         | Information in synchrony and timing rather than firing rates                       |
| Closed sensorimotor loops without central planners | Insect navigation [Webb 2002]                                                                                   | Complex behaviour without a controller                                             |

Each row is a real implementation of intelligence in nature, documented in substantial peer-reviewed literature, and barely engaged with by AI research as a _design source_.

The illustrative table is not exhaustive, and the engagement that this paper proposes is no longer purely prospective. The NEXI catalog presented in Section 5 contains, at the time of writing, fifteen architectural patterns drawn from four peer-reviewed sources: research on the social-communication networks of wild zebra finches [Hagedoorn et al. 2026], on the cognitive-capacity limits of non-human animals [Turner et al. 2026], on collective decision-making in bacterial communities without nervous systems [Nesin & Chandrankunnel 2025], and on the cortico-basal ganglia-thalamo-cortical loop as a substrate-general action-selection mechanism conserved across all vertebrates over half a billion years [Nordli & Todd 2022]. These four sources sit at four different positions relative to the table above — network-level cognition, capacity-limited sensory and cognitive integration, acerebrate computation, and vertebrate-deep action selection redeployed motor-to-cognitive via exaptation — and each has produced a coherent _cluster_ of mutually reinforcing patterns rather than a single isolated primitive. The diversity of cluster _shapes_ that has emerged (Section 5) is itself a finding: nature does not assemble adaptive behaviour in one canonical way, and the perceptron lineage has not yet engaged the alternatives at the level of design.

The juxtaposition of two of these sources — the bacterial-molecular case [Nesin & Chandrankunnel 2025] and the vertebrate-CBGTC case [Nordli & Todd 2022] — also resolves a question the table above leaves implicit. Bacteria implement action-selection-like architecture without any nervous system; vertebrates implement an action-selection mechanism on a specific neural substrate (CBGTC) virtually unchanged from lamprey to human. Both are _universal_ within their substrate scale. The position the program takes from this juxtaposition is **substrate-independence-of-architectural-pattern, not substrate-irrelevance**: the architectural function (default-inhibit / selective-disinhibit gating, goal-directed sequence construction, contextual reinforcement) is the substrate-general invariant; the substrate is one parameter among many, and different substrates produce architecturally-equivalent patterns. AI systems matching the architectural pattern are matching nature's deep invariant, regardless of whether the implementation substrate resembles bacterial regulatory networks, cnidarian nerve nets, or vertebrate CBGTC loops. This stance is operationalised as the canonical NEXI `action-selection-as-common-substrate` (Section 5.7) and is the load-bearing position behind the catalog's _embodied-action-selection_ cluster (Section 6.6).

The template pillar's claim is not that the perceptron lineage is wrong. It is that the perceptron lineage represents _one_ sample from the intelligence-design space; that the sample is heavily biased toward mammalian cortical computation; and that the unrepresented portion of the design space contains substantial unexplored value.

A counter-argument deserves explicit response: _biology is not engineering, and architectural primitives derived from biology may not transfer to engineering practice_. This is a real concern. The position taken here is that the transfer must be earned per-pattern, not assumed wholesale — which is why every NEXI in the catalog (Section 5) commits to a falsifiable architectural hypothesis. The template pillar is not a claim that biology should be imitated; it is a claim that biology should be _mined_, with engineering judgement applied to each candidate primitive.

## 3.3 Convergence

The two pillars converge on a single research direction.

The architectural pillar, alone, says: _AI systems need world models, learned from sensory data rather than from text_. This is operationally a constraint on the input modality and the learning objective. It does not, by itself, specify _what kind_ of world model — _what kind_ of internal architecture — should result.

The template pillar, alone, says: _AI's biological inspiration has been narrow; many natural intelligence implementations have been ignored_. This is operationally a constraint on the design space considered. It does not, by itself, specify _which_ implementations to draw from or _how_ to translate them.

Together, the two pillars specify a research direction that neither captures alone:

> **World models should be informed by the _plurality_ of natural intelligence designs documented across species — not by scaling up a single cortical template.**

This is the central thesis of the Nature Intelligence Project. It is operationalised through the methodology developed in Section 4 and the catalog framework presented in Section 5. The convergence is not coincidental: the architectural critique creates a vacuum (we need world models), and the template critique points to where candidate designs may be found (peer-reviewed comparative cognition). Each pillar is necessary; neither is sufficient.

A related framing: the two critiques together rule out two simpler positions. They rule out _scale-only_ (the architectural critique shows scaling does not produce world models). They rule out _pure-architecture-search_ within the perceptron lineage (the template critique shows the lineage is one biased sample of the intelligence-design space). What remains is the joint position taken here.

## 3.4 Falsifiability of the program

A research program of this scope must be falsifiable. The claims of the program operate at three levels, and each level admits independent refutation.

**At the program level.** The architectural pillar's claim is falsifiable in principle: if a system based on token prediction at sufficient scale demonstrably achieves human-level reliability on physical-world tasks with sample efficiency comparable to natural learners, the architectural pillar (in its strong form) is refuted. The template pillar's claim is falsifiable similarly: if perceptron-lineage architectures are demonstrated to span the full intelligence-design space — that is, if architectural primitives derivable from comparative cognition are shown not to exceed the capabilities of perceptron-lineage architectures on relevant tasks — the template pillar is refuted.

**At the cluster level.** Each cluster in NEXI commits to a _system-level falsifiable hypothesis_: a testable claim about the synergistic effect of its member patterns when adopted together. If subsetting a cluster produces no measurable degradation beyond the additive sum of individual-pattern losses, the cluster's synergy claim is refuted. The patterns may still be individually useful; the cluster claim is the load-bearing one. The four clusters introduced in Section 6 each carry a distinct system-level claim and a distinct structural _shape_: the **Distributed Social Cognition** cluster (constellation shape, anchored to wild zebra finch communication) predicts that subsetting its co-dependent patterns degrades referential robustness beyond linear loss; the **Bounded Cognitive Architecture** cluster (pipeline shape, anchored to capacity-limit research) predicts that downstream pattern stages fail without upstream capacity limits being honoured rather than circumvented; the **Acerebrate Decision-Making** cluster (composition shape, anchored to bacterial decision-making) predicts that adaptive collective behaviour is recoverable from a small set of substrate-independent components rather than from any specific molecular implementation; and the **Embodied Action Selection** cluster (isomorphism shape, anchored to vertebrate-CBGTC neuroanatomy [Nordli & Todd 2022]) predicts that an architecture redeploying one well-developed action-selection mechanism across motor and cognitive domains via explicit exaptation outperforms duplicate-module architectures on cross-domain benchmarks at lower marginal cost per added domain. Each system-level claim is independently refutable.

**At the pattern level.** Each individual NEXI commits to a falsifiable architectural hypothesis specifying what is being compared, under what conditions, with what metric, predicting what direction of effect, and what threshold counts as a meaningful effect. The methodology document accompanying the catalog (Section 4) specifies the standard. A pattern whose hypothesis is refuted under appropriate testing is marked deprecated and retained for traceability.

The program is therefore not a single global claim but a structured set of testable sub-claims, each of which can be supported or refuted independently. The overall program is supported when its sub-claims aggregate into evidence; it is refuted when sub-claim refutations accumulate. This structure is deliberate: it allows the catalog to grow incrementally, each entry standing or falling on its own evidence, while the program-level thesis is empirically anchored to the aggregate behaviour of its components.

The next section turns to the methodology that produces those components — how peer-reviewed sources are processed into NEXI entries, with provenance preserved and curation discipline enforced.
