# What is Namespace ?
- Each object has it's own entity, it can possess it's own features, properties but doesn't bother other ones.

---
# Example
``` python
class Chai:
	origin = "India" # properties
	
print(Chai.origin)

# Add an property
Chai.is_hot = True
print(Chai.is_hot)

# Creating objects from class Chai
masala = Chai
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")

masala.is_hot = False

print(f"Class: {Chai.is_hot}")
print(f"Masala: {masala.is_hot}")

# A property that doesn't exist in the class
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
