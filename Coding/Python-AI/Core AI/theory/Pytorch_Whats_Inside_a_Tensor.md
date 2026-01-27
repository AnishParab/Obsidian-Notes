# 3 Attributes: Shape, DataType, Device
- You will use this constantly for **debugging**.

``` python
tensor = torch.randn(2, 3)

print(f"Shape: {tensor.shape}")
print(f"DataType: {tensor.dtype}")
print(f"Device: {tensor.device}")
```

---
> 90% of your errors in PyTorch will be shape mismatches.

> Tensor lives in **CPU** or **cuda(GPU)**

> Default datatype is **float32**

---
# Why `float32` as Default
- Because of **Gradients**.
- Model parameters (weights, biases) **MUST** be a float type.
- **float32** is the standard.

---
> Data that represents categories or counts can be integers.

---
