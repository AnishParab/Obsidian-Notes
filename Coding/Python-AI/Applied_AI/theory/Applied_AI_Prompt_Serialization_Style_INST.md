# INST Format
- **INST** is the **instruction-tuning prompt format** used by **LLaMA / LLaMA-2 instruction models**.  
- It wraps the instruction and optional input inside special tokens so the model can clearly distinguish **what to do** from **what to answer**.

- It is **not role-based** like ChatML.  
- It is **not fully flat** like Alpaca either.

---
# Core Structure (LLaMA-2)

```text
<s>[INST] <INSTRUCTION> [/INST] <RESPONSE> </s>
```

With optional input:
```text
<s>[INST] <INSTRUCTION>

<INPUT> [/INST]
```

The model generates the **response after `[/INST]`**.

---
# Key Tokens Explained

| Token     | Meaning                    |
| --------- | -------------------------- |
| `<s>`     | Start of sequence          |
| `</s>`    | End of sequence            |
| `[INST]`  | Start of instruction block |
| `[/INST]` | End of instruction block   |

Everything **inside `[INST] ... [/INST]` is user intent**.  
Everything **after `[/INST]` is assistant output**.

---
# Example: Simple Instruction

```text
<s>[INST] Explain recursion simply. [/INST]
```

Model generates:
```text
Recursion is a technique where a function calls itself...
</s>
```

---
# Example: Instruction + Input

```text
<s>[INST]
Translate the following sentence to French.

Sentence: "I love programming."
[/INST]
```

---
# Multi-Turn (Flattened)

LLaMA-2 does **not truly support roles**.  
Conversation history is **manually concatenated**:

```text
<s>[INST] Hello [/INST] Hi there! </s>
<s>[INST] What is a mutex? [/INST]
```

Each turn is a **new sequence**.

---
# Why INST Exists
- Optimized for **instruction-following**
- Simple and efficient for **fine-tuning**
- Clear boundary between **instruction** and **response**
- Lower overhead than ChatML
- Works well with **single-turn and short context tasks**

---
# When to Use INST

Use INST when:
- Working with **LLaMA / LLaMA-2 instruction models**
- Doing **instruction fine-tuning**
- Running **single-turn inference**
- Building **synthetic datasets**
- You don’t need strong role separation

Avoid INST when:
- You need **system-level priority**
- You rely on **multi-role safety controls**
- You need **tool calling**
- You need long conversational memory

---
