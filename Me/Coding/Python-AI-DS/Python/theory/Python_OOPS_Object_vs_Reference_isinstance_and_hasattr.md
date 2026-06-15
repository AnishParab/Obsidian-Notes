# Object v/s Reference

- Reference = alias to the class, no object created
- Object = real instance in memory, created with `()`

---
# Core distinction

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

r1 = Dog           # reference — points to the class
d1 = Dog("Bruno", "Indie")  # object — real instance

print(type(r1))    # <class 'type'>
print(type(d1))    # <class '__main__.Dog'>
```

---
# `isinstance`

```python
print(isinstance(r1, Dog))   # False — r1 is the class, not an instance
print(isinstance(d1, Dog))   # True  — d1 is an instance of Dog
```

---
# `hasattr`

```python
print(hasattr(r1, "name"))   # False — class has no instance data
print(hasattr(r1, "breed"))  # False

print(hasattr(d1, "name"))   # True  — instance has name
print(hasattr(d1, "breed"))  # True
```

---
# **Class reference is still callable**

```python
d2 = r1("Gabbar", "Indie")   # same as Dog("Gabbar", "Indie")
print(isinstance(d2, Dog))   # True
print(hasattr(d2, "name"))   # True
```

---
# NOTE

- `isinstance(r1, Dog)` → `False` — the class is not an instance of itself
- `isinstance(r1, type)` → `True` — every class is an instance of `type`

---
