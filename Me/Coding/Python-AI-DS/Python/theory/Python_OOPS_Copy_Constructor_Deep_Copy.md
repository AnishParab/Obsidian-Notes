# Deep Copy

- Copies the object AND all nested objects — fully independent

```python
import copy

class Dog:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks


d1 = Dog("Bruno", ["sit", "shake"])
d3 = copy.deepcopy(d1)

d3.tricks.append("roll")
print(d1.tricks)  # ["sit", "shake"] — unaffected
```

---
