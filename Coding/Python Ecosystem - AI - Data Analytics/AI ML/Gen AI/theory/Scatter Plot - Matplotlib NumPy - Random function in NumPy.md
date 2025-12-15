# Scatter Plot
``` python
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)

# Scatter plot
plt.scatter(x, y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter plot")
plt.show()
```

---
# What is a Scatter Plot ?
- A scatter plot is a chart that displays individual data points as dots on an x–y coordinate plane. It’s used to show the relationship or correlation between two numerical variables, highlighting patterns, clusters, or outliers without connecting the points.

---
# `random.rand()` in NumPy

**`np.random`**
- This is the module that provides functions for generating random numbers. It includes many routines: uniform, normal, integers, permutations, etc. It’s the namespace for NumPy’s random utilities.

**`np.random.rand`**
- This is a specific function inside `np.random`.
- It generates random floating-point numbers in the interval **[0, 1)** from a uniform distribution.
- Its arguments specify the shape of the output array.

**Example**:
* `np.random.rand(100)` → 1D array of 100 random floats in [0, 1).
* `np.random.rand(3, 4)` → 3×4 array of random floats in [0, 1).

---
