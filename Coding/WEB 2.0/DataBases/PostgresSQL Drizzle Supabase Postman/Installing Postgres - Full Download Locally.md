# Why installing locally is a bad decision
- _Local_: You install the database directly on your machine. It’s fast for development but comes with a cost: you can only run **one database cluster** (a cluster = one PostgreSQL server process + multiple databases inside it). It’s tied to your machine, eats your resources, and makes collaboration harder.
- You’re constrained to one database cluster in your dev machine.
- No isolation between environments (test, staging, prod).
- Risk of polluting your system with multiple versions.
- Local installs are harder to replicate for team members compared to containers or remote DBs.

---
# Installing Postgres on Arch Linux
#### Install via pacman
``` bash
sudo pacman -S postgresql
```
#### Initialize the database cluster
``` bash
sudo -iu postgres
initdb -D /var/lib/postgres/data
exit
```
#### Enable and start the service
``` bash
sudo systemctl enable postgresql
sudo systemctl start postgresql
```
#### Check status
``` bash
systemctl status postgresql

```
#### Enter the Postgres shell
- The default database superuser is `postgres`
``` bash
sudo -iu postgres
psql
```
#### Connect as your new user
``` bash
psql -U asp -d aspdb

```

---
