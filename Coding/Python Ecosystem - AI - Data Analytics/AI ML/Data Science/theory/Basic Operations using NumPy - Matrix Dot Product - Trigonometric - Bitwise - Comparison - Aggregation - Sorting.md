# Arithmetic Operations
``` python
import numpy as np

a = np.array([1,2,3,4,5]) 
b = np.array([3,4,7,5,6]) 

# Addition
print(a+b)

# Subtraction
print(a-b)

# Multiplication
print(a*b)

# Division
print(a/b)

# Modulus
print(a%b)

# Exponential
print(a**b)
```

**Output**
``` text
[ 4  6 10  9 11]
[-2 -2 -4 -1 -1]
[ 3  8 21 20 30]
[0.33333333 0.5        0.42857143 0.8        0.83333333]
[1 2 3 4 5]
[    1    16  2187  1024 15625]
```

---
# Comparison Operations
``` python
import numpy as np

a = np.array([1,2,3,4,5]) 
b = np.array([3,4,7,5,6]) 

print(a==b)
print(a>b)
print(a<b)
print(a!=b)
print(a>=b)
print(a<=b)
```

> **NOTE** : It is doing a complete array check and not an element-wise check.

**Output**
``` text
[False False False False False]
[False False False False False]
[ True  True  True  True  True]
[ True  True  True  True  True]
[False False False False False]
[ True  True  True  True  True]
```

---
# Matrix Multiplication using `np.dot`
``` python
import numpy as np

# Matrix Multiplication
c = np.array([[1,2], [3,4]])
d = np.array([[5,6], [7,8]])
print(np.dot(c,d))
```

**Output**
``` text
[[19 22]
 [43 50]]
```

---
# Trigonometric Functions
``` python
import numpy as np

degree_values = np.array([0, 15, 30, 60])

# degree to radians
radian_values = np.deg2rad(degree_values)
print(radian_values)

# Sine
print("Sine", np.sin(radian_values))

# Cosine
print("Cosine", np.cos(radian_values))
```

**Output**
``` text
[0.         0.26179939 0.52359878 1.04719755]
Sine [0.         0.25881905 0.5        0.8660254 ]
Cosine [1.         0.96592583 0.8660254  0.5       ]
```

---
# Logarithmic Functions
``` python
import numpy as np

a = np.array([1,2,3,4,5]) 

# Logarithmic
print(np.log(a))
print(np.log10(a))
```

**Output**
``` text
[0.         0.69314718 1.09861229 1.38629436 1.60943791]
[0.         0.30103    0.47712125 0.60205999 0.69897   ]
```

---
# Bitwise Operations
``` python
import numpy as np

bit1 = np.array([1,2,3,4], dtype = np.uint8)
bit2 = np.array([2,4,6,8], dtype = np.uint8)

# AND Operation
print("Bitwise AND", np.bitwise_and(bit1, bit2))

# OR Operation
print("Bitwise OR", np.bitwise_or(bit1, bit2))
```

**Output**
``` text
Bitwise AND [0 0 2 0]
Bitwise OR [ 3  6  7 12]
```

---
# Aggregation Functions
``` python
import numpy as np

a = np.array([1,2,3,4,5]) 

# Sum
print(np.sum(a))

# Mean
print(np.mean(a))

# Median
print(np.median(a))

# Standard Deviation
print(np.std(a))

# Variance
print(np.var(a))

# Maximum
print(np.amax(a))

# Minimum
print(np.amin(a))
```

**Output**
``` text
15
3.0
3.0
1.4142135623730951
2.0
5
1
```

---
# Sorting Operations
``` python
import numpy as np

a = np.array([1,2,3,4,5]) 

# Ascending Order sort
print(np.sort(a))

# Descending Order sort
print(np.sort(a)[::-1])
```

**Output**
``` text
[1 2 3 4 5]
[5 4 3 2 1]
```

---
