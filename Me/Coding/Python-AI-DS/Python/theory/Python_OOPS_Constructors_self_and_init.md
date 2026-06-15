# Constructors

- Constructor = method that runs automatically when an object is created
- Used to ensure every object starts with defined properties
- `__init__` is the constructor in Python — dunder syntax because it's a reserved method
###### Syntax
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

d = Dog("Gabbar", "Indie")
print(d.name)   # Gabbar
print(d.breed)  # Indie
```

---
# `self`

- Refers to the instance being created
- Must be the first parameter of `__init__` — always
- `Dog("Gabbar", "Indie")` → Python internally calls `Dog.__init__(d, "Gabbar", "Indie")`
- Name `self` is convention — technically any name works, never deviate

---
# **What happens without `__init__`**

```python
class Dog:
    pass

d = Dog()  # works — Python uses a default empty constructor
```
###### Proof
``` python
class Dog:
    def __init__(self):
        print(self)  # memory address of the object being created

d = Dog()
print(d)  # same memory address — confirms self IS the object
```

---
###### Gotcha

- `__init__` must not return anything — returning a value raises `TypeError`
- Forgetting `self` → `TypeError` when called
- `self` is not a keyword — it's just a convention

---
