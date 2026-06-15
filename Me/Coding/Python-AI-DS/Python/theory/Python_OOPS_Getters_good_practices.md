# Getters - Good Practices

```python
class Dog:
    def __init__(self, age):
        self._age = age       # _field for storage

    @property
    def human_years(self):
        return self._age * 7  # computed on every access

d = Dog(3)
print(d.human_years)  # 21
```

---
# NOTE

- No setter = read-only — assignment raises `AttributeError`

> Getter runs on every access — avoid heavy computation inside it

> Always use `_field` internally to avoid infinite recursion

>Property name and internal field must differ — same name causes infinite recursion

> Use `_field` for storage — separation between storage and public interface is the point

---
