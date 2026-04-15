# Getter

- Read-only access to a private field
- Outside world can see the value, cannot set it directly
- Example: `getSpeed()` — speed is driven by `accelerate()`/`brake()`, never set arbitrarily

---
# Setter

- Controlled write access to a private field
- Key advantage: validation logic lives here
- Example: `setTyreCompany("")` can be rejected inside the setter before it corrupts state

---
# Not all fields need both

- `currentSpeed` → getter only — state is managed internally by the object
- `tyreCompany` → getter + setter — legitimate external modification, but still controlled
- Some fields → neither — purely internal, no exposure needed

---
# The real point

- Getters/setters are not just boilerplate wrappers
- They are the boundary between your object's internals and the outside world
- Validation, logging, computed values — all can live here

---
# Python note

- Python has no enforced `private` — convention is `_field` (soft) or `__field` (name mangled)
- Use `@property` for getters, `@field.setter` for setters — cleaner than explicit methods

```python
@property
def tyre_company(self):
    return self._tyre_company

@tyre_company.setter
def tyre_company(self, value):
    if not value:
        raise ValueError("Tyre company cannot be empty")
    self._tyre_company = value
```

---
