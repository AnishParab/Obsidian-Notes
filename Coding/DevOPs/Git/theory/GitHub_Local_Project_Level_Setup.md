# Generate a **separate SSH key** for the project

```bash
ssh-keygen -t ed25519 -C "other_email@example.com"
```

Save as:
```text
~/.ssh/id_ed25519_work
```

---
# Add key to SSH agent
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519_work
```

---
# Add the public key to the second **GitHub** account
```bash
cat ~/.ssh/id_ed25519_work.pub
```

GitHub → Settings → SSH & GPG keys → New SSH key

---
# Configure SSH **host alias**
Edit:
```bash
~/.ssh/config
```

```ssh
# Personal account
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519

# Work / second account
Host github-work
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_ed25519_work
```

---
# Clone the repo using the alias (IMPORTANT)
```bash
git clone git@github-work:username/repo.git
```

This binds the project to the **second account**.

---
# Set **project-local Git identity**

Inside the repo:
```bash
git config user.name "Work Name"
git config user.email "work_email@example.com"
```

Verify:
```bash
git config --list --local
```

---
## Result (what you get)
- Global GitHub account → unchanged
- This repo → **separate SSH key + separate identity**
- No credential conflicts
- Safe for DevOps / enterprise workflows

---
