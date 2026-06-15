# Why use Docker ?

> **Problem Docker solves:** "works on my machine" — environment inconsistency across dev, staging, prod

- Core mental model: Docker makes the **environment** a versioned, reproducible artifact — not a fragile snowflake configured manually on each machine.

---
## Developer perspective

- **Consistency** — same container runs on your Arch box, teammate's macOS, and CI. No more env drift.
- **Isolation** — each project gets its own container. Python 3.9 for one, 3.12 for another. No venv gymnastics at the OS level.
- **Portability** — ship the image, not setup instructions. Onboarding = `docker run`.
- **Efficiency** — spins up in milliseconds. Run 10 services locally without 10 VMs eating your RAM.
- **Easy** — one `Dockerfile` replaces pages of "how to set up this project" docs.

---
## DevOps perspective

- **Consistency** — the artifact (image) that passed CI is the exact artifact that goes to prod. No "but it worked in staging."
- **Scalability** — containers are cheap to spin up/down. Orchestrators (Kubernetes, Swarm) can scale horizontally by just running more instances of the same image.
- **Isolation** — process and filesystem isolation means one misbehaving service doesn't take down the host or neighbors.
- **Portability** — same image runs on any cloud provider, any Linux host. No vendor lock-in at the runtime level.
- **Efficiency** — high container density per host vs VMs. More apps per machine = lower infra cost.

---

