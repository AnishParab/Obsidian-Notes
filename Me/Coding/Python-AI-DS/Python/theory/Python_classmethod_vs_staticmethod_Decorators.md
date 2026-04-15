# Comparison

- Both live inside a class, neither accesses instance data
- One key difference: `@classmethod` gets the class, `@staticmethod` gets nothing

| Feature            | `@classmethod`           | `@staticmethod`          |
| ------------------ | ------------------------ | ------------------------ |
| First parameter    | `cls`                    | none                     |
| Access to class    | Yes                      | No                       |
| Access to instance | No                       | No                       |
| Inheritance-aware  | Yes — `cls` is dynamic   | No                       |
| Call via instance  | Works, misleading        | Works, misleading        |
| Primary use        | Alternative constructors | Utility/helper functions |

---
# Code

```python
class Chai:
    total_orders = 0

    @classmethod
    def increment_orders(cls):
        cls.total_orders += 1  # class-level state

    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]  # no class/instance needed

Chai.increment_orders()
print(Chai.total_orders)          # 1

print(Chai.is_valid_size("Large")) # True
```

---
# **Decision rule**

- Needs `cls` or class-level state → `@classmethod`
- Needs neither `self` nor `cls` → `@staticmethod`
- Needs instance data → regular instance method

---
**Gotcha**
- Both can be called on an instance — always call via class for clarity
- `@staticmethod` with inheritance → always resolves to the class it was defined in, not the subclass

---
