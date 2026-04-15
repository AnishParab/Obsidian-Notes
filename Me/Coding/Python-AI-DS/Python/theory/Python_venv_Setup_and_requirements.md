# venv setup (Linux)

## Create + activate
```bash
python3 -m venv .venv
source .venv/bin/activate
````

Verify:
```bash
echo $VIRTUAL_ENV
```

Upgrade pip:
```bash
pip install --upgrade pip
```

> In venv, use `python` (no need for `python3`).

---
# Dependencies (`requirements.txt`)

Example:
```text
requests==2.31.0
flask==3.0.0
```

Install:
```bash
pip install -r requirements.txt
```

---
