# Arithmetic Series
- $1 + 2 + 3 + ... + n = n(n+1)/2$  →  **O(n²)**

---
# Sum of Squares
- $1² + 2² + 3² + ... + n² = n(n+1)(2n+1)/6$  →  **O(n³)**

---
# Sum of Cubes
- $1³ + 2³ + 3³ + ... + n³ = [n(n+1)/2]²$  →  **O(n⁴)**

---
# Geometric Series
- General: $a + ar + ar² + ... + arⁿ = a(rⁿ⁺¹ - 1) / (r - 1)$  for $r ≠ 1$
- If $r = 1: sum = a(n+1)$
- If $|r| < 1 (infinite): sum = a / (1 - r)$
- If $r > 1: sum$ → **O(rⁿ)**  — exponential growth
- If $r < 1: sum$ → **O(1)**   — converges to constant
- Special case $(a=1, r=2)$: $1 + 2 + 4 + ... + 2ⁿ = 2ⁿ⁺¹ - 1$  →  **O(2ⁿ)**

---
# Harmonic Series
- $1 + 1/2 + 1/3 + ... + 1/n = ln(n) + γ$  →  **O(log n)**
- $γ ≈ 0.577$ (Euler-Mascheroni constant)

---
# Logarithmic Series
- $log 1 + log 2 + ... + log n = log(n!)  ≈  n·log(n)$  →  **O(n log n)**

---
# Telescoping Series
- $Σ (aₖ - aₖ₊₁) = a₁ - aₙ₊₁$  — most terms cancel
- Useful for recurrence analysis

---
# Power of 2 (common in recursion)
- $2⁰ + 2¹ + 2² + ... + 2ⁿ = 2ⁿ⁺¹ - 1$  →  **O(2ⁿ)**

---
# Recurrence-related
- $Σ n/2ⁱ (i=0 to log n)$ → **O(n)**  — appears in merge sort analysis

---
