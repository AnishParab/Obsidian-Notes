# Building The Graph
**Goal: Compute z = x.y , where y = a + b.**

``` python
import torch

# Three parameter tensors
a = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(3.0, requires_grad=True)
c = torch.tensor(4.0, requires_grad=True)

# PyTorch automatically a new node for add operation which creates a new tensor y = 5.0
y = a + b

# Another tensor created
z = x * y
```

---
# Proof that the Graph Exists
`.grad_fn`
- Think of it as a breadcrumb, pointing to the function that created it.

``` python
# z was created by multiplication
print(f"grad_fn for z: {z.grad_fn}")

# y was created by addition
print(f"grad_fn for y: {y.grad_fn}")

# a was created by the user, not an op
# result is None since created by user
print(f"grad_fn for a: {a.grad_fn}")
```

---
