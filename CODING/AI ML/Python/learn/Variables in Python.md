 A name that points to a value in memory.

``` python
x = 10          # Integer
name = "Anish"  # String
pi = 3.14       # Float
active = True   # Boolean
```

---
# Rules of naming
- Can't start with digits.
- Can't use _hyphen_ `-`.

---
# Dynamic Typing
You can reassign a variable to a new type.
``` python
x = 10
x = "now a string"
```

---
# Constants
Python has no true constants, but by convention:
``` python
PI = 3.14159    # uppercase
```

---
# Multiple Assignment
``` python
a, b, c = 1, 2, 3
x = y = z = 0     # all point to the same value
```

---
# Global and Local Variables
``` python
x = "awesome" # global

def myfunc() :
	x = "fantastic" # local
	print("Python is " + x)

myfunc()

print("Python is " + x)
```

---




