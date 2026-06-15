# Semantic Versioning in `npm`

Example:
```json
"express": "4.21.1"
```

```
MAJOR.MINOR.PATCH
```

---
# Version Segments

| Segment   | Meaning          | When it Changes     |
| --------- | ---------------- | ------------------- |
| **MAJOR** | Breaking changes | API incompatibility |
| **MINOR** | New features     | Backward compatible |
| **PATCH** | Bug fixes        | Backward compatible |

---
# Version Range Prefixes

| Prefix | Behavior                         | Example              |
| ------ | -------------------------------- | -------------------- |
| none   | Exact version only               | `"4.21.1"`           |
| `~`    | Patch updates allowed            | `~4.21.1` → `4.21.x` |
| `^`    | Minor + patch allowed (no major) | `^4.21.1` → `4.x.x`  |

---

# Expansion Examples

```text
~4.21.1  → >=4.21.1 <4.22.0
^4.21.1  → >=4.21.1 <5.0.0
```

---
# Common Notes

- `npm install` writes `^` by default.
- `^` assumes semantic versioning is respected by package authors.
- Lockfile (`package-lock.json`) pins the exact resolved version.

---
