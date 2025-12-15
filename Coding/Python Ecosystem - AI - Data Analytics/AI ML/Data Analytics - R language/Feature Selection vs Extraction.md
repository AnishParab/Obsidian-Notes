# Feature Selection vs Feature Extraction

# 1. Feature Selection
- **Definition:** Choosing the most important \( k < d \) features and ignoring the remaining \( d - k \).  
- **Method:** Subset selection algorithms.  
- **Goal:** Retain the most informative features while reducing dimensionality.  

---
# 2. Feature Extraction
- **Definition:** Transform the original features \( x_i, i = 1, \dots, d \) into a new set of \( k < d \) dimensions \( z_j, j = 1, \dots, k \).  
- **Techniques:**  
  - Principal Component Analysis (PCA)  
  - Linear Discriminant Analysis (LDA)  
  - Factor Analysis (FA)  
- **Goal:** Combine or project features to reduce dimensionality while preserving information.

---
# Usage
1. Start with data of dimension \( d \).  
2. Reduce dimensionality to \( k < d \).  
   - **Discard** unimportant features (selection).  
   - **Combine** features (extraction).  
3. Use resulting \( k \)-dimensional dataset for:  
   - **Classification:** Learning parameters for probability-based models.  
   - **Regression:** Learning parameters for predictive models.

---
