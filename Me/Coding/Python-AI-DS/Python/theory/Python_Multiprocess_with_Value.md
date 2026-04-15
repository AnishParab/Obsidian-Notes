# How `Value` helps in this code

### Problem without `Value`
- In multiprocessing, **each process has its own memory**.
- A normal integer (`counter = 0`) would be **copied**, not shared.
- Each process would increment its own private copy → incorrect final result.

### What `multiprocessing.Value` does
1. **Shared Memory Allocation**
    - `Value("i", 0)` creates an integer stored in **shared memory**.
    - All processes reference the **same memory location**.
2. **Atomic Access via Lock**
    - `Value` comes with an internal **synchronization lock**.
    - `counter.get_lock()` ensures:
        - Only one process updates the value at a time
        - Prevents race conditions
3. **Safe Read–Modify–Write**
    - Increment is not atomic (`read → add → write`).
    - The lock makes this sequence **mutually exclusive**.
4. **Correct Final Result**
    - 4 processes × 100000 increments = `400000`
    - Shared memory + lock guarantees correctness.

---
# Code
``` python
from multiprocessing import Process, Value


def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value("i", 0)

    processes = [Process(target=increment, args=(counter,)) for _ in range(4)]

    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value: ", counter.value)
```

**Output**:
``` text
Final counter value:  400000
```

---
