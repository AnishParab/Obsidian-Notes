# Problem
Some chai falvors are out of stock. You want to skip those and stop entirely if someone requests a restricted flavor.
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

---
# Code `for else`
``` python
staff = [("Amit, 16), ("Zara, 17), ("Raj", 15)]

for name, age in staff:
	if age >= 18:
		print(f"{name} is eligible to manage the staff")
		break
else:
	print(f"No one is eligible to manage the staff")	
```

- **The else block only runs if the loop didn't break.**
- Hence in the above code, the else block runs since break didn't run.

---
