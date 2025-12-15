# Example Code 1 - `try-except`
``` python
chai_menu = {"masala": 30, "ginger": 40}

# KeyError
# chai_menu["elaichi"]

try:
	chai_menu["elaichi"]
except KeyError:
	print("Key is not accessible")
	
print("Hello there!")
```

**Output**
``` text
Key is not accessible
Hello there!
```

---
# Example Code 2 - `raise` `else` `finally`
``` python
def serve_chai(flavor):
	try:
		print(f"Preparing {falvor} chai....")
		if flavor == "unknown":
			raise ValueError("We don't known that flavor")
	except ValueError as e:
		print("Error: ", e)
	else:
		print(f"{flavor} chai is served")
	finally:
		print("Next customer please")	
		
serve_chai("masala")
serve_chai("unknown")
```

**Output**
``` text
Preparing masala chai....
masala chai is served
Next customer please

Preparing unknown chai....
Error: We don't know that flavor
Next customer please
```

---
