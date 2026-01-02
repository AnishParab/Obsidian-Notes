# Step 4: Self-Attention (Contextualization)
- **Vector embeddings interact with each other**
- Each token updates its meaning based on **surrounding tokens**
- This produces **context-aware embeddings**

---
# What actually happens (simplified)
- Every word looks at **other words in the sentence**
- It decides **which words are important**
- Its vector is updated to reflect the **correct context**

So embeddings do not just “talk” — they **re-encode meaning using context**.

---
# Example: Word sense disambiguation

### Word: **Bank**

**Sentence 1**
> River bank

→ “bank” attends to **river**  
→ Meaning shifts to _land beside water_

**Sentence 2**
> ICICI bank

→ “bank” attends to **ICICI**  
→ Meaning shifts to _financial institution_

Same word → **different vector representation**.

---
# Key takeaway (important)

> Tokens start with the **same base embedding**, but after self-attention they become **context-specific embeddings**.

> **This is why Transformers understand ambiguity without rules**.

---
