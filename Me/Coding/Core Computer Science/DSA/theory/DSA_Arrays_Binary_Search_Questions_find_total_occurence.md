# Problem Statement

- array -> $[1, 2, 3, 3, 3, 3, 5]$
- Find total number of occurence of 3.

---
# Code

``` python
arr = [1, 2, 3, 3, 3, 3, 5]
arr.sort()


def total_occurence(arr, lo, hi, key):
    start, end = -1, -1

    # First occurence
    i, j = lo, hi
    while i <= j:
        mid = i + (j - i) // 2

        if arr[mid] == key:
            start = mid
            j = mid - 1
        elif arr[mid] < key:
            i = mid + 1
        else:
            j = mid - 1

    # Last occurence
    i, j = lo, hi
    while i <= j:
        mid = i + (j - i) // 2

        if arr[mid] == key:
            end = mid
            i = mid + 1
        elif arr[mid] < key:
            i = mid + 1
        else:
            j = mid - 1

    # Total occurences
    result = end - start + 1
    return result


lo = 0
hi = len(arr) - 1
key = 3
result = total_occurence(arr, lo, hi, key)

print(f"Total occurences of {key} in the array is {result}")
```

---
**Time complexity**: $O(log n)$
**Space Complexity**: $O(1)$

---
