# Common List Methods and Operations

### 1. `append()` → Add an element to the end

```python
ingredients.append("sugar")
print(f"Ingredients: {ingredients}")
```

**Output:** `['water', 'milk', 'black tea', 'sugar']`

---
### 2. `remove()` → Remove the first matching element

```python
ingredients.remove("water")
print(f"Ingredients: {ingredients}")
```

**Output:** `['milk', 'black tea', 'sugar']`

---
### 3. `extend()` → Add multiple elements from another list

```python
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]
chai_ingredients.extend(spice_options)
print(f"Chai: {chai_ingredients}")
```

**Output:** `['water', 'milk', 'ginger', 'cardamom']`

---
### 4. `insert()` → Add an element at a specific position

```python
chai_ingredients.insert(2, "black tea")
print(f"Chai: {chai_ingredients}")
```

**Output:** `['water', 'milk', 'black tea', 'ginger', 'cardamom']`

---
### 5. `pop()` → Remove and return the last element

```python
last_added = chai_ingredients.pop()
print(last_added)
print(f"Chai: {chai_ingredients}")
```

**Output:**
```
cardamom
Chai: ['water', 'milk', 'black tea', 'ginger']
```

---
### 6. `reverse()` → Reverse the list

```python
chai_ingredients.reverse()
print(f"Chai: {chai_ingredients}")
```

**Output:** `['ginger', 'black tea', 'milk', 'water']`

---
### 7. `sort()` → Sort items alphabetically or numerically

```python
chai_ingredients.sort()
print(f"Chai: {chai_ingredients}")
```

**Output:** `['black tea', 'ginger', 'milk', 'water']`

---
### 8. `max()` and `min()` → Find highest and lowest values

```python
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")
```

**Output:**
```
Maximum sugar level: 5
Minimum sugar level: 1
```

---
# Summary Table

| Method             | Description           | Example              | Result               |
| ------------------ | --------------------- | -------------------- | -------------------- |
| `append(x)`        | Add one element       | `lst.append(4)`      | Adds `4` at end      |
| `extend(iterable)` | Add multiple elements | `lst.extend([5,6])`  | Adds `5`, `6`        |
| `insert(i, x)`     | Insert at index       | `lst.insert(1, "a")` | Adds at position `1` |
| `remove(x)`        | Remove value          | `lst.remove("a")`    | Deletes first `"a"`  |
| `pop([i])`         | Remove by index       | `lst.pop()`          | Removes last         |
| `reverse()`        | Reverse order         | `lst.reverse()`      | Reverses in-place    |
| `sort()`           | Sort elements         | `lst.sort()`         | Alphabetic/numeric   |
| `max(lst)`         | Largest value         | `max([1,2,3])`       | `3`                  |
| `min(lst)`         | Smallest value        | `min([1,2,3])`       | `1`                  |

---
