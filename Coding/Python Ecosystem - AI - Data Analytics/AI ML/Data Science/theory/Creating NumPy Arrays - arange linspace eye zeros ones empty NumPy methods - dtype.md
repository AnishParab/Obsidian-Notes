# Converting Python Sequences to NumPy Arrays
```python
import numpy as np

# Converting Python List to NumPy array
list1 = [1, 2, 3, 4, 5]
array1 = np.array(list1)
print(array1)

# Converting tuple to NumPy array
tuple1 = (1, 2, 3, 4, 5)
array2 = np.array(tuple1)
print(array2)
```

---
# Creating 2-D and 3-D Arrays
```python
# 2D Array
array1 = np.array([[5, 7], [6, 8]])

# 3D Array
array2 = np.array([[[1,2],[3,4]], 
                   [[5,6],[7,8]]])

print(array1)
print(array2)
```

**Output**
```text
[[5 7]
 [6 8]]

[
  [[1 2] [3 4]]
  [[5 6] [7 8]]
]
```

---
# Creating Multi-Dimensional Arrays Using Array Creation Functions

- NumPy provides specialized functions for structured array generation.

---
# `np.arange` and `np.linspace`

### `np.arange(start, stop, step)`
* Creates values in a range with a fixed step.
* `stop` is **exclusive**.
* Good for integer or evenly stepped sequences.

### `np.linspace(start, stop, num)`
* Generates **evenly spaced values** between start and stop.
* `stop` is **inclusive**.
* Good for decimal or precise spacing.

### 1-D Examples
```python
# np.arange
array1 = np.arange(2, 10, 2.5, dtype=float)  # Values from 2 to <10

# np.linspace
array2 = np.linspace(2.5, 3.5, num=5)        # 5 values between 2.5 and 3.5 (inclusive)

print(array1)
print(array2)
```

**Output**
```text
[2.  4.5 7. ]
[2.5 2.75 3.  3.25 3.5 ]
```

---
# `np.eye`
- Creates a **2-D identity matrix** (diagonal elements = 1, rest = 0).

### 2-D Example
```python
array_eye = np.eye(3)  # 3x3 identity matrix
print(array_eye)
```

**Output**
```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---
# 3-D Arrays Using `np.zeros`, `np.ones`
### `np.zeros(shape)`
* Creates an array filled with **0s**.
* Useful for initializing variables.

### `np.ones(shape)`
* Creates an array filled with **1s**.
* Useful for weighting or base structures.

### Example
```python
array_zero = np.zeros((2, 3, 2))   # 3D array filled with zeros
array_one  = np.ones((2, 3, 2))    # 3D array filled with ones

print(array_zero)
print(array_one)
```

**Output**
``` text
[[[0. 0.]
  [0. 0.]
  [0. 0.]]

 [[0. 0.]
  [0. 0.]
  [0. 0.]]]

  
[[[1. 1.]
  [1. 1.]
  [1. 1.]]

 [[1. 1.]
  [1. 1.]
  [1. 1.]]]
```

---
# `np.empty`
- Creates an array without initializing values.
- Contents will be **garbage memory**, but fast.

```python
np.empty([2, 3], dtype=int)
```

**Output**
``` text
array([[304273923,         0,         0],
       [        0,         0,         0]])
```

---
