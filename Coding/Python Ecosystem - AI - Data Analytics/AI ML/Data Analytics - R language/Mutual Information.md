**Definition:**  
Mutual Information (MI) measures the amount of information shared between variables.  
It generalizes the concept of correlation using **Kullback–Leibler Divergence**.

---
# Feature Selection Using MI
- **Scenario:**  
  - Three features \( X, Y, Z \).  
  - Goal: Select 2 features that provide **most information**.  
- **Principle:**  
  - If \( X \) and \( Y \) are correlated, much of the information in \( Y \) is already contained in \( X \).  
  - Prefer selecting **uncorrelated features** to maximize information coverage.

---
# Extension
- Can be extended to \( n \) variables:  
  - Evaluate how much information variables \( x_1, \dots, x_n \) provide about variable \( x_{n+1} \).  
- Useful in **both supervised and unsupervised** feature selection scenarios.

---
