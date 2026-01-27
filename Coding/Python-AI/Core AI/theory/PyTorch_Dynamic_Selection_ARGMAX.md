# Dynamic Selection
- Finds the Index of the highest value.
- This is how you find a model's final prediction.

---
``` python
scores = torch.tensor([
	# Best score is at index 3
	[10, 0, 5, 20, 1]
	# Best score is at index 1
	[1, 30, 2, 5, 0]
])

# Find the index of the best score for each
best_indices = torch.argmax(scores, dim=1)
```

**Output**:
``` text
```

---
