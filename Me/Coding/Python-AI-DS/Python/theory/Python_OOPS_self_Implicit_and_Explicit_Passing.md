# Implicit and Explicit Passing of `self`

- `self` refers to the instance on which a method is called

---
# **Implicit passing — via instance**

```python
class Dog:
    size = "Large"

    def describe(self):
        return f"A {self.size} dog"

d = Dog()
print(d.describe())  # Python implicitly passes d as self
```

---
# **Explicit passing — via class**

```python
d2 = Dog()
d2.size = "Small"
print(Dog.describe(d2))  # manually passing d2 as self
```

---
# **Missing self — TypeError**

```python
print(Dog.describe())  # TypeError — self not provided
# TypeError: Dog.describe() missing 1 required positional argument: 'self'
```

---
# Key distinction

- Instance call → Python binds the instance automatically → `self` injected
- Class call → Python does nothing → you must pass the instance manually
- Class call with no argument → `self` missing → `TypeError`

---
###### Gotcha

- Objects can run methods only when `self` is passed — implicitly or explicitly
- References can call methods only with explicit instance passing
- This is why every instance method must declare `self` as first parameter

---
