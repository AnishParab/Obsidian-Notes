# Code
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

**Output**:
``` text
Sorry that chai is not on menu

Quantity must be a number

Total cost is 40
```

---
# Learning the new Syntax
**Syntax**
``` python
# New Syntax
price = {"masala": 20}[item]
```

**When we send `ginger`**
``` python
process_order("ginger", 2)
```

**We internally check it as**
``` python
price = {"masala": 20}["ginger"]
```

> So basically, both the keys, `masala` and `ginger` are checked and if they don't match then **KeyError** is raised.

---
