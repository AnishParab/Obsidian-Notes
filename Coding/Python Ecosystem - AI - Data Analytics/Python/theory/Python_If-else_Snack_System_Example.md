# Problem
A local cafe wants a program that suggests a snack. If a customer asks for cookies or samosa, it confirms the order. Otherwise, it says it's not available.
- Take snack input.
- If it's `"cookies"` or `"samosa"` , confirm the order.
- Else, show unavailability.

---
# Code
``` python
snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
	print(f"Great choice! We will serve you {snack}")
else:
	print(f"Sorry we only serve cookies or samosa with chai.")
```

---
