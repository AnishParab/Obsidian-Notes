# `CLAUDE.md` Content

- `CLAUDE.md` = context file that tells Claude what it's working in before touching any code
- Lives at project root; read first, every session

##### **Project Context**
- One-paragraph description of what the project is and does
- Claude should never have to guess the domain or purpose
- *Example*:
``` md
This is a FastAPI backend for a health-tracking application that stores patient BMI records and exposes CRUD APIs
```

##### **Architecture**
- Maps responsibilities to directories
- Prevents Claude from putting logic in the wrong layer
- *Example*:
``` md
- Routes live in `routers/`
- Business logic lives in `services/`
- Schemas live in `schemas/`
- Persistence logic lives in `repository/`
```

##### **Code Style**
- Conventions: type hints, naming, function size, patterns to follow
- Claude defaults to its own style without this — enforce yours explicitly
- *Example*:
``` md
- Use Python type hints everywhere
- Prefer Pydantic models for request and response schemas
- Keep functions small and focused
```

##### **Preferred Libraries**
- Locks the toolchain; prevents Claude from introducing unwanted dependencies
- Include hard negatives: "do not use X"
- *Example*:
``` md
- Use FastAPI for APIs
- Use Pydantic for validation
- Use SQLAlchemy for ORM
- Do not introduce new dependencies unless necessary
```

##### **Commands**
- Exact commands for install, run, test, lint, migrate
- No ambiguity — copy-paste ready
- *Example*:
``` md
- Install dependencies: pip install -r requirements.txt
- Run dev server: uvicorn main:app --reload
- Run tests: pytest
```

##### **Critical Rules**
- Hard constraints: files not to touch, IDs not to generate, logic not to move
- Anything where a wrong assumption causes real damage goes here
- *Example*:
```
- Do not modify `database.py` unless absolutely necessary
- Patient IDs are provided by the client; do not auto-generate UUIDs
```

##### **Implemented vs Stub Routes**
- Table or list of all routes with status: implemented / stub / not started
- Rule: never implement a stub unless the active task explicitly targets it
- *Example*:
``` md
| Route         | Status      |
|---------------|-------------|
| POST /patient | Implemented |
| GET /patient  | Stub        |
| DELETE /patient | Not started |
```

##### **Warnings and Things to Avoid**
- Gotchas specific to this codebase
- Anti-patterns that have already caused bugs
- *Example*:
``` md
- Do not use global state in service functions
- Avoid raw SQL outside of repository layer
```

---
