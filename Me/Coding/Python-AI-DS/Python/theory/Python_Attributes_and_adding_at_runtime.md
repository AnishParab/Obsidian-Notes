# Class attribute access and adding attributes at runtime

``` python
class Chai:
    origin = "India"

Chai.origin         # "India" — defined in class body
Chai.is_hot = True  # valid — adds attribute at runtime
```

> **NOTE**: IDE will throw an error while adding classes.

---
# Why IDE warns but Python allows it

- IDE (Pylance/Pyright/MyPy) = static analysis — reads class definition only, never executes code
- Sees only `origin` in the definition → flags `is_hot` as unknown
- Python runtime = dynamic — attribute lookup happens at execution time, not parse time
- Both are correct in their own context — IDE warns, runtime works fine

---
# Why this works

- Classes are objects in Python — mutating them is just setting a key in their `__dict__`
- No compile step, no schema enforcement

---
**Gotcha**
- Adding attributes at runtime is valid but avoid it in production code
- Makes code unpredictable — static analysis can't catch bugs, neither can your IDE
- Prefer defining all attributes upfront in `__init__` or class body

---
