---

---
# Instance-Based Learning

> **Memorization** of dataset.

> **Remember data → compare → decide**

**Formal Definition**
- Stores training data instead of learning a compressed model
- Makes predictions by **comparing new data with stored examples**

---
# How It Works


![[knn_instnce_based_learning.excalidraw|700]]

- Keep all data points (Memorize)
- For a new input:
    - Find similar points using a distance function
    - Use those points to decide output (e.g., majority vote)

---
# Key Properties

- Training: minimal (just store data)
- Inference: slow (search through data)
- Memory: high
- Adaptation: easy (add new data directly)

---
# Example

- k-Nearest Neighbors (k-NN)

---
# Failure Modes

- High dimensions → distance becomes unreliable
- Large data → slow predictions
- Sensitive to noise
- Depends heavily on distance metric

---
