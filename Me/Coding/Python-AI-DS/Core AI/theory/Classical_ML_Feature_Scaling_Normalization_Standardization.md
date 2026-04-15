---

---
# Feature Scaling Techniques
- Feature scaling is applied **column-wise (features), not row-wise (samples)**.  
- It ensures that numerical features are on comparable scales, which improves model convergence, stability, and interpretability.

---
# 1. Normalization (Min–Max Scaling)
### Definition
Rescales data to a fixed range, usually **[0, 1]**.
### Formula
$$
x_{\text{norm}} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
$$
### Output Range
- **[0, 1]** (or any custom range \([a, b]\))
### Characteristics
- Preserves the relative distances between values
- Sensitive to **outliers** (since it depends on min and max)
- Boundaries are fixed
### When to Use
- When features have **known and fixed bounds**
- Image data, pixel intensities
- Distance-based models:
  - KNN
  - K-Means
  - Neural Networks (often with sigmoid activations)

---
# 2. Standardization (Z-Score Normalization using Standard Deviation)
### Definition
Centers the data around zero mean and scales it using **standard deviation**.
### Formula (LaTeX)
$$
z = \frac{x - \mu}{\sigma}
$$
Where:
- $(\mu)$ = mean  
- $(\sigma)$ = standard deviation  
### Output Range
- **Unbounded**
- Practically:
  - ~68% in **[-1, 1]**
  - ~95% in **[-2, 2]**
  - ~99.7% in **[-3, 3]**
### Characteristics
- Mean becomes **0**
- Standard deviation becomes **1**
- Less sensitive to outliers than Min–Max
- Assumes data is approximately **normally distributed**
### When to Use
- Algorithms assuming Gaussian distribution:
  - Linear Regression
  - Logistic Regression
  - SVM
  - PCA
- When features have **different units/scales**

---
# 3. Standardization using Absolute Standard Deviation (Robust Z-Score)
### Definition
A **robust** alternative to Z-score that uses median and absolute deviation.
Commonly referred to as **Robust Scaling**.
### Formula (LaTeX)
$$
z_{\text{robust}} = \frac{x - \text{median}}{\text{MAD}}
$$
Where:
$$
\text{MAD} = \text{median}(|x - \text{median}|)
$$
*(Sometimes scaled by 1.4826 to match standard deviation for normal data)*
### Output Range
- **Unbounded**
- Typically concentrated around **[-2, 2]**
- No strict limits
### Characteristics
- Highly **resistant to outliers**
- Uses median instead of mean
- Better for skewed distributions
### When to Use
- Data contains **extreme outliers**
- Financial data
- Sensor data
- Real-world noisy datasets

---
## 4. Normalization using Decimal Scaling
### Definition
Decimal Scaling normalizes data by shifting the decimal point of values.
The goal is to bring all values into a range where the **maximum absolute value is less than 1**.
### Formula (LaTeX)
$$
x_{\text{scaled}} = \frac{x}{10^j}
$$
Where:
- \(j\) is the **smallest integer** such that:
$$
\max(|x_{\text{scaled}}|) < 1
$$
Equivalently:
$$
j = \lceil \log_{10}(\max(|x|)) \rceil
$$
### Output Range
- Typically:
$$
(-1, 1)
$$
- Not strictly bounded to a fixed interval like Min–Max, but controlled by powers of 10
### Example
Given values:
$$
x = \{120, 45, 3, -89\}
$$

$$
\max(|x|) = 120
\Rightarrow j = 3
$$

$$
x_{\text{scaled}} = \frac{x}{10^3}
$$
Result:
$$
\{0.12, 0.045, 0.003, -0.089\}
$$
### Characteristics
- Very **simple and fast**
- Does **not** depend on mean or variance
- Preserves relative order of values
- **Insensitive to distribution shape**
- Still affected by extreme values (but less than Min–Max)
### When to Use
- Quick, lightweight preprocessing
- When data magnitude varies by powers of 10
- Educational demonstrations of normalization
- Legacy systems or rule-based pipelines
### When *Not* to Use
- Modern ML pipelines requiring statistical grounding
- Algorithms sensitive to variance or distance metrics
- When feature distributions differ significantly

---
# Comparison Summary

| Method                  | Formula Basis  | Output Range | Outlier Sensitivity | Typical Use Case           |
| ----------------------- | -------------- | ------------ | ------------------- | -------------------------- |
| Min–Max Normalization   | Min & Max      | [0, 1]       | High                | Fixed bounds, KNN, K-Means |
| Z-score Standardization | Mean & Std Dev | ~[-3, 3]     | Medium              | Regression, SVM, PCA       |
| Robust Z-score          | Median & MAD   | ~[-2, 2]     | Low                 | Noisy, outlier-heavy data  |
| Decimal Scaling         | Power of 10    | (-1, 1)      | Medium              | Simple magnitude control   |

---
# Rule of Thumb
- **Need strict bounds → Min–Max**
- **Need statistical normalization → Z-score**
- **Outliers dominate → Robust scaling**
- **Just reduce magnitude → Decimal scaling**

---

