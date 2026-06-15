# Docker

- Docker is a platform for building, shipping, and running containers
- Packages an app + its dependencies into a portable, reproducible unit (image → container)
- Core components:
    - **Docker Engine** — daemon (`dockerd`) that manages containers on the host
    - **Docker CLI** — client that talks to the daemon via REST API
    - **Docker Hub** — default public registry for images
- Key workflow: write `Dockerfile` → build image → run container
- Images are layered (union filesystem); each instruction in a Dockerfile adds a layer
- Containers are running instances of images — same image can spawn many containers
- Uses Linux namespaces + cgroups under the hood (containers are just isolated processes)
- On non-Linux (macOS/Windows), Docker runs a lightweight Linux VM to host the daemon

---
# Virtual Machines

- A VM emulates a full machine: CPU, memory, storage, network — all virtualized
- Each VM runs its own OS (kernel + userspace) on top of a hypervisor
- Strong isolation: kernel panic in one VM doesn't touch others
- Slow to boot (full OS init), heavy on disk (GB-range images), high memory overhead
- Use VMs when you need: full OS-level isolation, different kernels, or legacy OS support
- Containers vs VMs — the core tradeoff:

|                   | Container     | VM              |
| ----------------- | ------------- | --------------- |
| Isolation unit    | Process       | Full OS         |
| Startup           | Milliseconds  | Seconds–minutes |
| Size              | MBs           | GBs             |
| Kernel            | Shared (host) | Own kernel      |
| Security boundary | Weaker        | Stronger        |

- Docker on macOS/Windows uses a VM (HyperKit / WSL2) to get a Linux kernel, then runs containers inside it — so you're paying VM cost once, not per container

---
![[Pasted image 20260516223412.png]]

---
