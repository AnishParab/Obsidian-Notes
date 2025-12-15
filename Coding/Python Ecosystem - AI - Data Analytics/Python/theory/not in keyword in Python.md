# Code
``` python
flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
	print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")
```

---
