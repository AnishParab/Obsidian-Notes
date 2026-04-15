> Arguments are passed as **tuples**.
> Good practice to add `, ` at the end of the arguments.

---
# Code
``` python
import threading
import time


def prepare_chai(type_, wait_time):
    print(f"{type_} chai brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: Ready.")

# Passing Arguments
t1 = threading.Thread(target=prepare_chai, args=("Masala", 2, ))
# Passing Arguments
t2 = threading.Thread(target=prepare_chai, args=("Masala", 3, ))

t1.start()
t2.start()

t1.join()
t2.join()
```

**Output**:
``` text
Masala chai brewing...
Masala chai brewing...
Masala chai: Ready.
Masala chai: Ready.
```

---
