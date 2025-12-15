# `nonlocal` keyword code
``` python
def update_order():
	chai_type = "Elaichi"
	def kitchen():
		nonlocal chai_type
		chai_type = "Kesar"
	kitchen()
	print("After kitchen update", chai_type)	
	
update_order()
```

- `chai_type` can now be used from one level above the current function.

Output
``` text
After kitchen update kesar
```

---
# `global` keyword code
``` python
chai_type = "Plain"

def front_desk():
	def kitchen():
		global chai_type
		chai_type = "Irani"
	kitchen()
	
front_desk()
print("Final global chai", chai_type)
```

- `chai_type` can now be used from the global scope.

Output
``` text
Final global chai Irani
```

---
