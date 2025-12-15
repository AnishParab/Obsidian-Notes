# Diagram
![[concurrency_and_parallelism.excalidraw|500]]

---
# Difference between Concurrency and Parallelism in Python

#### Concurrency
- `threading.Thread`
- `asyncio`
#### Parallelism
- `multiprocessing.Process`
- `concurrent.futures.ProcessPoolExecutor`

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

print(f"All orders taken and chai brewed")
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

> You have only **one core** engaged in this one, but you have **multiple threads** which are switched very frequently and performing the task.

---
# Example Parallelism
``` python
from multiprocessing import Process
import time

def brew_chai(name):
	print(f"Start of {name} chai brewing")
	time.sleep(3)
	print(f"End of {name} chai brewing")
	
if __name__ == "__main__":
	chai_makers = [
		Process(target = brew_chai, args=(f"Chai Maker #{i+1}", ))
		for i in range(3)
	]
	
	# Start all process
	for p in chai_makers:
		p.start()
	
	# Wait for all to complete
	for p in chai_makers:
		p.join()
		
	print("All chai served")
```

**Output**
``` text
Start of Chai Maker #1 chai brewing
Start of Chai Maker #2 chai brewing
Start of Chai Maker #3 chai brewing
End of Chai Maker #1 chai brewing
End of Chai Maker #2 chai brewing
End of Chai Maker #3 chai brewing
All chai served
```

> Multiple cores engaged.

---
