# Attributes at Runtime

- Classes are mutable objects — attributes can be added after definition

```python
class Dog:
    species = "Canis lupus"

Dog.species          # "Canis lupus" — defined in class body
Dog.is_domestic = True  # valid — adds attribute at runtime
```

---
**Why IDE warns but Python allows it**
- IDE (Pylance/Pyright/MyPy) = static analysis — reads class definition only, never executes
- Sees only `species` → flags `is_domestic` as unknown
- Python runtime = dynamic — lookup happens at execution time, not parse time

---
**Why this works**
- Classes are objects — mutating them is just setting a key in their `__dict__`
- No compile step, no schema enforcement

---
###### Gotcha
- Valid but avoid in production — makes code unpredictable
- Static analysis can't catch bugs introduced this way
- Prefer defining all attributes upfront in `__init__` or class body

---
