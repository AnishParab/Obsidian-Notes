# Short difference: `attrgetter` vs `itemgetter`

| Aspect               | `attrgetter`              | `itemgetter`                   |
| -------------------- | ------------------------- | ------------------------------ |
| Access style         | Attribute access          | Index / key access             |
| Works on             | Objects (class instances) | dicts, lists, tuples           |
| Syntax it represents | `obj.attr`                | `obj[key]` or `obj[index]`     |
| Typical use          | Sorting/grouping objects  | Sorting/grouping records       |
| Missing value error  | `AttributeError`          | `KeyError` / `IndexError`      |
| Nested access        | Yes (`"a.b.c"`)           | No (single-level keys/indices) |

**Rule of thumb:**
- **Dot access → `attrgetter`**
- **Bracket access → `itemgetter`**

---
