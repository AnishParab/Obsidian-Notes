# Lists/Arrays in YAML
Represented using `-` followed using `space`.

``` YAML
skills:
  - Linux
  - Docker
  - Kubernetes
```
##### Equivalent JSON code
``` JSON
{
  "skills": ["Linux", "Docker", "Kubernetes"]
}
```

# Inline Lists
``` YAML
# Inline
servers: [server1, server2, server3]
```


# List of Dictionaries (List of Objects)
Each list item can be a dictionary.
``` YAML
users:
  - name: Anish
    role: DevOps Engineer
    experience: 2 years
  - name: Priya
    role: Software Developer
    experience: 3 years
```

##### Equivalent JSON
``` JSON
{
  "users": [
    { "name": "Anish", "role": "DevOps Engineer", "experience": "2 years" },
    { "name": "Priya", "role": "Software Developer", "experience": "3 years" }
  ]
}
```

# Nested Lists
List can contain other lists.
``` YAML
projects:
  - name: DevOps Pipeline
    tools:
      - Docker
      - Kubernetes
      - Terraform
  - name: Web Development
    tools:
      - React
      - Node.js
      - MongoDB
```

