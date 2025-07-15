# Key-Value Formatting
- Each key-value pair must be separated by a colon (`:`) and a space.
- Keys and values must be on the same line unless using multi-line syntax.
### Correct
``` YAML
host: localhost
port: 5432
username: admin
```
### Incorrect
``` YAML
host :localhost   # ❌ No space after the colon
port 5432        # ❌ Missing colon between key and value
username:admin   # ❌ No space after the colon
```

# List Formatting
- Lists should be properly indented and aligned under their parent key.
- Each item in the list starts with a hyphen (`-`) followed by a space.
### Correct
``` YAML
skills:
  - Linux
  - Docker
  - Kubernetes
```
### Incorrect
``` YAML
skills:
- Linux    # ❌ No indentation under "skills"
 - Docker   # ❌ Inconsistent indentation
  - Kubernetes  # ❌ Wrong indentation level
```