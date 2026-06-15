# Problem Statement

- array -> $[20, -30, 10, 5, 7, 0, 29, \infty, \infty, \infty, \infty, .....]$
- Hence the `index value` of the first infinte here is `7`
- Hence **output = `7`**
###### Pseudocode
![[binary_search_interview_question_1.excalidraw|500]]

---
# Code

``` python
import math

# You will get the output as 7
arr = [20, -30, 10, 5, 7, 0, 29] + [math.inf] * 100


def first_infinte(arr):
    ## For finite arrays -> lo = 0, hi = len(arr) - 1
    lo, hi = 0, 1
    ## Time complexity is O(log n) for this loop
    while arr[hi] != math.inf:
        lo = hi
        hi *= 2

    ## Time complexity for binary search is O(log n)
    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] == math.inf and arr[mid - 1] != math.inf:
            return mid
        elif arr[mid] != math.inf:
            lo = mid + 1
        else:
            hi = mid - 1


result = first_infinte(arr)

print("The first infinite index value is", result)
```

---
**Time complexity**: $O(log n)$
**Space Complexity**: $O(1)$

---
