# Syntax
``` python
def decorator(func):
    def wrapper():
        print("Before call")
        func()
        print("After call")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()
```

---
# Output
``` pgsql
Before call
Hello!
After call
```

---
