# Example 1
$$
[  
1000. n\log n  
]
$$
Constants do not matter in asymptotic notation:
$$
[  
1000 . n\log n \in O(n\log n)  
]
$$
**Final:**  
$$
[  
O(n\log n)  
]
$$

---
# Example 2
$$
[  
n^{3}\cdot 64^{\log_{64} n}  
]
$$
Use the identity:
$$
[  
a^{\log_{a} n} = n  
]
$$
So:
$$
[  
64^{\log_{64} n} = n  
]
$$
Therefore:
$$
[  
n^{3} \cdot n = n^{4}  
]
$$
**Final:**  
$$
[  
O(n^{4})  
]
$$

---
# Example 3
$$
[  
64^{\log_{2} n} \cdot 32^{\log_{2} n}  
]
$$
Convert each base to powers of 2:
- $(64 = 2^{6})$
- $(32 = 2^{5})$
So:
$$
[  
64^{\log_{2} n} = (2^{6})^{\log_{2} n} = n^{6}  
]  
$$
$$
[  
32^{\log_{2} n} = (2^{5})^{\log_{2} n} = n^{5}  
]
$$
Multiply:
$$
[  
n^{6} \cdot n^{5} = n^{11}  
]
$$
**Final:**  
$$
[  
O(n^{11})  
]
$$

---
# Example 4
$$
[  
f(n)=\frac{1}{n}  
]
$$
As $(n\to\infty)$:
$$
[  
f(n) = \Theta!\left(\frac{1}{n}\right)  
]
$$
Nothing else simplifies.
**Final:**  
$$
[  
\Theta\left(\frac{1}{n}\right)  
]
$$

---
