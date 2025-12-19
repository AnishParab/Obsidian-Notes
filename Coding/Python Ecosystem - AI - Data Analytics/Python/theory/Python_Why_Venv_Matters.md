# Effects of not creating a Virtual Environment

### 1. Do they need to make a new environment?
- Yes.
- python -m venv .venv (or whatever they name it), then pip install -r requirements.txt.

---
### 2. What happens if they install packages without creating a venv?
- They install everything into their system Python’s site-packages. That can cause real problems depending on the system:

- **Package version collisions**
Installing your versions may overwrite or conflict with packages they already have installed globally.

- **Breaking system tools**
Some OS utilities (macOS, Linux) rely on the system Python environment. Replacing system-level dependencies can cause breakage or unpredictable errors.

- **Permission issues**
They may need sudo to install globally, which increases risk.
If they use sudo pip install …, they're effectively modifying OS files.

- **Uninstall conflicts**
Removing or upgrading packages later can break unrelated software because everything shares the same global site-packages.

---
### 3. Is it “bad for their system”?
- Potentially, yes.
- Not always catastrophic, but it’s bad practice and can cause subtle, time-wasting issues.

---
