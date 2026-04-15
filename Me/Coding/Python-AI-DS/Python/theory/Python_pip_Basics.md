# `pip`Basics

Check pip + which Python it belongs to:
```bash
python -m pip --version
```

List installed packages:
```bash
python -m pip list
```

Show package info:
```bash
python -m pip show <pkg>
```

Show where a package is installed:
```bash
python -c "import <pkg>; print(<pkg>.__file__)"
```

---
