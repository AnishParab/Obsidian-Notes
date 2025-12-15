# What is Degree of Freedom ?
The **degree of belief** is how strongly you believe a statement or event is true — expressed as a **probability between 0 and 1**.
- A value of **1** means total certainty (you’re sure it’s true).
- A value of **0** means total disbelief (you’re sure it’s false).
- Anything in between (say, 0.7 or 0.3) represents _how confident_ you are in that belief.

---
# In Probability terms
This concept belongs to the **Bayesian interpretation of probability**.  
Here, probability is _not_ just about counting outcomes (like dice rolls),  
but also about representing **subjective uncertainty** — how much you _believe_ something before and after seeing evidence.

Formally, we can write:

$$ P(H)=degree of belief in hypothesis HP(H) = \text{degree of belief in hypothesis } HP(H)=degree of belief in hypothesis H
$$

When you get new evidence EEE, you update your belief using **Bayes’ theorem**:

$$P(H∣E)=P(E∣H)×P(H)P(E)P(H|E) = \frac{P(E|H) \times P(H)}{P(E)}P(H∣E)=P(E)P(E∣H)×P(H)​
$$

---
# Example
- Suppose you believe there’s a **20% chance it will rain tomorrow**.  
That 0.2 isn’t based on rolling dice — it’s your _degree of belief_, perhaps informed by weather patterns or intuition.
- If you then see a radar image showing dark clouds, you update that belief to, say, 0.7.  
That’s Bayesian updating in action.

---
# Quick Summary

| Concept                                     | Meaning                                      |
| ------------------------------------------- | -------------------------------------------- |
| **Frequentist probability**                 | Long-run frequency of an event (objective)   |
| **Degree of belief (Bayesian probability)** | Personal confidence in an event (subjective) |

---

