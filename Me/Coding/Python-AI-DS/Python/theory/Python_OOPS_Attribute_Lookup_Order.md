# Attribute Lookup Order

- Python follows a strict chain when resolving any attribute access

**Order**
- Instance `__dict__` → Class `__dict__` → Parent classes (MRO) → `AttributeError`

```python
class Dog:
    species = "Canis lupus"

d1 = Dog()
d1.name = "Bruno"

print(d1.name)     # Bruno       — found in instance __dict__
print(d1.species)  # Canis lupus — not in instance, found in class __dict__
print(d1.unknown)  # AttributeError — found nowhere
```

---
###### Gotcha

- Instance namespace always wins over class namespace
- MRO determines order when multiple parent classes exist — covered in [[Python_OOPS_MRO]] and [[Python_OOPS_super_MRO_Behavior]]

---
