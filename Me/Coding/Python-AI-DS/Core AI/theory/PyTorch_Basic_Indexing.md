# Basic Indexing
- Standard Indexing works just like NumPy.
- It's for selecting uniform "blocks" of data.

---
``` python
x = torch.arange(12).reshape(3, 4)
# tensor([[0, 1, 2, 3],
#         [4, 5, 6, 7],
#         [8, 9, 10, 11]])

# Get the third column (at index 2)
col_2 = x[:, 2]
```

**Output**:
``` text
```

---
