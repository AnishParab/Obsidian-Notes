# What ?
- An **array** in JavaScript is an **ordered list-like object** used to store multiple values.
- Unlike some languages, JS arrays:
    - Can hold **mixed types** (`string`, `number`, `object`, etc.).
    - Can be **sparse** (missing indices).
    - Are **dynamic** (can grow/shrink in size).
- Internally, JavaScript arrays are **objects with special handling for integer keys**.

---
# Example
``` js
let arr = [1, "two", true, { key: "value" }];
console.log(arr[3]); // { key: "value" }
```

---
> **Large arrays** may become _deoptimized_ in V8 if they store mixed types.

---

