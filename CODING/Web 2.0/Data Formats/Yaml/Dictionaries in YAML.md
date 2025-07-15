# Nested Objects/Dictionaries in YAML
1. Indentation defines Nesting.
2. Also called **mappings**.
3. Store **key-value** pairs.

``` YAML
database:
  host: localhost
  port: 3306
  username: root
  password: secret
```

##### Equivalent JSON
``` JSON
{
  "database": {
    "host": "localhost",
    "port": 3306,
    "username": "root",
    "password": "secret"
  }
}
```

# Inline
``` YAML
# Inline
database: { host: localhost, port: 3306, username: root, password: secret }
```

# Nested dictionaries
Dictionaries can be nested within dictionaries.
``` YAML
application:
  name: MyApp
  version: 1.0
  database:
    host: localhost
    port: 5432
    username: admin
    password: password123
```
##### Equivalent JSON
``` JSON
{
  "application": {
    "name": "MyApp",
    "version": 1.0,
    "database": {
      "host": "localhost",
      "port": 5432,
      "username": "admin",
      "password": "password123"
    }
  }
}
```

