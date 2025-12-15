# Example Code
``` python
file = open("order.txt", "w")

try:
	file.write("Masala chai - 2 cups")
finally:
	file.close()
```

---
# Modern Way - `with`
``` python
with open("order.txt", "w") as file:
	file.write("ginger tea- 4 cups")
```

### Behind the Scenes
- Runs `file.__enter__()`
- Runs `file.__exit__()`

---
