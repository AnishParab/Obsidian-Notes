# Example: Dictionary Comprehension
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

---
### Explanation:

* `.items()` returns pairs of tea names and their prices in INR.
* `{tea: price / 80 for tea, price in tea_prices_inr.items()}`:
  * Iterates through each tea-price pair.
  * Divides the price by 80 to convert to USD.
  * Builds a new dictionary with updated prices.

---
