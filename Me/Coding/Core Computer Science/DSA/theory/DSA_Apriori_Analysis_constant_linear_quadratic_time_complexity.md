# Example 1 (Constant Time Complexity)

``` python
x = y + z
```
#### **Execution Count**
- The first statement  
$$
    [  
    x = y + z  
    ]  
	$$
    executes **1 time** and not dependent on `n`.
##### **Conclusion**
The time complexity of the program is:
$$
[  
T(n) = O(1)  
]
$$


---
# Example 2 (Linear Time Complexity)
##### **main function**
```python
x = y + z

for i in range(0, n):
    x = y + z
```
#### **Execution Count**
- The first statement  
$$
    [  
    x = y + z  
    ]  
	$$
    executes **1 time**.
    
- The loop body  
$$
    [  
    x = y + z  
    ]  
	$$
    executes once per iteration.
    

Since the loop runs from (i = 0) to (i = n - 1):
$$
[  
\text{Loop executes } n \text{ times}  
]
$$
##### **Total executions**
$$
[  
1 + n = n + 1  
]
$$
Asymptotically:
$$
[  
n + 1 \in O(n)  
]
$$
##### **Conclusion**
The time complexity of the program is:
$$
[  
T(n) = O(n)  
]
$$

---
# Example 3 (Quadratic Time Complexity)
##### **main function**
```cpp
x = y + z;

for(i = 0; i < n; i++) {
    x = y + z;
}

for(i = 0; i < n; i++) {
    for(j = 0; j < n; j++) {
        x = y + z;
    }
}
```
##### **Execution Count Analysis**
###### **1. Single statement**
$$
[  
x = y + z  
]  
$$
Executes **1 time**.
###### **2. First loop**
```cpp
for(i = 0; i < n; i++) {
    x = y + z;
}
```
- Executes once per iteration.
- Loop runs **n times**.
$$
[  
\text{Executions} = n  
]
$$
###### **3. Nested loop**
```cpp
for(i = 0; i < n; i++) {
    for(j = 0; j < n; j++) {
        x = y + z;
    }
}
```
- Outer loop executes **n times**.
- Inner loop executes **n times** for each outer iteration.
$$
[  
\text{Total} = n \times n = n^{2}  
]
$$
#### **Total Execution Count**
$$
[  
1 + n + n^{2}  
]
$$
Asymptotically:
$$
[  
1 + n + n^{2} \in O(n^{2})  
]
$$
#### **Final Time Complexity**
$$
[  
T(n) = O(n^{2})  
]
$$

---
