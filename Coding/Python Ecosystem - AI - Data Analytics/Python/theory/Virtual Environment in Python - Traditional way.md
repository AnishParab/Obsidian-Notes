# Environment Isolation
- Python virtual environment creates a **self-contained directory tree** that houses its own interpreter, libraries, and scripts. This isolation solves a fundamental problem in software engineering known as **dependency collision** — where two projects require incompatible versions of the same package.

In theory, this is similar to creating a **miniature operating system** inside your system, governed by the same Python interpreter rules but insulated from the rest of the machine.  
You could think of it as a _namespaced dependency universe_.

Formally:
- Each virtual environment contains:
    - A copy (or symlink) of the Python binary.
    - A private `site-packages/` directory for dependencies.
    - Metadata (like `pyvenv.cfg`) pointing to its base interpreter.

This setup ensures **dependency determinism** — your project’s behavior no longer depends on the global system state, only on what’s inside that environment.

---
# Setup for Mac and Linux
``` 
python3 -m venv .venv
```

- Activate virtual environment
``` bash
source .venv/bin/activate
```

``` bash
echo $VIRTUAL_ENV
```

``` bash
nvim requirements.txt
```

####### `requirements.txt`
``` text
requests==2.31.0
flask==3.0.0
```

``` bash
pip install -r requirements.txt
```

``` bash
mkdir src
```

---
# Note : While shipping the Project
 - Put `.venv` into `.gitignore`.

 ``` bash
 deactivate
 ```

- Now, delete `.venv`

- Now, the developers have to install a fresh copy using `requirements.txt`, by creating a new environment.

---

