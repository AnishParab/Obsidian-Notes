# Example code
``` python
# Class Methods
class ChaiOrder:
	def __init__(self, tea_type, sweetness, size):
		self.tea_type = tea_type
		self.sweetness = sweetness
		self.size = size

# Accepting values as a dictionery
# Does'nt use self but uses cls which is the reference to the same class
	@classmethod
	def from_dict(cls, order_data):
		return cls(
			order_data["tea_type"],
			order_data["sweetness"],
			order_data["size"],
		)
		
	@classmethod
	def from_string(cls, order_string):
		tea_type, sweetness, size = order_string.split("-")
		return cls(tea_type, sweetness, size)

# Staic Methods
class ChaiUtils:
	@staticmethod
	def is_valid_size(size):
		return size in ["Small", "Medium", "Large"]
		
print(ChaiUtils.is_valid_size("Medium"))

order1 = ChaiOrder.from_dict({"tea_type" : "masala", "sweetness": "medium", "size": "Large"})

order2 = ChaiOrder.from_string({"Ginger-Low-Small"})

order3 = ChaiOrder("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)
```

---
# Difference Between Class and Static Methods
- None of them access to self.
- Access to cls.

---
