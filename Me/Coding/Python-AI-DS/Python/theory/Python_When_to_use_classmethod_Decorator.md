# When to use `@classmethod` Decorator

- Use `@classmethod` when the method needs the class but not the instance

---
# **1. Alternative constructors — most common**

- Multiple ways to create an object from different input formats

```python
class Chai:
    def __init__(self, flavor, temperature):
        self.flavor = flavor
        self.temperature = temperature

    @classmethod
    def from_dict(cls, data):
        return cls(data["flavor"], data["temperature"])

    @classmethod
    def from_string(cls, s):
        flavor, temperature = s.split("-")
        return cls(flavor, temperature)
```

---
# **2. Accessing or modifying class-level state**

```python
class Chai:
    total_orders = 0

    def __init__(self, flavor):
        self.flavor = flavor
        Chai.total_orders += 1

    @classmethod
    def get_total_orders(cls):
        return cls.total_orders
```

---
# **3. Inheritance-aware factory**

- `cls` ensures subclass gets its own type, not the parent's

```python
class Chai:
    @classmethod
    def create(cls):
        return cls()

class MasalaChai(Chai):
    pass

obj = MasalaChai.create()
print(type(obj))  # <class '__main__.MasalaChai'> — not Chai
```

---
# **When NOT to use**

- Method doesn't need class or instance data → use `@staticmethod`
- Method needs instance data → use regular instance method

---
