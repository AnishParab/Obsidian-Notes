# Problem Statement

- Let's call the array a mountain if the following property holds:
	- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
	- `arr[0] < arr[1] < .... < arr[i-1] < arr[i]`
	- `arr[i] > arr[i+1] > .... > arr[arr.length - 1]`

- **Example 1:**
``` bash
Input: arr = [0,1,0]
Output = 1 (index)
```

- **Example 2:**
``` bash
Input: arr = [0,2,1,0]
Output = 1 (index)
```

- **Example 3:**
``` bash
Input: arr = [0,10,5,2]
Output = 1 (index)
```

- **Example 4:**
``` bash
Input: arr = [3,4,5,1]
Output = 2 (index)
```

- **Example 5:**
``` bash
Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output = 2 (index)
```

---
# Code

``` python
arr = [24, 69, 100, 99, 79, 78, 67, 38, 26, 19]


def peak_index(arr, lo, hi):
    # NOTE:
    ## arr[mid - 1] when mid = 0 → index -1 → wraps around in Python
    ## arr[mid + 1] when mid = hi → index out of bounds
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] < arr[mid - 1] and arr[mid] > arr[mid + 1]:
            hi = mid - 1
        elif arr[mid] > arr[mid - 1] and arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            return mid

    return -1
    """

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] < arr[mid + 1]:
            lo = mid + 1
        else:
            hi = mid

    return lo


lo = 0
hi = len(arr) - 1

result = peak_index(arr, lo, hi)

print("Peak index is", result)
```

---
**Time complexity**: $O(log n)$
**Space Complexity**: $O(1)$

---
