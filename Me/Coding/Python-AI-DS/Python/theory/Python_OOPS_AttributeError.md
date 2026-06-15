# `AttributeError`

- Raised when attribute lookup exhausts all namespaces and finds nothing

> **AttributeError** occurs when there is no **fallback-value**.

```python
class Dog:
    species = "Canis lupus"

d1 = Dog()
d1.nickname = "Bruno"
del d1.nickname
print(d1.nickname)  # AttributeError — no class-level fallback exists
```

---
###### Gotcha

- Shadowed attribute removed via `del` → falls back to class attribute, no error
- Attribute with no fallback removed via `del` → `AttributeError`

---
