# NOTE (Shortcut):
> Mostly used when there is a function inside a funstion.

---
# `nonlocal` keyword code
``` python
def update_order():
	chai_type = "Elaichi"
	def kitchen():
		# print(chai_type) here, gives syntax error, Explained at last
		nonlocal chai_type
		chai_type = "Kesar"
		print(chai_type)
	kitchen()
	print("After kitchen update", chai_type)	
	
update_order()
```

- `chai_type` can now be used from **one level above** the current function.

**Output**
``` text
Kesar
After kitchen update Kesar
```

**If `nonlocal` was not used, output would have been:**
``` text
Kesar
After kitchen upadte Elaichi
```

---
# `global` keyword code
``` python
chai_type = "Plain"

def front_desk():
	def kitchen():
		# print(chai_type) here, gives syntax error, Explained at last
		global chai_type
		chai_type = "Irani"
		print(chai_type)
	kitchen()
	
front_desk()
print("Final global chai", chai_type)
```

- `chai_type` can now be used from the **global** scope.

**Output**
``` text
Irani
Final global chai Irani
```

---
# Summary
- `global` gives access to global scoped object only, and hence it can be changed.
- `nonlocal` gives access to one level above the current function only, and hence it can be changed.

---
# Syntax Error Explanation
- `chai_type` cannot be used before, if using `nonlocal` or `global`.
- `nonlocal` (and `global`) are **declarations**, not statements.  
- Python requires them to appear **at the top level of a function body**, not inside control blocks like `if`, `for`, or `while`.
- That is why this is a **syntax error**, not a logic error.

---
