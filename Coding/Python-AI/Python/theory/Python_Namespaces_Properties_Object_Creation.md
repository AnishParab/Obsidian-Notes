# What is Namespace ?
- Each object has it's own entity, it can possess it's own features, attributes but doesn't bother other ones.
![[namespaces_python.excalidraw|500]]

---
# Example
``` python
class Chai:
	# Attributes
	origin = "India"

# Accessing the attributes
print(Chai.origin)

# Add a attribute
Chai.is_hot = True
print(Chai.is_hot)

# Creating a Reference of the Class
masala = Chai
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")

masala.is_hot = False

# Different Namespaces
print(f"Class: {Chai.is_hot}")
print(f"Masala: {masala.is_hot}")

# An attribute that doesn't exist in the class
masala.flavor = "Masala"
print(masala.flavor)
```

**Output**:
``` text
India

True

Masala: India
Masala: True

Chai: True
Masala: False

Masala
```

---
