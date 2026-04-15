# Git Diff
- Informative command
- Compare working with staging.

---
# How to read
- a -> file1  and  b -> file2  **(Same file overtime)**.
- `---` file1  and  `+++` file2  **(Indicates changes in file)**.
- Changes in file and little preview of it.

- `---` and `+++` actually represents `a` and `b` which is the same file in different timelines.

---
# Command
``` bash
git diff --staged
```

``` bash
git diff <commit_id>..<commit_id>
```

``` bash
git diff <branch_name_1>..<branch_name_2>
```

---
