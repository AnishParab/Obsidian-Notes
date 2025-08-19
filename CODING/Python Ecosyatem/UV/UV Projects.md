- No need of _virtual environments_ and `requirements.txt`.

``` bash
pip install uv
```

---
# Analogy
- _UV_ is like `npm`.

---
# Project Init
``` bash
uv init project-name

cd project-name
```

---
# Files
- `git ignore`
- `python version`
- `pyproject.toml` ---> Project Structure and Meta Data ---> Like _package.json_
- `README.md`

---
# Project Run
``` bash
uv run main.py
```
- This creates a virtual environment at `.venv`.
- `uv.lock` ---> This is like _package.lock_

---
# Adding Package
### Fast API
``` bash
uv add fastapi
```

---
# Distribute
``` bash
uv build
```

---
# Help
``` bash
uv
```

---





