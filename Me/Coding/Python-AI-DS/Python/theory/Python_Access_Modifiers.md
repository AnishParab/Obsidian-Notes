# Python Access Modifiers

- Python has no strict access control — it's convention-based, not compiler-enforced

---
# **Three levels**

```python
class Chai:
    def __init__(self):
        self.flavor = "Ginger"       # public
        self._temperature = "Hot"    # protected
        self.__strength = "Strong"   # private (name mangled)
```

---
# Public — `field`

- Accessible from anywhere
- No restriction

---
# Protected — `_field`

- Convention: "don't touch unless you're inside the class or a subclass"
- Nothing actually blocks access — just a signal to other developers

---
# Private — `__field`

- Name mangling: `__strength` becomes `_Chai__strength` internally
- Accessing `obj.__strength` from outside → `AttributeError`
- Accessing `obj._Chai__strength` → works — Python can't truly block it

---
# Access behaviour

```python
tea = Chai()

print(tea.flavor)             # works
print(tea._temperature)       # works — warning by convention only
print(tea.__strength)         # AttributeError
print(tea._Chai__strength)    # works — name mangling bypassed
```

---
**Gotcha**
- `__field` doesn't block access, it just renames it
- Only `@property` with no setter gives you true read-only behaviour

> Python philosophy: "we're all consenting adults here"

---
