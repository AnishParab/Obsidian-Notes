# Folder
```
quiz/
├─ quiz/
│  ├─ __init__.py
│  └─ main.py
```

- Hence **quiz** is a package you can import, as `__init__.py` exists.

---
# Run `main.py` as a module
```
python -m quiz.main
```

---
# `main.py`
- Put the program here and expose only one function that runs the quiz.  
- Also guard execution so the module isn’t run automatically when imported.
```python
def run_quiz():
    print("Welcome to my computer quiz")

    while (response := input("Do you want to play?\n").lower()) not in ("yes", "no"):
        print("Please answer yes or no.")

    if response == "no":
        print("Exiting.")
        return

    print("Let's play :)")
    # rest of the quiz goes here


if __name__ == "__main__":
    run_quiz()
```

**Notes:**
- `run_quiz()` contains all logic
- `if __name__ == "__main__":` ensures it executes only when run directly:
``` text
python3 main.py
```
- and not when imported as a module.

---
# `__init__.py`
- Expose `run_quiz` as the public entry point.

```python
from .main import run_quiz

__all__ = ["run_quiz"]
__version__ = "0.1.0"
```

**What this gives you:**
### 1) Importable API

- Anywhere else:
```python
from quiz import run_quiz

run_quiz()
```

### 2) Clean namespace

- Only `run_quiz` shows up as the main public callable.

### 3) Simple version metadata

``` python
import quiz
print(quiz.__version__)
```

---
