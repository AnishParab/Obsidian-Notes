# Tokens

 >Basic units of text a model processes — can be a char, subword, word, or punctuation
 
- Tokens are text units converted to numbers (token IDs) via a tokenizer
- Pipeline: `Text → Tokenizer → Tokens → Token IDs → Model`

 > Models see only numbers, never raw text

**Why it matters**:
- Token count drives context length, cost, and performance
- Tokenization differs across models

---
# Example

Text:
```
"ChatGPT is powerful"
```

Possible tokenization:
```
["Chat", "GPT", " is", " powerful"]
```

Mapped to IDs:
```
[1234, 5678, 42, 8910]
```

---
