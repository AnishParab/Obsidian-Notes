# Example 1

- **Given: $f(n) = n$ and $g(n) = 5n$, Check whether $f(n) = \Omega(g(n))$**
###### **Solution**
- $f(n) = \Omega(g(n))$
	- $f(n) >= c.g(n)$
	- $n >= c.5n$
- When $c > 0$, $n_o = n$ and $n_o >= 1$
	- $1 >= 5c$
	- $c >= \frac{1}{5}$
	- **Hence $c$ is a constant and `c > 0`**
- **Hence** $f(n) = \Omega(g(n))$

---
# Example 2

- **Given: $f(n) = n^2$ and $g(n) = n^2 + n + 10$, Check whether $f(n) = \Omega(g(n))$**
###### **Solution**
- $f(n) = \Omega(g(n))$
	- $f(n) >= c.g(n)$
    - $n² ≥ c·(n² + n + 10)$
- Trying $c = 1/2$: **(Something close to $0$)
    - $n² ≥ (1/2)·(n² + n + 10)$
    - $2n² ≥ n² + n + 10$
    - $n² - n - 10 ≥ 0$
    - **This holds for $n ≥ 4$ → take $n₀ = 4$**
	- $c = 1/2 > 0 ✓ \quad and \quad n₀ = 4 ≥ 1 ✓$
- **Hence $f(n) = Ω(g(n))$ with $c = 1/2$, $n₀ = 4$**

###### **Note**
- **When it fails — trying $c = 1$:**
	- $n² ≥ 1·(n² + n + 10)$
	- $0 ≥ n + 10$
	- **False for all $n ≥ 1 ✗$**
- **$c = 1$ fails — but that doesn't matter. Omega only requires *one valid $c$* to exist, not all $c$ to work.**

---
# Example 3

- **Given: $f(n) = n$ and $g(n) = n^2$, Check whether $f(n) = \Omega(g(n))$

###### **Solution**
- $f(n) = \Omega(g(n))$
	- $f(n) >= c.g(n)$
	- $n >= c.n^2$
- When $c > 0$, $n_o = n$ and $n_o >= 1$
	- $1 >= c.n$
	- $c <= \frac{1}{n}$
	- **Hence $c$ is a *not* a constant**
- **Hence** $f(n) \neq \Omega(g(n))$

---
# Example 4

- **Given: $f(n) = n^2 + n + 10$ and $g(n) = n^2$, Check whether $f(n) = \Omega(g(n))$**
###### **Solution**
- $f(n) = \Omega(g(n))$
	- $f(n) >= c.g(n)$
	- $n^2 + n + 10 >= c . n^2$
- Trying $c = 1/2$: **(Something close to $0$)
    - $(n² + n + 10) ≥ (1/2)·n²$
    - $2n² + n + 10 ≥ n²$
    - $n² + n + 10 ≥ 0$
    - **This holds for all $n ≥ 0$**
- **Hence $f(n) = Ω(g(n))$ with $c = 1/2$$**

---
