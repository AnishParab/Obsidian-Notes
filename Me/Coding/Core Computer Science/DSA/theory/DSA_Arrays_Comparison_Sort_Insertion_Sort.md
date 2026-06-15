# Insertion Sort

- A type of comparison based sorting algorithm.

![[insertion_sort.excalidraw|700]]
###### **Time complexity**
> **Best Case Scenario** = $O(n)$ -> *Ascending Order*
> **Worst Case Scenario** = $O(n^2)$ -> *Descending Order*

---
# Points to Note

###### `n = 6` => **6 passes**
- **Hence for `n` => `n passes`**

###### **Best Case Scenario**
- **Take the best case scenario (ascending order) to get the answer**
- `(n-1)` **comparisons**
- $0$ **swaps**
- **Hence Time Complexity for comparisons** = $O(n)$

###### **Worst Case Scenario**
- **Take the worst case scenario (descending order) to get the answer**
- $n$ **elements** $\implies$ $(1 + 2 + ... + (n-1))$ **comparisons** $\implies$ $(1 + 2 + ... + (n-1))$ **swaps** -> $O(n^2)$
- **Hence Time Complexity** = $O(n^2)$

###### **Time complexity**
> **Best Case Scenario** = $O(n)$ -> *Ascending Order*
> **Worst Case Scenario** = $O(n^2)$ -> *Descending Order*

###### **Space Complexity**
> $O(1)$

---
# **IMPORTANT NOTE**

> Hence for *Almost Ascending Ordered Arrays*, **Insertion Sort** is the best solution caompared to Bubble and Selection Sort as *Time Complexity is $O(n)$*.

---
