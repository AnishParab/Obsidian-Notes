# Code

``` python
# Check Prime
n = int(input())
if n < 2:
    print("Not Prime")
else:
    print("Not Prime" if any(n % i == 0 for i in range(2, int(n**0.5)+1)) else "Prime")
```

---
