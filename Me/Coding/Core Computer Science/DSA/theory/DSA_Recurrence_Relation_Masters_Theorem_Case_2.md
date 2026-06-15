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

**If** $log_b a = k$
- **for** $p > -1 \quad \implies \quad \Theta(n^k log ^ {p+1} n)$
- **for** $p = -1 \quad \implies \quad \Theta(n^k log log n)$
- **for** $p < -1 \quad \implies \quad \Theta(n^k)$

---
# Example 1

**Given**
$$
T(n) = 2 . T(\frac{n}{2}) + n
$$
###### **Solution**
- Here $a = 2$, $b = 2$ and $f(n) = n$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $n = \Theta (n^k \log^p(n))$
	- $\implies k=1, p=0$
- Hence:
	- $log_b a = log_2 2 = 1$
	- $\implies log_b a = k$
- Hence:
	- $p > -1$
- Hence:
	- $\implies O(n^k log ^ {p+1} n)$
	- $\implies O(n^1 log ^ {0+1} n)$
- **Hence $O (n . log n)$**

---
# Example 2

**Given**
$$
T(n) = 8 . T(\frac{n}{2}) + n^3
$$
###### **Solution**
- Here $a = 8$, $b = 2$ and $f(n) = n^3$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $n^3 = \Theta (n^k \log^p(n))$
	- $\implies k=3, p=0$
- Hence:
	- $log_b a = log_2 8 = 3$
	- $\implies log_b a = k$
- Hence:
	- $p > -1$
- Hence:
	- $\implies O(n^k log ^ {p+1} n)$
	- $\implies O(n^3 log ^ {0+1} n)$
- **Hence $O (n^3 . log n)$**

---
# Example 3

**Given**
$$
T(n) = 2 . T(\frac{n}{2}) + \frac{n}{logn}
$$
###### **Solution**
- Here $a = 2$, $b = 2$ and $f(n) = \frac{n}{logn}$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $\frac{n}{logn} = \Theta (n^k \log^p(n))$
	- $\implies k=1, p=-1$
- Hence:
	- $log_b a = log_2 2 = 1$
	- $\implies log_b a = k$
- Hence:
	- $p = -1$
- Hence:
	- $\implies O(n^k . log log n)$
	- $\implies O(n^1 log log n)$
- **Hence $O (n log log n)$**

---
# Example 4

**Given**
$$
T(n) = 2 . T(\frac{n}{2}) + \frac{n}{log ^ {2} n}
$$
###### **Solution**
- Here $a = 2$, $b = 2$ and $f(n) = \frac{n}{log ^ {2} n}$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $\frac{n}{log ^ {2} n} = \Theta (n^k \log^p(n))$
	- $\implies k=1, p=-2$
- Hence:
	- $log_b a = log_2 2 = 1$
	- $\implies log_b a = k$
- Hence:
	- $p < -1$
- Hence:
	- $\implies O(n^k)$
	- $\implies O(n^1)$
- **Hence $O(n)$**

---
