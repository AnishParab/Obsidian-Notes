# Deep Learning vs Machine Learning

## Data Dependency
- **Machine Learning**
    - Performs well with **small to medium-sized datasets**
    - Relies on manually engineered features
- **Deep Learning**
    - Requires **large amounts of data** to generalize well
    - Performance improves significantly as data size increases

![[deep_vs_machine_loearning.excalidraw|500]]

> **Conclusion:**  
> Machine Learning is suitable for limited data, while Deep Learning scales better with large datasets.

---
## Hardware Dependency
- **Machine Learning**
    - Can often run on CPUs
    - Lower memory and compute requirements
- **Deep Learning**
    - Requires **powerful GPUs/TPUs**
    - High memory usage due to large models and matrix multiplications

> Deep learning is computationally expensive by design.

---
## Training Time
- **Machine Learning**
    - Faster training time
    - Simpler models, fewer parameters
- **Deep Learning**
    - **Significantly longer training time**
    - Millions to billions of parameters
    - Training time increases with data and model size

---
## Prediction (Inference) Time
- **Deep Learning**
    - Usually **fast at inference** once trained
    - Optimized for batch and parallel execution
- **Machine Learning**
    - Varies by algorithm
    - Example: **KNN** is slow at prediction because it compares with the entire dataset

---
## Feature Selection
- **Machine Learning**
    - Requires **manual feature engineering**
    - Example: selecting academic scores, experience, skills explicitly
- **Deep Learning**
    - Performs **automatic feature extraction**
    - Learns hierarchical representations directly from raw data

> Feature learning is a **core advantage** of deep learning.

---
## Interpretability
- **Machine Learning**
    - Many models are **interpretable** (linear regression, decision trees)
	- Improves interpretability by **Decision Trees**.
- **Deep Learning**
    - Generally **not interpretable**
    - Often described as a **black box**
    - Learned features are abstract and difficult to explain

> Lack of interpretability is a **major limitation** of deep learning, especially in critical domains (healthcare, finance).

---
# Summary Table

| Aspect              | Machine Learning    | Deep Learning    |
| ------------------- | ------------------- | ---------------- |
| Data Requirement    | Low–Medium          | High             |
| Hardware            | CPU sufficient      | GPU/TPU required |
| Training Time       | Short               | Long             |
| Inference Time      | Algorithm dependent | Usually fast     |
| Feature Engineering | Manual              | Automatic        |
| Interpretability    | High                | Low (Black box)  |

---
# One-Line Summary

> **Machine Learning relies on human-designed features and works well with limited data, whereas Deep Learning learns features automatically and excels with large data at the cost of computation and interpretability.**

---
