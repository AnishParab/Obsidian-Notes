# Copy Constructor

- Copy constructor = creating a new object as a copy of an existing one
- Python has no built-in copy constructor like C++ — use `copy` module instead

---
# C++ vs Python

|                   | C++                           | Python                            |
| ----------------- | ----------------------------- | --------------------------------- |
| Copy constructor  | `ClassName(const ClassName&)` | `copy.copy()` / `copy.deepcopy()` |
| Default behaviour | Shallow copy                  | Shallow copy                      |
| Deep copy         | Manual implementation         | `copy.deepcopy()`                 |

---
# Without Copy Constructor

``` python
class Dog:
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks

d1 = Dog("Bruno", ["sit", "shake"])
d2 = d1  # not a copy — just another reference to the same object

d2.name = "Max"
print(d1.name)  # Max — d1 affected, same object
```

---
