> Lets perform CPU bound operations for example crunching numbers.

> Threading is inefficient for such operations.

---
# Code
``` python
import threading
import time


def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
	# CPU Bound Operation
    for i in range(10**8):
        total += i
    print("DONE.")


start = time.time()

threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]

[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time taken: {time.time() - start:.2f} seconds")
```

**Output**:
``` text
Crunching some numbers...
Crunching some numbers...
DONE.
DONE.
Time taken: 3.34 seconds
```

---

