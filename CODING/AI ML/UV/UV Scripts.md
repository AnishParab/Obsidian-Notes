``` bash
touch hello.py
```

---
# Flow
- You have imported _fastapi_ but you need not `uv add fastapi`.

Use This Instead:
``` python
uv run --with 'fastapi' --with 'pandas' hello.py
```

---
# What if you have many Dependencies
``` bash
uv add --script hello.py 'fastapi' 'requests' 'pandas'
```

This adds comments to your script.

---
