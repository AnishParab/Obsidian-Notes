# `send(value)`

> `send()` is used to **send value** to a **stop iteration caused by yield**. 

> It triggers a **yield**.

---
# What ?
![[yield_python.excalidraw|500]]

---
# Example: Sending Values to a Generator
```python
def chai_customer():
    print("Welcome! What chai would you like?")
	
    order = yield
	print(order)
	print()
	
    while True:
        print(f"Preparing: {order}")
		# Prevents Infinite loop
        order = yield

stall = chai_customer()

# Start the generator to reach the first yield
next(stall)

stall.send("Masala chai")
stall.send("Lemon tea")
```

**Output:**
```text
Welcome! What chai would you like?
Masala Chai

Preparing: Masala chai
Preparing: Lemon tea
```
### Explanation:
![[send_function_generator.excalidraw|500]]

---
### Key Points:
* `next(stall)` starts the generator and runs up to the first `yield`.
* `stall.send(value)` sends a value into the generator, which is assigned to `order`.
* After processing, the generator pauses again at the next `yield`, awaiting the next value.

---
