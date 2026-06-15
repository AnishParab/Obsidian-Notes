# Use Docker if:

- You need exact production parity
- You need multiple DB versions
- You constantly reset environments
- You are working on team-based infra
- You use Docker Compose already

Then:
```
docker run --name mysql \  -e MYSQL_ROOT_PASSWORD=password \  -p 3306:3306 \  -d mysql:8
```

---
