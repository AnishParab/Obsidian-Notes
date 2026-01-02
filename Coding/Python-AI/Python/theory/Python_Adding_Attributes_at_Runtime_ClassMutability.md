# Code
``` python
class Chai:
	# Attributes
	origin = "India"

# Accessing the attributes
print(Chai.origin)

# Add an attribute an runtime
Chai.is_hot = True
print(Chai.is_hot)
```

> **NOTE**: IDE will throw an _error_ while adding attributes.

---
# Reason: Static Analysis by IDE
Static analyzers (Pyright, Pylance, MyPy, IDEs):
- Read the class **definition only**
- Do **not execute your code**
- Cannot assume runtime mutations

From this definition:
```python
class Chai:
    origin = "India"
```

The editor knows only:
```python
Chai.origin
```

It has **no way to know** that later you will do:
```python
Chai.is_hot = True
```

So it warns:
> Attribute "is_hot" is unknown

---
# Python allows Dynamic Runtime: Classes are Mutable
```python
Chai.is_hot = True
```

> Python allows this because:
> - Classes are mutable objects
> - Attributes can be added at runtime
> - Lookup happens dynamically

So **at runtime**, this works perfectly.

---
