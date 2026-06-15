# `@classmethod` v/s `staticmethod`

- Both live inside a class, neither accesses instance data
- Key difference: `@classmethod` gets the class, `@staticmethod` gets nothing

| Feature            | `@classmethod`           | `@staticmethod`          |
| ------------------ | ------------------------ | ------------------------ |
| First parameter    | `cls`                    | none                     |
| Access to class    | Yes                      | No                       |
| Access to instance | No                       | No                       |
| Inheritance-aware  | Yes — `cls` is dynamic   | No                       |
| Primary use        | Alternative constructors | Utility/helper functions |

```python
class Dog:
    total_dogs = 0

    @classmethod
    def increment_count(cls):
        cls.total_dogs += 1

    @staticmethod
    def is_valid_name(name):
        return len(name) > 0

Dog.increment_count()
print(Dog.total_dogs)        # 1
print(Dog.is_valid_name("Bruno"))  # True
```

---
### **Decision rule**

- Needs class-level state → `@classmethod`
- Needs neither `self` nor `cls` → `@staticmethod`
- Needs instance data → regular instance method with `self`

---
###### Gotcha

- Both can be called on instance — always call via class for clarity
- `@staticmethod` with inheritance → always resolves to the class it was defined in, not the subclass

---
