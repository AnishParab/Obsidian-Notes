# `=` Assignment Operator
- **Purpose:** Assigns a value to a variable.
- **Does not compare** — it just stores a value.
``` js
let a = 5;    // Assigns 5 to a
let b = "hi"; // Assigns "hi" to b
```

---
# `==` (Equality Operator – Loose Comparison)
- **Purpose:** Compares two values **after converting them to the same type** (type coercion).
- This can lead to unexpected results because it tries to be "helpful."
``` js
5 == "5"    // true (string "5" is converted to number 5)
0 == false  // true (false is converted to 0)
null == undefined // true (special case)
```

---
# `===` (Strict Equality Operator)
- **Purpose:** Compares **both value and type** — no type conversion happens.
- **Safer** and more predictable than `==`.
``` js
5 === "5"   // false (different types: number vs string)
0 === false // false (number vs boolean)
5 === 5     // true (same type and value)
```

---
> Use `===` and `!==` for comparisons to avoid unexpected type coercion issues.  
> Use `=` only for assigning values.

---
