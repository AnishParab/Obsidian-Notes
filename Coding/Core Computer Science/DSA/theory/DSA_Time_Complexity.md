# **NOTE**
> **Apriori analysis** always gives us the approximate results.

> **Apriori Analysis** is finding **time complexity** of an algorithm, which is denoted by **Asymptotic Analysis**.

---
# Time Complexity
Time complexity measures the **order of magnitude of execution**, not the exact runtime.
It reflects **how many times the operations in an algorithm execute** as the input size (n) grows.

---
### **Magnitude of a Statement**
The **magnitude** of a statement refers to:
$$
[
\text{number of times the statement is executed}
]
$$
Time complexity classifies this execution count using asymptotic notation such as $(O(1)), (O(n)), (O(n^{2}))$, etc.

---
# Example
##### **main function**
```c
x = y + z;
```
This statement runs **exactly once**, regardless of input size (n).

> Not dependent on **n**.

Therefore:
$$
[
T(n) = O(1)
]
$$
This is a **constant-time** operation and represents the **worst-case time complexity** for that statement.

---
