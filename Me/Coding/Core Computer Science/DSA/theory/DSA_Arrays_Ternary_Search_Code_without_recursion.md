# Code: Without Recursion

``` python
def ternary_search(arr, left, right, target):
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if target == arr[mid1]:
            return mid1
        elif target == arr[mid2]:
            return mid2
        elif target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1
```

---
**Time complexity**: $O(log_3 n)$
**Space complexity**: $O(1)$

> Since **space complexity** is *lesser* for non-recursive we follow this approach over recursive one.

[[DSA_Arrays_Ternary_Search_Code_with_recursion]]


---
