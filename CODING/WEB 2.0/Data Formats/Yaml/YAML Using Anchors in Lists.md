``` YAMl
common_tools: &tools
  - Docker
  - Kubernetes
  - Terraform

dev_team:
  name: DevOps Engineers
  tools: *tools  # Reusing tools list
```

#### Expands to
``` YAML
dev_team:
  name: DevOps Engineers
  tools:
    - Docker
    - Kubernetes
    - Terraform
```

