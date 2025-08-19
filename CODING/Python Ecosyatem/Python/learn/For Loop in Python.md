``` python
for variable in iterable:
    # do something
```
An _Iterable_ can be `list`, `tuple`, `dict`, `string`, `range`.

---
# `else` with `for`

``` python
for x in range(5):
    if x == 3:
        break
else:
    print("Loop completed without break")
```

---
# Example
``` python
# Sum of even number
n = 10
sum_even = 0

for i in range(1, n+1):
	if i%2 == 0:
		sum_even += 1

print("sum of even number is", sum_even)
	
```

---
# Question
**Create an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries**.
``` python
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
	print("Attempt", attempts+1, "- wait_time",)
	time.sleep(wait_time)
	wait_time *= 2
	attempts += 1
```

---







