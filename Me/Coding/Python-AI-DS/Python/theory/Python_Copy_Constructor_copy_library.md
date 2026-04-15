# Copy Constructor

- Copy constructor = creating a new object as a copy of an existing one
- Python has no built-in copy constructor like C++ — use `copy` module instead

---
# C++ vs Python

| C++               | Python                        |                                   |
| ----------------- | ----------------------------- | --------------------------------- |
| Copy constructor  | `ClassName(const ClassName&)` | `copy.copy()` / `copy.deepcopy()` |
| Default behaviour | Shallow copy                  | Shallow copy                      |
| Deep copy         | Manual implementation         | `copy.deepcopy()`                 |

---
