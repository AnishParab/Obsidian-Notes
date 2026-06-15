# Problem Statement

- First and last position of an element in a sorted array

- **Example 1**: Element = 3
``` text
0 5 5 6 6 6
```
- Output
``` bash
-1 -1
```

- **Example 2**: Element = 2
``` text
0 1 1 1 2 2 2 2
```
- Output
``` bash
4 7
```

- **Example 3**: Element = 2
``` text
2
```
- Output
``` bash
0 0
```

---
# Code

``` python
arr = [0, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
arr.sort()


def first_last_occ(arr, lo, hi, key):
    start, end = -1, -1

    ## First occurence
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

    ## Last occurence
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

    return start, end


lo = 0
hi = len(arr) - 1
key = 2
first, last = first_last_occ(arr, lo, hi, key)

print(f"First occurence is {first} and last occurence is {last} for element {key}")
```

---
**Time complexity**: $O(log n)$
**Space Complexity**: $O(1)$

---
