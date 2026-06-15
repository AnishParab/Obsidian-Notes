# Pseudocode

- Pseudocode is a high-level, language-agnostic description of an algorithm
- Not actual code — no syntax rules, not executable
- Purpose: communicate logic clearly before implementation

#### Why use it
- Focus on logic, not language syntax
- Universally readable across languages
- Standard in algorithm analysis and textbooks

#### Common Conventions
- Assignment: x ← value
- Comparison: =, ≠, <, >, ≤, ≥
- Conditionals: if / else if / else / end if
- Loops: for, while, repeat...until
- Functions: procedure / function / return
- Comments: // this is a comment
- Array indexing: A[i] or A[1..n]

---
# Example (Binary Search)

``` text
procedure BinarySearch(A, target):
    lo ← 0
    hi ← len(A) - 1
    while lo ≤ hi:
        mid ← (lo + hi) / 2
        if A[mid] = target → return mid
        else if A[mid] < target → lo ← mid + 1
        else → hi ← mid - 1
    return -1
```

---
