# Shallow Copy

- Copies the object — nested mutable objects are still shared (same reference)

```python
import copy

class Dog:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks


d1 = Dog("Bruno", ["sit", "shake"])
d2 = copy.copy(d1)

d2.name = "Max"
print(d1.name)    # Bruno — primitive, independent

d2.tricks.append("roll")
print(d1.tricks)  # ["sit", "shake", "roll"] — list is shared
```

---
###### Gotcha

- `d2 = d1` → same object, not a copy — most common mistake

---
