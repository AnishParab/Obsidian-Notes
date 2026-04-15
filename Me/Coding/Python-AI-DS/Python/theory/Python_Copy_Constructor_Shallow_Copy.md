# Shallow Copy

- Copies the object — nested objects are still shared (same reference)

```python
import copy

class Chai:
    def __init__(self, flavor, ingredients):
        self.flavor = flavor
        self.ingredients = ingredients  # mutable — list

tea1 = Chai("Ginger", ["water", "milk", "ginger"])
tea2 = copy.copy(tea1)

tea2.flavor = "Lemon"
tea2.ingredients.append("lemon")

print(tea1.flavor)       # Ginger — primitive, not shared
print(tea1.ingredients)  # ["water", "milk", "ginger", "lemon"] — list IS shared

print(tea2.flavor)       # Lemon
print(tea2.ingredients)  # ["water", "milk", "ginger", "lemon"]
```

---
