# Broadcasting Rules
### **1. NumPy lines up shapes from the right**
If one array has fewer dimensions, NumPy adds 1s to the **left** so both shapes match in length.

Example:
`(3,)` becomes `(1,3)`
`(3,1)` stays `(3,1)`

---
### **2. Each dimension must follow ONE of these:**
* Both sizes are **equal**, OR
* One of them is **1**
If not → broadcasting fails.

Example:
`(3,1)` and `(3,4)` → OK (because 1 can stretch to 4)
`(2,3)` and `(3,3)` → ERROR (2 ≠ 3)

---
### **3. Dimensions with size 1 stretch**
If a dimension is 1, NumPy **repeats** the values to match the larger array.

Example:
```
[10,20,30]  → shape (3,)
[[1,2,3],
 [4,5,6]] → shape (2,3)
```

The first array becomes:
```
[10,20,30]
[10,20,30]
```

---
# Broadcasting Limitations

### **1. If any dimension doesn’t match and neither is 1 → ERROR**
This is the most important limitation.

Example: `(2,3)` + `(3,3)` → cannot broadcast → shapes incompatible.

---
### **2. Broadcasting can create large temporary arrays (memory cost)**
If you broadcast something small across a huge array, NumPy internally treats it as large during operations.
This can slow things down.

---
### **3. Only works for element-wise operations**
Broadcasting works for:
* addition, subtraction, multiplication, division
* comparisons
* exponentiation

But **not** for matrix multiplication (`@`, `dot`, etc.).

---
### **4. Shapes must follow the rule — not all arrays can broadcast**
Broadcasting is flexible, but not magic.
The shapes still must match the rules above.

---
