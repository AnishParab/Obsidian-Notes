``` cpp
int width = 5; // copy-initialization of value 5 into variable width
```

---
- **Don't Use** as it is inefficient for some complex types.
- It copies a value from the RHS to the LHS.

---
# **NOTE**
Copy-initialization is also used whenever values are _implicitly copied_ , such as when passing arguments to a function by value, returning from a function by value, or catching exceptions by value.

---
