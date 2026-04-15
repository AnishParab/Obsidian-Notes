# Supervised Learning

- Learn a mapping f(X) → y from labeled data
- Every training example has a known input X and correct output y
- The model adjusts parameters to minimize error between predicted and actual y

**Why "supervised"**
- A "supervisor" (the labels) provides ground truth signal
- Learning = reduce the gap between f(X) and y over the training set

**Example Dataset**

| IQ  | CGPA | Placement |
| --- | ---- | --------- |
| 87  | 7.1  | Y         |
| 111 | 8.9  | Y         |
| 75  | 6.3  | N         |

- Inputs (X): IQ, CGPA
- Output (y): Placement

---
## Two subtypes based on output type

**Regression**
- Output is continuous: y ∈ ℝ
- Model predicts a value on a number line
- Error measured by distance (MSE, MAE)
- Examples: predict salary from experience, house price from features

**Classification**
- Output is discrete: y ∈ {classes}
- Model outputs probabilities over classes → pick highest
- Error measured by cross-entropy or accuracy
- Examples: Placement (Y/N), spam detection

**Key Distinction**

| Type           | Output     | Error Metric  | Example            |
| -------------- | ---------- | ------------- | ------------------ |
| Regression     | Continuous | MSE, MAE      | Price, temperature |
| Classification | Discrete   | Cross-entropy | Yes/No, labels     |

**Common algorithms**
- Regression: Linear Regression, Ridge, Lasso, SVR
- Classification: Logistic Regression, SVM, Decision Trees, KNN, Naive Bayes

---
