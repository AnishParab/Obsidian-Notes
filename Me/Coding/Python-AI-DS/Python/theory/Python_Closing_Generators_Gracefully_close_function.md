# `close()`

> `close()` raises  **GeneratorExit**, which is not an error but rather more like a **Shutdown Signal**.

> It ensures that the **cleanup** is _predictable_ and generator does not accidentally continue.

---
# Code: Closing a Generator Gracefully
```python
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")

stall = chai_stall()
print(next(stall))

stall.send("Hello")
stall.send("Bello")

# Gracefully stop the generator
stall.close()
```

**Output:**
```text
Waiting for chai order
Hello
Bello
```

#### Explanation:
* `next(stall)` starts the generator and reaches the first `yield`.
- `stall.close()` this raises a **GeneratorExit** signal and immediately stops the program. 

---
# But how do we run the `Except` Block ?
``` python
except GeneratorExit:
    print("Stall closed, No more chai")
```

- This will run the `except` block when **GeneratorExit** is triggerred.

**Output**
``` text
Waiting for chai order
Hello
Bello
Stall closed. No more chai
```

---
