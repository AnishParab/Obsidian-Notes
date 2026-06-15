# Code

``` python
arr = [9, 5, 1, 4, 3]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


print("Sorted array is", insertion_sort(arr))
```

---
###### **Time complexity**
> **Best Case Scenario** = $O(n)$ -> *Ascending Order*
> **Worst Case Scenario** = $O(n^2)$ -> *Descending Order*

###### **Space Complexity**
> $O(1)$

---
