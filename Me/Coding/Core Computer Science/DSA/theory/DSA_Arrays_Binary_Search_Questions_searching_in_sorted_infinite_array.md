# Problem Statement

- Suppose you have  a sorted array of infinite numbers, how would you search an element in the array

###### Pseudocode Approach
- **Chunking approach**

---
# Code

``` python
import math

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91, 105, 134, 167, 190, 210] + [math.inf] * 1000


def search_infinite(arr, lo, hi, target):
    while arr[hi] < target:
        lo = hi
        hi *= 2

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


lo = 0
hi = 1
target = 91

result = search_infinite(arr, lo, hi, target)

print(f"{target} is at index {result}")
```

---
**Time complexity**: $O(log n)$
**Space complexity**: $O(1)$

---
