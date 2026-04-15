# Batch / Offline Machine Learning

> Train model on a **fixed dataset**, then deploy (no continuous updates)

![[batch_machine_learning.excalidraw|700]]

---
# Core Idea (Why it exists)

- Training is **computationally expensive**
- Easier to:
    - collect data → train once → deploy
- Suitable when data changes **slowly**

---
# Workflow

1. Collect full dataset
2. Train model on entire data
3. Evaluate
4. Deploy
5. Repeat periodically (retraining cycle)

---
# Properties

- Model is **static between retraining cycles**
- Learns only from **historical snapshot**
- Updates are **manual and scheduled**

---
# Problems

- **No real-time learning**
    - Cannot adapt to new patterns immediately
- **Staleness**
    - Model becomes outdated as data distribution changes
- **Retraining cost**
    - Large data → expensive and slow retraining
- **Lag in critical events**
    - Example: sudden economic changes (e.g., demonetization)
    - Model trained earlier has **no awareness**

---
# Real-World Example

- **Netflix recommendation system**
    - New content + user behavior changes daily
    - Static model → outdated recommendations

---
# Practical Workaround

- **Periodic retraining**
    - Daily / weekly retrain → redeploy
- Trade-off:
    - More frequent updates → higher compute cost

---
# Disadvantages (Condensed)

- High compute for large datasets
- Delayed adaptation to new data
- Requires full retraining cycles
- Limited responsiveness to real-world changes

---
# Summary

- Batch learning = **train once, update later**
- Works when:
    - Data is stable
- Fails when:
    - Data changes **continuously or rapidly**

---
