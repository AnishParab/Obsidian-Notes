# Problem Statement

- `prices = [7, 1 , 5, 3, 6, 4]`
- Indexes are *days* -> `1,2,3,4,5,6`
###### Solution
- Output = `max_profit = 6 - 1 = 5` = `proces[i] - min_price`

---
# Code

``` python
prices = [7, 1, 5, 3, 6, 4]


def find_max_profit(prices):
    min_price = float("inf")
    max_profit = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit


max_profit = find_max_profit(prices)

print("The maximum profit to buy and sell stock is", max_profit)
```

---
**Time complexity**: $O(n)$
**Space Complexity**: $O(1)$

---
