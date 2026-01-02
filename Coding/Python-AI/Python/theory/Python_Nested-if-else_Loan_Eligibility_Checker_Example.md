# Problem Statement
**Loan Eligibility Checker**
- You’re building a basic loan eligibility checker for a bank. A customer must meet two conditions to be eligible:  

**Tasks:**
1. If the user’s age is **21 or above**, check:
    - If income is **25,000 Bucks or above**, return: "Eligible for loan"
    - Otherwise, return: "Not eligible: Income too low"
2. If the user’s age is **less than 21**, return: "Not eligible: Age must be 21 or above"

---
# Code
``` python
age = input("Enter your age.\n")
income = input("Enter your income.\n")

age = int(age)
income = int(income)

if age >= 21:
    if income >= 25000:
        print("Eligible for loan")
    else:
        print("Not eligible, income too low")
else:
    print("Not eligible, age must be 21 or above.")
```

---
