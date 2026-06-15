#  `slots` 

- `__slots__` = explicitly declare which attributes an instance is allowed to have
- Blocks arbitrary attribute addition at runtime

---
# Without `__slots__`

```python
class Dog:
    pass

d = Dog()
d.name = "Bruno"   # works — no restriction
d.color = "Brown"  # also works
```

---
# With `__slots__`

```python
class Dog:
    __slots__ = ['name', 'breed']

d = Dog()
d.name = "Bruno"   # works — declared in __slots__
d.color = "Brown"  # AttributeError — not in __slots__
```

---
# **What it gives you**

- Restricts instance attributes to declared list only
- Memory efficient — no `__dict__` per instance
- Slight performance improvement on attribute access

---
# **What it doesn't give you**

- Not an access modifier — doesn't make attributes private
- Doesn't replace `@property` for validation
- Doesn't enforce types

---
###### Gotcha

- `__slots__` class has no `__dict__` — `obj.__dict__` → `AttributeError`
- Inheritance: if parent has no `__slots__`, child still gets `__dict__` — slots become pointless
- Add `__weakref__` if you need weak references

```python
class Dog:
    __slots__ = ['name', 'breed', '__weakref__']
```

---
