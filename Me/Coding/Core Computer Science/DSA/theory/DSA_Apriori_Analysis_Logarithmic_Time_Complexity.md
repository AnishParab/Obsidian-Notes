# Example 1

```python
i = n

while i > 2:
    i = i ** 0.5
```

- `i = n` -> **1 time**
- `n = 256` -> **3 times**
	- `256 > 2` -> $i = 256^\frac{1}{2}$ = $(2^8)^\frac{1}{2}$ = $2^4$ = 16
	-  `16 > 2` -> $i = (2^4)^\frac{1}{2}$ = $2^2$ = 4
	-  `4 > 2` -> $i = (2^2)^\frac{1}{2}$ = 2
- $n^\frac{1}{2^k} = 2$
	- Taking $log_2$ on both sides:
		- $\frac{1}{2^k} log_2 n$ = $log_2 2$
	- $\frac{1}{2^k} log_2 n$ = 1
	- $log_2 n$ = $2^k$
	- Taking $log_2$ on both sides:
		- $log_2 (log_2 n)$ = $k * log_2 2$
	- $log_2 (log_2) = k$
- **Hence $T(n) = O(log_2 (log_2 n))$

---
# Example 2

``` python
i = n

while i > 2:
	i = i ** 0.04
```

- $n^\frac{1}{25^k}$ = 2
	- Taking $log_2$ on both sides:
		- $\frac{1}{25^k} log_2 n$ = $log_2 2$
	- $\frac{1}{25^k} log_2 n$ = 1
	- $log_2 n$ = $25^k$
	- Taking $\log_{25}$ on both sides:
		- $\log_{25} (log_2 n)$ = $k * \log_{25} 25$
	- $\log_{25} (log_2 n) = k$
- **Hence** $T(n) = O(\log_{25} (\log_2 n))$

---
