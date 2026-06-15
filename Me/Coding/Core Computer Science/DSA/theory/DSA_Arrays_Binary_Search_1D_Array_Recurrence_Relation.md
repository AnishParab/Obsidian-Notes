# Recurrence Realtion - Binary Search

![[binary_search_recurrence_relation.excalidraw|700]]

---
###### **Solution using Master's Theorem
- Here $a = 1$, $b = 2$ and $f(n) = c$
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
	- $\implies \Theta(n^k log ^ {p+1} n)$
	- $\implies \Theta(n^0 log ^ {0+1} n)$
- **Hence $\Theta(log n)$**

---
