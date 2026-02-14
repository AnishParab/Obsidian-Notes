# Vim vs Vi Compatible Mode

### Check if Vim is running in _Vi-compatible_ mode
```vim
:help compatible
```

### Key option
- `'compatible'`
    - **on** → Vim behaves like old **Vi**
    - **off** → Vim behaves like **Vim** (Recommended)

### Check current value
```vim
:set compatible?
```

### Force Vim behavior (Recommended)
```vim
:set nocompatible
```

### Notes
- Modern Vim defaults to `nocompatible` when a **vimrc** is found.
- If stuck in Vi behavior, explicitly set `set nocompatible` early in config.

---
