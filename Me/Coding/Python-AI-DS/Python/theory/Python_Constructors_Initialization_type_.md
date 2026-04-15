# Constructors

- Constructors are used so that every single object we make has some properties.
- This proces is called as `init`, short for **Intialization**.
- Since `init` is a keyword, we write it as `__init__()`.
- ` __init__` is the constructor method that runs automatically when an object is created.
- Should compulsarily take *self* as an argument.

---
# Code

``` python
class ChaiOrder:
    # Creating a constructor
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    # Method
    def summary(self):
        return f"{self.size}ml of {self.type} chai"

order = ChaiOrder("Masala", 200)
print(order.summary())

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary())
```

**Output**:
``` text
200ml of Masala chai
220ml of Ginger chai
```

---
# Why `type_` is used:

- `type()` is a _built-in function_ in Python (used to **check** the **type of an object**).

> To avoid overriding or shadowing this built-in name, developers use a trailing underscore `type_` for variable or parameter names that might conflict.

---
