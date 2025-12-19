# Project Structure
```bash
mkdir src
```

- **src** allows us to keep the code-base separated from tooling requirements. 

---
# Shipping the Project
- Add `.venv` to `.gitignore`
- Do **not** commit `.venv`
- Deactivate and delete before sharing:

```bash
deactivate
rm -rf .venv
```

- Other developers recreate the env using `requirements.txt`

---
