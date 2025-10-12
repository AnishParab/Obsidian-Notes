- Strings with special characters (`:`, `@`, `#`, etc.).
- Strings that resemble booleans (`yes`, `no`, `on`, `off`).
- Strings with leading or trailing spaces.
### Correct
``` YAML
email: "user@example.com"
description: "This is a description with a colon: inside."
boolean_string: "no"  # Prevents YAML from interpreting as `false`
```
### Incorrect
``` YAML
email: user@example.com  # ❌ Invalid if '@' is unquoted in some parsers
description: This is a description with a colon: inside.  # ❌ Colon can cause issues
```