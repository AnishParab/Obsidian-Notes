# Folder Structure
```text
chai_business/
│
├── main.py
│
├── recipes/
│   ├── __init__.py
│   ├── flavors.py
│
└── utils/
    └── discounts.py
```

---
# Packages and Modules
- **`recipes`** is a **package** because it contains an `__init__.py` file.
- **`flavors.py`** and **`discounts.py`** are **modules**.
- A **package** is a directory that groups related modules.

> Since **Python 3.3**, `__init__.py` is not strictly required (namespace packages),  
> but it is still **commonly used** for clarity and compatibility.

###### This can be used as a Package using:
``` python
import recipes
```

---
# Importing Functions / Objects

#### `recipes/flavors.py` - Function Definitions
```python
def elaichi_chai():
    return "Elaichi chai is ready"

def ginger_chai():
    return "Ginger chai is ready"
```

---
#### `main.py` - Importing the Functions
###### Example 1: Local Import / Runtime Import / Lazy Loading
``` python
def make_chai():
    from recipes.flavors import ginger_chai
    return ginger_chai()
```

###### Example 2: Absolute Import
``` python
from recipes.flavors import ginger_chai

print(ginger_chai())
```

###### Example 3: Module Import
```python
import recipes.flavors

print(recipes.flavors.ginger_chai())
```

###### Example 4: Selective Import
```python
from recipes.flavors import elaichi_chai, ginger_chai

print(ginger_chai())
```

###### Example 5: Import everything (NOT recommended)
```python
from recipes.flavors import *
```
❌ **Avoid this as much as possible** because:
- Pollutes the namespace
- Makes code harder to read
- Can cause name collisions
- Breaks static analysis and IDE support

---
# `__init__.py`
###### Example 6: Relative Import
``` python
from .flavors import ginger_chai
```
- `.` → current package (`recipes`)
- `..` → parent package

- Marks a directory as a **package** (traditional behavior)
- Can be used to:
    - Initialize package-level variables
    - Control what gets imported with `from package import *`
    - Re-export selected modules or functions

⚠️ **NOTE**
> `__init__.py` does **not** turn code into a module.  
> It turns a **directory into a package**.

---
