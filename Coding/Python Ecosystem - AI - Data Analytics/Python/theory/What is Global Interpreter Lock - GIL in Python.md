# GIL
![[gil.excalidraw|500]]
- Whoever reaches the value first gets a **mutex lock** and prevents **race condition**.

---
# Example Code: Using Threads
``` python
import threading
import time

def brew_chai():
	print(f"{threading.current_thread().name} started brewing...")
	count = 0
	for _ in range(100_000_000):
		count += 1
	print(f"{threading.current_thread().name} finished brewing...")
	
thread1 = threading.Thread(target = brew_chai, name = "Barista-1")
thread2 = threading.Thread(target = brew_chai, name = "Barista-2")

start = time.time()
thread1.start()
thread2.start()

thread1.join()
thread2.join()

end = time.time()

print(f"Total time taken: {end - start:.2f} seconds")
```

**Output**
``` text
Barista-1 started brewing...
Barista-2 started brewing...
Barista-1 finished brewing...
Barista-2 finished brewing...
Total time taken: 6.35 seconds
```

---
# Example Code: Using Processes
``` python
from multiprocessing import Process
import time

def crunch_number():
    print("Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print("Ended the count process...")


if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number)
    p2 = Process(target=crunch_number)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-processing is {end - start:.2f} seconds")
```

**Output**
``` text
Started the count process...
Started the count process...
Ended the count process...
Ended the count process...
Total time with multi-processing is 3.63 seconds
```

---
