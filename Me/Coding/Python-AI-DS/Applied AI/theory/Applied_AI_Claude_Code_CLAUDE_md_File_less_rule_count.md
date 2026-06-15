# Rule Count

- Keep the file **short** `under ~200 lines`
As instruction count increases, instruction-following quality decreases uniformly.

---
> **If you can't keep the rule count under `200 lines` then follow this strategy:**
###### Split into `.claude/rules/files`
- Topic specific files:
``` css
.claude/rules/
	|- code-style.md
	|- testing.md
	|- security.md
	|- api-conventions.md
```
- Claude now, only refers to the specific file
- Improves maintainabilty

###### Use `@` imports  to reference external docs
- Example
``` md
## API Conventions
See @docs/api-guidelines.md

## Git Workflow
See @docs/contributing.md
```

###### Use subdirectory `CLAUDE.md` files
[[Applied_AI_Claude_Code_CLAUDE_md_Subdirectory_File]]

---
