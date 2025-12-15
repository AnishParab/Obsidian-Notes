# Code (Pure Function)
``` python
def pure_chai(cups):
	return cups * 10

total_chai = 0
```

---
# Code (Impure Function) **Not Recommended**
``` python
total_chai = 0

def impure_chai(cups):
	global total_chai
	total_chai += cups
```

---
# Code (Recursive Functions)
``` python
def pour_chai(n):
	print(n)
	if n == 0:
		return "All cups poured"
	return pour_chai(n-1)
	
 return pour_value = pour_chai(3)
 print(pour_value)
```

---
# Code (Lambdas)
``` python
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_Chai)
```

Output:
``` text
['light', 'ginger']
```

---
