# Example 1
##### **main**
```python
i = n

while (i > 1):
    i = i - 1
```
##### **Execution Count**
The loop runs as long as:
$$
[  
i > 1  
]
$$
Starting from (i = n), the loop decrements (i) by 1 each iteration:
$$
[  
n \rightarrow n-1 \rightarrow n-2 \rightarrow \dots \rightarrow 2  
]
$$
If (n = 5):
- Iterations: (5, 4, 3, 2)
- That is **4 executions**, which equals (n - 1).
In general:
$$
[  
\text{Number of iterations} = n - 1  
]
$$
##### **Asymptotic Time Complexity**
$$
[  
n - 1 \in O(n)  
]
$$
Thus:
$$
[  
T(n) = O(n)  
]
$$
This is a simple linear-time loop.

---
# Example 2
##### **main**
```python
i = n
while i >= 1:
    i = i - 2
```
##### **Execution Count**
The loop decreases `i` by **2** each iteration.
For (n = 10):
$$
[  
10 \rightarrow 8 \rightarrow 6 \rightarrow 4 \rightarrow 2 \rightarrow 0  
]
$$
This is **5 iterations**.
In general, the number of iterations is:
$$
[  
\frac{n}{2}  
]
$$
(More precisely: $(\left\lceil \frac{n}{2} \right\rceil))$
##### **Asymptotic Time Complexity**
$$
[  
\frac{n}{2} \in O(n)  
]
$$
Thus:
$$
[  
T(n) = O(n)  
]
$$
This is still **linear time**, because constants do not affect asymptotic complexity.

---
