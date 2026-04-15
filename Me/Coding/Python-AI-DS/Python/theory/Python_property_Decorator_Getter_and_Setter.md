# `@property` Decorator

- `@property` = controlled attribute access without exposing internals directly
- Caller uses attribute syntax — no idea whether it's a raw field or a method underneath

---
# Getter

- `@property` — called implicitly on access
- Can compute or transform the returned value

---
# Setter

- `@<property>.setter` — called implicitly on assignment
- Used for validation, constraints, side effects

---
# Code

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age        # _field = protected by convention

    @property
    def age(self):
        return self._age + 2   # computed — not raw value

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")

leaf = TeaLeaf(2)
print(leaf.age)   # 4  — getter adds 2
leaf.age = 4      # setter validates, stores 4
print(leaf.age)   # 6  — getter adds 2 again
leaf.age = 6      # ValueError — outside 1-5
```

---
# Why `_age` and not `age` internally

> **RecursionError** : maximum recursion depth exceeded

- If internal field and property share the same name → infinite recursion
- `self.age = age` inside `__init__` would call the setter, not set a field
- `_age` sidesteps this

---
**Gotcha**
> Getter runs on every access — avoid heavy computation inside it
- No setter defined = read-only property — assignment raises `AttributeError`

---
