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
print(cup.label)

# Give Inheritance Order
print(D.__mro__)
```

**Output**
``` text
B: Masala Blend

D > C > B > A > object
```

---
