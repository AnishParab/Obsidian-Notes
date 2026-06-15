# Linked List v/s Arrays

| Property         | Array                    | Linked List                 |
| ---------------- | ------------------------ | --------------------------- |
| Memory layout    | Contiguous               | Non-contiguous              |
| Memory usage     | Less (data only)         | More (data + next pointer)  |
| Insertion/Delete | Slow — shifting required | Fast — pointer reassignment |
| Access           | Random access — O(1)     | No random access — O(n)     |
| Search           | Binary search possible   | Linear search only — O(n)   |

---
**Gotcha**
- No random access in Linked List — you must traverse from head every time
- Arrays win on search; Linked List wins on insert/delete

---
