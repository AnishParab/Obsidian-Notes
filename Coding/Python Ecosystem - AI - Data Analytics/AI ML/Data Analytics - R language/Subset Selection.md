**Definition:**  
Subset selection involves choosing the **best subset of features** from an initial set of size \( d \).

---
# Key Points

1. **Number of Possible Subsets**  
   - Total subsets: \( 2^d \).  
   - Exhaustive search is usually impractical for large \( d \).

2. **Criteria for Selection**  
   - A **criterion function** is needed to evaluate and compare subsets.  
   - Example: Minimizing error, maximizing information gain, or optimizing model performance.

3. **Search Methods**  
   - Cannot check all \( 2^d \) subsets.  
   - Use **heuristics** to efficiently explore promising subsets:  
     - Forward selection  
     - Backward elimination  
     - Stepwise selection  
     - Genetic algorithms  

---
**Goal:**  
Find a **near-optimal subset** that balances model accuracy and complexity without evaluating every possible combination.

---
