# Default Parameters`eg:- empty list`
``` python
def chai_order(order=[]):
	order.append("Masala chai")
	print(order)
	
chai_order()
chai_order()
```

**Output**
``` text
['Masala', 'Masala']
```

---
# Code (Default Parameters)
##### Example 1
``` python
def chai_order(order=None):
	if order is None:
		order = []
	print(order)
		
chai_order()
```
**Output**
``` text
[]
```

##### Example 2
``` python
def greet(name = "Shutter Island"):
	print(f"Welcome to {name}")
	
greet()
greet("Derry")
```
**Output**
``` text
Welcome to Shutter Island
Welcome to Derry
```

---
