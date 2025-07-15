# Installation
``` bash
pip3 install virtualenv
```

---
# Basic Steps
``` bash
cd /path/to/new/virtual/environment/

python3 -m venv .venv

source .venv/bin/activate

python --version
```

---
# `requirement.txt`
``` bash
pip list

pip list > requirement.txt
```

---
# Install Packages from`requirement.txt`

``` bash
pip install -r requirement.txt

pip list
```

---
# Exit the Virtual Environment safely
``` bash
deactivate
```

---
# Upgrade `pip`
``` bash
python -m pip install --upgrade pip
```

---
