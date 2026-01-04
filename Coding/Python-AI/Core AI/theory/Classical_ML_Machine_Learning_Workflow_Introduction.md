# Machine Learning Workflow
- A structured workflow ensures that machine learning models are **reliable, reproducible, and generalizable**.

---
# 1. Data Preprocessing
- **Purpose**: Convert raw data into a **model-ready** format.
### 1.1 Import the Data
- Load data from sources (CSV, databases, APIs, sensors, logs)
- Inspect structure: rows, columns, data types
- Identify target variable and features
### 1.2 Clean the Data
- Handle missing values:
  - Remove rows/columns
  - Impute (mean, median, mode, model-based)
- Remove duplicates
- Fix inconsistent data (typos, units, formats)
- Handle outliers (cap, transform, or remove)
- Encode categorical variables:
  - Label Encoding
  - One-Hot Encoding
### 1.3 Feature Engineering (Optional but Critical)
- Create new features
- Transform features (log, square root, binning)
- Feature scaling:
  - Normalization (Min–Max)
  - Standardization (Z-score)
- Feature selection:
  - Correlation-based
  - Model-based importance
### 1.4 Train–Test Split
- Split dataset into:
  - **Training set** → used to learn parameters
  - **Test set** → used only for final evaluation
- Common splits:
  - 70–30
  - 80–20
- Prevents **data leakage**

---
# 2. Modelling
- **Purpose**: Learn patterns and relationships from data.
### 2.1 Build the Model
- Choose algorithm based on problem type:
  - Regression
  - Classification
  - Clustering
- Define model architecture and hyperparameters
### 2.2 Train the Model
- Fit the model on the training data
- Optimize parameters using a loss function
- Use validation or cross-validation if required
### 2.3 Make Predictions
- Generate predictions on:
  - Validation set (for tuning)
  - Test set (for final evaluation)

---
# 3. Evaluation
- **Purpose**: Measure how well the model generalizes to unseen data.
### 3.1 Performance Metrics
- Regression:
  - MAE, MSE, RMSE, R²
- Classification:
  - Accuracy
  - Precision, Recall, F1-score
  - ROC–AUC
- Clustering:
  - Silhouette Score
  - Inertia
### 3.2 Model Diagnostics
- Bias vs Variance analysis
- Check overfitting and underfitting
- Analyze residuals and error distribution
### 3.3 Make a Verdict
- Is the model good enough for deployment?
- Compare with baseline models
- Decide next steps:
  - Tune hyperparameters
  - Collect more data
  - Try different algorithms

---
# Optional (Production-Oriented Steps)

# 4. Deployment
- Package the model
- Expose via API or batch pipeline
- Integrate with applications

# 5. Monitoring & Maintenance
- Monitor performance drift
- Retrain with new data
- Handle data and concept drift

---
# One-Line Summary

> **Preprocess → Train → Evaluate → Decide → Deploy → Monitor**

---
