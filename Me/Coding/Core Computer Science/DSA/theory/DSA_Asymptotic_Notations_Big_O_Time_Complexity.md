# Big O - Time Complexity

- Asymptotic notation for **worst case** (upper bound)
- $f(n) = O(g(n))$ means $f$ grows no faster than $g$ (up to constant factors)
- Most used in practice — optimise against the worst case

## Formal Definition
$$
f(n) = O(g(n))\quad iff\quad ∃\quad c > 0,\quad n₀ ≥ 1 
$$
- such that:
$$
0 ≤ f(n) ≤ c·g(n)\quad  for\ all\quad n ≥ n₀
  $$

## In plain terms
- Past a threshold n₀, g(n) always dominates f(n) (with some constant c)
- Constants and lower-order terms don't matter — only the growth rate does

---
# Graphical Representation

![[bigOOOO.excalidraw]]

---
