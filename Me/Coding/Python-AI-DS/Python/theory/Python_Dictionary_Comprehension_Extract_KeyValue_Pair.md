# Syntax
``` python
{expression for item in iterable if condition}
```
**where**
``` text
expression = key: value
```

> **NOTE**: Dictionary and set, both use `{}`, but the difference is the expression is stored as a **key: value** pair instead of **unique** values.

---
# Example
```python
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

# Convert prices from INR to USD (assuming 1 USD = 80 INR)
tea_prices_usd = {tea: price / 80 for tea, price in tea_prices_inr.items()}

print(tea_prices_usd)
```

**Output:**
```python
{'Masala Chai': 0.5, 'Green Tea': 0.625, 'Lemon Tea': 2.5}
```
### Explanation:
![[dictionary_comprehension.excalidraw|500]]

---
