# Number Types **(Immutable Data Types)**

## **Integers (`int`)** – Whole numbers, positive or negative.  
    _Examples:_ `10`, `-5`, `0`
``` python
# Improve readability
total_tea_leaves_harvested = 1_000_000_000
```

---
## **Booleans (`bool`)** – Logical values representing truth.  
    _Values:_ `True`, `False`
**True = 1**
**False = 0**
``` python
# Upcasting
# Boolean
is_boiling = True
stir_count = 5

# Upcasting
total_actions = stir_count + is_boiling
```

---
## **Floating-Point (`float`)** – Numbers with decimal points.  
    _Examples:_ `3.14`, `-0.5`, `2.0`0
``` python
import sys
from fractions import Fraction
from decimal import Decimal

# Real numbers
ideal_temp = 95.5
current_temp = 95.4999999999
print(f"Ideal temp {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Difference temp {ideal_temp - current_temp}")
print(sys.float_info)
```

---
## **Complex Numbers (`complex`)** – Combine real and imaginary parts.  
    _Examples:_ `2 + 3j`, `-1j`, `4 - 2j`
- Dealt with using the **Fractions** library in Python.

---
