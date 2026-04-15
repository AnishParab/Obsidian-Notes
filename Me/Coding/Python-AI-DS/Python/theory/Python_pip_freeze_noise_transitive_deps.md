---

---
# Case study: `pip freeze` is noisy
## What happened
- installed: `numpy`, `matplotlib`, `seaborn` (in venv)
- `pip freeze` added many extra packages

---
## Why
- libraries pull transitive dependencies
- `pip freeze` lists everything installed

---
## Manual filtering
```bash
pip freeze | grep -E '^(numpy|matplotlib|seaborn|pandas|scipy)=' > requirements.txt
````

> transitive deps will still be installed by `pip`

---
## OK for
- small projects
- learning/experiments
- controlled installs

---
