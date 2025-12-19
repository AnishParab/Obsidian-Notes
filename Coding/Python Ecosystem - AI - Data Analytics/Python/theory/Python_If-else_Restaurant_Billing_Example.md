# Problem Statement
**Restaurant Billing System**
- You’re designing a billing system for a restaurant. Depending on the total bill amount entered by the customer, they might get a free dessert.

**Tasks:**
1. If the bill amount is greater than 500, return the string "You get a free dessert!"
2. Otherwise, return the string: "No free dessert this time."

---
# Code
``` python
total_bill_amount = input("Enter your bill amount here.\n")

total_bill_amount = int(total_bill_amount)

if total_bill_amount > 500:
    print("You get a free desert.")
else:
    print("No free desert this time. Fuck off!")
```

---
