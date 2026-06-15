# Custom Copy Behaviour

- Override `__copy__` and `__deepcopy__` to control exactly how your object is copied

---
# **`__copy__`**

- Called when `copy.copy(obj)` is used
- New object created — but nested mutable objects are still shared

```python
def __copy__(self):
    return Dog(self.name, self.tricks)
    # self.name — immutable, safe to pass directly
    # self.tricks — mutable list, shared between both objects
```

---
# **`__deepcopy__`**

- Called when `copy.deepcopy(obj)` is used
- New object + fully independent copy of all nested objects

```python
def __deepcopy__(self, memo):
    return Dog(self.name, copy.deepcopy(self.tricks, memo))
    # self.tricks — fully independent copy of the list
```

---
# **`memo` — what it is and why it matters**

- Dictionary passed internally by Python: `{id(original): copied_object}`
- Tracks already-copied objects to prevent infinite recursion on circular references

```python
class Dog:
    def __init__(self):
        self.friend = None

d1 = Dog()
d2 = Dog()
d1.friend = d2
d2.friend = d1  # circular reference

copy.deepcopy(d1)  # memo prevents infinite recursion here
```

- Without `memo` → Python would copy `d1` → copy `d1.friend` (d2) → copy `d2.friend` (d1) → infinite loop
- With `memo` → "already copied d1, here it is" → stops the loop

---
# Full example

```python
import copy

class Dog:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks

    def __copy__(self):
        return Dog(self.name, self.tricks)

    def __deepcopy__(self, memo):
        return Dog(self.name, copy.deepcopy(self.tricks, memo))

d1 = Dog("Bruno", ["sit", "shake"])
d2 = copy.copy(d1)
d3 = copy.deepcopy(d1)

d2.tricks.append("roll")
print(d1.tricks)  # ["sit", "shake", "roll"] — shared, shallow copy

d3.tricks.append("fetch")
print(d1.tricks)  # ["sit", "shake", "roll"] — unaffected, deep copy
```

---
