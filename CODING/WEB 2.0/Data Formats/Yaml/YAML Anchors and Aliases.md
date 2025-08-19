For Reusing Data.

## **Important Considerations**
- **Anchors & aliases work only within the same YAML file.**
- **Overriding values after using `<<:` does not affect the original anchor.**
- **Some YAML parsers do not support merging (`<<:`).**
# Anchor
1. `&`
2. Define a reusable block.

# Alias
1. `*`
2. Reference the anchored block.

# Code for Reusing Data
Both `server1` and `server2` inherit values from `default_settings`.
``` YAML
default_settings: &defaults
  timeout: 30
  retries: 3

server1:
  <<: *defaults
  host: server1.example.com

server2:
  <<: *defaults
  host: server2.example.com
```

