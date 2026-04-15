# ChatML
- **ChatML (Chat Markup Language)** is a **role-based message format** used to represent multi-turn conversations for chat-oriented LLMs.  
- Each message is explicitly tagged with a **role** and **content**, preserving conversational structure and priority.

---
# Core Structure

A ChatML conversation is a **list of messages**.

```json
messages = [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Explain recursion."},
  {"role": "assistant", "content": "Recursion is a function calling itself..."}
]
```

---
# Roles in ChatML

| Role                     | Purpose                                    |
| ------------------------ | ------------------------------------------ |
| `system`                 | Sets behavior, rules, persona, constraints |
| `user`                   | User input or query                        |
| `assistant`              | Model-generated response                   |
| `tool` _(optional)_      | Output from tools/functions                |
| `developer` _(optional)_ | App-level instructions (API-specific)      |

**Priority order (highest → lowest):**  
`system` → `developer` → `user` → `assistant`

---
# Why ChatML Exists
- Enforces **instruction hierarchy**
- Enables **multi-turn conversations**
- Preserves **context and memory**
- Supports **tool calling and function execution**
- Safer and more controllable than flat prompts

---
# Example: ChatML vs Flat Prompt

**ChatML**
```json
[
  {"role": "system", "content": "Answer concisely."},
  {"role": "user", "content": "What is a mutex?"}
]
```

**Flat prompt**
```text
Answer concisely. What is a mutex?
```

ChatML keeps **intent and control explicit**.

---
# When to Use ChatML

Use ChatML when:
- Building **chatbots**
- You need **conversation memory**
- You want **strong system control**
- You use **tools / function calling**
- You care about **instruction precedence**

Avoid ChatML when:
- Creating **instruction datasets**
- Doing **single-shot fine-tuning**
- You want **minimal prompt overhead**
- You don’t need conversation history

---
