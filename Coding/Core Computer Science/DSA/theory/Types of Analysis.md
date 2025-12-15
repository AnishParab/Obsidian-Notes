---

---
# Choosing the Best Solution (S1, S2, S3)

## Criteria
* **Time Complexity** — how fast the algorithm grows with input size.
* **Space Complexity** — how much extra memory the algorithm needs.

Choose the solution with:
* Lower **time complexity** first.
* If tie, choose lower **space complexity**.

---
# Asymptotic Notations

## Types of Analysis

### **1. Aposteriori Analysis**
* Depends on hardware, compiler, language.
* Gives exact empirical results.
* Results differ across systems.

### **2. Apriori Analysis (Preferred)**
* Independent of hardware/software.
* Gives asymptotic (approximate) behavior.
* Produces consistent theoretical results.

---
# Code Examples

### Example 1: Summing by Iteration

```python
def sum_of_numbers(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total

lst = [1, 2, 3, 4, 5]
result = sum_of_numbers(lst)
print(f"Sum of first 5 natural numbers is: {result}")
```

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---
### Example 2: Summing Using Formula

```python
def sum_of_numbers(lst):
    n = len(lst)
    sum = (n * (n + 1)) / 2
    return sum

lst = [1, 2, 3, 4, 5]
result = sum_of_numbers(lst)
print(f"Sum of numbers is: {result}")
```

**Time Complexity:** O(1)
**Space Complexity:** O(1)

---
# Conclusion
For this problem, the formula-based solution (2nd) is better because it runs in constant time **O(1)** compared to the iterative **O(n)** approach.

---
