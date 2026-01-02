> Better alternative to ensure a file is always closed, even if an error occurs.

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
