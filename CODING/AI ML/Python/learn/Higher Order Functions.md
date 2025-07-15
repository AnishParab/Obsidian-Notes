Functions that take other functions as arguments, or return functions.

``` python
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func, msg):
    return func(msg)

print(speak(shout, "hello"))
```

---
