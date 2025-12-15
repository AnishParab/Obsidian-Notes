# Pie Chart
``` python
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

labels = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]

# Pie Chart
plt.pie(values, labels=labels, startangle=90, autopct='%1.1f%%')

plt.axis('equal')
plt.title("Pie Chart")
plt.show()
```

---
# What is Pie Chart ?
- A pie chart shows how a whole is divided into parts. Each category is represented as a slice of a circle, with the slice size proportional to its share of the total. It’s useful for showing percentage or proportional data when the number of categories is small.

---
