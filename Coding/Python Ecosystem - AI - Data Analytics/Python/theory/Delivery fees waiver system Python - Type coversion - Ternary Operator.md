# Problem
You run an online tea store. If the order amount is more than Rs 300, delivery is free, otherwise, it costs Rs 30.
- Input: `order_amount`
- Use ternary operator to decide delivery fee.

---
# Code
``` python
order_amount = input("Enter the order amount: ")

# This returns a 'str' value
print(f"Order amount: {type(order_amount)}")
```

---
# Final Code
``` python
# Covert 'str' to 'int', it will try it's best
order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is : {delivery_fees}")
```

---
