# What is a Context Window ?

- A contexrt window is the amount of information (tokens) that a model like Claude Code can see and remember at one time while generating a response.
- Think of it as model's working memory.
- Context is all the information available to understand something correctly.

---
> **Context Window**: The maximum amount of context the model can hold at once.

---
# Claude Code's Context Window

- Claude code has a context window of `200k tokens` - *for Sonnet*
- *for Opus* -> `1 million`

---
# IMPORTANT NOTES

- Each new session starts with a fresh context window
- Tokens are consumed by both your messages and Claude's replies
- Claude's replies consume roughly `6x` more tokens than your messages
- Every request sends the entire conversation history from scratch.
- Sub-agents get their own isolated context window completely separate from the main session
- Sub-agents return only a summary to the main context, not their full working history

---
