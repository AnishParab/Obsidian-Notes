# Folder Structure
``` css
chai_business/
	main.py
	recipes/
		__init__.py
		flavors.py
	utils/
		discounts.py
```

# Importing Object/Functions
`flavors.py`
``` python
def elaichi_chai():
	return "Elaichi chai is ready"
	
def ginger_chai():
	return "Ginger chai is ready"
```

---
# `main.py`

**Example 1**
``` python
import recipes.flavors

print(recipes.falvors.ginger_chai())
```

**Example 2**
``` python
from recipes.flavors import elaichi_chai, ginger_chai

print(ginger_chai())
```

**Example 3 (Avoid importing * )**
``` python
from .recipes.flavors import *
```

---
# `__init__.py`
- This turns the python code into a **module**.

> You don't have to do this after **python 3.3** but it is still commonly used.

---
