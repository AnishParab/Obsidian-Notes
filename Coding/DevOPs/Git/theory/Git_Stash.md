# Git Stash
- Create a repo, work and commit on main.
- Switch to another branch and work.
- Conflicting changes do not allow to switch branch, without commits.

- Stash is like a temporary shelf that keeps the code.
- You can bring back the content from the shelf.

---
# Command
- You can switch branch
``` bash
git stash
```

- Get a list of all stash
``` bash
git stash list
```

- Bring back those changes
``` bash
git stash pop
```

- Optional: Apply changes and keep them in stash
``` bash
git stash apply stash@{0}
```

---
