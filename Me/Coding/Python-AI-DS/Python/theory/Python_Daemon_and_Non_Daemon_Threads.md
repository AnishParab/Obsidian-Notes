# Daemon Threads
- Background threads that automatically shutdown when the main program exit.
``` python
import threading
import time


def monitor_tea_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(3)


t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done")
```

---
# Non-Daemon Threads
``` python
import threading
import time


def monitor_tea_temp():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(3)


t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done")
```

---
