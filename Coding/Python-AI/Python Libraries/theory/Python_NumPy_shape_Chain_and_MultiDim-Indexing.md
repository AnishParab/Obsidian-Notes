# `shape`
- Shows a tuple of integers:
- `(depth, numOfRows, numOfCols)`

---
# Note
> Multi-Dimensional Indexing is **Faster** than Chain-Indexing.

---
# Code
``` python
import numpy as np

array = np.array(
    [
        [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
        [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
        [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", "_"]],
    ]
)

# Printing Shape
print(array.shape)

# Chain-Indexing
print(array[0][0][0])

# Multi-Dimensional Indexing
print(array[0, 0, 0])

# Printing the word ASS
print_ass = array[0, 0, 0] + array[2, 0, 0] + array[2, 0, 0]
print(print_ass)
```

**Output**:
``` text
(3, 3, 3)
A
A
ASS
```

---
