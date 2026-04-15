# Tools: deps + requirements

## `pipdeptree`

- shows dependency tree

Install:
```bash
pip install pipdeptree
````

Use:
```bash
pipdeptree
pipdeptree -p matplotlib
```

---
## `pipreqs`

- generates `requirements.txt` by scanning imports

Install:
```bash
pip install pipreqs
```

Use:
```bash
pipreqs .
pipreqs . --force
```

---
# Mental model

- `pip freeze` → everything installed
- `pipdeptree` → dependency graph
- `pipreqs` → packages actually imported

---
