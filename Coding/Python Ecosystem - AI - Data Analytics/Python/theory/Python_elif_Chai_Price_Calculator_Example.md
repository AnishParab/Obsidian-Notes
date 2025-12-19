# Problem
A tea stall offers different prices for different cup sizes. Write a program that calculates the price based on size.
- Input: "small", "medium", "large"
- Small -> Rs 10, Medium -> Rs 15, Large -> Rs 20
- If invalid: show "Unknown cup size"

---
# Code
``` python
cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
	price("Price is 10 rupees")
elif cup == "medium":
	price("Price is 15 rupees")
elif cup == "large":
	price("Price is 20 rupees")
else:
	print("Unknown cup size")
```

---
