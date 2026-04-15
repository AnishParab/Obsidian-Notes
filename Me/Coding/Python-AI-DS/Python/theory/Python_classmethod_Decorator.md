# `@classmethod` Decorator

- `@classmethod` = method that receives the class itself, not the instance
- First parameter is always `cls` — the class, not the object

> Hence it changes the state of the class, even though an object is changing it.

**Note the state of the class**
```python
class Chai:
    total_orders = 0

    @classmethod
    def increment_orders(cls):
        cls.total_orders += 1  # class-level state

obj = Chai()

obj.increment_orders()
Chai.increment_orders()

print(Chai.total_orders)  # 2
print(obj.total_orders)   # 2
```
> Both will change it's state to **2**.

---
# Primary use — alternative constructors

- Accept different input formats without bloating `__init__`
- `cls(...)` = calling the constructor

```python
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, data):
        return cls(data["tea_type"], data["sweetness"], data["size"])

    @classmethod
    def from_string(cls, s):
        tea_type, sweetness, size = s.split("-")
        return cls(tea_type, sweetness, size)

order1 = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": "Medium", "size": "Large"})

order2 = ChaiOrder.from_string("Ginger-Low-Small")
```

---
# `cls` vs hardcoded class name

```python
# Wrong — breaks inheritance
@classmethod
def from_string(cls, s):
    return ChaiOrder(...)  # hardcoded

# Correct — works with subclasses
@classmethod
def from_string(cls, s):
    return cls(...)        # dynamic
```

**Gotcha**
- Can be called on instance too — `order1.from_dict(...)` works but misleading
- Prefer calling via class — `ChaiOrder.from_dict(...)`

---
