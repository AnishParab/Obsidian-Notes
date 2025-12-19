# Refer This first
[[Python_VirtualEnv_Concepts_TraditionalApproach]]

---
# Add this to `requirements.txt`
``` text
jupyter
tensorflow
tensorflow-datasets
ipywidgets
ipykernel
matplotlib
```

---
# Install or upgrade Jupyter Notebook
``` bash
pip install --upgrade notebook
```

``` bash
jupyter --version
```
---
# Upgrade all packages
``` bash
pip install --upgrade -r requirements.txt
```

---
# Launch Jupyter Notebook using tmux
``` bash
jupyter notebook
```


----
# Make a new Notebook file
- Click **“New” → “Python 3”** (or your kernel name).
- A new notebook will open, usually named `Untitled.ipynb`.
- Rename it: **File → Rename** (e.g., `nsynth_training.ipynb`).

---
