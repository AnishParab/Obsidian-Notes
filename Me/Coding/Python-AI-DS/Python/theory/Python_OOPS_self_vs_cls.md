# `self` v/s `cls`

- `self` = reference to the instance
- `cls` = reference to the class

---
# What each can access

|        | Instance data | Class data             |
| ------ | ------------- | ---------------------- |
| `self` | Yes           | Yes — via lookup chain |
| `cls`  | No            | Yes                    |

**Proof**
```python
class Dog:
    species = "Canis lupus"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        print(self.name)     # instance data
        print(self.species)  # class data — accessible via self too

    @classmethod
    def class_method(cls):
        print(cls.species)   # class data
        print(cls.name)      # AttributeError — no instance exists
```

**Why `cls` can't access instance data**
- Instance data doesn't exist at the class level
- `@classmethod` can be called without ever creating an object — there is no instance to reference

---
