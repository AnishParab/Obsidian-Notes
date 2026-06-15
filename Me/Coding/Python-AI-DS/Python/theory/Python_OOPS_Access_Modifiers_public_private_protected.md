# Access Modifiers

- Python has no strict access control — convention-based, not compiler-enforced

---
# Three levels

```python
class Dog:
    def __init__(self):
        self.name = "Gabbar"      # public
        self._age = 8             # protected
        self.__strength = "High"  # private
```

---
# **Public** — `field`

- Accessible from anywhere, no restriction

---
# **Protected** — `_field`

- Convention: "internal use / subclasses only"
- Nothing blocks access — just a signal to other developers

---
# **Private** — `__field`

- Name mangling: `__strength` → `_Dog__strength` internally
- `obj.__strength` → `AttributeError`
- `obj._Dog__strength` → works — Python can't truly block it

---
# Access behaviour

```python
d = Dog()
print(d.name)            # Gabbar — works
print(d._age)            # 8 — works, convention only
print(d.__strength)      # AttributeError
print(d._Dog__strength)  # High — name mangling bypassed
```

---
# Achieving true access control

- Read-only → `@property` with no setter
- Controlled write → `@property` + `@field.setter` with validation
- Block runtime attribute addition → `__slots__`
- No Python mechanism gives full compiler-level enforcement

---
###### Gotcha

- `__field` doesn't block — it renames
- `_field` is a social contract, not a lock
- Bypassing `__` via name mangling is always the caller's fault

---
