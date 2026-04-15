# `wraps` from `functools`
- When a function is decorated, the original function is **replaced** by the wrapper function.  
- By default, this causes the decorated function to **lose its original identity**.

---
> **See the output**: It prints greet

---
# Example: Decorators
``` python
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")

    return wrapper


@my_decorator
def greet():
    print("Hello from decorators class")


greet()

print()

print(greet.__name__)
```

**Output**:
``` text
Before function runs
Hello from decorators class from chaicode
After function runs

greet
```

---
