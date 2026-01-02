# `staticmethods`

> `staticmethod` does not require any **object creation**.

**A static method**:
- Does not receive `self`
- Does not receive `cls`
- Behaves like a regular function namespaced inside a class

---
# Usual Code
``` python
class ChaiUtils:
	# Instance method: receives 'self' automatically when called on an object
    def clean_ingredients(self, text):
        return [item.strip() for item in text.split(",")]


raw = " water, milk, ginger, honey "

# Usual way
obj = ChaiUtils()
print(obj.clean_ingredients(raw))
```

---
# Decorator Way
``` python
class ChaiUtils:
	# Static method: no access to instance (self) or class (cls)	
	
	@staticmethod
	def clean_ingredients(text):
		return [item.strip() for item in text.split(",")]
		
raw = " water, milk, ginger, honey "

# No object creation is required
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
```


---
