# `__new__` v/s `__init__`

- You already know `__init__` — but `__new__` runs before it. They do different things.

```python
class Dog:
    def __new__(cls, name):
        print(f"__new__ called — allocating memory")
		# return instance
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print(f"__init__ called — populating object")
        self.name = name

d = Dog("Bruno")
# __new__ called — allocating memory
# __init__ called — populating object
```

---
# What each does

|           | `__new__`            | `__init__`             |
| --------- | -------------------- | ---------------------- |
| Job       | Creates the instance | Populates the instance |
| First arg | `cls`                | `self`                 |
| Returns   | The new instance     | Nothing (`None`)       |
| Called    | Before `__init__`    | After `__new__`        |

---
# `__new__` must return the instance

- If `__new__` doesn't return an instance of `cls` → `__init__` never runs

```python
class Dog:
    def __new__(cls, name):
        print("__new__ called")
        # forgot to return instance
        
    def __init__(self, name):
        print("__init__ called")  # never runs
        self.name = name

d = Dog("Bruno")
# __new__ called
# __init__ never runs — d is None
print(d)  # None
```

---
###### Gotcha

- Almost never override `__new__` for regular classes — `__init__` is enough
- `__new__` is for controlling instance creation itself, not populating it
- Always call `super().__new__(cls)` inside `__new__`

---
