# Step 1

``` bash
pip install --upgrade transformers
```

---
# Step 2

``` python
from transformers import AutoTokenizer
import os

os.environ["HF_TOKEN"] = "your_api_key"

tokenizer = AutoTokenizer.from_pretained("google/gemma-3-1b-it")
tokens = tokenizer("Hey There!", return_tensor="pt")
print(tokens)
```

---
# Step 3

``` python
import torch
from transformers import AutoModelForCausalLM

model = AutoModelForCausallLM.from_pretrained("google/gemma-3-1b-it", torch_dtype=torch.bfloat16)
```

---
# Step 4

``` python
out = model(input_ids=input_tokens["input_ids"])
print(out)

gen_out = model.generate(input_ids=input_tokens["input_ids"], max_new_tokens=100)
print(gen_out)

tokenizer.batch_decode(gen_out)
```

---
