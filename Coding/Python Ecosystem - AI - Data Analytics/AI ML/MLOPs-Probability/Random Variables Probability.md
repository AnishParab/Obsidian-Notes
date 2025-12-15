# Random Variables

### **Definition**

A **random variable** is a **function that assigns a numerical value to every outcome** of a random experiment.

- Even though the experiment is random, the random variable gives us a way to quantify it.
- Denoted usually as ( X, Y, Z, \dots )

---
### **Types of Random Variables**

1. **Discrete Random Variables**
    - Take **countable values** (finite or infinite).
    - Examples:
        - Rolling a six-sided die → $$ X \in {1,2,3,4,5,6} $$
        - Number of heads in 10 coin flips → $$ X \in {0,1,\dots,10} $$
2. **Continuous Random Variables**
    - Take values from a **continuous range** (uncountable).
    - Examples:
        - Height of a person → $$ X \in [0, \infty) $$
        - Temperature in a city → $$ X \in \mathbb{R} $$

---

### **Key Concepts**

- **Probability Mass Function (PMF):**  
    For discrete RVs, it gives $$ P(X = x) $$  
    Example: For a fair die, $$ P(X=3) = 1/6 $$
    
- **Probability Density Function (PDF):**  
    For continuous RVs, gives the _density_ at a point ( x ) (probability is area under curve).
    
- **Cumulative Distribution Function (CDF):**  
    Gives $$ P(X \le x) $$for both discrete and continuous RVs.
    

---
### **Example**

**Coin flip (discrete RV):**  
$$  
X =  
\begin{cases}  
1 & \text{if Heads} \ 

0 & \text{if Tails}  
\end{cases}  
$$

- PMF: $$ P(X=1)=0.5, P(X=0)=0.5 $$
    
- CDF: $$ F(0)=0.5, F(1)=1 $$
    

**Height (continuous RV):**

- PDF might follow a normal distribution:  
    $$  
    f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-(x-\mu)^2/2\sigma^2}  
    $$
    
- Probability between 160 cm and 170 cm = area under curve between these two values.

---

Random variables are critical in **machine learning**:

- Features, labels, loss functions, and even weights in neural networks are modeled as random variables.
- Understanding RVs lets you reason about **expectations, variance, and sampling**.

---

