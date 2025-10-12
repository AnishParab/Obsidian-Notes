``` YAML
base_config: &config
  environment: production
  debug: false
  replicas: 3

staging:
  <<: *config
  environment: staging  # Override environment

development:
  <<: *config
  environment: development  # Override environment
  debug: true  # Override debug
```

#### Expands to
``` YAML
staging:
  environment: staging
  debug: false
  replicas: 3

development:
  environment: development
  debug: true
  replicas: 3
```