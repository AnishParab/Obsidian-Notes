# Code (Local)
``` python
def serve_chai():
	chai_type = 'Masala' # local scope
	print(f"Inside function {chai_type}")
	
chai_type = "Lemon" # global scope
serve_chai()
print(f"Outside function: {chai_type}")
```

Output:
``` text
Inside function Masala
Outside function: Lemon
```

---
# Code (Enclosing)
``` python
def chai_counter():
	chai_order = "Lemon" # Enclosing scope
	def print_order():
		chai_order = "Ginger" # Local scope
		print("Inner: ", chai_order)
	print_order()
	print("Outer: ", chai_order)
	
chai_order = "Tulsi" # Global scope
chai_counter()
print("Global: ", chai_order)
```

Output:
``` text
Inner: Ginger
Outer: Lemon
Global: Tulsi
```

---
