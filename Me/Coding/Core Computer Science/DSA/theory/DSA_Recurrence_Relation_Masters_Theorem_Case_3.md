# Pre-requisites

**Your recurrence relation should look like this**
$$
T(n) = a \; T(\frac{n}{b}) + f(n)
$$
where, `a` and `b` are positive constants $a \ge 1 \; ; \; b > 1$ and $f(n)$ is a positive function.

**f(n) can be represented as:**
$$
f(n) = \Theta (n^k \log^p(n))
$$

---
# Case 2

**If** $log_b a < k$
- **for** $p >= 0 \quad \implies \quad \Theta(n^k log ^ {p} n)$
- **for** $p < 0 \quad \implies \quad \Theta(n^k)$

---
# Example 1

**Given**
$$
T(n) = 2 . T(\frac{n}{2}) + n ^ 2
$$
###### **Solution**
- Here $a = 2$, $b = 2$ and $f(n) = \frac{n}{logn}$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $n ^ 2 = \Theta (n^k \log^p(n))$
	- $\implies k=2, p=0$
- Hence:
	- $log_b a = log_2 2 = 1$
	- $\implies log_b a < k$
- Hence:
	- $p >= 0$
- Hence:
	- $\implies O(n^k . log ^ {p} n)$
	- $\implies O(n^2 log ^ {0} n)$
- **Hence $O (n^2)$**

---
# Example 2

**Given**
$$
T(n) = 2 . T(\frac{n}{2}) + n ^ 2 . logn
$$
###### **Solution**
- Here $a = 2$, $b = 2$ and $f(n) = n^2 . logn$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $n ^ 2 . logn = \Theta (n^k \log^p(n))$
	- $\implies k=2, p=1$
- Hence:
	- $log_b a = log_2 2 = 1$
	- $\implies log_b a < k$
- Hence:
	- $p >= 0$
- Hence:
	- $\implies O(n^k . log ^ {p} n)$
	- $\implies O(n^2 log ^ {1} n)$
- **Hence $O (n^2. logn)$**

---
# Example 3

**Given**
$$
T(n) = 4 . T(\frac{n}{2}) + \frac {n^3}{logn}
$$
###### **Solution**
- Here $a = 4$, $b = 2$ and $f(n) = n^3 . logn$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $\frac{n^3} {logn} = \Theta (n^k \log^p(n))$
	- $\implies k=3, p=-1$
- Hence:
	- $log_b a = log_2 2 = 1$
	- $\implies log_b a < k$
- Hence:
	- $p < 0$
- Hence:
	- $\implies O(n^k)$
	- $\implies O(n^3)$
- **Hence $O (n^3)$**

---
