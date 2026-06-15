# When to use `@classmethod`

- Use `@classmethod` when the method needs the class but not the instance

---
# **1. Alternative constructors — most common**

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
# **2. Accessing or modifying class-level state**

- `@classmethod` called via instance still modifies class state — not instance state
- `cls` always points to the class regardless of how it's called

```python
class Dog:
    total_dogs = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def increment_count(cls):
        cls.total_dogs += 1

d = Dog("Bruno")

d.increment_count()        # called on instance — still modifies class state
print(d.total_dogs)        # 1
print(Dog.total_dogs)      # 1 — same value

Dog.increment_count()
print(Dog.total_dogs)      # 2
```

---
# **3. Inheritance-aware factory**

- `cls` ensures subclass gets its own type, not the parent's

```python
class Dog:
    @classmethod
    def create(cls):
        return cls()

class Labrador(Dog):
    pass

obj = Labrador.create()
print(type(obj))  # <class '__main__.Labrador'> — not Dog
```

---
# **When NOT to use**

- Method needs neither class nor instance data → `@staticmethod`
- Method needs instance data → regular instance method

---
