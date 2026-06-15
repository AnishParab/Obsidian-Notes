# Accessing Base Class

- Three ways to access parent class from child — each with tradeoffs

**1. Code duplication — avoid**
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Labrador(Dog):
    def __init__(self, name, breed, color):
        self.name = name    # duplicated
        self.breed = breed  # duplicated
        self.color = color
```

- Repeating parent logic in child — breaks DRY
- Change parent `__init__` → must update every child manually

---
**2. Explicit call — avoid**
```python
class Labrador(Dog):
    def __init__(self, name, breed, color):
        Dog.__init__(self, name, breed)  # hardcoded parent name
        self.color = color
```

- Works but hardcodes the parent class name
- Breaks with multiple inheritance — skips MRO

---
**3. `super()` — always use this**
```python
class Labrador(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)  # follows MRO, no hardcoding
        self.color = color

d = Labrador("Bruno", "Labrador", "Brown")
print(d.name)   # Bruno
print(d.color)  # Brown
```

- Follows MRO — works correctly with multiple inheritance
- No hardcoded class name — safe to refactor

---
###### Gotcha

- Always call `super().__init__()` before setting child attributes
- Explicit call bypasses MRO — never use it in multiple inheritance chains

---
