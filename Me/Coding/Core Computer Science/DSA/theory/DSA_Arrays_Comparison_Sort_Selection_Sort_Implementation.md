# Code

``` python
arr = [50, 38, 75, 29, 11, 17, 20, 37]


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print("Sorted array is", selection_sort(arr))
```

---
**Time complexity**
> = *Swap* + *Comparisons* = $O(n)$ + $O(n^2)$ = $O(n^2)$

**Space Complexity**
> $O(1)$

---
