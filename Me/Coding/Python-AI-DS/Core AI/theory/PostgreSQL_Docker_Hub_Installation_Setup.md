# Docker Hub

[Search for docker postgres](https://hub.docker.com/_/postgres)

---
# Example

**docker-compose.yml**
``` yaml
service:
	postgres:
		image: postgres:17.4
		ports:
			- 5432:5432
		environment:
			POSTGRES_DB: mydb
			POSTGRES_USER: postgres
			POSTGRES_PASSWORD: admin
```

**docker command - To run in the background**
``` bash
docker compose up -d
```

---
