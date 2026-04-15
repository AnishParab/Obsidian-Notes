# Class Internals

> Classes and Objects are both **dictionaries** under the hood.

> Everything in Python is an object — including classes themselves

---
# `type` — the metaclass

- Every class is an instance of `type`
- `class Chai:` is syntactic sugar for:

```python
Chai = type("Chai", (object,), {"origin": "India"})
#            name    bases        namespace
```

- `type(Chai)` → `<class 'type'>`
- `type(type)` → `<class 'type'>` — type is its own metaclass

---
# **Bases**

- Second argument to `type()` — tuple of parent classes
- Every class implicitly inherits from `object` if no base specified
- `object` is the root of all classes in Python

```python
print(Chai.__bases__)   # (<class 'object'>,)
```

---
# **Namespace**

- Third argument to `type()` — dictionary of class attributes and methods
- Becomes the class `__dict__`

```python
class Chai:
    origin = "India"
    def brew(self): pass

print(Chai.__dict__)
# {'origin': 'India', 'brew': <function>, '__module__': '__main__', ...}
```

---
# Object internals

- Every instance has its own `__dict__` — stores instance-specific attributes only
- Methods live in class `__dict__`, not instance `__dict__`

```python
tea = Chai()
tea.flavor = "Ginger"
print(tea.__dict__)  # {'flavor': 'Ginger'} — no methods here
```

---
# Attribute lookup chain

- `tea.flavor` → `tea.__dict__` → `Chai.__dict__` → parent classes → `AttributeError`

---
# Method calls internally

- `tea.brew()` → found in `Chai.__dict__` → wrapped as bound method → `tea` passed as `self`
- This wrapping is done by the **descriptor protocol**

---
# Full picture

```python
print(type(type))   # <class 'type'>  — type's own metaclass
print(type(Chai))   # <class 'type'>  — Chai is instance of type
print(type(tea))    # <class '__main__.Chai'> — tea is instance of Chai
```

---
