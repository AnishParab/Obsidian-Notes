# Vector Embeddings

### Definition
Vector embeddings are **numerical representations** of data (text, images, etc.) that capture **semantic meaning** and **relationships** between items in a continuous vector space.

---
### Key Idea
- Each input (e.g., a word, sentence, or document) is mapped to a **high-dimensional vector**.
- These vectors encode **contextual meaning** — words or items with similar meanings have vectors that are **close together** in that space.

---
### Examples

| Text                                               | Semantic Relationship                                                   |
| -------------------------------------------------- | ----------------------------------------------------------------------- |
| “The **dog** ate a **cat**.”                       | “dog” and “cat” share animal context.                                   |
| “A **mobile** is less powerful than a **laptop**.” | “mobile” and “laptop” are related as electronic devices.                |
| “**Paris**” → “**Eiffel Tower**”                   | “**India**” → “**India Gate**” — both show city–landmark relationships. |

---
# Note
[Tensorflow Vector Embedding of all words](https://projector.tensorflow.org/)

---

![[vector_embedding_visualization.excalidraw|700]]

---
## Purpose
- Adds **real-world meaning** to tokens beyond surface text.
- Enables machines to understand **similarity**, **analogy**, and **context**.
- Foundation for **semantic search**, **recommendation systems**, **clustering**, and **LLM reasoning**.

---
## In Summary

> A **vector embedding** converts symbolic data into **mathematical meaning**, allowing models to measure similarity and context numerically.

---
