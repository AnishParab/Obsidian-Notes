# Install

- Uses HuggingFace `transformers` + PyTorch to tokenize and run inference on a pretrained model

Install:
```bash
pip install transformers
```

---
# Code

```python
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

os.environ["HF_TOKEN"] = "your_api_key"

# Load tokenizer for the model
tokenizer = AutoTokenizer.from_pretained("google/gemma-3-1b-it")

# Tokenize input text → returns input_ids as PyTorch tensors
input_tokens = tokenizer("Hey There!", return_tensor="pt")
print(input_tokens)

# Load the model in bfloat16 (memory efficient)
model = AutoModelForCausallLM.from_pretrained("google/gemma-3-1b-it", torch_dtype=torch.bfloat16)

# Raw forward pass → returns logits
out = model(input_ids=input_tokens["input_ids"])
print(out)

# Autoregressive generation → returns token IDs
gen_out = model.generate(input_ids=input_tokens["input_ids"], max_new_tokens=100)
print(gen_out)

# Decode token IDs back to text
tokenizer.batch_decode(gen_out)
```

---
