# Pre-requisites

- Ternary search requires array to be **unimodal** (*logically sorted*)
- Does not need to be physically sorted (ascending/descending) like in Binary Search
- Unimodal: strictly increases then strictly decreases (or vice versa) — single peak or valley

###### Valid cases
- Increases then decreases: [1, 4, 8, 12, 7, 3]  → peak at 12
- Decreases then increases: [9, 6, 3, 1, 4, 8]   → valley at 1
- Strictly increasing:      [1, 2, 3, 4, 5]       → peak at last element
- Strictly decreasing:      [5, 4, 3, 2, 1]       → peak at first element

###### Invalid cases
- [1, 3, 2, 4, 1] → two peaks, not unimodal
- [1, 2, 2, 3, 4] → duplicate elements, not strictly unimodal

###### Key distinction
- Binary search → physically sorted (ascending/descending)
- Ternary search → logically sorted (unimodal)

---
# Theory

- Split your search space into **three halves**

**Hence**
$$
mid1 = l + \frac{(r - l)}{3}
$$
$$
mid2 = r - \frac{(r-l)}{3}
$$

![[ternary_search.excalidraw|500]]

---
