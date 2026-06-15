# Child `__init__` and `super()`

When child defines its own `__init__`, parent's `__init__` is not called automatically.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

class Labrador(Dog):
    def __init__(self, name, breed, color):
        self.color = color  # only color is set — name and breed are missing!

d = Labrador("Bruno", "Labrador", "Brown")
print(d.color)   # Brown
print(d.name)    # AttributeError — parent __init__ never ran
```

---
# **Fix — `super()`**

```python
class Labrador(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)  # calls Dog.__init__
        self.color = color

d = Labrador("Bruno", "Labrador", "Brown")
print(d.name)    # Bruno
print(d.breed)   # Labrador
print(d.color)   # Brown
```

---
# **`super()` on methods too**

```python
class Labrador(Dog):
    def bark(self):
        super().bark()                        # calls Dog's bark first
        print(f"{self.name} wags tail too!")  # then adds own behaviour

d = Labrador("Bruno", "Labrador", "Brown")
d.bark()
# Bruno says Woof!
# Bruno wags tail too!
```

---
###### Gotcha

- `super()` always calls the next class in MRO — not necessarily the direct parent
- Always call `super().__init__()` first before setting child attributes

---
