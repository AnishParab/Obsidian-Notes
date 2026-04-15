# Code
``` python
def make_chai():
	return "Here is your masala chai"

return_value = make_chai()

print(return_value)
```

---
# What can you return ?
- Nothing -> implicitly returns None
- One value
- Multiple values
- Early return

---
# Code (Nothing)
``` python
def idle_chaiwala():
	pass

print(idle_chaiwala())
```

**Output**
``` text
None
```

---
# Code (One value)
``` python
def sold_cups():
	return 120

total = sold_cups()
print(total)
```

**Output**
``` text
120
```

---
# Code (Multiple value)
``` python
def chai_report():
	return 100, 20, 10 # sold, remaining
	
sold, remaining, _ = chai_report()

print("Sold ", sold)
print("Remaining ", remaining)
print("Common Practice to use '_' ", _)
```

**Output**
``` text
Sold  100
Remaining  200
Common practice to use '_'  10
```

---
# Code (Early return)
``` python
def chai_status(cups_left):
	if cups_left == 0:
		return "Sorry, chai over"
	return "Chai is ready"

print(chai_status(0))
print(chai_status(5))
```

**Output**
``` text
Sorry, chai over
Chai is ready
```

---
