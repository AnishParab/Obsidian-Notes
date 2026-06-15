# C3 Linearization

**How MRO is calculated**
- Left to right — order of parents in class definition matters
- Depth first — goes deep before moving to next parent
- No class appears before its subclasses

**Example**
``` python
class D(B, C):  # B before C → B comes first in MRO
    pass

class D(C, B):  # C before B → C comes first in MRO
    pass
```

---
