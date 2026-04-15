# Out of Core Learning

> Train on datasets that **do not fit into memory** by processing them in chunks

![[out_of_core_learning.excalidraw|700]]

---
# Core Problem

- Batch learning assumes **entire dataset fits in RAM**
- Large datasets → memory constraint → cannot load all at once

---
# Key Idea (Why it works)

- Break dataset into **small chunks (mini-batches)**
- Load → train → discard → repeat
$$
\text{Data} = {B_1, B_2, ..., B_n}  
$$
- Each batch updates the model incrementally

---
# How It Works

1. Read chunk from disk
2. Train model on chunk
3. Update parameters
4. Discard chunk from memory
5. Repeat for next chunk

> Conceptually: **online learning applied in an offline setting**

---
# When to Use

- Dataset size > RAM
- Disk-based or distributed datasets
- Large-scale logs, images, or text corpora

---
# Advantages

- **Memory efficient**
- Enables training on **very large datasets**
- Compatible with incremental algorithms

---
# Disadvantages / Failure Modes

- **Order sensitivity**
    - Data order can affect learning
- **Slower training**
    - Disk I/O bottleneck
- **Hyperparameter sensitivity**
    - Batch size and learning rate matter more
- **Not all algorithms support it**
    - Requires incremental/partial-fit capability

---
# Relation to Other Paradigms

- Batch learning → full data in memory
- Online learning → streaming data
- Out-of-core → **batch data, but streamed from disk**

---
# Summary

- Out-of-core = **handle large data via chunked training**
- Uses **incremental updates without loading full dataset**
- Trade-off: **scalability vs speed and stability**

---
