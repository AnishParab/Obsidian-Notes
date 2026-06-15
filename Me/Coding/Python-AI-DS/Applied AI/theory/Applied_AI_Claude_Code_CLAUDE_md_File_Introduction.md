# Why do we need `CLAUDE.md` file ?

- LLM's do not have memory
- Claude code can't remember things from previous sessions
- Need to repeat instructions across sessions
- Repeating instructions is cumbersome and error prone
- Leads to inconsistent code generation

---
# What is `CLAUDE.md` file ?

- The `CLAUDE.md` file is a special project-level instruction file used by Claude Code to guide how it behaves while working on your codebase.
- Think of it as a persistent system prompt for your project.

- Instead of repeatedly telling Claude:
	- how your project is structured
	- coding conventions
	- how to run / build / test
	- what tools to use
	we put all of that into this file, and Claude automatically uses it as context everytime.

---
