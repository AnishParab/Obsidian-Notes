# Ollama v/s Claude Code

**Core distinction:** Claude Code is an _agent harness_, not a chat UI.

| Feature          | Direct Ollama | Claude Code + Ollama |
| ---------------- | ------------- | -------------------- |
| Orchestration    | You           | Claude Code          |
| File Read/Write  | ✗             | ✓                    |
| Shell Execution  | ✗             | ✓                    |
| Multi-step Tasks | Manual        | Automated            |

- **Mental model:** Ollama provides the _reasoning engine_. Claude Code provides the _scaffolding_ — planning loop, tool calls, codebase context, git ops.

- Direct Ollama = you are the agent. Claude Code + Ollama = you have an agent.

- **Requirement:** Model must support tool calling + 64K+ context window.

---
