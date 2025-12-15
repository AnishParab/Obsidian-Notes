# Histogram
``` python
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

data = np.random.normal(100, 20, 1000)

# Histogram
plt.hist(data, bins=20, color='purple')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Histogram")
plt.show()
```

---
# What is a Histogram ?
- A histogram is a chart that shows how data is distributed by grouping values into bins and displaying the frequency of each bin as a bar. It’s used to understand the shape, spread, and central tendencies of numerical data.

---
# `random.normal` in NumPy

`np.random.normal` 
- It generates random numbers drawn from a **normal (Gaussian) distribution**.

Key points:
* The normal distribution is defined by a **mean** (`loc`) and **standard deviation** (`scale`).
* You can also specify the **size** (shape) of the output array.

Function signature:
```python
np.random.normal(loc=0.0, scale=1.0, size=None)
```

Meaning:
* `loc` → mean of the distribution
* `scale` → standard deviation
* `size` → number of samples or shape of the array

Examples:
* `np.random.normal()` → one sample from N(0, 1)
* `np.random.normal(5, 2, 100)` → 100 samples from a normal distribution with mean 5 and std dev 2
* `np.random.normal(0, 1, (3, 4))` → 3×4 array of Gaussian samples


---
