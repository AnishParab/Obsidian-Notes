# Multiple Exception Handling
- This is basically writing multiple **except cases**.

---
# **NOTE**
To understand the below code, refer this first:
[[Python_Checking_Keys_Dictionary_Syntax]]

---
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
		# New Syntax
        price = {"masala": 20}[item]
        quantity = int(quantity)
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except ValueError:
        print("Quantity must be a number")

process_order("ginger", 2)

print()

process_order("masala", "two")

print()

process_order("masala", 2)
```

**Output**
``` text
Sorry that chai is not on menu

Quantity must be a number

Total cost is 40
```

---
