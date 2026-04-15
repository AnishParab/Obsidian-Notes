# Shallow v/s Deep Copy

|                  | Shallow Copy  | Deep Copy         |
| ---------------- | ------------- | ----------------- |
| Primitive fields | Independent   | Independent       |
| Mutable fields   | Shared        | Independent       |
| Method           | `copy.copy()` | `copy.deepcopy()` |
| Performance      | Faster        | Slower            |

---
