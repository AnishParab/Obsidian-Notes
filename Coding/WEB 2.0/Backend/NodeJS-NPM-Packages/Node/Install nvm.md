# Install
``` bash
yay -S nvm

```

---
# Install manually via `curl`
``` bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

```

---
# Add to shell config
- For `zsh`
``` bash
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.zshrc
echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> ~/.zshrc
```

- Reload config:
``` bash
source ~/.zshrc

```

---
