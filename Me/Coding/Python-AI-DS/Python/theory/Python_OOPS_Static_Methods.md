# Static Methods

- Decorated with `@staticmethod`.
- Receives nothing — no `self`, no `cls`.

```python
class Dog:
    @staticmethod
    def is_valid_name(name):
        return len(name) > 0

print(Dog.is_valid_name("Bruno"))  # True
print(Dog.is_valid_name(""))       # False
```

---
**When to use**
- Logic belongs conceptually to the class but needs neither instance nor class data
- Utility/helper functions — validation, formatting, parsing
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def human_to_dog_years(human_years):
        return human_years * 7

    @staticmethod
    def is_valid_age(age):
        return 0 < age < 20

d = Dog("Bruno", 3)
print(Dog.human_to_dog_years(5))  # 35
print(Dog.is_valid_age(3))        # True
```

---
**Without `@staticmethod` vs with**
```python
# Without — object creation required
class Dog:
    def is_valid_name(self, name):
        return len(name) > 0

d = Dog()
d.is_valid_name("Bruno")  # needs an instance

# With — no object needed
class Dog:
    @staticmethod
    def is_valid_name(name):
        return len(name) > 0

Dog.is_valid_name("Bruno")  # clean
```

---
###### Gotcha
- Can be called on instance too — `d.is_valid_name("Bruno")` works but misleading
- No access to `cls` — not inheritance-aware, always resolves to class it was defined in
- If you find yourself needing `cls` inside a static method — it should be a `@classmethod`

---
