# Requirements
``` bash
pip install tiktoken
```

---
# Code: Encoding and Decoding
``` python
import tiktoken

text = "Hello there! How are you ?"

# Encoder
enc = tiktoken.encoding_for_model("gpt-4o")

tokens = enc.encode(text)
print(tokens)

decoded = enc.decode([13225, 1354, 0, 3253, 553, 481, 1423])
print(decoded)
```

---
