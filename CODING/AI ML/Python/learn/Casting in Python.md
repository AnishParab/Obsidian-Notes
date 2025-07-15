# Casting
- _Type Conversion_
- Used for safety and clarity since python is dynamically typed.
``` python
x = str(3) # x will be '3'
y = int("3") # x will be 3
z = float(3) # x will be 3.0

# Get the type
print(type(x))
```

---
# Basic Types

| Function   | Description        | Example            |
| ---------- | ------------------ | ------------------ |
| `int(x)`   | Convert to integer | `int("42") → 42`   |
| `float(x)` | Convert to float   | `float("3.14")`    |
| `str(x)`   | Convert to string  | `str(123)`         |
| `bool(x)`  | Convert to boolean | `bool("") → False` |
| `list(x)`  | Convert to list    | `list("abc")`      |
| `tuple(x)` | Convert to tuple   | `tuple([1,2,3])`   |

---
# Boolean Casting
``` python
print(bool(""))       # False (empty string is falsy)
print(bool("hi"))     # True
print(bool(0))        # False
print(bool(123))      # True
```

---
# Falsy and Truthy Values

| Type           | Falsy Values                                             | Truthy Example     |
| -------------- | -------------------------------------------------------- | ------------------ |
| `NoneType`     | `None`                                                   | anything not None  |
| `bool`         | `False`                                                  | `True`             |
| `int`, `float` | `0`, `0.0`                                               | `42`, `-1`, `3.14` |
| `str`          | `""` (empty string)                                      | `"hello"`, `" "`   |
| `list`         | `[]`                                                     | `[1, 2, 3]`        |
| `tuple`        | `()`                                                     | `(0,)`             |
| `dict`         | `{}`                                                     | `{"key": "value"}` |
| `set`          | `set()`                                                  | `{1, 2}`           |
| `range`        | `range(0)`                                               | `range(1, 5)`      |
| `custom class` | class with `__bool__()` or `__len__()` returning `False` | if returns True    |

---
