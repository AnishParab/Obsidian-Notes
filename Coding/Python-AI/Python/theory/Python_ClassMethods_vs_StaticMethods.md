# Difference Between Class and Static Methods

| Feature          | `@classmethod`                     | `@staticmethod`                       |
| ---------------- | ---------------------------------- | ------------------------------------- |
| First parameter  | `cls`                              | None                                  |
| Use case         | Operate on the class, not instance | Utility function related to the class |
| Access to `cls`  | Yes                                | No                                    |
| Access to `self` | No                                 | No                                    |

---
# Example code
> To accept values in any format such as a dictionary and string using a classmethod.

``` python
# Class Methods
class ChaiOrder:
	def __init__(self, tea_type, sweetness, size):
		self.tea_type = tea_type
		self.sweetness = sweetness
		self.size = size

	# Syntax
	@classmethod
	def from_dict(cls, order_data):
		return cls(
			order_data["tea_type"],
			order_data["sweetness"],
			order_data["size"],
		)

	# Syntax
	@classmethod
	def from_string(cls, order_string):
		tea_type, sweetness, size = order_string.split("-")
		return cls(tea_type, sweetness, size)

# Staic Methods
class ChaiUtils:
	@staticmethod
	def is_valid_size(size):
		return size in ["Small", "Medium", "Large"]

# Accessing Static Method
print(ChaiUtils.is_valid_size("Medium"))

print()

# Accessing Class Methods
order1 = ChaiOrder.from_dict({"tea_type" : "masala", "sweetness": "medium", "size": "Large"})

# Accessing Class Methods
order2 = ChaiOrder.from_string({"Ginger-Low-Small"})

# Accessing the class
order3 = ChaiOrder("Large", "Low", "Large")

# Print key-value pairs
print(order1.__dict__)
print()
print(order2.__dict__)
print()
print(order3.__dict__)
```

**Output**:
``` text
True

{'tea_type': 'masala', 'sweetness': 'medium', 'size': 'Large'}

{'tea_type': 'Ginger', 'sweetness': 'Low', 'size': 'Small'}

{'tea_type': 'Large', 'sweetness': 'Low', 'size': 'Large'}
```

---
