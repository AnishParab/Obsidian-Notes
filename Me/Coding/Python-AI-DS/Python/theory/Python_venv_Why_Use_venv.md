# If you don’t use a venv

## 1) Do they need a new environment?

- Yes:
```bash
python -m venv .venv
pip install -r requirements.txt
````

---
## 2) What happens without venv?

- packages install into system Python `site-packages`
- risks:
    - version collisions
    - breaking system tools
    - permission issues (`sudo pip install`)
    - uninstall/upgrade conflicts

---
## 3) Is it bad for the system?

- potentially yes
- bad practice (can cause hard-to-debug issues)

---
