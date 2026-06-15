# Destructors

- Destructor = method called when an object is about to be garbage collected
- Python: `__del__`
###### Syntax
```python
class Dog:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} destroyed")

d = Dog("Bruno")  # __init__ called
del d             # __del__ called
```

---
### **When `__del__` is called**

- `del obj` — explicit deletion
- Object goes out of scope
- Program exits

---
### **When to actually use `__del__`**
- Check next section also:
[[#**Prefer context managers over `__del__`**]]

- Closing file handles
- Releasing network connections
- Cleanup of external resources not managed by GC

---
# **Prefer context managers over `__del__`**

```python
with open("file.txt") as f:  # cleanup handled automatically
    pass
```

---
###### Gotcha

- GC timing is non-deterministic — never rely on `__del__` for critical cleanup
- Circular references can delay or prevent `__del__` from being called
- `__del__` is not guaranteed to run on program crash

---
