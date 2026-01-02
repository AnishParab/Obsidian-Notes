# Problem
Some chai flavors are out of stock. You want to skip those and stop entirely if someone requests a restricted flavor.
- Skip if flavor is `"Out of Stock"`
- Break if flavor is `"Discontinued"`

---
# Code for Break and Continue
``` python
flavors = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in flavors:
	if flavor == "Out of Stock":
		continue
	if flavor == "Discontinued":
		break
	print(f"{flavor} item found")
	
print(f"Outside of loop")
```

**Output**
``` text
Ginger item found
Lemon item found
Outside of loop
```

---
