# 1. What problem `attrgetter` actually solves
In Python, many operations need a **function that extracts a value** from each object:
- sorting
- ranking
- grouping
- selecting min / max
- mapping objects to values

The naïve solution is always a `lambda`:
```python
lambda x: x.score
```

`attrgetter` exists to:
- remove boilerplate
- avoid repeated lambdas
- provide faster, intention-revealing code

---
# 2. Mental model (important)
- Think of `attrgetter` as a **precompiled attribute-access function**.
```python
get_score = attrgetter("score")
```

Now:
```python
get_score(obj)
```

is exactly:
```python
obj.score
```

But implemented in **C**, not Python.

---
# 3. Real-world example 1: Leaderboard system (clean version)

### Data model
```python
class Player:
    def __init__(self, username, score, level):
        self.username = username
        self.score = score
        self.level = level
```

### Ranking players by score
```python
from operator import attrgetter

leaderboard = sorted(players, key=attrgetter("score"), reverse=True)
```

Why this is better than lambda:
- instantly readable
- no inline logic
- communicates _“we are ranking by score”_

---
# 4. Real-world example 2: Multi-level sorting (very common)

> Sort by **level first**, then **score**, then **username**

```python
sorted(players, key=attrgetter("level", "score", "username"))
```

What Python actually compares:
```python
(level, score, username)
```

Why this matters:
- avoids writing tuple lambdas
- no accidental ordering bugs
- identical behavior to SQL `ORDER BY`

---
# 5. Real-world example 3: Nested domain objects (important)

### Data model
```python
class Profile:
    def __init__(self, reputation):
        self.reputation = reputation

class User:
    def __init__(self, name, profile):
        self.name = name
        self.profile = profile
```

### Sort users by reputation
```python
sorted(users, key=attrgetter("profile.reputation"))
```

Equivalent lambda:
```python
lambda u: u.profile.reputation
```

This is **extremely common** in:
- ORM objects
- API SDKs
- Clean architecture layers

---
# 6. Real-world example 4: `min`, `max`, not just `sorted`

### Highest reputation user
```python
top_user = max(users, key=attrgetter("profile.reputation"))
```

### Lowest latency service
```python
fastest = min(services, key=attrgetter("latency_ms"))
```

Rule:
> Any function that accepts `key=` can use `attrgetter`.

---
# 7. Real-world example 5: `groupby` (advanced but realistic)

```python
from itertools import groupby
from operator import attrgetter

# must be sorted first
users.sort(key=attrgetter("country"))

for country, group in groupby(users, key=attrgetter("country")):
    print(country, list(group))
```

This pattern appears in:
- analytics pipelines
- reporting code
- data processing tools

---
# 8. Why `attrgetter` is faster (but don’t overhype it)

- `lambda x: x.attr` → Python bytecode
- `attrgetter("attr")` → C-level attribute lookup

Difference:
- negligible for small lists
- noticeable in tight loops / large datasets
- **main value is clarity**, not micro-optimizations

---
# 9. Common mistakes (important)

### ❌ Using it with dicts
```python
attrgetter("score")(my_dict)  # WRONG
```

Reason:
```python
my_dict.score  # invalid
```

Use `itemgetter` for dicts.

---
### ❌ Expecting defaults

```python
attrgetter("age")(obj)  # raises AttributeError if missing
```

`attrgetter` does **not** support:
- defaults
- fallbacks
- conditionals

Use `lambda` if uncertainty exists.

---
# 10. When `attrgetter` is the right choice
Use it when:
- data is object-oriented
- access is simple and direct
- no transformation is needed
- readability matters

Avoid it when:
- logic exists
- validation is required
- attribute may not exist

---
# 11. One-sentence summary (accurate)
- `attrgetter` is a **clean, fast, intention-revealing way to extract object attributes**, mainly used for sorting, ranking, grouping, and selection.

---
