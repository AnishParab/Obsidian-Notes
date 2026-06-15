# Problem Statement

**Constraints**
- Row-wise sorted from left to right
- First integer of each row $>$ Last integer of the previous row, eg:- $10 > 7$

$$
\begin{bmatrix}
1 & 3 & 5 & 7 \\
10 & 11 & 16 & 20 \\
23 & 30 & 34 & 60
\end{bmatrix}
$$

- Let $target = 3$ then *output* is **true**.
- Let $target = 22$ then *output* is **false**.

###### Brute Force Approach
- **Time Complexity**: $O(n^2)$

---
# Pseudocode

- Convert the array into it's **row major form**
$$
[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]
$$
- Now you can apply *Binary Search*
- Hence the **time complexity** is $O(log \ m n)$

###### Formulae to calculate *row number* and *column number*

> $row \ number = index \ // \ total \ number \ of \ columns$
 $column \ number = index \ \% \ total \ number \ of \ columns$

---
# Code

``` python
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]


def search_sorted_matrix(matrix, target):
    # Number of rows
    m = len(matrix)

    if m == 0:
        return False

    # Number of columns
    n = len(matrix[0])

    left, right = 0, m * n - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_element = matrix[mid // n][mid % n]

        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1

    return False


target = 16
result = search_sorted_matrix(matrix, target)

print("Searching element present status =", result)
```

---
