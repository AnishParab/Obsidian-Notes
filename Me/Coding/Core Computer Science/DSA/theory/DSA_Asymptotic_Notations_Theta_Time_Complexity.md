# Theta - Time Complexity

- Asymptotic notation for **average case** (tight bound)
- f(n) = Θ(g(n)) means f grows at exactly the same rate as g asymptotically

## Formal Definition
$$
f(n) = Θ(g(n))\quad iff\quad ∃\ c₁ > 0,\quad c₂ > 0,\quad n₀ ≥ 1 
$$
such that:
$$
  c₂·g(n) ≤ f(n) ≤ c₁·g(n)\quad  for\ all\quad n ≥ n₀
$$

## In plain terms
- $f(n)$ is sandwiched between two constant multiples of $g(n)$
- Theta = Big-O AND Omega simultaneously

## Key equivalence
$f(n) = Θ(g(n))  ⟺  f(n) = O(g(n))\quad  AND\quad  f(n) = Ω(g(n))$

---
# Graphical Representation
![[omega.excalidraw]]

---
