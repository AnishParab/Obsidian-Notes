# Different Namespaces among Objects

- Instances each get their own namespace — unlike class references which share one

```python
class Dog:
    origin = "India"

d1 = Dog()
d2 = Dog()

d1.name = "Bruno"
d2.name = "Max"

print(d1.name)  # Bruno
print(d2.name)  # Max

d1.name = "Gabbar"
print(d1.name)  # Gabbar
print(d2.name)  # Max — unchanged

d1.origin = "UK"
print(d1.origin)  # UK
print(d2.origin)  # India — falls back to class attribute
```

- Mutating `d1` has zero effect on `d2`
- Each instance owns its attribute space

#### **Contrast with class reference**
```python
rex = Dog    # alias — same namespace as Dog
d1 = Dog()   # instance — own namespace
```

---
###### Gotcha

- Class-level attributes (`origin`) are shared across all instances until overridden
- `d1.origin` → instance namespace first → falls back to class namespace if not found

---
