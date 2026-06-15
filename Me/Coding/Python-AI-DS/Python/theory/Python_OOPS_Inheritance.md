**Pre-requisites**
[[LLD_OOPS_Inheritance_Introduction]]

---
# Inheritance

- Child class acquires properties and behaviour of parent class. Define once in parent, reuse in all children.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

class Labrador(Dog):  # Labrador inherits from Dog
    pass

d = Labrador("Bruno", "Labrador")
d.bark()  # Bruno says Woof! — inherited from Dog
```

- `Labrador` gets everything from `Dog` for free
- No code duplication

---
# **Adding child-specific behaviour**

```python
class Labrador(Dog):
    def fetch(self):
        print(f"{self.name} fetches the ball!")

d = Labrador("Bruno", "Labrador")
d.bark()   # inherited
d.fetch()  # child-specific
```

---
# **Overriding parent behaviour**

```python
class Labrador(Dog):
    def bark(self):
        print(f"{self.name} says Woof Woof!")  # overrides Dog's bark

d = Labrador("Bruno", "Labrador")
d.bark()  # Bruno says Woof Woof! — child's version
```

---
# **What child gets from parent**

- All public and protected methods and attributes
- Does NOT get: private attributes (`__field`), constructors are not inherited but `__init__` is called via MRO

---
###### Gotcha

- If child defines `__init__`, parent's `__init__` is NOT called automatically
- Must call `super().__init__()` explicitly — covered next

---
