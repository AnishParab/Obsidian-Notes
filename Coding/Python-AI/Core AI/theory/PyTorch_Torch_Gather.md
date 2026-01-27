> Standard indexing: Column 2 for all rows.

> But what if you need something specific?

---
# Code
- From row 0, get the element at comlumn 2.
- From row 1, get the element at comlumn 0.
- From row 2, get the element at comlumn 3.

> For loop would be slow.

> torch.gather() does this in one highly optimized operation.

``` python
data = torch.tensor([
	[10, 11, 12, 13], # row 0
	[20, 21, 22, 23], # row 0
	[30, 31, 32, 33], # row 3
])

# Our shopping list of which column to get from each row
indices_to_select = torch.tensor([[2], [0], [3]])

# Gather from 'data' along dim=1 (the columns)
selected_values = torch.gather(data, dim=1, index=indices_to_select)
```

---
