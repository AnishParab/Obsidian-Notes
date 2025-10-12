# Strings
- Strings are **immutable**.

---
# Code
``` python
chai_type = "Ginger chai"
```

### Indexing
- Indexing starts with `0`.
- `G` ---> `0`
- `i` ---> 1

### First Word
``` python
chai_type = "Ginger chai"

print(f"First word: {chai_type[0:6]}")
```
- `6` is not inclusive.
- You can also use `[:6]` to make it look cool.

### Note
- `0:6:2` ---> This gives every second character.

### Last Word
``` python
chai_type = "Ginger chai"
print(f"First word: {chai_type[7:11]}")
```

---
# Reverse a String
``` python
print(f"First word: {chai_type[::-1]}")
```

---
# Encode a String
``` python
label_text = "Any language string"
encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
```

---
