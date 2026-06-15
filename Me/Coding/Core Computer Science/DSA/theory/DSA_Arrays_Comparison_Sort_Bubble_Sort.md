# Bubble Sort

- A type of comparison based sorting algorithm.

![[bubble_sort.excalidraw|700]]

> After every pass, the **biggest element in the unsorted part moves to the end**.

> **Bubble Sort** = *Swap* + *Comparisons* = $O(n^2)$ + $O(n^2)$ = $O(n^2)$

---
# Points to Note

###### `n = 7` => **6 passes**
- **Hence for `n` => `(n-1) passes`**

###### **Comparisons**
- `(n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1`
- $\frac {n (n - 1)} {2}$
- **Hence Time Complexity for comparisons** = $O(n^2)$

###### **Swaps**
- *Best Case* -> $0$ swaps
- *Worst Case* -> $\frac {n (n - 1)} {2}$ -> $O(n^2)$
- **Hence Time Complexity for swaps** = $O(n^2)$

###### **Time complexity**
> = *Swap* + *Comparisons* = $O(n^2)$ + $O(n^2)$ = $O(n^2)$

###### **Space Complexity**
> $O(1)$

---
