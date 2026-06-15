# Example 1

- **Given**: $1000. n\log n$
###### **Solution**
- Constants do not matter in asymptotic notation:
	- $1000 . n\log n \in O(n\log n)$
- **Hence** $T(n) = O(n\log n)$

---
# Example 2

- **Given**: $n^{3}\cdot 64^{\log_{64} n}$
###### **Solution**
- Use the identity: $a^{\log_{a} n} = n$
	- So: $64^{\log_{64} n} = n$
- Therefore: $n^{3} \cdot n = n^{4}$
- **Hence** $T(n) = O(n^{4})$

---
# Example 3

- **Given:** $64^{\log_{2} n} \cdot 32^{\log_{2} n}$

###### **Solution**
- Convert each base to powers of 2:
	- $(64 = 2^{6})$
	- $(32 = 2^{5})$
- **So: $64^{\log_{2} n} = (2^{6})^{\log_{2} n} = n^{6}$ and** $32^{\log_{2} n} = (2^{5})^{\log_{2} n} = n^{5}$
- Multiply: $n^{6} \cdot n^{5} = n^{11}$
- **Hence** $T(n) = O(n^{11})$

---
# Example 4

- **Given:** $f(n)=\frac{1}{n}$

###### **Solution**
- As $(n\to\infty)$: $f(n) = \Theta\left(\frac{1}{n}\right)$
- Nothing else simplifies.
- **Hence**  $T(n) = \Theta\left(\frac{1}{n}\right)$

---
