# Probability Axioms (Kolmogorov’s Axioms)

Let $$( \Omega )$$ be the **sample space** — the set of all possible outcomes.  
Let ( A ) be any **event**, which is a subset of ( \Omega ).  
Then, the probability function ( P ) must satisfy the following three axioms:

---
### **Axiom 1 — Non-negativity**


$$P(A) \ge 0  
$$
Probability values are **never negative**.  
Every event has a probability between 0 and 1.

_Example:_  
Even if something is unlikely (like being hit by a meteor), its probability can’t be less than 0.

---
### **Axiom 2 — Normalization (Certainty)**

$$  
P(\Omega) = 1  
$$
  
The probability of the **entire sample space** — i.e., something _must_ happen — is 1.

_Example:_  
When rolling a die, one of the six faces _must_ appear, so $$ P({1,2,3,4,5,6}) = 1 $$

---
### **Axiom 3 — Additivity (Mutually Exclusive Events)**

If two events ( A ) and ( B ) **cannot happen at the same time** (i.e., $$ (A \cap B = \emptyset ) 
$$
then
$$
[  
P(A \cup B) = P(A) + P(B)
]
$$

_Example:_  
When tossing a coin:  
$$  
P(\text{Heads or Tails}) = P(\text{Heads}) + P(\text{Tails}) = \tfrac{1}{2} + \tfrac{1}{2} = 1  
$$

---
### From These Axioms, We Derive Key Rules

Using the axioms, we can prove:

1. $$ P(\emptyset) = 0 $$
    
2. $$ 0 \le P(A) \le 1 $$
    
3. $$ P(A') = 1 - P(A) $$ (where ( A' ) is the complement of ( A ))

---
