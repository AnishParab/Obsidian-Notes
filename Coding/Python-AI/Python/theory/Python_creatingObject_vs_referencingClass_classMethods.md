# Code
``` python
class Chai:
	def __init__(self, flavor):
	    self.flavor = flavor

# Creating an instance (object)
ginger_tea = Chai("ginger")

# Assigning the class itself (no object created), Reference to the class
lemon_tea = Chai

# --- Demonstration ---

# Object
print("ginger_tea:")
print("  type:", type(ginger_tea))
print("  isinstance:", isinstance(ginger_tea, Chai))
print("  flavor:", ginger_tea.flavor)

print()

# Reference
print("lemon_tea:")
print("  type:", type(lemon_tea))
print("  isinstance:", isinstance(lemon_tea, Chai))

print()

# Showing the difference clearly
print("Can ginger_tea access instance data?", hasattr(ginger_tea, "flavor"))
print("Can lemon_tea access instance data?", hasattr(lemon_tea, "flavor"))

print()

# Calling lemon_tea creates a NEW instance
new_tea = lemon_tea("Lemon")
print("new_tea flavor:", new_tea.flavor)
```

**Output**:
``` text
ginger_tea:
  type: <class '__main__.Chai'>
  isinstance: True
  flavor: Ginger

lemon_tea:
  type: <class 'type'>
  isinstance: False

Can ginger_tea access instance data? True
Can lemon_tea access instance data? False

new_tea flavor: Lemon
```

---
