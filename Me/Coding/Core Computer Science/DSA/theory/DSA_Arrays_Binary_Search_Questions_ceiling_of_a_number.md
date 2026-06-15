# Problem Statement

- Given array = [2, 3, 5, 9, 14, 16, 18]
- Target number = 15
- Ceiling = **Smallest number in the array, greater than or eqaul to the target number** = 16

- **Example**:
	- Target = 14
	- Ceiling = 14

- **Example**:
	- Target = 4
	- Ceiling = 5

---
# Code

``` python
arr = [2, 3, 5, 9, 14, 16, 18]


def ceiling_number(arr, lo, hi, target):
    result = -1

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] < target:
            lo = mid + 1
        else:
            result = arr[mid]
            hi = mid - 1

    return result


lo = 0
hi = len(arr) - 1
target = 15

result = ceiling_number(arr, lo, hi, target)

print(f"The ceiling of {target} is {result}")
```

`return arr[lo] if lo < len(arr) else -1` -> *If not using `result` variable*

---
**Time complexity**: $O (log n)$
**Space complexity**: O(1)

---
