# Docker Arch-Linux Installation

- Install Docker
``` bash
sudo pacman -S docker
```

- Start and enable daemon
``` bash
sudo systemctl enable --now docker
```

- Add user to docker group
``` bash
sudo usermod -aG docker $USER
```

- Re-login or apply group in current shell only
``` bash
newgrp docker
```

- Verify install
``` bash
docker run hello-world
```

---
**Gotchas**

- `usermod` group change needs re-login to persist — `newgrp docker` is session-only
- Any `docker` command fails if daemon isn't running → `systemctl status docker`
- Arch stock kernels (`linux`, `linux-zen`) have cgroup/namespace support — custom kernels may not

---
