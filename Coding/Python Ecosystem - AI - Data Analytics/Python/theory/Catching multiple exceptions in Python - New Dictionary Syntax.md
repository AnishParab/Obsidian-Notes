# Example Code
``` python
def process_order(item, quantity):
	try:
		price = {"masala": 20}[item]
		cost = price * quantity
		print(f"Total cost is {cost}")
	except KeyError:
		print("Sorry that chai is not on menu")
	except TypeError:
		print("Quantity must be in number")
		
process_order("ginger", 2)
process_order("masala", "two")
```

**Output**
``` text
Sorry that chai is not on menu

Total cost is twotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwo
```

---
# Corrected Code
``` python
def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        quantity = int(quantity)
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except ValueError:
        print("Quantity must be a number")


process_order("ginger", 2)
process_order("masala", "two")
```

**Output**
``` text
Sorry that chai is not on menu
Quantity must be a number
```

---
