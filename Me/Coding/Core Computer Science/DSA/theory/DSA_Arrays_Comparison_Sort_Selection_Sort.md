# Selection Sort

- A type of comparison based sorting algorithm.

![[selection_sort.excalidraw|700]]

> After every pass, the **smallest element in the unsorted part moves to the front**.
> Hence we swap only once in each pass.

> **Selection Sort** = *Swap* + *Comparisons* = $O(n)$ + $O(n^2)$ = $O(n^2)$

---
# Points to Note

###### `n = 6` => **6 passes**
- **Hence for `n` => `n passes`**

###### **Comparisons**
- `(n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1`
- $\frac {n (n - 1)} {2}$
- **Hence Time Complexity for comparisons** = $O(n^2)$

###### **Swaps**
- **At every pass, only one swap is required.**
- *Best Case* -> $0$ swaps
- *Worst Case* -> $(n - 1)$ **swaps** -> $O(n)$
- **Hence Time Complexity for swaps** = $O(n)$

###### **Time complexity**
> = *Swap* + *Comparisons* = $O(n^2)$ + $O(n^2)$ = $O(n^2)$

###### **Space Complexity**
> $O(1)$

---
