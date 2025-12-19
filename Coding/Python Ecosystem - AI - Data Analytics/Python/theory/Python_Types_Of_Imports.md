# Common Other types of Imports
## 1. Importing a Module
- Imports the **entire module**.
```python
import math
```

Usage:
```python
math.sqrt(16)
```

**Use when**
- You want clarity
- You want to avoid name collisions

---
## 2. Importing a Module with Alias
- Gives the module a **shorter name**.
```python
import numpy as np
import pandas as pd
```

Usage:
```python
np.array([1, 2, 3])
```

**Use when**
- Module name is long
- Industry-standard aliases exist

---
## 3. Importing Specific Objects from a Module
- Imports only selected functions/classes/variables.
```python
from math import sqrt, pi
```

Usage:
```python
sqrt(25)
```

**Use when**
- You need only a few objects
- You want concise code

---
## 4. Importing with Alias (Selective)
- Renames imported objects.
```python
from math import sqrt as square_root
```

Usage:
```python
square_root(36)
```

---
## 5. Star Import (Wildcard Import)
- Imports **everything** from a module.
```python
from math import *
```

⚠️ **Avoid this**
- Pollutes namespace
- Causes name collisions
- Hard to debug
- Bad for readability

---
## 6. Conditional Import
- Import based on condition.
```python
if DEBUG:
    import logging
```

---
## 7. Import Order (Best Practice)

```python
# Standard library
import os
import sys

# Third-party
import numpy as np

# Local application
from recipes.flavors import ginger_chai
```

---
