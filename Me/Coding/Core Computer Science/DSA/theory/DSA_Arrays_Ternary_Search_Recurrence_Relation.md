# Recurrence Realtion - Ternary Search

![[ternary_search_recurrence_realtion.excalidraw|700]]

---
###### **Solution using Substitution Method 
- $T(n) = T(\frac{n}{3}) + c$.
- $T(\frac{n}{3}) = T(\frac{n}{3^2}) + c$ .
- By substituting,
	- $\implies \quad T(n) = T(\frac{n}{3^2}) + 2c$
	- $\implies \quad T(n) = T(\frac{n}{3^3}) + 3c$
- T(n) in terms of k terms is
	- $\implies \quad T(n) = T(\frac{n}{3^k}) + k.c$
- **Note that** $3^k = n$
	- $\implies \quad k = log_3 n$
- $\implies \quad T(n) = T(\frac{n}{3^{log_3n}}) + c.log_3 n$
- $\implies \quad T(n) = T(\frac{n}{n^{log_33}}) + c.log_3 n$
- $\implies \quad T(n) = T(1) + c.log_3 n$

- **Time Complexity**: $T(n) = O(log_3 n)$

---
