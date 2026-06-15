# How `/init`  works

- Triggers an internal agent that takes over the scanning and writing task
- Agent scans high-signal config files first - `package.json`, `requirements.txt`, `README.md`
- Reads directory tree structure
- Infers tech stack, folder layout, and naming conventions
- Writes `CLAUDE.md` to the project root with the inferred context

---
