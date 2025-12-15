# Case Study (Happens Sometimes and NOT Always)
- I had installed `matplotlib`, `numpy` and `seaborn` using **pip** in a **virtual environment**
- I used `pip freeze` command after installing the above dependencies.
- But then, my `requirements.txt` file looked something like this...

`requirements.txt`
``` txt
absl-py==2.3.1
anyio==4.11.0
argon2-cffi==25.1.0
argon2-cffi-bindings==25.1.0
array_record==0.8.1
arrow==1.3.0
asttokens==3.0.0
astunparse==1.6.3
async-lru==2.0.5


.......and much more.........
```

---
# Reason
-  The above packages require a lot of **dependencies** in order to run.

---
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
# Solution

## Filter `pip freeze` for specific packages
``` bash
pip freeze | grep -E '^(numpy|matplotlib|seaborn|pandas|scipy)=' > requirements.txt
```

---
