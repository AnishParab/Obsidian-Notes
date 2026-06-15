**Two types of attributes**
- One belongs to the class
- One belongs to the object

---
# Instance attributes

- Defined inside `__init__` using `self`
- Each object has its own independent copy

```python
class Dog:
    def __init__(self, name):
        self.name = name

d1 = Dog("Bruno")
d2 = Dog("Max")

print(d1.name)  # Bruno
print(d2.name)  # Max — completely independent
```

---
# Class attributes

- Defined directly in the class body
- Shared across all instances

```python
class Dog:
    species = "Canis lupus"

    def __init__(self, name):
        self.name = name

print(d1.species)   # Canis lupus
print(d2.species)   # Canis lupus
print(Dog.species)  # Canis lupus
```

---
