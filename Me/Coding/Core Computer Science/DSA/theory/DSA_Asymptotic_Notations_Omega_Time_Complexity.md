# Omega - Time Complexity

- Asymptotic notation for **best case** (lower bound)
- $f(n) = Ω(g(n))$ means $f$ grows no slower than $g$ (up to constant factors)

## Formal Definition
$$
f(n) = Ω(g(n))\quad iff\quad ∃\quad c > 0,\quad n₀ ≥ 1
$$
- such that:
$$
  0 ≤ c·g(n) ≤ f(n)\quad  for\ all\quad n ≥ n₀
$$

## In plain terms
- Past threshold $n₀$, $f(n)$ always stays above $c·g(n)$
- $g(n)$ is a floor — $f(n)$ never drops below it

---
## **Key equivalence**
> $$f(n) = Ω(g(n))  ⟺  g(n) = O(f(n))$$

---
# Graphical Representation

![[omega_time_complexity.excalidraw]]

---
