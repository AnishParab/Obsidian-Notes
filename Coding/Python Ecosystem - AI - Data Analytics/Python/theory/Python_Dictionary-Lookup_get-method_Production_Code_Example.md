# Code
``` python
# Use dictionaries instead of repeated match cases
# List
users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

# (percentage_discount, fixed_discount)
# Dictionary
discounts = {
    "P20": (0.2, 0),  # 20% discount
    "F10": (0, 10),  # ₹10 fixed discount
    "P50": (0.5, 0),  # 50% discount
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed

    print(
        f"{user['id']} paid {user['total']} and got a discount of ₹{discount} for next visit"
    )
```

**Output**
``` text
1 paid 100 and got a discount of ₹20.0 for next visit
2 paid 150 and got a discount of ₹10 for next visit
3 paid 80 and got a discount of ₹40.0 for next visit
```

---
# Dictionary lookup using `get()`
``` python
percent, fixed = discounts.get(user["coupon"], (0, 0))
```

1. `user["coupon"]`
    - Accesses the `"coupon"` key in the user dictionary.
    - Example: `"P20"`
2. `discounts.get("P20", (0, 0))`
    - Looks up `"P20"` in `discounts`
    - Returns `(0.2, 0)`
    - If coupon doesn’t exist → returns `(0, 0)` (safe default)
3. Tuple unpacking:
``` python
percent, fixed = (0.2, 0)
```
	- `percent = 0.2`
    - `fixed = 0`

---
