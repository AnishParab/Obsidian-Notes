# Step 4: **Self Attention**

---
# Why It’s Needed
* Words can have **different meanings** depending on context:

  * **River Bank** → “Bank” means *land beside a river*
  * **ICICI Bank** → “Bank” means *financial institution*
* A model must understand **which other words** in a sentence give meaning to the current word.
  That’s what **Self-Attention** does.

---
# What It Does

Self-Attention allows every token to:
* “Look at” or **attend to** other tokens in the sequence.
* Weigh how **important** each surrounding word is for understanding the current one.

---
# How It Works (Simplified)
1. Each token embedding produces three vectors:
   * **Query (Q)** → What am I looking for?
   * **Key (K)** → What do I contain?
   * **Value (V)** → What information do I offer?

2. For each word:
   * Compute **similarity** between its Query and all other Keys.
   * Assign **attention weights** based on similarity.
   * Combine all Values using these weights to produce a **context-aware vector**.

---
### Example

Sentence: *“The river bank overflowed.”*

* “Bank” pays more attention to “river.”
  Sentence: *“He opened a bank account.”*
* “Bank” pays more attention to “account” and “opened.”

---
# Key Idea

> Self-Attention lets tokens understand meaning **in relation to others**, not in isolation.
> It’s the core mechanism that enables transformers to capture **context**, **disambiguate meaning**, and **process sequences in parallel**.

---



