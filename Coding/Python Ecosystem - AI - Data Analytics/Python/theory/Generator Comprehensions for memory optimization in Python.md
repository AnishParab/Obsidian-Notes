---

---
# Difference: List vs Generator Comprehension

**List Comprehension**:
  `[x for x in items]`
  * Creates the entire list in memory.
  * Suitable when you need to reuse or index the collection.

**Generator Comprehension**:
  `(x for x in items)`
  * Produces items one at a time (lazy evaluation).
  * Memory efficient, useful for large datasets or streaming.

---
# Example: Generator Comprehension
```python
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# Create a generator to filter sales greater than 5
total_cups = (sale for sale in daily_sales if sale > 5)

print(total_cups)
```

**Output:**
```text
<generator object>
```

---
### Consuming the Generator
Since the generator yields items one by one:
```python
# Calculate the total in a memory-efficient way
total_cups = sum(sale for sale in daily_sales if sale > 5)
```

**Output:**
```text
61
```

---
### Why Use a Generator?
* No list is stored in memory.
* Ideal for operations like `sum()`, `max()`, or iterating once through large datasets.

---
