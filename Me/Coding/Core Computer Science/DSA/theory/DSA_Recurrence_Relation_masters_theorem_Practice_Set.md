# Example 1

**Given**
$$
T(n) = T(\sqrt{n}) + c
$$
###### **Solution**
- Converting into master's theorem form:
	- Let $n = 2 ^ k$
	- Hence:
		- $T(2^k) = T(2 ^ \frac{k}{2}) + c$
	- Let $S(k) = T(2^k)$
		- $S(\frac{k}{2}) = T(2 ^ \frac{k}{2})$
	- $S(k) = S(\frac{k}{2}) + c$
- Now, $a = 1$, $b = 2$ and $f(n) = c$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $c = \Theta (n^k \log^p(n))$
	- $\implies k=0, p=0$
- Hence:
	- $log_b a = log_2 1 = 0$
	- $\implies log_b a = k$
- Hence:
	- $p > -1$
- Hence:
	- $\implies O(n^k log ^ {p+1} n)$
	- $\implies O(n^0 log ^ {0+1} n)$
- **Hence $O (logn)$ for $S(k)$**
- **Now,**
	- $2^k = n$
	- $\implies k = logn$
- **Hence the final solution is $O(log log n)$**

---
# Example 2

**Given**
$$
T(n) = 2 . T(\frac{n}{2}) + n.logn
$$
###### **Solution**
- Here $a = 2$, $b = 2$ and $f(n) = n.logn$
- Hence:
	- $f(n) = \Theta (n^k \log^p(n))$
	- $n.logn = \Theta (n^k \log^p(n))$
	- $\implies k=1, p=1$
- Hence:
	- $log_b a = log_2 2 = 1$
	- $\implies log_b a = k$
- Hence:
	- $p > -1$
- Hence:
	- $\implies O(n^k log ^ {p+1} n)$
	- $\implies O(n^1 log ^ {1+1} n)$
- **Hence $O (n . log ^ {2} n)$**

---
# Example 3

**Given**
$$
T(n) = 2 . T(\frac{n}{2}) + n
$$
###### **Solution**
- Here $a = 2$, $b = 2$ and $f(n) = n.logn$
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
