# Substitution method: Example 3
**Given a Recurrence Relation**
$$
\begin{aligned}
T(n) &= 1, \quad \text{for } n = 1 \\
T(n) &= T(\frac{n}{2}) + n \quad \text{for } n > 1.
\end{aligned}
$$
- Equation 1
$T(n) = T(\frac{n}{2}) + n$.
> **Here $T(\frac{n}{2})$ is the recursive term**.

- Equation 2
**Hence $T(\frac{n}{2}) = T(\frac{n}{4}) + \frac{n}{2}$ .

- Substituting 2 in 1
**Hence** $T(n) = T(\frac{n}{4}) + \frac{n}{2} + n$
$\implies \quad T(n) = T(\frac{n}{8}) + \frac{n}{4} + \frac{n}{2} + n$
$\implies \quad T(n) = T(\frac{n}{2^3}) + \frac{n}{2^2} + \frac{n}{2} + n$

- T(n) in terms of k terms is
**Hence** $\implies \quad T(n) = T(\frac{n}{2^k}) + \frac{n}{2^{k-1}} + \frac{n}{2^{k-2}} + .... + \frac{n}{2^2} + \frac{n}{2} + n$


- **Note that** $2^k = n$ (Repeating the same task for `k` number of times until base case condition arrives)
$\implies \quad k = log_2 n$

- **Hence**
**Hence** $\implies \quad T(n) = T(\frac{n}{2^{log_2n}}) + \frac{n}{2^{log_2n-1}} + \frac{n}{2^{log_n-2}} + .... + \frac{n}{2^2} + \frac{n}{2} + n$

$\implies \quad T(n) = T(1) + n[(\frac{1}{2})^0 + (\frac{1}{2})^1 + (\frac{1}{2})^2 + .... + (\frac{1}{2})^{log_2{n-2}} + (\frac{1}{2})^{log_2{n-1}}]$

- Substituting **base case condition: $T(1) = 1$
$\implies \quad T(n) = 1 + n[(\frac{1}{2})^0 + (\frac{1}{2})^1 + (\frac{1}{2})^2 + .... + (\frac{1}{2})^{log_2{n-2}} + (\frac{1}{2})^{log_2{n-1}}]$

- This is a **GP Series** where $r = \frac{1}{2}$ and $a = 1$
$\implies \quad T(n) = 1 + n [\frac{{1 - \frac{1}{2}^{log_2n}}}{1 - \frac{1}{2}}]$
$\implies \quad T(n) = 1 + (1) n$

- Hence 
> Time complexity of the problem is:
   $O(n)$

---
