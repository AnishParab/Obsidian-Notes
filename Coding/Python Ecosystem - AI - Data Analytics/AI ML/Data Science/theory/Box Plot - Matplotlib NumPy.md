# Box Plot
``` python
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

data = [np.random.normal(50, 10, 100), np.random.normal(80, 20, 100), np.random.normal(40, 15, 100)]

# Box Plot
plt.boxplot(data)

plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()
```

---
# What is a Box Plot ?
A box plot (box-and-whisker plot) summarizes a dataset’s distribution using five key values:

* Minimum
* First quartile (Q1)
* Median (Q2)
* Third quartile (Q3)
* Maximum

The box shows the interquartile range (Q1 to Q3), the line inside marks the median, and the whiskers extend to the data’s min and max (or a defined range). Outliers are often shown as individual points. It’s used to compare distributions and spot skewness and outliers.

---
