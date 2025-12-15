# What is Indexing and Slicing
- **Indexing** is the process of accessing individual elements of an array.
- **Slicing** is the process of accessing a sub-array or a subset of elements within an array.

---
# Indexing

### 1-D Array
``` python
import numpy as np

# NumPy arrays have 0-based indexing
a = np.array([3,6,18,19,37])

print(a[0])

# From last element, the indexing starts with -1
print(a[-1])
```

**Output**
``` text
3
37
```

---
### 2-D Array
``` python
import numpy as np

# Index value = (List number, element of list number)
# Also 0-based
a = np.array([[1,2], [3,4]])

print(b[0][1])
```

**Output**
``` text
2
```

---
# Boolean Indexing
- Filtering out values based on desired results.

``` python
import numpy as np

x = np.array([1,2,3,4,1,18,19,1])

# Example: Whichever value is not 1 should be reduced by 1.
x[x != 1] -= 1

print(x)
```

**Output**
``` text
[ 1  1  2  3  1 17 18  1]
```

---
# Slicing
- **Syntax** - `[start: stop: step-size`
``` python
import numpy as np

a = np.array([1,2,3,4,5])

print(a[2:4:1])
```

**Output**
``` text
[3 4]
```

---
