# Master vs Main Branch

- In **Git**, **`master`** was the traditional default branch name.  

- **`main`** is the modern, recommended default branch name used by most new repositories.

**Key points**
- Functionally identical (no technical difference).
- `main` is preferred for inclusive naming standards.

---
# Why was `master` controversial
**Why it was criticized**
- The term _master_ was associated by some with **master–slave terminology**, commonly used in older tech systems.
- It was viewed as **non-inclusive language**, even though Git’s `master` was never intended with that meaning.

---
# By default
``` bash
git branch
```

- This shows **master** branch.
- Which means **HEAD** file points to the **master** branch.
- **HEADS** can be seen in the `.git/heads` folder, where each file is a branch name.

---
