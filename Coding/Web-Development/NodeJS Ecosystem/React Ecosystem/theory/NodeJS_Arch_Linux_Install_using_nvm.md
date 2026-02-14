# Using `nvm`

**Why:** isolates Node versions per user; avoids system-wide conflicts.

Install:
```bash
sudo pacman -S nvm
```

Add to shell config (`~/.bashrc` or `~/.zshrc`):
```bash
export NVM_DIR="$HOME/.nvm"
source /usr/share/nvm/init-nvm.sh
```

Reload shell:
```bash
source ~/.bashrc   # or ~/.zshrc
```

Install Node:
```bash
nvm install --lts
nvm use --lts
```

Verify:
```bash
node -v
```

---
