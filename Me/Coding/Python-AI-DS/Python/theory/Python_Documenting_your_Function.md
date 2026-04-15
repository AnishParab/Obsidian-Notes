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
