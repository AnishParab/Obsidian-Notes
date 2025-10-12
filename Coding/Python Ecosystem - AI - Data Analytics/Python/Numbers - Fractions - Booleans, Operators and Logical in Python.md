# Types of Numbers
- Integers
- Boolean
- Real (Floating)
- Complex Numbers

---
# Operators
- `+`
- `-`
- `*`
- `/` ---> Real number outputs
- `//` ---> Integer outputs
- `%`
- `**`

---
# Improve readability in Python
``` python
total_tea_leaves = 1_000_000_000
```

- This is treated as `1000000000` only.

---
# Booleans
``` python
is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling
print(f"total actions: {total_actions}")
```

### Upcasting Output
``` bash
total actions: 6
```

### Hence
- `True` ---> 1 and any other value
- `False` ---> 0 and `None`

---
# Logical Operators
- `and`
- `or`
- `not`

---
# Real Numbers
``` python
import sys

print(sys.float_info)
```

- The output differs from machine to machine depending on RAM, CPU, etc.
- Python is known for it's precision.

---
# Fractions - Decimal
``` python
from fractions import Fraction
from decimal import Decimal
```

- These are designed for huge decimal point precision.

---
