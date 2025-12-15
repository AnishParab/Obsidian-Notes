# Pre-requisite
[[Self Attention]]

---
# Multi-Head Attention Mechanism

**Definition:**
Multi-head attention is an extension of self-attention that allows the model to focus on **different parts of the input simultaneously**. Instead of computing one set of attention weights, it computes several in parallel — called “heads.”

---
# Why It’s Needed
* A single attention head can only capture **one type of relationship** (e.g., subject–verb).
* Multi-head attention lets the model learn **different contextual relationships** at once (e.g., syntax, meaning, position).

---
# How It Works
1. The input embeddings are projected into multiple sets of **Query (Q)**, **Key (K)**, and **Value (V)** vectors — one set per head.
2. Each head performs **self-attention independently**, producing its own output.
3. All heads’ outputs are **concatenated** and passed through a final linear layer to combine information.

---
# Formula (Conceptual)
$$
[
\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1, \text{head}_2, ..., \text{head}_h) W^O
]
$$

where each head is:
$$
[
\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)
]
$$

---
# Intuition
* **Each head = a unique “perspective.”**

  * One head might focus on nearby words.
  * Another might focus on long-range dependencies.
  * Another might capture relationships between entities or time steps.

---
# Example
Sentence: *“The river bank overflowed after the rain.”*

* **Head 1:** Connects “bank” ↔ “river.”
* **Head 2:** Connects “overflowed” ↔ “after.”
* **Head 3:** Connects “rain” ↔ “river.”

Each head sees context differently, and combining them gives a richer understanding.

---

