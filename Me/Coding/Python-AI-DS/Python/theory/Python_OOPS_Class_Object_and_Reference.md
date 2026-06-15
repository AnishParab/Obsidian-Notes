# Class, Object and Reference

- OOP = paradigm of writing code around objects

> **Class** = blueprint
> **Object / Instance** = real thing built from that blueprint
> **Reference** = alias pointing to the class itself

**Naming convention**
- Classes: `UpperCamelCase` — `Dog`, `SportsCar`, `ChaiOrder`

---
# Creating a class, reference and object

```python
class Dog:
    pass

# Class itself
print(type(Dog))   # <class 'type'> — class is an instance of type

# References — aliases to the class, no object created
r1 = Dog
r2 = Dog
print(type(r1))    # <class 'type'>
print(type(r2))    # <class 'type'>

# Objects — real instances in memory
o1 = Dog()
o2 = Dog()
print(type(o1))    # <class '__main__.Dog'>
print(type(o2))    # <class '__main__.Dog'>

print(r1 is r2)    # True  — both point to the same class
print(o1 is o2)    # False — two separate objects in memory
```

---
# NOTE

- `Dog` and `r1 = Dog` → same object in memory, `r1 is Dog` is `True`
- `Dog()` → new object every time, no two instances are the same

- `type(Dog)` → `type` — every class is an instance of `type`
- `type(o1)` → `Dog` — every object is an instance of its class

---
