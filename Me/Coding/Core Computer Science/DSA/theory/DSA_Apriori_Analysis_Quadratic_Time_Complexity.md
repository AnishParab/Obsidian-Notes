# Example 1

```cpp
x = y + z;

for(i = 0; i < n; i++) {
    x = y + z;
}

for(i = 0; i < n; i++) {
    for(j = 0; j < n; j++) {
        x = y + z;
    }
}
```

- `x = y + z` -> **1 time**
- `for(i=0; i<n' i++)` -> `0 to (n-1) times` -> **n times**
- `for(i=0; i<n' i++)` and `for(j=0; j<n; j++)`
	- **$n^2$ times
- Hence **$1 + n + n^2$ times**
	- $T(n) = O(1 + n + n^2)$
	- **Hence $T(n) = O(n^2)$.

---
