## Definition

**Pythonic** = writing code that matches Python’s **intended style**:

- readable first
- uses Python language features directly (not “translated from C/Java”)
- follows community conventions (PEP 8 + common idioms)

In practice:
- **Pythonic ≈ Idiomatic Python**
- “Pythonic” is the broader term; “idiomatic” is more specific.

---
# What Pythonic code looks like (signals)

- uses **truthiness** (`if items:`)
- iterates over **values**, not indices
- prefers **built-ins** (`sum`, `any`, `enumerate`, `zip`)
- uses **comprehensions** when they improve clarity
- uses **context managers** (`with ...`)
- keeps code **flat and readable** (avoid deep nesting)
- avoids redundant comparisons (`if flag:` not `if flag == True`)

---
