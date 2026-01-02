# What are tokens?
**Tokens** are the **basic units of text** that a language model processes.

A token can be:
- A **character**
- A **subword**
- A **word**
- Or even **punctuation / whitespace**

---
# Definition
> Tokens are **numerical representations of text units** obtained by converting text into discrete pieces using a tokenizer.

---
# What actually happens

> _Text is first split into tokens, then tokens are mapped to numbers (token IDs)._

So the pipeline is:
```
Text → Tokenizer → Tokens → Token IDs → Model
```

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
# Why tokens matter
- Models **do not see text**, only numbers
- Token count affects:
    - Context length
    - Cost
    - Performance
- Different models tokenize differently

---
