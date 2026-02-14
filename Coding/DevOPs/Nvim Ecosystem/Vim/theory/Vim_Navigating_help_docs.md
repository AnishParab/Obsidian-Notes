# Open Help

```vim
:help
```

**Navigate help links**
- `Ctrl-]` → jump to link under cursor
- `Ctrl-O` → jump back (older position)

**Help window control**
- `Ctrl-W o` → keep only current window open
- `Ctrl-W w` → cycle through windows

---
# Index / Overview Pages

**Complete index**
```vim
:help index
```

**Help summary**
```vim
:help help-summary
```

---
# Help Search Auto-completion

While typing a help topic:
- `Ctrl-D` → list all matching topics
- `Tab` → autocomplete topic

---
# Help Lookup Patterns

**General topics**
```vim
:help deleting
```

**Keybindings**
```vim
:help CTRL-A
```

#### Mode-specific keys
- Normal mode:
```vim
:help CTRL-H
```
- Insert mode:
```vim
:help i_CTRL-H
```
- Visual-mode commands → `v_`
```vim
:help v_o
```
- Command-line editing / arguments → `c_`
```vim
:help c_%
```
- Ex commands → `:`
```vim
:help :s
```
- Debugger commands → `>`
```vim
:help >cont
```


---
# Help Syntax Conventions

#### Command-line arguments
- Use `-` prefix:
```vim
:help -t
```

#### Options
- Use single quotes:
```vim
:help 'number'
```

#### Special keys
- Use `<...>` notation:
```vim
:help i_<Up>
```

#### Error messages (by ID)
```vim
:help E37
```

#### Warnings (by ID)
```vim
:help W10
```

---
# Vim Regex Help Lookup

Regex help topics start with `/`:
```vim
:help /\+
```

---
# Docs for Built-in Packages

Example:
```vim
:help package-termdebug
```

---
