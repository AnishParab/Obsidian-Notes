---

---
# `@property` **/ Getter**

- `@property` = controlled attribute access without exposing internals directly.

> Caller uses attribute syntax and has no idea whether it's a raw field or a method underneath.

``` python
class Dog:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

d = Dog(3)
print(d.age)   # 3 — looks like attribute access, actually calls a method
d.age = 5      # AttributeError — no setter defined, read-only
```

---
# **Setter**

``` python
class Dog:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

d = Dog(3)
d.age = 5   # calls setter
print(d.age) # 5
d.age = -1  # ValueError
```

---
# NOTE:

**Why `_age` and not `age` internally:
- If Internal field and property share the same name -> infinite recursion
- `self.age = age` inside `__init__` calls the setter, not set a field
- `_age` sidesteps this

---
