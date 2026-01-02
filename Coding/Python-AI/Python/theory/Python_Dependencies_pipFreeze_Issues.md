---

---
# Case Study (Sometimes)
- Installed `numpy`, `matplotlib`, `seaborn` inside a **virtual environment**
- Ran `pip freeze`
- But......`requirements.txt` contained **many extra packages**

```txt
absl-py==2.3.1
anyio==4.11.0
argon2-cffi==25.1.0
...
```

---
# Reason
- Many libraries install **transitive dependencies**
- `pip freeze` lists **everything installed**, not just what you requested

---
# Solution (Manual Filtering)
```bash
pip freeze | grep -E '^(numpy|matplotlib|seaborn|pandas|scipy)=' > requirements.txt
```

---
> **Transitive dependencies** will still be installed automatically by `pip`

---
# When This Approach Is Acceptable
- Small projects
- Learning / experimentation
- You know exactly what you installed

---
