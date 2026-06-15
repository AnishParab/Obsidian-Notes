# Example 1

- **Given: $f(n) = 5n$ and $g(n) = n$, Check whether $f(n) = O(g(n))$**
###### **Solution**
- $f(n) = O(g(n))$
	- $f(n) <= c.g(n)$
	- $5n <= c.n$
- When $c > 0$, $n_o = n$ and $n_o >= 1$
	- $5 <= c$
	- $c >= 5$
	- **Hence $c$ is a constant and statisfies `c > 0`**
- **Hence** $f(n) = O(g(n))$

---
# Example 2

- **Given: $f(n) = n$ and $g(n) = 5n$, Check whether $f(n) = O(g(n))$

###### **Solution**
- $f(n) = O(g(n))$
	- $f(n) <= c.g(n)$
	- $n <= c.5n$
- When $c > 0$, $n_o = n$ and $n_o >= 1$
	- $1 <= c.5$
	- $c >= \frac{1}{5}$
	- **Hence $c$ is a constant and satisfies `c > 0`**
- **Hence** $f(n) = O(g(n))$


---
# Example 3

- **Given: $f(n) = n^2$ and $g(n) = n$, Check whether $f(n) = O(g(n))$

###### **Solution**
- $f(n) = O(g(n))$
	- $f(n) <= c.g(n)$
	- $n^2 <= c.n$
- When $c > 0$, $n_o = n$ and $n_o >= 1$
	- $n <= c$
	- $c >= n$
	- **Hence $c$ is a *not* a constant**
- **Hence** $f(n) \neq O(g(n))$

---
