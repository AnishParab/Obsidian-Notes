# Python Destructors

- Destructor = method called when an object is about to be garbage collected
- Python: `__del__`

---
# Syntax

```python
class Chai:
    def __init__(self, flavor):
        self.flavor = flavor
        print(f"{self.flavor} tea created")

    def __del__(self):
        print(f"{self.flavor} tea destroyed")

tea = Chai("Ginger")  # __init__ called
del tea               # __del__ called
```

---
# When `__del__` is called

- `del obj` — explicit deletion
- Object goes out of scope
- Program exits

---
# C++ vs Python

| C++           | Python                                          |                                |
| ------------- | ----------------------------------------------- | ------------------------------ |
| Destructor    | `~ClassName()`                                  | `__del__`                      |
| When called   | Deterministic — exactly when `delete` is called | Non-deterministic — GC decides |
| Manual memory | Yes — `new`/`delete`                            | No — GC handles it             |
| Need it?      | Often                                           | Rarely                         |

---
# When to actually use `__del__`

- Closing file handles
- Releasing network connections
- Cleanup of external resources not managed by GC

---
# Prefer this over `__del__`

```python
with open("file.txt") as f:  # context manager handles cleanup
    pass
```

---
**Gotcha**
- GC timing is non-deterministic — never rely on `__del__` for critical cleanup
- Circular references can delay or prevent `__del__` from being called
- `__del__` is not guaranteed to run on program crash

---
