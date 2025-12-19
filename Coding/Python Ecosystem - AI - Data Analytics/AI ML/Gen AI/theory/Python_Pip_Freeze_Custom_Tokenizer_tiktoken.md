# `requirements.txt`

Run `pip install tiktoken`
- `tiktoken` is a package made by **OpenAI**.
- To tokenize and detokenize a text.
### **pip freeze**
Run `pip freeze > requirements.txt`
- pip freeze > requirements.txt saves a list of all currently installed Python packages and their exact versions into a file named requirements.txt.

---
# Code (Tokenizer) - `main.py`
``` python
import tiktoken

# encoder
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! My name is Anish Parab"
tokens = enc.encode(text)

print("Tokens:", tokens)

```

**Output**
``` text
Tokens [25216, 1354, 1073, 3673, 1308, 382, 1689, 1109, 3371, 378]
```

---
# Code (Detokenizer) - `main.py`
``` python
decoded = enc.decode([25216, 1354, 1073, 3673, 1308, 382, 1689, 1109, 3371, 378])

print("Decoded", decoded)
```

**Output**
``` text
Decoded Hey there ! My name is Anish Parab
```

---
