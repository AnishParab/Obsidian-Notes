# Importance of Train–Test Split in Data Preprocessing
- Splitting data into **training** and **testing** sets is essential to evaluate how well a model generalizes to unseen data.

---
# Training Set
- Used to **learn patterns** from the data.
- Model parameters (weights, coefficients) are fitted only on this data.
- Typically contains **70–80%** of the dataset.

---
# Test Set
- Used to **evaluate** the trained model.
- The model **never sees** this data during training.
- Typically contains **20–30%** of the dataset.

> We compare the model’s predictions on the test set with the **actual values** to measure performance (accuracy, MSE, precision, recall, etc.).

---
# Why This Split Matters
- Prevents **overfitting** from going unnoticed.
- Gives an **unbiased estimate** of real-world performance.
- Ensures the model learns **general patterns**, not memorized data.

---
# Key Rule
**Never preprocess (scale, encode, impute) using the full dataset.**  
Always:
1. Split the data
2. Fit preprocessing on the **training set**
3. Apply it to the **test set**

This avoids **data leakage**.

---
