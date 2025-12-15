# What is Reshaping, Splitting and Stacking ?
- **Reshaping** : It is the process of converting a NumPy array into a different shape without changing it's actual data.
- **Splitting** : It is a process of dividing a NumPy array into smaller arrays along one or more axes.
- **Stacking** : It is the process of combining two or more NumPy arrays into a single array along a new axis.

---
# Reshaping
``` python
import numpy as np

a = np.array([[1,2,4], [3,6,9]])

# Prints shape of 1st and 2nd dimension
print(a.shape)

# Reshaping
b = a.reshape([3,2])

print(b)
```

**Output**
``` text
(2, 3)

[[1 2]
 [4 3]
 [6 9]]
```

---
# Splitting
- `axis = 0` → split along rows
You cut downward, producing multiple sub-arrays stacked vertically.

- `axis = 1` → split along columns
You cut sideways, producing sub-arrays next to each other.

**Note**
- 1D array → axes: **0**
- 2D array → axes: **0, 1**
- 3D array → axes: **0, 1, 2**
- 4D array → axes: **0, 1, 2, 3**  
    …and so on.

``` python
import numpy as np

a = np.array([[1,2,4], [3,6,9]])

# Splitting : (array, num_of_partitions, axis)
# Split among rows
b, c = np.split(a, 2, axis = 0)
print(b)
print(c)

# Split along cloumns
x, y, z = np.split(a, 3, axis = 1)
print(x)
print(y)
print(z)
```

**Output**
``` text
[[1 2 4]]
[[3 6 9]]

[[1]
 [3]]
[[2]
 [6]]
[[4]
 [9]]
```

---
# Stacking
- **Vertical Stack**
- **Horizontal Stack**
``` python
import numpy as np

a = np.array([1,2,4])
b = np.array([5,7,8])

# Vertical Stack
c = np.vstack((a,b))

# Horizontal Stack
d = np.hstack((a,b))

print(c)
print(d)
```

**Output**
``` text
[[1 2 4]
 [5 7 8]]
 
[1 2 4 5 7 8]
```

---
# Concatenation
> **NOTE**
	`np.concatenate` **cannot combine arrays with different shapes or different dimensions along the chosen axis.**

``` python
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6], [7,8]])

c = np.concatenate((a,b), axis = 0)

d = np.concatenate((a,b), axis = 1)

print(a)
print(b)
```

**Output**
``` text
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
 
[[1 2 5 6]
 [3 4 7 8]]
```

### **NOTE**
> **BUT for `axis = None` , array shape doesn't matter.**
``` python
import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

# Gives no error : axis = None
c = np.concatenate((a,b), axis = None)

print(c)
```

``` text
[1 2 3 4 5 6]
```

---
# Transpose
- **Axis is transposed** : Rows become columns, and columns become rows.

``` python
import numpy as np

a = np.array([[1,2],[3,4]])

print(a.T)
```

**Output**
``` text
[[1 3]
 [2 4]]
```

---
# `ndims`, `nsize` and `nshape`
- `ndims`: Returns number of dimensions of an array.
- `nsize` : Return total number of elements in an array.
- `nshape` : Returns a tuple showing the size of each dimension.

``` python
import numpy as np

a = np.array([[1,2,4], [3,6,9]])

# nshape
print(a.shape)

# nsize
print(a.size)

# ndims
print(a.ndim)
```

**Output**
``` text
(2, 3)
6
2
```

---
