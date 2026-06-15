# Comparison

|                  | Assignment | Shallow Copy  | Deep Copy         |
| ---------------- | ---------- | ------------- | ----------------- |
| New object       | No         | Yes           | Yes               |
| Primitive fields | Shared     | Independent   | Independent       |
| Mutable fields   | Shared     | Shared        | Independent       |
| Method           | `=`        | `copy.copy()` | `copy.deepcopy()` |

---
###### Gotcha

- Shallow copy is faster but dangerous with mutable nested objects
- Always use `deepcopy` when object contains lists, dicts, or other objects

---
