# Problem Statement
**Smart Token Dispenser**
- You are developing a **Smart Token Dispenser** system, like those found in banks or clinics. This system reset counters based on user activity and needs to run until manually stopped.

**Tasks:**
1. **Create an infinite generator function** called token_dispenser(start=1).
2. On each call to next(), it should yield the current token number and increment it.
3. If a value is passed to the generator using send(), the generator should **reset** the token number to that new value.
4. The generator should handle the .close() method gracefully and print "Dispenser closed." when it is closed.

---
# Code
``` python
def token_dispenser(start: int = 1):
    try:
        current = start
        while True:
            new_value = yield current
            if new_value is not None:
                current = new_value
            else:
                current += 1
    except GeneratorExit:
        print("Dispenser closed")


tokens = token_dispenser()

print(next(tokens))
print(next(tokens))
print(next(tokens))

print(tokens.send(10))

print(next(tokens))
print(next(tokens))
print(next(tokens))

tokens.close()
```

---
