# Make this File
`docker-compose.yml`
``` yml
services:
  postgres:
    image: postgres:17.4
    ports:
      - 5432:5432
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: admin
```

---
# Run these commands
- `docker compose up -d` --> Creates and Starts
- `docker compose down` ---> Stops and Removes
- `docker ps -a` ---> Show all containers

---
