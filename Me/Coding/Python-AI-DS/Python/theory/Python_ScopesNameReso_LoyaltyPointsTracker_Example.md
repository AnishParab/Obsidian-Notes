# Problem Statement
**Loyalty Points Tracker**
- You are building a **Loyalty Points Tracker** for a retail chain that rewards customers based on their spending. The tracker calculates the total transaction amount per customer and awards loyalty points accordingly. Some customers may also qualify for bonus points based on their total spending.  

**Your Tasks:**
- Global Loyalty Points:
    - Define a global variable loyalty_points that keeps track of the total loyalty points earned by all customers.
- Create Function: process_transactions(transactions: list[int]) -> int
    - Accept a list of transaction amounts from a single customer.
    - Initialize a **local variable** total to store the sum of all the customer’s transactions.
- Nested Bonus Logic:
    - Define a **nested function** apply_bonus() inside process_transactions.
    - If the total exceeds ₹1000, add a bonus of ₹50.
    - Use the nonlocal keyword to modify the total from within the nested function.
- Point Calculation:
    - After applying the bonus (if any), update the global loyalty_points using the global keyword.
    - Customers earn **1 point for every ₹100 spent** (total // 100).
- Return the Final Total:
    - Return the final amount (including bonus if applicable) from process_transactions.
**Example:**
1. process_transactions([400, 700]) 
2. # total = 1100 → bonus applied → total = 1150 
3. # points earned = 11

---
# Code
``` python
loyalty_points = 0


def process_transactions(transactions: list[int]):
    total = 0

    for transaction in transactions:
        total += transaction

    def apply_bonus():
        nonlocal total
        global loyalty_points

        if total > 1000:
            total += 50

        loyalty_points = total // 100

    apply_bonus()
    return total


final_total = process_transactions([400, 700])
print(final_total)
print(loyalty_points)
```

---
