# Alpaca Prompts
- Alpaca prompting is a **structured single-prompt format** used to guide LLMs without relying on chat roles.

### Format
Instruction: <SYSTEM_PROMPT>
Input: <USER_QUERY>
Response:

---
# Convert your prompt to **Alpaca-style prompting**

### Original (chat-style)
```python
messages=[
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Bro project zalo re?"},
]
```

### Alpaca-style equivalent (single prompt)
```text
### Instruction:
<SYSTEM_PROMPT>

### Input:
Bro project zalo re?

### Response:
```

That’s it.  
Alpaca style **flattens roles into a single structured prompt**.

---
# Why Alpaca style exists
- Easier to generate synthetic data
- Easier to fine-tune models
- Works well with instruction-following models

---
# When to use it ?

Use Alpaca style when:
- Creating **instruction datasets**
- Doing **fine-tuning**
- Running **single-shot inference**
- You don’t need multi-turn memory

Avoid Alpaca style when:
- You need strict role separation
- You rely on system-message priority
- You need conversation state

---
