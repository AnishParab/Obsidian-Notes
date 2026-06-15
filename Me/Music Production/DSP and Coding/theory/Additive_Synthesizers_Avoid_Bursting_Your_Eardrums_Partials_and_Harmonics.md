# The amplitude rule

- If you have `N` partials each at amplitude `A`, the peak output is `N × A`. To keep the sum within `[-1, 1]`:
```
Aₙ = 1/N  for equal amplitude partials
```

- But in real instruments, higher partials are quieter. A common model is:
```
Aₙ = 1/n   (amplitude falls off with partial number)
```

> Partial 1 → amplitude 1.0, Partial 2 → 0.5, Partial 3 → 0.33 ... This naturally keeps the sum bounded and sounds more organic.

---
