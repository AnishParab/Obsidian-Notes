# Why not pass `null`/`nullptr`
- You are pushing the burden of validation into every function that receives it.
- Nulls usually signal missing design.

---
# Why Avoid `bool` parameters
- `true` and `false` are **ambiguous** at call site.
- It often leads to **flag arguments** that change behavior inside the function (code smell).
- They increase **cyclomatic complexity**.

---
# Rule of Thumb

| Symptom                     | Better Alternative                  |
| --------------------------- | ----------------------------------- |
| `nullptr`, `NULL`, `null`   | Use `optional` or redesign contract |
| `bool` flags                | Use `enum`, split functions         |
| `param = null` default args | Avoid — it's a code smell           |

---



