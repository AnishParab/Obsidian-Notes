# Line Plot
``` python
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Line plot
plt.plot(x, y)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line plot")
plt.show()
```

---
# What is a Line Plot ?
- A line plot is a chart that displays data points connected by straight lines. It shows how a value changes over a continuous variable—typically time—making trends, increases, and decreases easy to see.

---
