# Code: Immutable
``` python
chai = "Ginger chai"

def prepare_chai(order):
	print("Preparing ", order)
	
prepare_chai(chai)
# Original value will not change
print(chai)
```

Output
``` text
Preparing Ginger chai
Ginger chai
```

---
# Code: Mutable
``` python
chai = [1,2,3]

def edit_chai(cup):
	cup[1] = 42
	
edit_chai(chai)
print(chai)
```

Output
``` text
[1,42,3]
[1,42,3]
```

---
# Two types of arguments
- `args` - Arguments
- `kwargs` - Key-value arguments

---
## Positional and Keyword Arguments Code
``` python
def make_chai(tea, milk, sugar):
	print(tea, milk, sugar)

# Positional
make_chai("Darjeeling", "Yes", "Low")

# Keywords
make_chai(tea="Green", sugar="Medium", milk="No")
```

---
# Code
``` python
def special_chai(*ingredients, **extras):
	print("Ingredients", ingredients)
	print("Extras", extras)
	
special_chai("Cinnamon", "Cardmom", sweetner="Honey", foam="yes")
```

Output
``` text
Ingredients ('Cinnamon', 'Cardmom')
Extras {'sweetner': 'Honey', 'foam': 'yes'}
```
- Hence `Ingredients` will get all the non-named attributes.
- And `Extras` will get all the named attributes.

---
# Default values
``` python
def chai_order(order=[]):
	order.append("Masala chai")
	print(order)
	
chai_order()
chai_order()
```

Output:
``` text
['Masala', 'Masala']
```

---
# Code
``` python
def chai_order(order=None)
	if order is None:
		order = []
	print(order)
		
chai_order()
```

---
