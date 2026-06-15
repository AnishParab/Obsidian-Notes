# Same Namespaces among References

- Class reference = alias — same object in memory, shared namespace
- Any mutation via either name affects the one shared object

```python
class Dog:
    origin = "India"

# Attribute addition
Dog.is_domestic = True

# Reference
rex = Dog

print(rex.is_domestic)   # True
print(Dog.is_domestic)   # True

# Attribute addition via reference
rex.is_trained = True

print(rex.is_trained)    # True
print(Dog.is_trained)    # True — same namespace

# Changing attribute value via reference
rex.is_domestic = False
print(rex.is_domestic)   # False
print(Dog.is_domestic)   # False — no divergence

# Changing class attribute via reference
rex.origin = "UK"
print(rex.origin)        # UK
print(Dog.origin)        # UK — same namespace
```

---
#### Summary

```python
rex = Dog    # alias — same namespace as Dog
d1 = Dog()   # instance — own namespace
```

- `rex is Dog` → `True` — identical object
- No divergence ever occurs between references

---
