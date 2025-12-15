# The Law of Large Numbers (LLN)

### **Informal Definition**

As you repeat a random experiment many times, the **average result** tends to get closer and closer to the **expected (true) value**.

---
### **Formal Definition**

Let $$( X_1, X_2, X_3, \ldots, X_n )$$ be a sequence of independent, identically distributed (i.i.d.) random variables, each with:

- Expected value $$( E[X_i] = \mu )$$
- Finite variance $$( Var(X_i) = \sigma^2 )$$

Then the **sample mean**  
$$  
\bar{X}_n = \frac{1}{n}\sum_{i=1}^{n} X_i  
$$  
converges to $$( \mu ) as ( n \to \infty )$$

Formally:  
$$  
\lim_{n \to \infty} P(|\bar{X}_n - \mu| < \varepsilon) = 1 \quad \text{for any } \varepsilon > 0  
$$

This means: as the number of trials increases, the probability that your average is close to the true mean goes to **1**.

---
### **In Plain Words**
If you flip a fair coin:
- The theoretical probability of heads is **0.5**.
- But short-term results (like 3 heads in a row) might look biased.
- However, as you flip more coins (say 1,000 or 10,000),  
    the proportion of heads will get closer to **0.5**.

That’s the law of large numbers in action.

---
### **Types of LLN**
- **Weak Law:**  
    The sample mean converges _in probability_ to the true mean.
- **Strong Law:**  
    The sample mean converges _almost surely_ (with probability 1) to the true mean.

(Think of “almost surely” as a stronger guarantee — it holds in the long run, for almost every random sequence.)

---
### **Intuition in Practice**
In machine learning, the LLN justifies why:
- Larger datasets give more reliable estimates.
- Model performance stabilizes as you train on more data.
- Random sampling becomes representative as sample size grows.

---
