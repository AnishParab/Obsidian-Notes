# Memory (Garbage Collector)
- `username = "Anish"` ---> username is a variable and is referenced to Anish _Object_.
- `username = "Bipin"` ---> Now, username variable is referenced to Bipin _Object_.
- Since _Anish_ is no longer used, **Garbage Collector** deletes it.

---
# Numbers and Strings
- Both of these are treated differently in Python.
- Garbage Collector doesn't collect them immediately.

---
# List
### Example 1
``` python
l1 = [1,2,3]
l2 = l1

l1 = 'chai'
l1 = [1,2,3]

l1[0] = 33

# Hence l1 = [33,2,3]
# Hence l2 = [1,2,3]
```

### Example 2
``` python
l1 = [1,2,3]
l2 = l1

l1[0] = 44

# Hence l1 = [44,2,3]
# Hence l2 = [44,2,3]
```

### Example 3
``` python
p1 = [1,2,3]
p2 = p1

p2 = [1,2,3]

p1[0] = 69

# Hence p1 = [69,2,3]
# Hence p2 = [1,2,3]
```

#### The reason for the behavior in the above given examples is due to referencing.

---
# To avoid the above problem
`:` creates a _copy_.

``` python
h1 = [1,2,3]
h2 = h1[:]

h1[0] = 77

# Hence h1 = [77,2,3]
# Hence h2 = [1,2,3]
```

---
# Proof For the above concept using `is`
``` python
n = [1,2,3]
m = n

m == n     
# Gives True
m is n     
# Also Gives True

m = [1,2,3]

m == n
# Gives True
m is n
# Gives False
```

---


