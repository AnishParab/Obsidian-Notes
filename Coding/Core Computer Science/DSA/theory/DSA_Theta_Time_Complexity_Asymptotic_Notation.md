# Average Case Scenario
**Asymptotic Notation:**
$$
[
\Theta(f(n))
]
$$

Represents the **tight bound** — captures typical performance when inputs are randomly distributed.

---
Here is a clean, complete, mathematically correct **Θ (Theta) Time Complexity** section, formatted for Obsidian and consistent with the definitions of **O** and **Ω**.

---
# Θ (Theta) Time Complexity
$$
[  
f(n)=\Theta(g(n))  
]
$$
Theta notation represents a **tight bound**.  
It means (f(n)) grows **as fast as** (g(n)) asymptotically.
#### Formal Mathematical Definition
$$
[  
f(n)=\Theta(g(n))  
]
$$
if and only if there exist constants
$$
[  
c_{1}>0,\quad c_{2}>0,\quad n_{0}\ge1  
]
$$
such that
$$
[  
c_{2} , g(n)\ \le\ f(n)\ \le\ c_{1} , g(n)  
\quad\text{for all } n\ge n_{0}  
]
$$
#### Interpretation
Theta notation requires **both**:
##### **1. Big-O upper bound**
$$
[  
f(n)\le c_{1} . g(n)  
]
$$
##### **2. Omega lower bound**
$$
[  
f(n)\ge c_{2} . g(n)  
]
$$
When **both** conditions hold simultaneously (for some constants and sufficiently large (n)), then:
$$
[  
f(n)=\Theta(g(n))  
]
$$

---
# Graphical Representation
![[omega.excalidraw]]

---
# Example
$$
[
f(n)=n^{2}+3n+10
\quad\text{and}\quad
g(n)=n^{2}
]
satisfy
[
f(n)=\Theta(n^{2})
]
$$
### Step 1 — Prove the Big-O upper bound
We need constants (c_{1}>0) and (n_{0}) such that:
$$
[
n^{2}+3n+10 \le c_{1} n^{2}
]
$$
Divide everything by $(n^{2})$ (for (n>0)):
$$
[
1 + \frac{3}{n} + \frac{10}{n^{2}} \le c_{1}
]
$$
As $(n\to\infty)$:
$$
[
1 + \frac{3}{n} + \frac{10}{n^{2}} \to 1
]
$$
Choose $(c_{1}=2)$.
Check when the inequality holds:
$$
[
1 + \frac{3}{n} + \frac{10}{n^{2}} \le 2
]
$$
Solve:
$$
[
\frac{3}{n} + \frac{10}{n^{2}} \le 1
]
$$
Multiply by $(n^{2})$:
$$
[
3n + 10 \le n^{2}
\quad\Longleftrightarrow\quad
n^{2} - 3n - 10 \ge 0
]
$$
This is true for all $(n\ge 5)$.

Thus **Big-O holds** with:
$$
[
c_{1}=2,\quad n_{0}=5
]
$$
So:
$$
[
n^{2}+3n+10 = O(n^{2})
]
$$
### Step 2 — Prove the Omega lower bound
We need $(c_{2}>0)$ and $(n_{0})$ such that:
$$
[
n^{2}+3n+10 \ge c_{2} n^{2}
]
$$
Divide by $(n^{2})$:
$$
[
1 + \frac{3}{n} + \frac{10}{n^{2}} \ge c_{2}
]
$$
Since the expression is **always ≥ 1** for all (n>0), choose:
$$
[
c_{2}=1
]
$$
Thus:
$$
[
1 + \frac{3}{n} + \frac{10}{n^{2}} \ge 1
\quad\forall n\ge 1
]
$$
Therefore **Omega holds** with:
$$
[
c_{2}=1,\quad n_{0}=1
]
$$
So:
$$
[
n^{2}+3n+10 = \Omega(n^{2})
]
$$
### Final Conclusion
Since both were proven:
$$
[
n^{2}+3n+10 = O(n^{2})
]
[
n^{2}+3n+10 = \Omega(n^{2})
]
$$
Therefore:
$$
[
n^{2}+3n+10 = \Theta(n^{2})
]
$$
---
