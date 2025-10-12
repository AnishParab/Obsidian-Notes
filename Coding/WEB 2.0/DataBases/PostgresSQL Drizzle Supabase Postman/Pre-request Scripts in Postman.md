# **Pre-request Scripts**
- JS code that runs **before the request**.
- Used for generating tokens, setting timestamps, random IDs, etc.  
    Example:
``` js
pm.variables.set("uuid", crypto.randomUUID());

```

---
