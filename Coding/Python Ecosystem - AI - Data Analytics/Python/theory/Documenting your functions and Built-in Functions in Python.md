# Built-in in Python
``` python
def chi_flavor(flavor == "masala"):
	"""Return the flavor of chai.""" # This need to be the first line or else it won't work
	return falvor
	
print(chai_flavor.__doc__)
print(chai_flavor.__name__)

# Opens up a vim-based doc
help(len)
```

Output:
``` text
Return the flavor of chai.
chai_flavor
```

- `__doc__` -> This is called as **dunder** rather than calling it as `underscore underscore`

---
# Documenting Functions
``` python
def generate_bill(chai=0, samosa=0):
	"""
	Calculate the total bill for chai and samosa
	
	:param chai: Number of chai cups (10 rupees each)
	:param samosa: Number of samosa (10 rupees each)
	:return: (total amount, thank you message as a string)
	"""
	total = chai*10 + samosa*15
	return total, "Thank you for visiting chaicode.com"
```

---
