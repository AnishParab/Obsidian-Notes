# Example (Decorators)
``` python
from functools import wraps

def my_decorator(func):
	@wraps(func) # Using functool to preserve metadata - greet
	def wrapper():
		print("Before function runs")
		func()
		print("After function runs")
	return wrapper()
	
@my_decorator
def greet():
	print("Hello from decorators class from chaicode")
	
greet()
print(greet.__name__)
```

**Output**:
``` text
Before function runs
Hello from decorators class from chaicode
After function runs

wrapper # If functool is not used

greet # If functool is used
```

---
