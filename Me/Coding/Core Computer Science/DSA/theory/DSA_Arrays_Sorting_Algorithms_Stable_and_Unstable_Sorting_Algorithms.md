# Sorting Stability

- A sort is **stable** if elements with equal keys maintain their original relative order

## Example
- Input:  $(4,2) (5,7) (4,3) (6,8) (7,10)$  — sorted by key
- Stable:   $(4,2) (4,3) (5,7) (6,8) (7,10)$  ✓ original order preserved
- Unstable: $(4,3) (4,2) (5,7) (6,8) (7,10)$  ✗ order swapped

---
# Stable algorithms

- Bubble, Insertion, Merge, Count, Radix, Bucket Sort

---
# Unstable algorithms

- Quick, Selection, Heap Sort

---
#### When it matters

- Sorting objects with multiple fields (e.g. sort by name, then by age)
- Hashing/dictionary structures where key collisions must preserve insertion order

---
