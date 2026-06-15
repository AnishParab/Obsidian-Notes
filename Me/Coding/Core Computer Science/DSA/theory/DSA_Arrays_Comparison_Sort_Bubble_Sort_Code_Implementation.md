# Code

``` python
arr = [70, 20, 50, 30, 90, 5, 15]


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print("Sorted array:", bubble_sort(arr))
```

---
**Time complexity**
> = *Swap* + *Comparisons* = $O(n^2)$ + $O(n^2)$ = $O(n^2)$

**Space Complexity**
> $O(1)$

---
