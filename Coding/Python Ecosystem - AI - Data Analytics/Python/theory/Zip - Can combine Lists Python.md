# Project
You're preparing an order summary with customer names and their total bill.
- Use two lists: one for names and one for bills.
- Print: `[Name] paid Rs[amount]`

---
# Code using `zip`
- Iterate over several iterables in parallel, producing tuples with an item from each one.
``` python
names = ["Anish", "Mithila", "Bheem", "Raju"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
	print(f"{name} paid {amount} rupees")
```

Output:
``` bash
Anish paid 50 rupees
Mithila paid 70 rupees
Bheem paid 100 rupees
Raju paid 55 rupees
```

---
