# Step 5: Multi-Head Attention
- **Multi-head attention** runs **self-attention multiple times in parallel** using different learned projections.
- Each head looks at the **same sentence**, but focuses on **different relationships**.

---
# Why it exists
A single attention pass is too limited.

Multiple heads allow the model to:
- Track **meaning**
- Track **grammar**
- Track **long-range dependencies**
- Track **local relationships**
All at the same time.

---
# What actually happens (step-by-step)
1. Start with the **same token embeddings**
2. Split them into **multiple heads**
3. Each head:
    - Computes its own **Q, K, V**
    - Attends to different tokens
4. Outputs from all heads are:
    - **Concatenated**
    - **Linearly mixed**

Result → a richer representation.

---
# Intuition

> One head asks _“What does this word refer to?”_  
> Another asks _“What is its grammatical role?”_  
> Another asks _“What relates across long distance?”_

---
# Example: “Bank”

Sentence:

> ICICI bank approved the loan

Possible heads:
- **Head 1** → focuses on _ICICI_ (entity meaning)
- **Head 2** → focuses on _approved_ (action relation)
- **Head 3** → focuses on _loan_ (financial context)

All confirm: **bank = financial institution**.

---
# Key difference from self-attention

- **Self-attention**: one view
- **Multi-head attention**: many views in parallel

---
