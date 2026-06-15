# Containers

- A container is an isolated process (or group of processes) running on the host OS
- Shares the host kernel — no separate OS per container
- Isolated via Linux primitives:
    - **Namespaces** — what the process can _see_ (filesystem, network, PIDs, users)
    - **cgroups** — what the process can _use_ (CPU, memory, I/O limits)
- Has its own filesystem layer (from a container image)
- Starts in milliseconds; low overhead
- vs VM: no hypervisor, no guest OS, less isolation but far lighter
- Ephemeral by default — state is lost on container removal unless persisted via volumes

---
# Hypervisors (Virtual Machines)

- A hypervisor virtualizes hardware to run multiple full OS instances (VMs) on one machine
- Each VM has its own kernel, drivers, and OS — full isolation
- Two types:
    - **Type 1 (bare-metal)** — runs directly on hardware (VMware ESXi, Hyper-V, KVM). Better performance.
    - **Type 2 (hosted)** — runs on top of a host OS (VirtualBox, VMware Workstation). Easier for dev use.
- Resource-heavy: each VM carries a full OS (~GBs of overhead)
- Strong isolation — kernel bugs in one VM don't affect others
- Docker on non-Linux (macOS/Windows) uses a lightweight Type 1-ish hypervisor (HyperKit / WSL2) to run the Linux kernel that containers need

![[Hypervisor.excalidraw|500]]

---
# Difference

![[Pasted image 20260516222804.png]]

---
