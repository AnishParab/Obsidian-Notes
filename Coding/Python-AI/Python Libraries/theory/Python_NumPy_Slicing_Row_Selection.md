# Code
``` python
import numpy as np

array = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
)

# array[start:end:step]
# 1st row
print(array[0])
print()

# First 3 rows
print(array[0:3])
print()

# Every 2nd row, strating with the first
print(array[::2])
```

**Output**:
``` text
[1 2 3 4]

[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

[[ 1  2  3  4]
 [ 9 10 11 12]]
```

---
