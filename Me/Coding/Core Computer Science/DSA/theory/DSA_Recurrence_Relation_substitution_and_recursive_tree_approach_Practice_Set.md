# Problem 1

**Given**: $T(n) = T(\frac{n}{2}) + T(\frac{n}{2}) + n$
###### **Solution: Recursive Tree Approach - *Since `2` recursive terms are present**
![[problems_on_recurrence_relation.excalidraw|500]]

---
# Problem 2

**Given**
$$
\begin{aligned}
T(n) &= 1, \quad \text{for } n = 1 \\
T(n) &= 8T(\frac{n}{2}) + n^2 \quad \text{for } n > 1.
\end{aligned}
$$
###### **Solution: Substitution method *Since only `1` recursive term is present**
- Step 1: Substitute
	- $T(n) = 8T(n/2) + n²$
	- $T(n) = 8[8T(n/4) + (n/2)²] + n²$
	- $T(n) = 8²T(n/4) + 8·n²/4 + n²$
	- $T(n) = 8²T(n/4) + 2n² + n²$
- Step 2: Substitute again
	- $T(n) = 8²[8T(n/8) + (n/4)²] + 2n² + n²$
	- $T(n) = 8³T(n/8) + 8²·n²/16 + 2n² + n²$
	- $T(n) = 8³T(n/8) + 4n² + 2n² + n²$
- Step 3: Generalize for $k$ terms
	- $T(n) = 8ᵏT(n/2ᵏ) + n²(1 + 2 + 4 + ... + 2ᵏ⁻¹)$
	- $T(n) = 8ᵏT(n/2ᵏ) + n²·(2ᵏ - 1)$
- Step 4 — Base case: $n/2ᵏ = 1 → k = log₂n$
	- $T(n) = 8^(log₂n) · T(1) + n²·(2^(log₂n) - 1)$
	- $T(n) = 8^(log₂n) + n²·(n - 1)$
	- $T(n) = n^(log₂8) + n³ - n² ← using 2^(3log n) = n³$
	- $T(n) = n³ + n³ - n²$
	- $T(n) = 2n³ - n²$
- **Hence $T(n) = O(n³)$**

---
# Problem 3

**Given**:
$$
\begin{aligned}
T(n) &= 1, \quad \text{for } n = 1 \\
T(n) &= T(\frac{n}{2}) + c \quad \text{for } n > 1.
\end{aligned}
$$
###### **Solution**
- Step 1: Substitute
	- $T(n/2) = T(n/4) + c$
	- Hence $T(n) = T(n/2^2) + 2c$
- Step 2: Substitute again
	- $T(n/4) = T(n/8) + c$
	- Hence $T(n) = T(n/2^3) + 3c$
- For $k$ terms
	- $T(n) = T(n/2^k) + kc$
- Substituting $n/2^k = 1 \quad \implies \quad k = log_2 n$
	- $T(n) = T(1) + log_2 n . c$
	- $T(n) = 1 + log_2 n . c$
- **Hence $T(n) = O(log_2 n)$**

---
