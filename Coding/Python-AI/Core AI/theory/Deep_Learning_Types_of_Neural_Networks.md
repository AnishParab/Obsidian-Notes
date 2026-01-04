# Types of Neural Networks

## 1. Artificial Neural Network (ANN)
- Also called **Fully Connected Network** or **Dense Network**
- Neurons in one layer are connected to **all neurons in the next layer**
- Best suited for:
    - Tabular data
    - Simple regression and classification
- Does **not** exploit spatial or temporal structure

**Example use cases**
- House price prediction
- Credit risk scoring

---
## 2. Convolutional Neural Network (CNN)
- Designed to process **grid-like data**
- Uses **convolutions** to capture local patterns
- Exploits **spatial structure**

**Commonly used for**
- Images (primary use)
- Audio spectrograms
- Video frames

**Key ideas**
- Local connectivity
- Weight sharing
- Translation invariance

---
## 3. Recurrent Neural Network (RNN)
- Designed for **sequential data**
- Maintains a **hidden state** (memory)
- Output depends on current input **and past inputs**

**Commonly used for**
- Speech
- Text
- Time-series data

**Variants**
- LSTM (Long Short-Term Memory)
- GRU (Gated Recurrent Unit)

---
## 4. Generative Adversarial Network (GAN)
- Consists of **two neural networks**:
    - **Generator** → creates fake data
    - **Discriminator** → distinguishes real vs fake
- Trained in an **adversarial setup**

**Used for**
- Image generation
- Audio synthesis
- Style transfer

> GANs **do not usually generate text** effectively due to discrete token sampling.

---
# Compact Comparison Table

| Network | Data Type            | Key Strength             |
| ------- | -------------------- | ------------------------ |
| ANN     | Structured / Tabular | General-purpose modeling |
| CNN     | Spatial data         | Local feature extraction |
| RNN     | Sequential data      | Temporal dependencies    |
| GAN     | Data generation      | Realistic synthetic data |

---
# Important Conceptual Note
- **ANN, CNN, RNN** → primarily **predictive models**
- **GAN** → **generative model**
- Architecture choice depends on **data structure**, not task name

---
# One-Line Summary

> **Different neural network architectures exist to exploit different data structures—spatial, sequential, or generative.**

---
