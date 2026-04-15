# Profiling
``` bash
python -m cProfile -s time bgworker.py
```

---
# Unpredictable Code: Race Condition
``` python
import threading

chai_stock = 0


def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1


threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("Chai stock: ", chai_stock)
```

---
# Deadlock Code
``` python
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    with lock_a:
        print("Task 1 acquired lock A")
        with lock_b:
            print("Task 1 acquired lock B")


def task2():
    with lock_b:
        print("Task 2 acquired lock B")
        with lock_a:
            print("Task 2 acquired lock A")


t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()
```

---
# Tools
- pyspy
- vprof

---
