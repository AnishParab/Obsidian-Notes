# Usual Code
``` python
class ChaiUtils:
	def clean_ingredients(text):
		return [item.strip() for item in text.split(",")]
		
raw = " water, milk, ginger, honey "

# Usual way
obj = ChaiUtils()
obj.clean_ingredients(raw)
```

---
# Decorator Way
``` python
class ChaiUtils:
	@staticmethod
	def clean_ingredients(text):
		return [item.strip() for item in text.split(",")]
		
raw = " water, milk, ginger, honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
```

> `staticmethod` does not require any **object creation**.

---
