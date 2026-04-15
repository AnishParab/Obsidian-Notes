**Let us create a class:**
``` python
class Chai:
	def __init__(self, flavor):
	    self.flavor = flavor
```

---
# Core distinction

``` python
# Instance - Object in memory 
ginger_tea = Chai("ginger")

# Class reference - points to the class itself
lemon_tea = Chai
```

---
# Type difference

``` python
type(ginger_tea)  # <class '__main__.Chai'>
type(lemon_tea)   # <class 'type'>
```

---
# `isinstance` Behavior

``` python
isinstance(ginger_tea, Chai)  # True  — it's an instance
isinstance(lemon_tea, Chai)   # False — it's the class itself
```

---
# Instance data access

``` python
hasattr(ginger_tea, "flavor")  # True  — instance has flavor
hasattr(lemon_tea, "flavor")   # False — class has no instance data
```

---
# Class reference is still callable

> Class reference behaves exactly like the class — calling it creates a new instance.

``` python
new_tea = lemon_tea("Lemon")  # same as Chai("Lemon")
print(new_tea.flavor)         # Lemon
```

---
**Gotcha**
- `isinstance(lemon_tea, Chai)` is `False` — the class is not an instance of itself
- `isinstance(lemon_tea, type)` would be `True` — every class is an instance of `type`

---
