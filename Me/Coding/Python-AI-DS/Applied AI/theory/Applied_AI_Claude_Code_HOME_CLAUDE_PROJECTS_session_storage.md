# `~/.claude/projects/`

- Claude Code saves your conversation locally as you work. Each message, tool use, and result is written to a plaintext JSONL file under `~/.claude/projects/`, which enables [rewinding](https://code.claude.com/docs/en/how-claude-code-works#undo-changes-with-checkpoints), [resuming, and forking](https://code.claude.com/docs/en/how-claude-code-works#resume-or-fork-sessions) sessions.
- Before Claude makes code changes, it also snapshots the affected files so you can revert if needed.
- For paths, retention, and how to clear this data, see [application data in `~/.claude`](https://code.claude.com/docs/en/claude-directory#application-data).**Sessions are independent.**
- Each new session starts with a fresh context window, without the conversation history from previous sessions.
- Claude can persist learnings across sessions using [auto memory](https://code.claude.com/docs/en/memory#auto-memory), and you can add your own persistent instructions in [CLAUDE.md](https://code.claude.com/docs/en/memory).

---
