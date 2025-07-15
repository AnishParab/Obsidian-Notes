1. YAML relies on **indentation** to define structure instead of brackets (`{}`) or commas (`,`) like JSON.
2. Proper indentation and formatting ensure valid YAML syntax.

# Rules
1. YAML uses **spaces** for indentation (not tabs).
2. Indentation **must be consistent** (usually **2 or 4 spaces** per level).
3. Indentation defines **hierarchy** in mappings and lists.

### Correct
``` YAML
user:
  name: Anish
  role: DevOps Engineer
  skills:
    - Linux
    - Docker
    - Kubernetes
```
### Incorrect
``` YAML
user:
	name: Anish  # ❌ Invalid: Uses a tab instead of spaces
  role: DevOps Engineer
```