# Unsupervised Learning

- Learn structure from data with no labels
- Input only: X — no target y
- Goal: discover patterns, groups, or compressed representations

**Why unsupervised**
- Labeled data is expensive; most real-world data is unlabeled
- Model must find signal without a supervisor

---
# Clustering

- Partition data into groups based on similarity/distance
- X → {C₁, C₂, ..., Cₖ}
- No ground truth → evaluation is indirect (silhouette score, inertia)

Examples:
- Customer segmentation (high-spend vs low-spend)
- Student grouping (high IQ + high CGPA cluster together)

Algorithms: 
- K-Means, DBSCAN, Hierarchical Clustering


---
# Dimensionality Reduction

- Compress high-dim data into lower-dim representation while preserving structure
- X_high-dim → X_low-dim

Why needed:
- High dimensions → sparse data, noise amplification, impossible to visualize

Examples:
- Rooms + washrooms → single "size" feature
- PCA on MNIST: 784-dim pixel vectors → 2D plot where digit clusters emerge

Use cases: 
- visualization, compression, noise reduction, preprocessing before supervised learning


---
# Anomaly Detection

- Model the normal distribution of data → flag low-probability deviations
- Rare events don't fit the learned "normal" region

Examples:
- Fraud detection (transaction outside normal spending pattern)
- Network intrusion (traffic spike deviating from baseline)
- Sensor failure (reading outside operational range)

---
# Association Rule Mining

- Discover co-occurrence relationships between items
- Form: A ⇒ B ("if A, then B tends to appear")

Classic example:
- Walmart: customers buying diapers also buy beer → Diapers ⇒ Beer
- Used to optimize shelf placement and bundling

Key metrics:
- Support — how often A and B appear together
- Confidence — P(B | A)
- Lift — confidence / P(B); lift > 1 means A genuinely predicts B

Use cases: 
- market basket analysis, recommendation systems

---
# Common algorithms by technique

| Technique         | Algorithms                                    |
| ----------------- | --------------------------------------------- |
| Clustering        | K-Means, DBSCAN, Hierarchical                 |
| Dim. Reduction    | PCA, t-SNE, UMAP, Autoencoders                |
| Anomaly Detection | Isolation Forest, One-Class SVM, Autoencoders |
| Association Rules | Apriori, FP-Growth                            |

---
