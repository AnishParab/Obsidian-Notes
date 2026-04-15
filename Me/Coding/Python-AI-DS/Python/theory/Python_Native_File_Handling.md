# Example Code
``` python
# file, write mode
file = open("order.txt", "w")

try:
	# write into the file
	file.write("Masala chai - 2 cups")
finally:
	# close file
	file.close()
```

- **Creates** `order.txt` if it doesn't exist.

---
