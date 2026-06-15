# Attribute Shadowing

- Assigning to an instance attribute that shares a name with a class attribute = shadowing
- Creates a new key in instance `__dict__` — class attribute untouched

```python
class Dog:
    species = "Canis lupus"

d1 = Dog()
d1.species = "Something else"  # shadows class attribute

print(d1.species)   # Something else — instance namespace
print(Dog.species)  # Canis lupus   — class namespace untouched
```

---
# Removing shadow with `del`

```python
del d1.species      # removes instance attribute only
print(d1.species)   # Canis lupus — falls back to class attribute
```

---
