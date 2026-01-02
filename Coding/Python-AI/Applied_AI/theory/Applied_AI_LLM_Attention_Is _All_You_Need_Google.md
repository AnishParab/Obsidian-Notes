# Attention Is All You Need

> [Attention is all you need](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)

---
# Architecture
![Image](https://towardsdatascience.com/wp-content/uploads/2020/11/1ZCFSvkKtppgew3cc7BIaug.png)


---
# What it is
**“Attention Is All You Need” (2017)** introduced the **Transformer** architecture, showing that **attention alone** (without RNNs or CNNs) is sufficient for sequence modeling tasks like machine translation.

---
# Key idea
Replace recurrence and convolution with **self-attention**, enabling:
- Parallel processing of tokens
- Better long-range dependency modeling
- Faster training

---
# Architecture Components
### 1. Input Embedding
- Converts each **token ID** into a dense vector
- Similar words get similar vectors
- This is what the model actually works with

**Think:** numbers → meaning-like vectors

---
### 2. Positional Encoding
- Adds **order information** (since Transformers have no sequence memory)
- Without this, “dog bites man” = “man bites dog”

**Think:** tells the model _where_ each word is

---
### 3. Self-Attention
- Each word looks at **other words in the sentence**
- Decides which words matter more for understanding the current word

**Example:**  
In “The animal didn’t cross the street because **it** was tired”  
→ “it” attends more to “animal”

---
### 4. Multi-Head Attention
- Runs self-attention **multiple times in parallel**
- Each head focuses on different relationships:
    - Grammar
    - Meaning
    - Long-range links

**Think:** multiple perspectives at once

---
### 5. Feed-Forward Network (FFN)
- A small neural network applied **independently to each token**
- Refines the information after attention

**Think:** per-word thinking step

---
### 6. Add & Layer Normalization
- **Residual connection (Add):** keeps original information
- **LayerNorm:** stabilizes training

**Think:** don’t forget what you already knew; stay numerically stable

---
### 7. Encoder Stack
- All the above layers are stacked multiple times
- Each layer builds **deeper understanding**

**Think:** rereading the sentence multiple times

---
### 8. Decoder (for generation models)
- Similar to encoder but with **masked self-attention**
- Prevents looking at future words while generating text

**Think:** write one word at a time without cheating

---
### 9. Output Linear + Softmax
- Converts final vectors into **probabilities over vocabulary**
- Chooses the next token

**Think:** which word comes next?

---
