- `x=5` ---> This is a statement --> It is just an **assignment**
- `3+3` ---> This is an expression ---> Its **returns** something

---
# Code (without walrus operator)
``` python
value = 13
remainder = value % 5

if remainder:
	print(f"Not divisible, remainder is {remainder}")
```

---
# Using Walrus Operator
``` python
value = 13

if (remainder := value % 5):
	print(f"Not divisible, remainder is {remainder}")
	
available_sizes = ["small", "medium", "large"]

if (requested_size := input("Enter your chai cup size:\n").lower()) in available_sizes: 
	print(f"Serving {requested_size} chai")
else:
	print(f"Size is unavailable - {requested_size}")
	
flavors = ["masala", "ginger", "lemon", "mint"]
print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
	print(f"Sorry, {flavor} is not available")
	
print(f"You choose {flavor} chai")
```

- **No need to declare remainder separately**.

---
