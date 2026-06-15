[]()# Problem Statement

- Given a rotated sorted array (no duplicates), find the index of the pivot element (smallest element) where the rotation begins
- Array was originally sorted in ascending order before rotation
**Examples**
- Input: [3, 4, 5, 1, 2]   → Output: 3  (element 1, index 3)
- Input: [3, 8, 10, 17, 1] → Output: 4  (element 1, index 4)
- Input: [50, 60, 70, 10, 20, 30, 40] → Output: 3  (element 10, index 3)
- Input: [1, 2, 3, 4, 5]   → Output: 0  (not rotated, smallest at index 0)
- Input: [2, 1]             → Output: 1  (element 1, index 1)
**Constraints**
- All elements are unique
- arr.length >= 1
- Sorted in ascending order before rotation

---
# Code

``` python
arr = [3, 8, 10, 17, 1]


def pivot_rotated_index(arr, lo, hi):
    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] > arr[hi]:
            lo = mid + 1
        else:
            hi = mid

    return lo


lo = 0
hi = len(arr) - 1
result = pivot_rotated_index(arr, lo, hi)
print("Pivot index is", result)
```

---
- **Time complexity**: $O(log n)$
- **Space complexity**: $O(1)$

---
