# NumPy Arrays
* Multi-dimensional data structures
* Store **homogeneous** values only

---
#  Python Lists
* Store **heterogeneous** values

---
# Creating NumPy Arrays
```python
import numpy as np

# Creation of NumPy array
a = np.array([1, 2, 3, 4, 5])

# Creation of Python list
b = [1, "hello", 37.98]

print("List:", b)
print("Array:", a)
```

---
# Advantages of NumPy Arrays over Python Lists

## 1. Mathematical Operations

- NumPy supports fast vectorized math.
### Dot Product Example
```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print("Dot Product:", np.dot(x, y))
# Output → 32
```

---
## 2. Performance (Memory + Speed)

- NumPy arrays use contiguous memory in C.

```python
import sys
import numpy as np

a = [1,2,3,4,5,6,7]
b = np.array([1,2,3,4,5,6,7])

print("List", sys.getsizeof(a))
print("Array", b.nbytes)
```

**Output**
```text
List 120
Array 56
```

---
## 3. Compatibility

* Works seamlessly with Pandas, SciPy, scikit-learn, TensorFlow, PyTorch, and more.

---
# When to Use What?

## NumPy Arrays
* Numerical computations
* Large datasets
* Machine learning and statistics
* High-performance vectorized operations

## Python Lists
* Small datasets
* Mixed data types
* Situations not requiring heavy mathematical operations

---
