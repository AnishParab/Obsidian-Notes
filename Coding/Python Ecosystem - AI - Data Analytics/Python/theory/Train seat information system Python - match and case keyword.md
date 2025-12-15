# Project
You are building a ticket info system for a railway app. Based on seat type, show it's features.
- Input: `"sleeper"`, `"AC"`, `"general"`, `"luxury"`.
- Match using `match-case`.
- Unknown -> show: `"Invalid seat type"`

---
# Code
``` python
seat_type = input("Enter your preferred seat type (sleeper, AC, general, luxury): ").lower()

match seat_type:
	case "sleeper":
		print("Sleeper - No AC - Beds available")
	case "ac":
		print("AC - Air conditioned, comfy ride")
	case "general":
		print("General - Cheapest option - No reservation")
	case "luxury":
		print("Luxury - Premium seats with meals")
	case _:
		print("Invalid seat type")
```

---
