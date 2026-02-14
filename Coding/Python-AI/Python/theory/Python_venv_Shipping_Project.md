# Project structure + sharing

## `src/`
```bash
mkdir src
````

- keeps code separate from tooling/config

---
# Shipping the project

- add `.venv/` to `.gitignore`
- don’t commit `.venv`

Remove venv before sharing:
```bash
deactivate
rm -rf .venv
```

- others recreate env using `requirements.txt`

---
