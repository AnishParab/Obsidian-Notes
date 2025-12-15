- `x=5` ---> This is a statement
- `3+3` ---> This is an expression

---
# Code
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

if (requested_size := input("Enter your chai cup size:\n").lower()) in available_size: 
	print(f"Serving {requested_size} chai")
else:
	print(f"Size is unavailable - {requested_size}")
```

- **No need to declare remainder separately**.

---
