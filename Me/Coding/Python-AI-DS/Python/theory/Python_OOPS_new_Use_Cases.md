
# Singleton pattern — only one instance ever exists

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True — same object
```

---
# Immutable types — subclassing `int`, `str`, `tuple`

```python
class PositiveInt(int):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Must be positive")
        return super().__new__(cls, value)

n = PositiveInt(5)   # works
n = PositiveInt(-1)  # ValueError
```

---
