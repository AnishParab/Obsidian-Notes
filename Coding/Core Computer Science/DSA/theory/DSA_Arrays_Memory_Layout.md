
# Address Formula

``` text
address(arr[i]) = base_address + (i - lower_bound_of_index) × element_size
```

- Enables constant-time access.
- Requires a single contiguous block → impacts resizing.

---
# Memory Layout

![[array_ds.excalidraw|500]]

---
# Allows Random Access

- Random access is possible without using any loops.
- `arr[0]` -> For accessing first position in an array.
- `arr[n-1]` -> For accessing last position in an array.
- Here `n` is the size of the array.

---
