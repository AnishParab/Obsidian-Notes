# Find which Python you are using

Show Python path:
```bash
which python
````

Show all `python` found in `$PATH`:
- example: Shows python _3.14_ and _3.13_.
```bash
which -a python
```

Show the actual file behind symlinks:
```bash
readlink -f "$(which python)"
```

Inspect what `python` really is:
```bash
ls -l "$(which python)"
file "$(which python)"
```

---
# Check PATH / env

```bash
echo $PATH
```

Show shell command resolution:
```bash
type -a python
command -v python
```

---
## Python runtime info

Python executable path:
```bash
python -c "import sys; print(sys.executable)"
```

Python version:
```bash
python -V
python --version
```

Where site-packages are:
```bash
python -m site
python -c "import site; print(site.getsitepackages())"
python -c "import site; print(site.getusersitepackages())"
```

---
# pip basics

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
# Common file locations (Arch)

System Python:
- executable: `/usr/bin/python`
- stdlib: `/usr/lib/pythonX.Y/`
- site-packages: `/usr/lib/pythonX.Y/site-packages/`

User installs (pip --user):
- packages: `~/.local/lib/pythonX.Y/site-packages/`
- scripts: `~/.local/bin/`

Virtualenv:
- venv folder: `./venv/`
- python: `./venv/bin/python`
- pip: `./venv/bin/pip`

---
# Package manager ownership (Arch)

Check which package installed a file:
```bash
pacman -Qo /usr/bin/python
```

List files installed by a package:
```bash
pacman -Ql python
```

---
# Troubleshooting quick checks

Confirm which Python + pip pair you are using:
```bash
which python
python -c "import sys; print(sys.executable)"
python -m pip --version
```

---
