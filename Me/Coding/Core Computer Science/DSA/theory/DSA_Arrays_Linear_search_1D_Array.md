# Linear Search

``` python
arr = [2, 1, 8, 9, 12, 15, 11, 19]


def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


x = 15

result = linear_search(arr, x)

print("Searching element is present at the index ", result)
```

---
# Time Complexities

- Worst Case Scenario
>**O(n)**.

- Best Case Scenario
> **O(1)**

- Average Case Scenario:
$$
\frac{1+2+3+.....+n}{n} = \frac{\frac{n(n+1)}{2}}{n} = \frac{n+1}{2}
$$
>hence, time complexity for average case is:
> **O(n)**

---
# Space Complexity

- We are not using any extra space apart from the given array:

> Space Complexity: **O(1)**.

---
