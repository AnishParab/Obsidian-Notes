# Example 1

```python
x = y + z

for i in range(0, n):
    x = y + z
```

- `x = y + z` -> **1 time**
- `range(0, n)` -> `0 to (n-1) times` -> **n times**
- Hence **(n + 1) times**
	- $T(n) = O(n + 1)$
	- **Hence $T(n) = O(n)$.

---
# Example 2

```python
i = n

while (i > 1):
    i = i - 1
```

 - `i = n` -> **1 time**
 - `while loop`
	 - Let `i = 5` -> 4 times -> **(n-1) times**
		 - `i = 5-1 = 4`
		 - `i = 4-1 = 3`
		 - `i = 3-1 = 2`
		 - `i = 2-1 = 1`
- Hence **(1 + n - 1) times**
	- $T(n) = O(1 + n - 1)$
	- **Hence $T(n) = O(n)$.

---
# Example 3

```python
i = n
while i >= 1:
    i = i - 2
```

 - `i = n` -> **1 time**
 - `while loop`
	 - Let `i = 10` -> 5 times -> **$\frac{n}{2}$ times**
		 - `i = 10-2 = 8`
		 - `i = 8-2 = 6`
		 - `i = 6-2 = 4`
		 - `i = 4-2 = 2`
		 - `i = 2-2 = 0`
- Hence **(1 + $\frac{n}{2}$) times**
	- $T(n) = O(\frac{n}{2})$
	- **Hence $T(n) = O(n)$.

---
# Example 4

``` python
i = n
while i >= 1:
	i = i - 3
```

- $T(n) = O(\frac{n}{3})$
- **Hence $T(n) = O(n)$.

---
# Example 5

``` python
i = n
while i >= 1:
	i = i - 2
	i = i - 3
```

- $T(n) = O(\frac{n}{5})$
- **Hence $T(n) = O(n)$.

---
