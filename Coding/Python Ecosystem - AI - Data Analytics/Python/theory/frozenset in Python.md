# **Frozenset (Immutable Set)**

A **frozenset** is the **immutable** version of a `set`.
Once created, its elements cannot be changed, added, or removed.
It supports all **read-only** set operations like union, intersection, and difference.

### **Example**

```python
frozen_spices = frozenset({"cardamom", "ginger", "cinnamon"})

print(f"Frozenset: {frozen_spices}")

# Supported operations
print(f"Contains 'ginger'? {'ginger' in frozen_spices}")
print(f"Union with {{'cloves'}}: {frozen_spices | {'cloves'}}")
print(f"Intersection with {{'ginger', 'black pepper'}}: {frozen_spices & {'ginger', 'black pepper'}}")

# Unsupported (will raise AttributeError)
# frozen_spices.add("cloves")
```

**Output:**

```
Frozenset: frozenset({'cardamom', 'ginger', 'cinnamon'})
Contains 'ginger'? True
Union with {'cloves'}: frozenset({'cardamom', 'ginger', 'cloves', 'cinnamon'})
Intersection with {'ginger', 'black pepper'}: frozenset({'ginger'})
```

---

## **Set vs. Frozenset Comparison**

| Feature                                | `set`   | `frozenset`        |
| -------------------------------------- | ------- | ------------------ |
| Mutable                                | ✅       | ❌                  |
| Hashable (usable as dict key)          | ❌       | ✅                  |
| Supports add/remove                    | ✅       | ❌                  |
| Supports union/intersection/difference | ✅       | ✅                  |
| Syntax                                 | `{...}` | `frozenset({...})` |

---
