# Ternary Search: Code with recursion

``` python
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def ternary_search(arr, left, right, target):
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if target == arr[mid1]:
            return mid1
        elif target == arr[mid2]:
            return mid2
        elif target < arr[mid1]:
            return ternary_search(arr, left, mid1 - 1, target)
        elif target > arr[mid2]:
            return ternary_search(arr, mid2 + 1, right, target)
        else:
            return ternary_search(arr, mid1 + 1, mid2 - 1, target)

    return -1


left = 0
right = len(arr) - 1

target = 2

result = ternary_search(arr, left, right, target)

print("Element at", result)
```

---
**Time Complexity**: $O(log_3 n)$
**Space Complexity**: $O(log_3 n)$

> Since **space complexity** is *greater* for recursive we follow the non-recursive approach.

[[DSA_Arrays_Ternary_Search_Code_without_recursion]]

---
