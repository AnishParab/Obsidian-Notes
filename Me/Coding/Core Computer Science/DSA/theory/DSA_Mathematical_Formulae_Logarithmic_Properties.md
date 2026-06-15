# DSA_Logarithm_Properties

## Core Properties
- log(ab) = log a + log b
- log(a/b) = log a - log b
- log(aᵇ) = b·log a
- log(1) = 0
- log(b) = 1  (where b is the base)

## Change of Base
- log_a(b) = log_c(b) / log_c(a)
- In DSA: log base doesn't matter asymptotically — O(log₂n) = O(log₁₀n)

## Useful Identities
- a^(log_a(b)) = b
- log_a(aⁿ) = n
- log(√n) = (1/2)·log n
- log(2ⁿ) = n·log 2

## Inequalities (useful in analysis)
- log n < n  for all n > 1
- log n < √n < n < n log n < n² < 2ⁿ  (growth order)

## In DSA context
- Binary search → O(log₂n)
- Tree height → O(log n)
- Each time you halve input: +1 to log count


---
