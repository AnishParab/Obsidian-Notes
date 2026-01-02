# Example Code
``` python
def brew_chai(flavor):
	if flavor not in ["masala", "ginger", "elaichi"]:
		# Syntax
		raise ValueError("Unsupported chai flavor....")
	print(f"brewing {flavor} chai....")
	
brew_chai("mint")

print()

brew_chai("masala")
```

**Output**
``` text
ValueError: Unsupported chai flavor....

brewing masala chai....
```

---
