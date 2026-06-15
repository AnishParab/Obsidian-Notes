# Code

``` python
## Without recursion
arr = [2, 1, 8, 9, 12, 15, 11, 19]
arr.sort()


def binary_search(arr, key, i, j):
    while i <= j:
        mid = i + (j - i) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            i = mid + 1
        else:
            j = mid - 1
    return -1


key = 11
i = 0
j = len(arr) - 1
result = binary_search(arr, key, i, j)

print("Searching element is present at index", result)
```

---
**See time complexities here**
[[DSA_Arrays_Binary_Search_1D_Array_Theory]]

> Hence this one is better compared to `with recursion`, as *space complexity* is **lesser**.

---
