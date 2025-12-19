# `split()` in Python (string → list)
- `split()` is a **string method** used to break a string into a **list of substrings** based on a separator.

---
# Basic syntax
```python
string.split(separator=None, maxsplit=-1)
```

---
## 1. Default behavior (most common)

```python
text = "tomato cucumber spinach"
result = text.split()
```

**Output**
```python
["tomato", "cucumber", "spinach"]
```
#### What happens internally
- Splits on **any whitespace** (space, tab, newline)
- Multiple spaces are treated as **one separator**
```python
"  a   b  c ".split()
# ["a", "b", "c"]
```

---
## 2. Splitting using a specific separator
```python
data = "apple,banana,milk"
data.split(",")
```

**Output**
```python
["apple", "banana", "milk"]
```

Important:
- The separator is **removed**
- Exact match is required
```python
"apple, banana".split(",")
# ["apple", " banana"]  ← space preserved
```

---
## 3. Using `maxsplit`
```python
text = "2025-09-16-logs"
text.split("-", 2)
```

**Output**
```python
["2025", "09", "16-logs"]
```

Meaning:
- Split **at most 2 times**
- Remaining string stays intact

---
## 4. Common real-world uses

#### **User input processing**
```python
input_text = "milk bread eggs"
items = input_text.split()
```

#### **CSV-like data**
```python
row = "john,25,engineer"
name, age, job = row.split(",")
```

#### **Command parsing**
```python
command = "git commit -m"
command.split()
```

---
## 5. Common mistakes

#### ❌ Forgetting it works only on strings
```python
my_list.split()  # AttributeError
```

#### ❌ Expecting it to modify the string
```python
text.split()
print(text)  # original string unchanged
```

> Strings are **immutable**.

---
## 6. `split()` vs `rsplit()`

```python
"path/to/file.txt".rsplit("/", 1)
# ["path/to", "file.txt"]
```
- `split()` → from the left
- `rsplit()` → from the right

---
## One-line summary

> `split()` converts a string into a list by cutting it at separators.

---
