# Configure Git Identity
``` bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

---
# Generate SSH Key
``` bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

---
# Start SSH agent and add key
``` bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---
# Add SSH Key to GitHub
``` bash
cat ~/.ssh/id_ed25519.pub
```

Copy output → GitHub → **Settings → SSH and GPG keys → New SSH key**

---
# Test Connection
``` bash
ssh -T git@github.com
```

---
