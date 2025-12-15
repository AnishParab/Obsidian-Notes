---

---
# Why They’re Needed
* Sentences like:
  * **Dog ate Cat**
  * **Cat ate Dog**
    contain the same tokens but have **different meanings** due to **word order**.
* Plain **vector embeddings** alone do not encode sequence order, so the model cannot distinguish between the two without **positional information**.

---
# Step 1: Tokenization

| Word | Token ID |
| ---- | -------- |
| Dog  | 56       |
| ate  | 74       |
| Cat  | 89       |

---
# Step 2: Vector Embedding
Each token is converted into a high-dimensional vector representing its semantic meaning — but **order is still missing**.

---
# Step 3: Positional Encoding
Adds **position information** to each token vector so the model understands **sequence structure**.

| Token | Position | Meaning     |
| ----- | -------- | ----------- |
| Dog   | 0        | First word  |
| ate   | 1        | Second word |
| Cat   | 2        | Third word  |

If you swap positions (e.g., “Cat ate Dog”), the positional encodings change, altering the sentence’s meaning numerically.

---
# Concept
Positional encoding injects **order awareness** into transformer models by combining:
* **Token embedding** (semantic meaning)
* **Positional embedding** (word order)

Together they form a complete representation of **what** each word is and **where** it occurs.

---
