# First
``` python
import torch

# Simple Python List
data = [[1,2,3], [4,5,6]]

my_tensor = torch.tensor(data)

print(my_tensor)
```

**Output**:
``` text
```

---
# Second
- Creation from a desired shape
``` python
# Input: A shape tuple (2 rows, 3 columns)

ones = torch.ones(shape)
zeros = torch.zeros(shape)
random = torch.randn(shape)

print(f"Random Tensor:\n {random}")
```

**Output**:
``` text
```

---
# Third
- Creation by mimicking another tensor
``` python
# A template tensor
template = torch.tensor([[1,2], [3,4]])

# Create a new tensor with the same properties
randn_like = torch.randn_like(template, dtype=torch.float)

print(f"Template Tensor:\n {template})
print(f"Randn_like Tensor:\n {randn_like})
```

**Output**:
``` text
```

---
