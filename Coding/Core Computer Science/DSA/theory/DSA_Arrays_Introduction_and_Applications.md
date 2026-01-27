# Arrays
- An **array** is a collection of **homogeneous elements** stored in **contiguous memory locations**.
- Elements are accessed using an **index**.
- Indexing convention (most languages): **0-based**.

---
# Address Formula
``` text
address(arr[i]) = base_address + i × element_size
```
- Enables constant-time access.
- Requires a single contiguous block → impacts resizing.

---
![[array_ds.excalidraw|500]]

---
# Allows Random Access
- Random access is possible without using any loops.
- `arr[0]` -> For accessing first position in an array.
- `arr[n-1]` -> For accessing last position in an array.
- Here `n` is the size of the array.

---
# Applications of Array
- Array is used in **Searching-based algorithms** due to its _random access property_.

---
