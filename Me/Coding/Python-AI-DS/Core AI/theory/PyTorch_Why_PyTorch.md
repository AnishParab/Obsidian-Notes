# Why PyTorch

## 1. Industry Adoption

Used in production and research by organizations such as:
- Tesla, Inc.
- Microsoft
- OpenAI

Adoption at scale implies:
- Proven reliability
- Ecosystem maturity
- Long-term viability

---
## 2. Define-by-Run (Dynamic Graph)

PyTorch builds the computation graph at runtime.

Why this matters:
- Native Python control flow (if/loops)
- Easier debugging
- More flexible research workflows

Common misconception:
> It is “just easier.”  
> Reality: It aligns model definition with actual program execution semantics.

---
## 3. First-Class Autograd

Automatic differentiation is built into tensor operations.

Implication:
- Any differentiable computation can be optimized
- Not restricted to predefined layers

PyTorch enables **general differentiable programming**, not just neural networks.

---
## 4. Strong Research → Production Path

Research flexibility:
- Rapid experimentation
- Transparent computation graphs

Production readiness:
- TorchScript
- ONNX export
- Distributed training support

This reduces rewrite cost between experimentation and deployment.

---
## 5. Hardware Acceleration

- CUDA (NVIDIA GPUs)
- Multi-GPU support
- TPU and accelerator integrations (via ecosystem)

Performance is not an afterthought; it is fundamental to the design.

---
## 6. Ecosystem Depth

Core + Extensions:
- torchvision
- torchaudio
- torchtext
- HuggingFace integration
- Distributed tooling

Large ecosystem → lower integration friction.

---
