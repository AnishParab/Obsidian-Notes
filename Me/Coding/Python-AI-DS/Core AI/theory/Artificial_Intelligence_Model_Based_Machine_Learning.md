# Model-based Machine Learning

> **Generalizing** the dataset.

> **Learn pattern → store model → apply directly**

**Formal definition**
- Learns a **compressed representation (model)** from data
- Makes predictions using **learned parameters**, not stored examples

---
# How it works

![[modle_based_learning.excalidraw|700]]

- **Need not** keep all data points
- Train on dataset to learn parameters
- Model captures patterns:
- For a new input:
    - Directly compute output using the model

---
# Key Properties

- Training: computational (optimization required)
- Inference: fast (constant-time per input)
- Memory: low (store only parameters)
- Adaptation: requires retraining or incremental updates

---
# Examples

- Linear Regression
- Logistic Regression
- Decision Trees
- Neural Networks

---
# Failure Modes

- Underfitting (model too simple)
- Overfitting (memorizes noise in training)
- Model misspecification (wrong assumptions)
- Requires retraining under distribution shift

---
