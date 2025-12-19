# Code (Pure Function)
- You don't touch anything globally.
- It does not change external state.
``` python
def pure_chai(cups):
	return cups * 10

total_chai = 0
```

---
# Code (Impure Function) **Not Recommended**
- You use global variable, using **global** to change it globally.
``` python
total_chai = 0

def impure_chai(cups):
	global total_chai
	total_chai += cups
```

---
