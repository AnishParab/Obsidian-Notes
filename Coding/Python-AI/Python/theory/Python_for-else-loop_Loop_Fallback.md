# Code `for else`
``` python
staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
	if age >= 18:
		print(f"{name} is eligible to manage the staff")
		break
else:
	print(f"No one is eligible to manage the staff")	
```

- **The else block only runs if the loop didn't break.**
> Triggered only when **break** occurs.
- Hence in the above code, the else block runs since break didn't run.

---
