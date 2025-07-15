### Correct
``` YAML
# This is a comment
database:
  host: localhost  # Hostname for the database
  port: 3306       # MySQL default port
```
### Incorrect
``` YAML
database: localhost #Comment without space ❌
```
### Fix
``` YAML
database: localhost  # Space after `#`
```

