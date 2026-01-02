# MRO (Multiple Resolution Order)
- **Method Resolution Order (MRO)** defines the **order in which Python searches for methods and attributes** in a class hierarchy, especially when **multiple inheritance** is involved.
- In multiple inheritance, the same method may appear in more than one parent class.  
- MRO provides a **deterministic and consistent rule** to decide **which implementation is used**.

---
# Example ER Diagram
![[mro.excalidraw|300]]

---
# Code
``` python
class A:
	label = "A: Base Class"
	
class B(A):
	label = "B: Masala Blend"

class C(A):
	label = "C: Herbal Blend"
	
class D(B, C):
	pass
	
cup = D()

# First inherited class is B: from (B, C)
print(cup.label)

print()

# Give Inheritance Order
print(D.__mro__)
```

**Output**
``` text
B: Masala Blend

(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

---
