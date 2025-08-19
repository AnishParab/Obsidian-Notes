# What is a Large Language Model (LLM)?
- A **Large Language Model (LLM)** is a type of AI model designed to **generate and understand text**.  
- Built on **neural networks**, trained on massive amounts of data.  
- Unlike simple statistical models, LLMs capture deep patterns in language.

---
# Some Types of Models

## Statistical Models (Before Neural Nets)
- Early models predicted the **next word** using the previous **(n−1) words**.  
- Example: a **bigram model** uses just the last word; a **trigram model** uses the last two words.  
- Limitation: they can’t capture long-range context or meaning.

> **Learn here** : [[Statistical Language Models and NLP]]

---
## Recurrent Neural Networks (RNNs)
- Introduced **hidden state (memory)** to carry information across sequences.  
- Helped capture context better than statistical models.  
- Limitation: struggle with **long sequences** (forgetting earlier context).

---
## Transformer Models (LLMs)
- Introduced in Google’s **“Attention Is All You Need” (2017)** paper.  
- Use **attention mechanisms** to capture relationships between all words in a sequence, regardless of distance.  
- Enabled powerful models like **GPT (Generative Pretrained Transformer)**.  
- Much better at handling **long-range dependencies** and parallel computation.

---
