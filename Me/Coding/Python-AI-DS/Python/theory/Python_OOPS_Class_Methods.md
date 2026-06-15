# Class Methods

- Decorated with `@classmethod`
- Receives `cls` — the class itself, not the instance.

```python
class Dog:
    species = "Canis lupus"
    total_dogs = 0

    def __init__(self, name):
        self.name = name
        Dog.total_dogs += 1

    @classmethod
    def get_total(cls):
        return cls.total_dogs

d1 = Dog("Bruno")
d2 = Dog("Max")

print(Dog.get_total())  # 2
```

---
**Primary use — alternative constructors**
- Accept different input formats without bloating `__init__`
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    @classmethod
    def from_string(cls, s):
        name, breed = s.split("-")
        return cls(name, breed)

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["breed"])

d1 = Dog.from_string("Bruno-Indie")
d2 = Dog.from_dict({"name": "Max", "breed": "Lab"})
```

---
**Why `cls` and not the class name directly**
```python
class Dog:
    @classmethod
    def create(cls):
        return cls()        # correct — works with subclasses

class Labrador(Dog):
    pass

obj = Labrador.create()
print(type(obj))  # <class '__main__.Labrador'> — not Dog
```

- Hardcoding `Dog()` instead of `cls()` would always return a `Dog`, breaking inheritance

---
###### Gotcha

- Can be called on an instance — `d1.get_total()` works but misleading, always call via class
- `cls` is the class at the time of the call — dynamic, not hardcoded

---
