# `Queue` in Multiprocessing
- In multiprocessing, **each process has its own memory space**.
- Variables cannot be shared directly between processes.
- `multiprocessing.Queue` provides a **safe inter-process communication (IPC)** mechanism.
- It allows processes to **send and receive data** using FIFO order.
- Internally, it uses **pipes + locks** to ensure data integrity.

**Why it is needed**
- Enables result passing from child process to parent
- Prevents race conditions and data corruption
- Essential for coordinating work between processes

**One line**
> `Queue` is used in multiprocessing to **share data safely between separate processes that do not share memory**.

---
# Code
``` python
from multiprocessing import Process, Queue


def prepare_chai(queue):
    queue.put("Masala chai is ready")


if __name__ == "__main__":
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())
```

**Output**:
``` text
Masala chai is ready
```

---
