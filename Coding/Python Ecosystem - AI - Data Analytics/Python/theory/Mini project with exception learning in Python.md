# Question
- Make a **bill app**

---
# Example Code
``` python
class InvalidChaiError(Exception): pass

def bill(flavor, cups):
	menu = {"masala": 20, "ginger": 40}
	try:
		if flavor not in menu:
			raise InvalidChaiError("That chai is not available")	
		if not isinstance(cups, int):
			raise TypeError("Number of cups must be an integer")
		total = menu[flavor] * cups
		print(f"Your bill for {cups} of {flavor} chai: rupees {total}")
		
	except Exception as e:
		print("Error: ", e)
	finally:
		print("Thank you, Visit again")
		
bill("mint", 2)
bill("masala", "three")
bill("ginger", 3)
```

**Output**
``` text
Error:  That chai is not available
Thank you, Visit again

Error:  Number of cups must be an integer
Thank you, Visit again

Your bill for 3 of ginger chai: rupees 120
Thank you, Visit again
```

---
