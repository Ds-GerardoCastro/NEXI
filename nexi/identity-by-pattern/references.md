# References — Identity by Pattern

## Primary natural-system literature

- **Hagedoorn, K., Tschirren, N., ter Avest, E., Tyson, C., Snijders, L., Griffith, S. C., Naguib, M., & Loning, H. (2025).** _Communication Networks of Wild Zebra Finches (Taeniopygia castanotis)._ bioRxiv preprint, posted 2025-09-11. DOI: [10.1101/2025.09.11.675577](https://doi.org/10.1101/2025.09.11.675577). License CC-BY-NC-ND 4.0. Unrefereed preprint; observational.
  _Documents individual identification of zebra finches from distinctive song. Pretrained species-level BirdNET embeddings serve as an impartial validator of manually assigned individual IDs (intra < inter cosine distance); the authors call this "a promising approach to scale up" and build no standalone individual classifier._

- **Snijders, L., & Naguib, M. (2017).** _Communication in animal social networks: a missing link?_ Advances in the Study of Behavior, 49, 297–359.
  _Theoretical synthesis on individual signature signals as the basis for acoustic social-network construction._

## Computational analogs

- **Deng, J., Guo, J., Xue, N., & Zafeiriou, S. (2019).** _ArcFace: Additive Angular Margin Loss for Deep Face Recognition._ CVPR 2019.
  _Margin-based loss for explicit within-class discriminability — the dominant approach for face recognition; directly applicable to other particularity-preserving tasks._

- **Schroff, F., Kalenichenko, D., & Philbin, J. (2015).** _FaceNet: A Unified Embedding for Face Recognition and Clustering._ CVPR 2015.
  _Triplet-loss training for identity embeddings — the foundational technique._

- **Desplanques, B., Thienpondt, J., & Demuynck, K. (2020).** _ECAPA-TDNN: Emphasized Channel Attention, Propagation and Aggregation in TDNN Based Speaker Verification._ Interspeech 2020.
  _State-of-the-art speaker re-identification — the closest computational analog to song-based individual ID._

- **Chen, T., Kornblith, S., Norouzi, M., & Hinton, G. (2020).** _A Simple Framework for Contrastive Learning of Visual Representations (SimCLR)._ ICML 2020.
  _Foundational contrastive representation learning. Note the scope: SimCLR performs **augmentation-instance discrimination** — different augmented views of the *same image* are pulled together — as a self-supervised proxy. This is an analogy for, not a drop-in substitute for, **identity-instance discrimination** across genuinely different observations of the same individual (different songs, different sessions), which is what re-identification requires._

## Vault references (private)

- Atomic principles: `P03 — Individual Distinctiveness Enables Network Mapping`, `P09 — Song Individuality Enables Tracking in Nomadic Species`
- Metamodel: `MM4 — Identity Through Distinctive Patterning`
- Source ingestion: `Wild Zebra Finch Communication Networks`
