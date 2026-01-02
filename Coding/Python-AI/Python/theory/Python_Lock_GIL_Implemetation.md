> Note that the **output** I got was **very fast**.

---
# `Lock()`
- Ensures that only **one thread** modifies the shared data at a time.

---
# Code
``` python
import threading

counter = 0
# Lock() method
lock = threading.Lock()


# Designing a thread safe method
def increment():
    global counter
    for _ in range(100000):
        # Lock a particular memory location
        with lock:
            counter += 1


# Letting multiple threads access increment
threads = [threading.Thread(target=increment) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")
```

**Output**:
``` text
Final counter: 1000000
```

---
