# Represents Worst Case Scenario **(Preferred)**
**Asymptotic Notation:**
$$
[
O(f(n))
]
$$

Describes the **upper bound** on running time — the algorithm will never be slower than this bound.

> **NOTE**: This is mostly used to optimize your code.

---
# Input size (n) : For machine specific : Aposteriori Analysis
![[bigO.excalidraw]]

---
# Big O Notation
To express that a function ( f(n) ) grows **no faster** than another function ( g(n) ), we write:
$$
[
f(n) = O(g(n))
]
$$
This means **“f(n) is bounded above by g(n) up to constant factors.”**

### **Formal Definition**
$$
[
f(n) = O(g(n))
\quad\text{iff}\quad
\exists, c > 0,; n_0 \ge 1; \text{such that}
]
$$
$$
[
0 \le f(n) \le c \cdot g(n) \quad \text{for all } n \ge n_0
]
$$
### **Conditions Summary**
* $( c > 0 )$ is a constant multiplier
* $( n_0 \ge 1 )$ is a threshold after which the inequality holds
* For all $( n \ge n_0 )$:
  $$
  [
  f(n) \le c \cdot g(n)
  ]
  $$

---
# Graphical Representation
![[bigOOOO.excalidraw]]

---
# Example
Given:
$$
[
f(n) = n^2,\qquad g(n) = n
]
$$
Check whether:
$$
[
f(n) = O(g(n))
]
$$
### Test the Big-O condition
Big-O requires:
$$
[
f(n) \le c \cdot g(n) \quad \text{for all } n \ge n_0
]
$$
Substitute:
$$
[
n^2 \le c \cdot n
]
$$
Divide both sides by ( n ) (valid for ( n > 0 )):
$$
[
n \le c
]
$$
This forces:
$$
[
c = n
]
$$
But **c must be a constant**, and here it depends on ( n ).
Therefore the inequality cannot hold for all large ( n ).

### Conclusion
$$
[
n^2 \notin O(n)
]
$$
Hence:
$$
[
f(n) \ne O(g(n))
]
$$

---
