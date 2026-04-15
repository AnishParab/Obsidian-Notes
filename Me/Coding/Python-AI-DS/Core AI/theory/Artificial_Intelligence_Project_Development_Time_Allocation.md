# Project Development Time Allocation

- Data quality work dominates ML project time — most issues trace back to bad data, not bad models

**Typical time allocation**

| Phase                                 | Time |
| ------------------------------------- | ---- |
| Data collection, cleaning, refinement | ~60% |
| Feature engineering & preprocessing   | ~15% |
| Model selection & training            | ~10% |
| Evaluation & iteration                | ~10% |
| Deployment & monitoring               | ~5%  |

---
# Why data dominates

> Garbage in → garbage out: model quality is bounded by data quality

- Cleaning, deduplication, labeling, and distribution checks are slow and manual
- Feature engineering requires domain understanding, not just code

---
# **Gotcha**

- Beginners invert this — spend 60% on model tuning, 10% on data
- Result: marginal model improvements on fundamentally flawed data

---
