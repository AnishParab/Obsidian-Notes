# What ?
Naive Bayes is a probabilistic classification algorithm based on **Bayes’ theorem** with a **naive assumption** that features are conditionally independent given the class.

---
# **Formula:**  
$$
[  
P(C_k | x_1, x_2, ..., x_n) = \frac{P(C_k) \prod_{i=1}^{n} P(x_i | C_k)}{P(x_1, x_2, ..., x_n)}  
]  
$$
Where:
$$
( C_k ): class label
 $$   
$$
( x_i ): feature value
$$    
$$
( P(C_k) ): prior probability of class ( C_k )
$$    
$$
( P(x_i | C_k) ): likelihood of feature given class
$$    
$$
( P(C_k | x_1, ..., x_n) ): posterior probability (what we want)
$$    

Since the denominator is constant across classes, classification picks the class maximizing the numerator:  
$$
[  
\hat{C} = \arg\max_{C_k} P(C_k) \prod_{i=1}^{n} P(x_i | C_k)  
]
$$

---
# Types:
1. **Gaussian Naive Bayes** – assumes features follow a normal distribution.
2. **Multinomial Naive Bayes** – for discrete counts (e.g., word frequencies).
3. **Bernoulli Naive Bayes** – for binary features.

---
# Advantages:
- Fast and simple.
- Works well for text classification (spam filtering, sentiment analysis).
- Needs little training data.

---
# Limitations:
- Independence assumption rarely holds.
- Poor with highly correlated features.

---
