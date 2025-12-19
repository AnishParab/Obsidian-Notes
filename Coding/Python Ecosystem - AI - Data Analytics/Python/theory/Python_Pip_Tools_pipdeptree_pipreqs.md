# `pipdeptree`
- Get the dependency tree of a particular package or all the packages.
- **Installation**
``` bash
pip install pipdeptree
```
- **Get full dependency tree**
``` bash
pipdeptree
```
- **Get package-specific dependency tree**
``` bash
pipdeptree -p matplotlib
```

---
# `pipreqs`
- Generates `requirements.txt` by **scanning source code**
- Lists only **imported packages**
- Ignores unused installed dependencies
- **Installation**
```bash
pip install pipreqs
```
- **Generate** `requirements.txt`
```bash
pipreqs .
```
- **Overwrite Existing File**
```bash
pipreqs . --force
```

---
# Key Difference (Mental Model)
- `pip freeze` → everything installed
- `pipdeptree` → how installed packages depend on each other
- `pipreqs` → what the project actually uses

---
