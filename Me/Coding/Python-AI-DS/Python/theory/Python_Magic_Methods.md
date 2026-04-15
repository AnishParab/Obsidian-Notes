# Magic Methods

- Dunder methods (`__method__`) — Python calls these implicitly in specific situations
- Let you define how your object behaves with built-in operations
- Never call them directly — Python calls them for you

---
# Common Magic Methods

|Method|Triggered by|
|---|---|
|`__init__`|object creation|
|`__str__`|`print(obj)`, `str(obj)`|
|`__repr__`|`repr(obj)`, shell output, fallback for `__str__`|
|`__len__`|`len(obj)`|
|`__eq__`|`obj1 == obj2`|
|`__lt__`|`obj1 < obj2`|
|`__add__`|`obj1 + obj2`|
|`__del__`|object garbage collected|

---
# **`__str__` vs `__repr__`**

- `__str__` → human-readable, for end users
- `__repr__` → unambiguous, for developers/debugging
- `print(obj)` → calls `__str__` first, falls back to `__repr__`

```python
class Chai:
    def __init__(self, flavor):
        self.flavor = flavor

    def __str__(self):
        return f"{self.flavor} tea"          # user-facing

    def __repr__(self):
        return f"Chai(flavor={self.flavor})" # debug-facing

tea = Chai("Ginger")
print(tea)       # Ginger tea       — __str__
print(repr(tea)) # Chai(flavor=Ginger) — __repr__
```

---
# **Other examples**

```python
class Chai:
    def __init__(self, flavor, ingredients):
        self.flavor = flavor
        self.ingredients = ingredients

    def __len__(self):
        return len(self.ingredients)

    def __eq__(self, other):
        return self.flavor == other.flavor

    def __add__(self, other):
        combined = self.ingredients + other.ingredients
        return Chai("Blend", combined)

tea1 = Chai("Ginger", ["water", "milk", "ginger"])
tea2 = Chai("Masala", ["water", "milk", "masala"])

print(len(tea1))         # 3
print(tea1 == tea2)      # False
blend = tea1 + tea2      # new Chai object
```

---
**Gotcha**
- Not defining `__eq__` → Python compares by memory address by default
- Not defining `__repr__` → fallback is `<__main__.Chai object at 0x...>` — useless for debugging
- Always define at minimum `__repr__` for any non-trivial class

---
