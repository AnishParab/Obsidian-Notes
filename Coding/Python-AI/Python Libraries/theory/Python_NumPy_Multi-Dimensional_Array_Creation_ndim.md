# NOTE:
- For NumPy Arrays, we need a consistent number of elements.

---
# Code
``` python
import numpy as np

# 0-Dimensional Array
array_0 = np.array(["A"])
print(array_0.ndim)
print()

# 1-Dimensional Array
array_1 = np.array(["A", "B", "C"])
print(array_1.ndim)
print()

# 2-Dimensional Array
array_2 = np.array(
    [
        ["A", "B", "C"],
        ["D", "E", "F"],
        ["G", "H", "I"],
    ]
)
print(array_2.ndim)
print()

# 3-Dimensional Array
array_3 = np.array(
    [
        [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
        [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
        [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", "_"]],
    ]
)
print(array_3.ndim)
```

**Output**:
``` text
1

1

2

3
```

---
