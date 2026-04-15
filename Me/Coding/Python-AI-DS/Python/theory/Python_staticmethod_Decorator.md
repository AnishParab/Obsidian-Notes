# Why `@staticmethod`

> **Pre-requisite**
[[Python_Self_Argument_Implicit_Explicit_Passing]]

- `@staticmethod` = a function that lives inside a class but doesn't need the object or class to work
- No `self`, no `cls` — behaves like a plain function, just namespaced under the class

---
# Without `@staticmethod` and no `self`

```python
class ChaiUtils:
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

ChaiUtils.clean_ingredients("water, milk, ginger ")  # This works

obj = ChaiUtils()

# TypeError: Static method required
obj.clean_ingredients(" water, milk, ginger ")
```

---
# With `@staticmethod`

```python
class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]

obj = ChaiUtils()

obj.clean_ingredients(" water, milk, ginger ")  # prints properly
```

---
**Gotcha**
- Can be called on an instance too — `obj.clean_ingredients(...)` works but misleading
- Prefer calling via class — `ChaiUtils.clean_ingredients(...)` makes intent clear

---
