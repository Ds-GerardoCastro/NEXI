# References — Niche Specification

## Primary natural-system literature (multi-source)

This is the catalog's first **multi-source** NEXI: two independent biological sources converge on niche-conditional cognitive design.

- **Turner, C. R., Russek, E. M., Seed, A., McEwen, E. S., Vélez, N., Morgan, T. J. H., & Griffiths, T. L. (2026).** _Cognitive capacity and control in the evolution of intelligence._ bioRxiv preprint, posted 2026-03-09. DOI: [10.1101/2026.03.07.710317](https://doi.org/10.1101/2026.03.07.710317). License CC-BY 4.0.
  _Mathematical model with explicit "information-processing niches" framing. Niche conditions (task complexity, cue reliability, metabolic-energy availability) translate into the metabolic-cost-to-recall-benefit ratio that places a species in a regime. Specialisation emerges via canalisation of an initially domain-general substrate under niche pressure._

- **Hagedoorn, K., Tschirren, N., ter Avest, E., Tyson, C., Snijders, L., Griffith, S. C., Naguib, M., & Loning, H. (2026).** _Communication Networks of Wild Zebra Finches (Taeniopygia castanotis)._ bioRxiv preprint, posted 2026-04-27. DOI: [10.1101/2025.09.11.675577](https://doi.org/10.1101/2025.09.11.675577). License CC-BY-NC-ND 4.0.
  _Wild ethological documentation of fission-fusion social architecture as niche-conditional response to arid-zone non-stationarity. Same signal type (song) takes different functions in different contexts (breeding-colony vs. social-hotspot vs. dawn). Independent biological evidence that cognition is shaped by ecological niche, not abstracted from it._

The methodological convergence — formal evolutionary modelling and wild ethology arriving at compatible niche-binding claims — is non-trivial and load-bearing for this NEXI's elevation to multi-source status.

## Comparative-cognition / niche-binding context

- **Sterelny, K. (2003).** _Thought in a Hostile World: The Evolution of Human Cognition._ Blackwell Publishing.
  _Cognition as response to environmental challenge — niche-binding articulated in evolutionary-ecological terms._
- **Pinker, S. (2010).** _The cognitive niche: coevolution of intelligence, sociality, and language._ PNAS 107, 8993–8999.
  _The "cognitive niche" framing — explicitly names the niche as the unit cognitive design fits._
- **Sol, D. (2009).** _Revisiting the cognitive buffer hypothesis for the evolution of large brains._ Biology Letters 5, 130–133.
- **Lefebvre, L., Reader, S. M., & Sol, D. (2004).** _Brains, innovations and evolution in birds and primates._ Brain, Behavior and Evolution 63, 233–246.
  _Brain expansion as response to niche-specific demands — innovation, social learning, ecological complexity._
- **Henrich, J. (2015).** _The Secret of Our Success: How Culture is Driving Human Evolution, Domesticating Our Species, and Making Us Smarter._ Princeton University Press.
- **Heyes, C. (2018).** _Cognitive Gadgets: The Cultural Evolution of Thinking._ Harvard University Press.
- **Laland, K., & Seed, A. (2021).** _Understanding human cognitive uniqueness._ Annual Review of Psychology 72, 689–716.
  _Cultural-niche framing — niche-binding extended to include the cumulative cultural environment, not just the physical one._

## Ecological validity in cognitive science

- **Brunswik, E. (1956).** _Perception and the Representative Design of Psychological Experiments._ University of California Press.
  _Foundational argument that cognitive performance in artificial laboratory tasks does not necessarily transfer to ecologically valid contexts. The historical antecedent of the niche-specification claim._
- **Neisser, U. (1976).** _Cognition and Reality: Principles and Implications of Cognitive Psychology._ W. H. Freeman.
  _Direct successor to Brunswik in cognitive psychology; the argument that cognition must be studied in its niche, not abstracted away._

## No-Free-Lunch and domain-adaptation grounding

- **Wolpert, D. H., & Macready, W. G. (1997).** _No free lunch theorems for optimization._ IEEE Transactions on Evolutionary Computation 1, 67–82.
  _Formal statement that no algorithm performs best across all problem distributions. The mathematical version of the niche-binding claim — and the strongest theoretical grounding for the niche-specification step. If NFL holds, generic-purpose architectures are necessarily sub-optimal for any specific niche._
- **Quiñonero-Candela, J., Sugiyama, M., Schwaighofer, A., & Lawrence, N. D. (Eds.) (2009).** _Dataset Shift in Machine Learning._ MIT Press.
  _Decades of work on the failure modes of architectures deployed outside their training distribution. Niche specification is the prescriptive flip of the dataset-shift descriptive literature._

## Benchmark design and evaluation framing

- **Srivastava, A., et al. (2022).** _Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models (BIG-Bench)._ arXiv:2206.04615.
- **Liang, P., et al. (2022).** _Holistic Evaluation of Language Models (HELM)._ arXiv:2211.09110.
  _Recent attempts to systematise benchmark coverage. The niche-specification NEXI argues benchmark design should be primary (niche-driven), not retrospective (model-driven). BIG-Bench and HELM are partial steps in that direction._

## Computational analogs in deployment-context-aware ML

- Production ML practice increasingly distinguishes development from deployment metrics; deployment-context awareness is becoming a structured engineering concern. Model cards (Mitchell et al. 2019, _Model Cards for Model Reporting_) and data sheets (Gebru et al. 2018, _Datasheets for Datasets_) are upstream of the niche specification in this NEXI but stop short of being the typed input to architecture decisions.
  - **Mitchell, M., et al. (2019).** _Model Cards for Model Reporting._ FAT\* 2019.
  - **Gebru, T., et al. (2018).** _Datasheets for Datasets._ arXiv:1803.09010.

## Theoretical grounding for the AGI critique

- The niche-specification NEXI takes a strong stance: AGI as currently framed (general intelligence abstracted from environment) is structurally incoherent if cognition is niche-bound. The argument has antecedents in:
  - **Searle, J. (1980).** _Minds, brains, and programs._ Behavioral and Brain Sciences 3, 417–457.
    _The Chinese Room argument is partially a niche-binding argument — symbol manipulation abstracted from grounded niche fails to produce understanding._
  - **Dreyfus, H. (1972).** _What Computers Can't Do._ MIT Press.
    _Phenomenological critique of disembodied cognition; an early niche-binding argument applied to AI._

  These are philosophical grounding rather than empirical evidence; cited for completeness in the broader argument but not load-bearing for the falsifiable hypothesis.

## Vault references (private)

- Source ingestions: `Cognitive Capacity and Control in the Evolution of Intelligence`, `Wild Zebra Finch Communication Networks` (sources/)
- Atomic principles: `P06 — Environmental Unpredictability Drives Social Strategy`, `P07 — Context-Dependent Song Function`, `P11 — Dynamic Social Structure as Evolutionary Adaptation`, `P18 — Three Cognitive Regimes Across Species`, `P19 — Metabolic Energy as Evolutionary Constraint`, `P23 — Task Compressibility Shapes Cognitive Design`, `P24 — Domain-General vs Domain-Specific Cognition Trade-off` (principles/)
- Per-source analyses: `Analysis — Cognitive Capacity and Control in the Evolution of Intelligence`, `Analysis — Zebra Finch Communication Networks` (analyses/)
- Metamodels analyses: `Metamodels — Cognitive Capacity and Control in the Evolution of Intelligence` (MM5 — Niche-Conditional Cognition), `Metamodels — Zebra Finch Communication Networks` (MM7 — Niche-Bound Cognition) (analyses/)
- Consolidation hub: `Niche-Bound Cognition` (concepts/) — the multi-source consolidation hub from which this NEXI draws its evidence
