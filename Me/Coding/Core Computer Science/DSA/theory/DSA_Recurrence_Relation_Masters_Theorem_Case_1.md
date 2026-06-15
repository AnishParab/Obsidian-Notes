# Pre-requisites

**Your recurrence relation should look like this**
$$
T(n) = a \; T(\frac{n}{b}) + f(n)
$$
- where, `a` and `b` are positive constants $a \ge 1 \; ; \; b > 1$ and $f(n)$ is a positive function.

**f(n) can be represented as:**
$$
f(n) = \Theta (n^k \log^p(n))
$$

---
# Case 1

**If** $log_b a > k$
$\implies \Theta\left(n^{\log_b(a)}\right)$

---
# Example 1

**Given**
$$
T(n) = 2 . T(\frac{n}{2}) + 1
$$
###### **Solution**
- Here $a = 2$, $b = 2$ and $f(n) = 1$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $1 = \Theta (n^k \log^p(n))$
	- $\implies k=0, p=0$
- Hence:
	- $log_b a = log_2 2 = 1$
	- $\implies log_b a > k$
- Hence:
	- $\implies O\left(n^{\log_b(a)}\right)$
	- $\implies O\left(n^{\log_2(2)}\right)$
- **Hence $O (n)$**

---
# Example 2

**Given**
$$
T(n) = 4 . T(\frac{n}{2}) + n
$$
###### **Solution**
- Here $a = 4$, $b = 2$ and $f(n) = n$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $n = \Theta (n^k \log^p(n))$
	- $\implies k=1, p=0$
- Hence:
	- $log_b a = log_2 4 = 2$
	- $\implies log_b a > k$
- Hence:
	- $\implies O\left(n^{\log_b(a)}\right)$
	- $\implies O\left(n^{\log_2(4)}\right)$
- **Hence $O (n^2)$**

---
# Example 3

**Given**
$$
T(n) = 8 . T(\frac{n}{2}) + n^2
$$
###### **Solution**
- Here $a = 8$, $b = 2$ and $f(n) = n^2$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $n^2 = \Theta (n^k \log^p(n))$
	- $\implies k=2, p=0$
- Hence:
	- $log_b a = log_2 8 = 3$
	- $\implies log_b a > k$
- Hence:
	- $\implies O\left(n^{\log_b(a)}\right)$
	- $\implies O\left(n^{\log_2(8)}\right)$
- **Hence $O (n^3)$**

---
