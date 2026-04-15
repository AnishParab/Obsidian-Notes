# What ?
- `itemgetter` is a utility from Python’s standard library module `operator`. It is used to **extract items from indexable objects** (lists, tuples, strings, dictionaries) and is commonly used as a **key function** in sorting and grouping.

---
# Import
```python
from operator import itemgetter
```

---
# Basic usage (single index)
```python
data = [10, 20, 30]

get_second = itemgetter(1)
print(get_second(data))   # 20
```

Equivalent to:
```python
data[1]
```

---
# Multiple indices
```python
data = (10, 20, 30, 40)

get_items = itemgetter(1, 3)
print(get_items(data))    # (20, 40)
```

---
# With dictionaries
```python
person = {"name": "Alice", "age": 25}

get_age = itemgetter("age")
print(get_age(person))    # 25
```

---
# Sorting **(most common use)**

### Sort list of tuples
```python
students = [
    ("Alice", 85),
    ("Bob", 72),
    ("Charlie", 90)
]

students.sort(key=itemgetter(1))
print(students)
```

Output:
```python
[('Bob', 72), ('Alice', 85), ('Charlie', 90)]
```

---
### Sort by multiple keys
```python
records = [
    ("Alice", "Math", 85),
    ("Alice", "Science", 90),
    ("Bob", "Math", 80)
]

records.sort(key=itemgetter(0, 1))
```

Sorts by **name first**, then **subject**.

---
## `itemgetter` vs lambda

```python
# Using lambda
sorted(students, key=lambda x: x[1])

# Using itemgetter (faster + cleaner)
sorted(students, key=itemgetter(1))
```

> **`itemgetter` is implemented in C, so it is slightly faster and more readable for simple indexing.**

---
## When to use
- Sorting lists of tuples or dicts
- Extracting fixed positions repeatedly
- Cleaner alternative to `lambda x: x[i]`

---
## When not to use
- Complex logic → use `lambda` or a normal function
- Attribute access → use `attrgetter` instead

---
