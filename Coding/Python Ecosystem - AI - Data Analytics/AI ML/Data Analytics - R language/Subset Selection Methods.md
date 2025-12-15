# 1. Forward Search
- **Process:**  
  1. Start with an **empty set** of features.  
  2. For each remaining feature, estimate its effect on **classification/regression error**.  
  3. Add the feature that gives the **maximum improvement**.  
  4. Repeat until **no significant improvement** occurs.  

- **Goal:** Incrementally build a feature set that improves model performance.

---
# 2. Backward Search
- **Process:**  
  1. Start with the **full set of features** (size \( d \)).  
  2. Remove features with the **smallest impact** on validation error.  
  3. Repeat until further removal degrades performance significantly.  

- **Goal:** Reduce feature set size while maintaining model accuracy.

---