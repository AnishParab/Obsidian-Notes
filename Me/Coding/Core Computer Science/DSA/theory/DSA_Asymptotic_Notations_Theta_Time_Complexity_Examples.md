# Example 1

- **Given: $f(n) = n$ and $g(n) = 5n$, Check whether $f(n) = \Theta(g(n))$**
###### **Solution**
- $f(n) = \Theta(g(n))$
	- **Case 1**
		- $f(n) >= c.g(n)$
		- $n >= c.5n$
		- When $c > 0$, $n_o = n$ and $n_o >= 1$
			- $1 >= 5c$
			- $c >= \frac{1}{5}$
			- **Hence $c$ is a constant**
			- **Hence** $f(n) = \Omega(g(n))$
	- **Case 2**
		- $f(n) <= c.g(n)$
		- $n <= c.5n$
		- When $c > 0$, $n_o = n$ and $n_o >= 1$
			- $1 <= 5c$
			- $c <= \frac{1}{5}$
			- **Hence $c$ is a constant**
			- **Hence** $f(n) = O(g(n))$
- **Hence $f(n) = \Theta(g(n))$ is also satisfied.**

---
