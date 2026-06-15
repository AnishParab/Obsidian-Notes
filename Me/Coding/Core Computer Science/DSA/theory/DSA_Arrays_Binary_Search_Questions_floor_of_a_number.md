# Problem Statement

- Given array = [2, 3, 5, 9, 14, 16, 18]
- Target number = 15
- Floor = **Biggest number in the array, smaller than or eqaul to the target number** = 14

- **Example**:
	- Target = 14
	- Ceiling = 14

- **Example**:
	- Target = 4
	- Ceiling = 3

---
# Code

``` python
arr = [2, 3, 5, 9, 14, 16, 18]


def floor_number(arr, lo, hi, target):
    result = -1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] <= target:
            result = arr[mid]
            lo = mid + 1
        else:
            hi = mid - 1

    return result


lo = 0
hi = len(arr) - 1
target = 15

result = floor_number(arr, lo, hi, target)

print(f"Floor of {target} is {result}")
```

`return arr[hi] if hi >= 0 else -1` -> *if not using `result` variable*

---
**Time complexity**: $O(log n)$
**Space complexity**: O(1)

---
