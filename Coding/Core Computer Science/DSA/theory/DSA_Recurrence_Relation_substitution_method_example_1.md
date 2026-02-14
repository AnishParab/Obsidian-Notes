# Substitution method: Example 1
**Given a Recurrence Relation**
$$
\begin{aligned}
T(n) &= 1, \quad \text{for } n = 1 \\
T(n) &= T(n-1) + n \quad \text{for } n > 1.
\end{aligned}
$$
- Equation 1
$T(n) = T(n - 1) + n$.
> **Here $T(n-1)$ is the recursive term**.

- Equation 2
**Hence $T(n-1) = T(n-2) + n - 1$ .

- Substituting 2 in 1
**Hence** $T(n) = T(n - 2) + (n - 1) + n$
$\implies \quad T(n) = T(n - 3) + (n - 2) + (n - 1) + n$

- T(n) in terms of k terms is
**Hence** $T(n) = T(n-k) + (n - k + 1) + (n - k + 2) + ..... + (n - 2) + (n - 1) + n$

- **Note that** $n - k = 1$
$\implies \quad n - 1 = k$

- **Hence**
$T(n) = T(n - (n - 1)) + (n - (n - 1) + 1) + (n - (n - 1) + 2) + .... + (n - 2) + (n - 1) + n$

$\implies \quad T(n) = T(1) + 2 + 3 + .... + (n - 2) + (n - 1) + n$

- Substituting **base case condition: $T(1) = 1$
$\implies \quad T(n) = 1 + 2 + 3 + .... + (n - 2) + (n - 1) + n$

- This is sum of `n` natural numbers
$T(n) = (n^2 + n) / 2$

> Time complexity of the problem is:
   $O(n^2)$

---
