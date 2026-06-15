# Binary Search
 
 - This problem is an application of **divide and conquer** approach. 

---
# Pre-requisites - Sorted Array

> The array should be arranged in an ascending order.

---
# Middle Value

- Approach 1
$$
mid = \frac{(i+j)}{2}
$$
- Approach 2 **(Preferred)**
$$
mid = i + \frac{(j-i)}{2}
$$

> Approach 1 has the problem of **overflow** - *Summation of  `i` and `j` can be large*

---
# Algorithm

![[binary_search.excalidraw|500]]

---
# Time Complexities

- **Best**: $O(1)$ — target is the mid element
- **Worst**: $O(log n)$ — element not present or at the edge
- **Average**: $O(log n)$

---
# Space Complexities

- **Iterative**: $O(1)$ — no extra space
- **Recursive**: $O(log n)$ — call stack depth = $log n$

---
