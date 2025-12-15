[[Learn Broadcasting in Simple terms NumPy]]

---
# What is Broadcasting ?
- **Broadcasting** is a feature in NumPy that allows arithmetic operations between arrays of different shapes.
- It solves the problem of compatibility in shape between arrays of different dimensions during arithmetic operations.
- It allows a means of **vectorized** array operations so that looping occurs in C instead of Python.

> The smaller array is broadcasted across the larger array so that they have compatible shapes.

---
# Simple Broadcasting
- Multiplying a scalar to a bigger array.
![[simple_broadcasting.excalidraw|700]]
### Example code
``` python
import numpy as np

a = np.array([1,2,3,4,5,6])
b = 2.0

c = a*b

print(c)
```

**Output**
``` text
[ 2.  4.  6.  8. 10. 12.]
```

---
# General Rules of Broadcasting

### 1. Axes must be aligned
If arrays have different numbers of dimensions, NumPy **left-pads** the smaller array with 1s in its shape.

```python
import numpy as np

a = np.array([1,2,3])
b = np.array([[4],[5],[6]])

c = a + b
print(c)
```

**Output** :
```text
[[5 6 7]
 [6 7 8]
 [7 8 9]]
```

---
### 2. Sizes must match OR one must be 1
A dimension is compatible when:
* they are equal, OR
* one of them is **1**
If not → `ValueError`.

```python
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9]])

c = a + b
print(c)
```

**Output** :
```text
[[ 8 10 12]
 [11 13 15]]
```

---
### 3. Broadcasting stretches dimensions of size 1
A dimension with size 1 is **repeated** to match the larger array.

```python
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = np.array([10,20,30])

c = a + b
print(c)
```

**Output** :
```text
[[11 22 33]
 [14 25 36]]
```

---
# Limitations of Broadcasting

### 1. Shapes must follow broadcast rules
NumPy can only broadcast when **every dimension** satisfies:
* equal size, or
* one of them is 1
If any dimension fails → error.

---
### 2. Broadcasted arrays don’t actually copy data
NumPy creates a **virtual expanded view**.
Heavy operations on very large broadcasted shapes can use more memory during computation.

---
### 3. Operations must be element-wise
Broadcasting only applies to element-wise operations:

* `+`, `-`, `*`, `/`, `**`, comparisons, etc.

It does **not** apply to matrix operations like:
* `@` (matrix multiplication)
* `dot()`, etc.

---
### 4. Broadcasting is directional but not restricted to “smaller → larger”
Any array can broadcast with any other as long as shapes match the rules — dimensionality does not matter.

---
