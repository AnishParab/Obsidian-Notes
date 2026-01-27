# Represents Best Case Scenario
**Asymptotic Notation:**
$$
[
\Omega(f(n))
]
$$

Represents the **lower bound** — the algorithm will never be faster than this bound.

---
# Ω (Omega) Time Complexity
Ω-notation gives a **lower bound** on the growth of a function.
It describes the *best-case* asymptotic behavior or the minimum growth rate.

### Mathematical Definition
$$
[
f(n) = \Omega(g(n))
]
$$
if and only if there exist constants:
$$
[
c > 0,\quad n_0 \ge 1
]
$$
such that:
$$
[
0 \le c \cdot g(n) \le f(n) \quad \text{for all } n \ge n_0
]
$$
### Interpretation
* ( g(n) ) is a **lower bound** for ( f(n) ), up to constant scaling.
* For sufficiently large ( n ), the function ( f(n) ) never goes below some constant multiple of ( g(n) ).
### Conditions Summary
* **Positive constant:**
$$
[
  c > 0
  ]
  $$
* **Threshold value:**
$$
  [
  n_0 \ge 1
  ]
  $$
* **Lower-bound inequality:**
$$
  [
  f(n) \ge c \cdot g(n) \quad \forall, n \ge n_0
  ]
  $$
### Alternative Wording
$$
[
f(n) = \Omega(g(n)) \quad\Longleftrightarrow\quad g(n) = O(f(n))
]
$$

---
# Graphical Representation
![[omega_time_complexity.excalidraw]]

---
# Example 1
Let
$$
[
f(n)=n^{2},\qquad g(n)=n^{2}+n+10.
]
$$
#### Show $(f(n)=O(g(n)))$
We need constants $(c>0,\ n_{0})$ such that
$$
[
f(n)\le c\cdot g(n)\quad\forall n\ge n_{0}.
]
$$
Observe for all $(n\ge 0)$:
$$
[
n^{2}\le n^{2}+n+10,
]
$$
so choose $(c=1)$ and $(n_{0}=1)$. Thus
$$
[
n^{2}\le 1\cdot (n^{2}+n+10)\quad\forall n\ge1,
]
$$
hence $(f(n)\in O(g(n)))$.
### Show $(f(n)=\Omega(g(n)))$
We need $(c>0,\ n_{0})$ with
$$
[
f(n)\ge c\cdot g(n)\quad\forall n\ge n_{0}.
]
$$
Rearrange:
$$
[
n^{2}\ge c(n^{2}+n+10)
\quad\Longleftrightarrow\quad
1 \ge c\Big(1+\frac{1}{n}+\frac{10}{n^{2}}\Big).
]
$$
Pick $(c=\tfrac{1}{2})$. We require
$$
[
1 \ge \tfrac{1}{2}\Big(1+\frac{1}{n}+\frac{10}{n^{2}}\Big)
\quad\Longleftrightarrow\quad
1 \ge \frac{1}{n}+\frac{10}{n^{2}}.
]
$$
Solve $( \frac{1}{n}+\frac{10}{n^{2}}\le 1 )$. Multiply by $(n^{2})$:
$$
[
n+10\le n^{2}\quad\Longleftrightarrow\quad n^{2}-n-10\ge0,
]
$$
which holds for all integer $(n\ge 4)$. Therefore with $(c=\tfrac{1}{2})$ and $(n_{0}=4)$,
$$
[
n^{2}\ge \tfrac{1}{2}(n^{2}+n+10)\quad\forall n\ge4,
]
$$
so $(f(n)\in\Omega(g(n)))$.
#### Conclude $(f(n)=\Theta(g(n)))$
Since $(f(n)\in O(g(n)))$ and $(f(n)\in\Omega(g(n)))$, it follows that
$$
[
f(n)=\Theta(g(n)).
]
$$
#### Summary (concrete constants)
* $(n^{2}\le 1\cdot (n^{2}+n+10)) for all (n\ge1) → (f\in O(g)) with (c=1,\ n_{0}=1)$.
* $(n^{2}\ge \tfrac{1}{2}(n^{2}+n+10)) for all (n\ge4) → (f\in\Omega(g)) with (c=\tfrac{1}{2},\ n_{0}=4)$.
* Therefore $(n^{2}=\Theta(n^{2}+n+10))$.

---
# Example 2
$$
[
f(n)=n,\quad g(n)=n^{2}
]
$$
#### Goal
Determine whether:
$$
[
n = \Omega(n^{2})
]
$$
#### Ω Definition
$$
[
f(n)=\Omega(g(n))\quad\Longleftrightarrow\quad
\exists, c>0,\ n_{0}\ge1\ \text{s.t.}\
f(n)\ge c,g(n)\ \forall n\ge n_{0}
]
$$
Substitute $(f(n)=n)$ and $(g(n)=n^{2})$:
$$
[
n \ge c n^{2}
]
$$
#### Solve the Inequality
Start with:
$$
[
n \ge c n^{2}
]
$$
Divide by (n) (valid for (n>0)):
$$
[
1 \ge c n
]
$$
Rearrange:
$$
[
c \le \frac{1}{n}
]
$$
#### Interpretation
For Ω to hold:
* (c) must be a **positive constant**
* And it must satisfy
$$
  [
  c \le \frac{1}{n}\quad\forall n\ge n_{0}
  ]
$$
But as $(n\to\infty)$:
$$
[
\frac{1}{n}\to 0
]
$$
This forces:
$$
[
c \le 0
]
$$
But Ω requires:
$$
[
c > 0
]
$$
Contradiction.

Therefore, **no positive constant (c)** can satisfy the inequality for all sufficiently large (n).
#### Conclusion
$$
[
n \ne \Omega(n^{2})
]
$$
or equivalently:
$$
[
n = o(n^{2})
]
$$
---
