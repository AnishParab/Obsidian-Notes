# Semi-Supervised Learning

- Learn from a small labeled set + large unlabeled set
- Few labeled (X, y) + Many unlabeled (X)

**Why labels are the bottleneck**
- Labels: expensive — require human annotation, expert judgment
- Inputs: cheap — scraped, recorded, collected at scale
- Semi-supervised closes that gap

**Why it works**
- Unlabeled data reveals the underlying data distribution and structure
- Labeled data anchors the correct output mapping onto that structure
- Together: better generalization than labeled data alone

**Real-world examples**
- Image classification — few labeled images, millions unlabeled from the internet
- Speech recognition — limited transcribed audio, massive raw recordings
- Medical imaging — few expert-labeled scans, many unlabeled ones
- Spam detection — few labeled emails, massive unlabeled inbox

---
# Common techniques
- Pseudo-labeling — model predicts labels for unlabeled data → treats predictions as ground truth → retrains
- Consistency regularization — same input under different perturbations should produce same output (FixMatch, MixMatch)
- Graph-based methods — build similarity graph over all data → propagate known labels to nearby unlabeled nodes

**Failure modes**
- Wrong pseudo-labels → error amplification through retraining loops
- Poor data distribution → unlabeled data misleads rather than helps
- Imbalanced labeled set → model inherits and amplifies that bias

---
# When it works vs when it doesn't

| Works well                                 | Breaks down                                         |
| ------------------------------------------ | --------------------------------------------------- |
| Data has strong cluster/manifold structure | Data is noisy or highly irregular                   |
| Small labeled set is representative        | Labeled set is biased or too small to anchor        |
| Unlabeled data is from same distribution   | Distribution mismatch between labeled and unlabeled |

---
