# What is Recursion ?
- Recursion is when a function solves a problem by **calling itself**, each time with a **smaller or simpler** version of the same problem, until it reaches a **base case** that stops the calls.

 - **Recursive Case**
The part where the function calls itself.

- **Base Case**
The stopping condition that prevents infinite recursion.

---
# Example
``` python
def fact(n):
    if n == 0:      # base case
        return 1
    return n * fact(n - 1)   # recursive case
```

The recurrence relation represented by that code is:
$$
\[
\begin{aligned}
f(0) &= 1, \\
f(n) &= n \cdot f(n-1) \quad \text{for } n > 0.
\end{aligned}
\]

$$

---
# What is Recurrence Relation ?
A recurrence relation expresses:
$$
T(n)=some\;function\;involving\;T(smaller\;n)
$$
It describes how a problem of size `n` depends on solutions of **smaller subproblems**.

---
# Recurrence relation can be solved using Three Methods
- **Substitution method**
- **Recursive tree approach**
- **Masters theorem**

---
