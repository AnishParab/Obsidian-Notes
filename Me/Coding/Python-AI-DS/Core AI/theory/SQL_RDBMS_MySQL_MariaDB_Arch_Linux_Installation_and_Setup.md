# Arch-Linux Installation Guide

**Install**
```bash
sudo pacman -S mariadb
```

**Initialize database**
```bash
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
```

**Start service**
```bash
sudo systemctl enable --now mariadb
```

**Secure setup**
```bash
sudo mariadb-secure-installation
```

**Login**
```bash
mariadb
```

**Verify**
```bash
systemctl status mariadb
```

```bash
mariadb -u root -p
```

---
