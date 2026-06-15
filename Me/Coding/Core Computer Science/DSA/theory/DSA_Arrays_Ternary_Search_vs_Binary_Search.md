# Difference

| Property             | Binary Search     | Ternary Search              |
| -------------------- | ----------------- | --------------------------- |
| Splits into          | 2 parts (1 mid)   | 3 parts (2 mids)            |
| Array type           | Physically sorted | Unimodal (logically sorted) |
| Finds                | Specific element  | Peak / valley               |
| Iterations           | O(log₂ n)         | O(log₃ n)                   |
| Comparisons/iter     | 1                 | 2                           |
| Effective complexity | O(log₂ n)         | O(2 · log₃ n) = O(log₂ n)   |
| Faster?              | ✓ Slightly        | ✗ Equal or worse            |

---
#### Proof
- By change of base:
	- `log₃ n = log₂ n / log₂ 3`
- So:
	- `2 · log₃ n = 2 · log₂ n / log₂ 3 = 2/1.585 · log₂ n ≈ 1.26 · log₂ n`

> So `2 · log₃ n ≈ 1.26 · log₂ n` — not exactly equal, just the same asymptotic class O(log n). I was imprecise. Ternary is strictly slightly worse.

---
