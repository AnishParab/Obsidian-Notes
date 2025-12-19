# Two types of arguments
- `args` - Arguments - **Accepts any number of positional arguments**
- `kwargs` - Key-value arguments - **Accepts any number of keyword arguments into a dictionery**

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

**Output**
``` text
Ingredients ('Cinnamon', 'Cardmom')
Extras {'sweetner': 'Honey', 'foam': 'yes'}
```
- Hence `Ingredients` will get all the non-named attributes. **Arguments**
- And `Extras` will get all the named attributes. **Keyword Arguments**

---
