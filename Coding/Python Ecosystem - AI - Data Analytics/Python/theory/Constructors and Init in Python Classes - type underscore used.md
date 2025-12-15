# Example (Constructors)
``` python
class ChaiOrder:
	# Creating a Constructor
	def __init__(self, type_, size):
		self.type = type_
		self.size = size
		
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
- ` __init__ is the constructor method that runs automatically when an object is created.`

---
# Why type_ (with underscore) is used:

- Type is a built-in function in Python (used to check the type of an object).
- To avoid overriding or shadowing this built-in name, developers use a trailing underscore (type_) for variable or parameter names that might conflict.

---
