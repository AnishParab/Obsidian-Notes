---

---
# Feed Forward Layer
* A **fully connected neural network** applied to each token’s output from the attention layer.
* It processes information **independently for each position**.
* Purpose: introduce **non-linearity** and enable the model to learn complex transformations.

**Simplified formula:**
$$
[
\text{FFN}(x) = \text{ReLU}(xW_1 + b_1)W_2 + b_2
]
$$

---
# Linear Layer
* A **linear transformation** maps the processed embeddings to a **logit vector** — one score per possible token in the vocabulary.
* This produces a **probability matrix** that represents how likely each token is to appear next.

**Conceptually:**
$$
[
\text{logits} = xW_{\text{vocab}} + b
]
$$
where $$ ( W_{\text{vocab}} ) $$ connects hidden representations to vocabulary tokens.

---
# Softmax Layer
* Converts raw logits into **probabilities** that sum to 1.
* Ensures the model predicts the **most likely next token** while still maintaining all probabilities.

**Formula:**
$$
[
P_i = \frac{e^{z_i}}{\sum_j e^{z_j}}
]
$$
where $$ ( z_i ) $$ is the logit for token *i*.

---
### Key Properties:
* Emphasizes high scores (makes the most probable token dominate).
* **Tunable:** via the *temperature* parameter —

  * Lower temperature (<1) → sharper, more confident outputs.
  * Higher temperature (>1) → more random, exploratory outputs.

---
### End-to-End Flow in a Transformer:
1. **Attention Layer:** understands context.
2. **Feed Forward Network:** refines meaning per token.
3. **Linear Layer:** maps to vocabulary space.
4. **Softmax:** chooses the next most probable token.

---

