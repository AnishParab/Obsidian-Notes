# Data v/s Parameters
``` python
# A standard data tensor
x_data = torch.tensor([1., 2.], [3., 4.])

# A parameter tensor (We need Gradients)
w = torch.tensor([[1.0], [2.0]], requires_grad=True)

print(f"Data tensor requires_grad: {x_data.requires_grad}")
print(f"Parameter tensor requires_grad: {w.requires_grad}")
```

**Output**:
``` text
```

---
