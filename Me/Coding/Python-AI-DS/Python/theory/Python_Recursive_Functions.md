# Code (Recursive Functions)
``` python
def pour_chai(n):
	print(n)
	if n == 0:
		return "All cups poured"
	return pour_chai(n-1)
	
 pour_value = pour_chai(3)
 print(pour_value)
```

---
