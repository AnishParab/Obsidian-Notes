> You have only **one core** engaged in this one, but you have **multiple threads** which are switched very frequently and performing the task.

---
# Example Concurrency: `threading`
``` python
import threading
import time

def take_orders():
	for i in range(1, 4):
		print(f"Taking order for #{i}")
		time.sleep(1)
		
def brew_chai():
	for i in range(1, 4):
		print(f"Brewing chai for #{i}")
		time.sleep(2)
		
# Create threads
order_thread = threading.Thread(target = take_orders)
brew_thread = threading.Thread(target = brew_chai)

# Start thread
order_thread.start()
brew_thread.start()

# Wait for thread to finish
order_thread.join()
brew_thread.join()

print()

print("All orders taken and chai brewed")
```

**Output**
``` text
Taking order for #1
Brewing chai for #1
Taking order for #2
Brewing chai for #2
Taking order for #3
Brewing chai for #3
All orders taken and chai brewed
```

---
