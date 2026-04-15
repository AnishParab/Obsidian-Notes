# Python Slots

- `__slots__` = explicitly declare which attributes an instance is allowed to have
- Blocks arbitrary attribute addition at runtime

---
# Without `__slots__`

```python
class Chai:
    pass

tea = Chai()
tea.flavor = "Ginger"   # works — Python allows this by default
tea.color = "Brown"     # also works — no restriction
```

---
# With `__slots__`

```python
class Chai:
    __slots__ = ['flavor', 'temperature']

tea = Chai()
tea.flavor = "Ginger"      # works — declared in __slots__
tea.color = "Brown"        # AttributeError — not in __slots__
```

---
# What it gives you

- Restricts instance attributes to declared list only
- Memory efficient — no `__dict__` per instance
- Slight performance improvement on attribute access

---
# What it doesn't give you

- Not an access modifier — doesn't make attributes private
- Doesn't replace `@property` for validation
- Doesn't enforce types

---
# Gotcha

- Class with `__slots__` has no `__dict__` by default — `obj.__dict__` → `AttributeError`
- Inheritance: if parent has no `__slots__`, child still gets `__dict__` — slots become pointless
- Add `__weakref__` to slots if you need weak references

```python
class Chai:
    __slots__ = ['flavor', 'temperature', '__weakref__']
```

---
