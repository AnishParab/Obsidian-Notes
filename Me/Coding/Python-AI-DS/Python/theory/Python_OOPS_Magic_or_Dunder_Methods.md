# Magic/Dunder Methods

- Dunder methods (`__method__`) — Python calls these implicitly in specific situations
- Never call them directly — Python calls them for you

---
# **Common magic methods**

| Method     | Triggered by              |
| ---------- | ------------------------- |
| `__init__` | object creation           |
| `__str__`  | `print(obj)`, `str(obj)`  |
| `__repr__` | `repr(obj)`, shell output |
| `__len__`  | `len(obj)`                |
| `__eq__`   | `obj1 == obj2`            |
| `__lt__`   | `obj1 < obj2`             |
| `__add__`  | `obj1 + obj2`             |
| `__del__`  | object garbage collected  |

---
# **`__str__` vs `__repr__`**

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"{self.name} the {self.breed}"     # user-facing

    def __repr__(self):
        return f"Dog(name={self.name}, breed={self.breed})"  # debug-facing

d = Dog("Bruno", "Indie")
print(d)        # Bruno the Indie     — __str__
print(repr(d))  # Dog(name=Bruno, breed=Indie) — __repr__
```

---
# **Other examples**

```python
class Dog:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks

    def __len__(self):
        return len(self.tricks)

    def __eq__(self, other):
        return self.name == other.name

    def __add__(self, other):
        combined = self.tricks + other.tricks
        return Dog("Combined", combined)

d1 = Dog("Bruno", ["sit", "shake", "roll"])
d2 = Dog("Max", ["sit", "fetch"])

print(len(d1))       # 3
print(d1 == d2)      # False
merged = d1 + d2     # new Dog object
```

---
###### Gotcha

- Not defining `__eq__` → Python compares by memory address by default
- Not defining `__repr__` → fallback is `<__main__.Dog object at 0x...>` — useless
- Always define at minimum `__repr__` for any non-trivial class
- `print(obj)` calls `__str__` first — falls back to `__repr__` if `__str__` not defined

---
