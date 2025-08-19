``` python
def print_env(**env):
    for k, v in env.items():
        print(f"{k} = {v}")

print_env(shell="zsh", distro="Arch")
```

- `**env` means pack all keyword arguments into a dictionary called `env`.

---

