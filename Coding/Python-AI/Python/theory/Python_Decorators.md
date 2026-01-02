# **NOTE**
- Designing decorators requires **importing wraps from functools**.
>**Refer this:**
[[Python_Decorators_functools_wraps]]

---
# What ?
- It adds extra functionality to a function.
![[decorator.excalidraw|500]]

---
# Code: Decorators Design
``` python
def my_decorator(func):
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
**Ouput**:
``` text
Before function runs
Hello from decorators class
After function runs

wrapper
```

---
> **See the output**: It prints wrapper.

---
