# Substitution method: Example 2
**Given a Recurrence Relation**
$$
\begin{aligned}
T(n) &= 1, \quad \text{for } n = 1 \\
T(n) &= T(n-1) + \frac{1}{n} \quad \text{for } n > 1.
\end{aligned}
$$
- Equation 1
$T(n) = T(n - 1) + \frac{1}{n}$.
> **Here $T(n-1)$ is the recursive term**.

- Equation 2
**Hence $T(n-1) = T(n-2) + \frac{1}{n-1}$ .

- Substituting 2 in 1
**Hence** $T(n) = T(n - 2) + \frac{1}{n-1} + \frac{1}{n}$
$\implies \quad T(n) = T(n - 3) + \frac{1}{n-2} + \frac{1}{n-1} + \frac{1}{n}$

- T(n) in terms of k terms is
**Hence** $T(n) = T(n-k) + \frac{1}{n - k + 1} +  \frac{1}{n - k + 2} + ..... + \frac{1}{n-2} + \frac{1}{n-1} + \frac{1}{n}$

- **Note that** $n - k = 1$ (Repeating the same task for `k` number of times until base case condition arrives)
$\implies \quad n - 1 = k$

- **Hence**
**Hence** $T(n) = T(n-(n-1)) + \frac{1}{n - (n-1) + 1} +  \frac{1}{n - (n-2) + 2} + ..... + \frac{1}{n-2} + \frac{1}{n-1} + \frac{1}{n}$

$\implies \quad T(n) = T(1) + \frac{1}{2} + \frac{1}{3} + .... + \frac{1}{n-2} + \frac{1}{n-1} + \frac{1}{n}$

- Substituting **base case condition: $T(1) = 1$
$\implies \quad T(n) = 1 + \frac{1}{2} + \frac{1}{3} + .... + \frac{1}{n-2} + \frac{1}{n-1} + \frac{1}{n}$

- This is a **Logarithmic Series**

> Time complexity of the problem is:
   $O(logn)$

---
