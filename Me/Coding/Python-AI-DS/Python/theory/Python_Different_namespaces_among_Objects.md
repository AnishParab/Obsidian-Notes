# Different namespaces among Objects

- Instances each get their own namespace — unlike class references which share one

```python
class Chai:
    origin = "India"

tea1 = Chai()
tea2 = Chai()

tea1.flavor = "Ginger"
tea2.flavor = "Lemon"

print(tea1.flavor)  # Ginger
print(tea2.flavor)  # Lemon

tea1.flavor = "Masala"
print(tea1.flavor)  # Masala
print(tea2.flavor)  # Lemon — unchanged

tea1.origin = "USA"
print(tea1.origin)  # USA
print(tea2.origin)  # India
```

- Mutating `tea1` has zero effect on `tea2`
- Each instance owns its attribute space

**Contrast with class reference**
```python
masala = Chai        # alias — same namespace as Chai
tea1 = Chai()        # instance — own namespace
```

---
**Gotcha**
- Class-level attributes (`origin`) are shared across all instances until overridden
- `tea1.origin` → looks up instance namespace first, falls back to class namespace if not found

---
