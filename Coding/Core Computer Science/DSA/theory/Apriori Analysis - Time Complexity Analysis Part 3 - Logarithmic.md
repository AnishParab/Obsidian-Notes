# Example 1
##### **main**
```python
i = n

while i > 2:
    i = i ** 0.5
```
##### **Execution Pattern**
Each iteration replaces:
$$
[  
i \leftarrow i^{1/2}  
]
$$
So values evolve as:
$$
- (n)
- (n^{1/2})
- (n^{1/4})
- (n^{1/8})
- (\dots)
$$
We stop when:
$$
[  
i \le 2  
]
$$
##### **Solve for Number of Iterations**
After (k) iterations:
$$
[  
i = n^{1/2^{k}}  
]
$$
Stop when:
$$
[  
n^{1/2^{k}} = 2  
]
$$
Take logarithm on both sides:
$$
[  
\log(n^{1/2^{k}}) = \log 2  
]
$$
Apply log rule:
$$
[  
\frac{1}{2^{k}} \log n = \log 2  
]
$$
Solve for (2^{k}):
$$
[  
2^{k} = \frac{\log n}{\log 2}  
]
$$
$$
[  
2^{k} = \log_{2} n  
]
$$
Take log base 2:
$$
[  
k = \log_{2}(\log_{2} n)  
]
$$
##### **Time Complexity**
$$
[
T(n)=O(\log_{2}\log_{2} n)
]
$$
##### **Check with your example (n = 256)**
$$
[  
\log_{2} 256 = 8  
]
$$
$$
[  
\log_{2} 8 = 3  
]
$$
Matches the observed iterations:
$$
[  
256 \rightarrow 16 \rightarrow 4 \rightarrow 2  
]
$$
Total = **3 iterations**

---
# **Example 2**
#### **main**
```python
i = n

while i > 2:
    i = i ** (1/25)
```
##### **Iteration Analysis**
Each iteration applies:
$$
[  
i \leftarrow i^{1/25}  
]
$$
After (k) iterations:
$$
[  
i = n^{1/25^{k}}  
]
$$
The loop stops when:
$$
[  
n^{1/25^{k}} \le 2  
]
$$
Take logarithm (base 2) on both sides:
$$
[  
\frac{1}{25^{k}} \log_{2} n \le \log_{2} 2  
]
$$
$$
[  
\frac{1}{25^{k}} \log_{2} n \le 1  
]
$$
Invert:
$$
[  
25^{k} \ge \log_{2} n  
]
$$
Take $(\log) base 25$:
$$
[  
k \ge \log_{25}(\log_{2} n)  
]
$$
##### **Final Big-O Time Complexity**
$$
[  
T(n) = O!\left(\log_{25} \log_{2} n\right)  
]
$$
Because changing the base of any logarithm is only a constant factor:
$$
[  
O(\log_{25} \log_{2} n) = O(\log \log n)  
]
$$
---
