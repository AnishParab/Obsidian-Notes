> I have implemented a CPU bound work: Crunching Numbers to test which one is better for it.

---
# Conclusion
- **CPU-bound work → Multiprocessing / Parallelism is better**
- **I/O-bound work → Concurrency / Threading is better**

---
# Code Thread
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

> Time Taken is 3.34 seconds.

---
# Code Process
``` python
from multiprocessing import Process
import time


def cpu_heavy():
    print("Crunching some numbers...")
    total = 0
    for i in range(10**8):
        total += i
    print("DONE.")


if __name__ == "__main__":
    start = time.time()

    processes = [Process(target=cpu_heavy) for _ in range(2)]

    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"Time taken: {time.time() - start:.2f} seconds")
```

``` text
Crunching some numbers...
Crunching some numbers...
DONE.
DONE.
Time taken: 1.82 seconds
```

> Time Taken is 1.82 seconds.

---
