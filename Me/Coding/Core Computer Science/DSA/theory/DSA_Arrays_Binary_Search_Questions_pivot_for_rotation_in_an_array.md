# Problem Statement

- Given a rotated sorted array (no duplicates), find the **index of the pivot element** (smallest element) where the rotation begins.
- The array was originally sorted in ascending order and rotated at some unknown pivot point.
- **Upon rotation on a certain pivot index, the array is ordered in ascending order**

- **Example 1:**
```
Input:  [3, 4, 5, 1, 2]
Output: 3
Explanation: smallest element is 1, at index 3
```

- **Example 2:**
```
Input:  [50, 60, 70, 80, 90, 100, 10, 20, 30, 40]
Output: 6
Explanation: smallest element is 10, at index 6
```

- **Example 3:**
```
Input:  [1, 2, 3, 4, 5]
Output: 0
Explanation: array not rotated, smallest element is at index 0
```

- **Example 4:**
```
Input:  [2, 1]
Output: 1
Explanation: smallest element is 1, at index 1
```

- **Constraints:**
- All elements are unique
- `arr.length >= 1`
- Array was sorted in ascending order before rotation

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
**Time Complexity**: $O(log n)$
**Space Complexity**: $O(1)$

---
