# Set
``` python
setone = {1,2,3,4}

# Intersection
setone & {1,3}

# Union
setone | {1,3}

# Difference
setone - {1,2,3,4}
# Does not give {} since it is a dictionary, but instead gives set()

```

---
# Decimal Precision
- Number precision is infinite in python.
- But Fuck Decimal Precision. That doesn't work.
- Hence import `decimal`
``` python
from decimal import Decimal

Decimal('0.1') + Decimal('0.1')
```

---
# Fractions
``` python
from fractions import Fraction

myFra = Fraction(2,7)
# 2/7
```

---
# Int
``` python
x = 1  
y = 35656222554887711  
z = -3255522  
  
print(type(x))  
print(type(y))  
print(type(z))
```

---
# Float
``` python
x = 1.10  
y = 1.0  
z = -35.59  
  
print(type(x))  
print(type(y))  
print(type(z))
```

---
# Scientific Numbers
``` python
x = 35e3  
y = 12e4  
z = -87.7e100  
  
print(type(x))  
print(type(y))  
print(type(z))
```

---
# Complex
``` python
x = 3+5j  
y = 5j  
z = -5j  
  
print(type(x))  
print(type(y))  
print(type(z))
```

---
# Type Conversion
``` python
x = 1    # int  
y = 2.8  # float  
z = 1j   # complex  
  
#convert from int to float:  
a = float(x)  
  
#convert from float to int:  
b = int(y)  
  
#convert from int to complex:  
c = complex(x)  
  
print(a)  
print(b)  
print(c)  
  
print(type(a))  
print(type(b))  
print(type(c))
```

---
# Random Number
``` python
import random  
  
print(random.randrange(1, 10))
```

---


