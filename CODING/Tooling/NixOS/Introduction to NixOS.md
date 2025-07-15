- **Declarative**, **reproducible Linux Distribution**.
- Built on top of Nix Package Manager.
 ---
# Traditional Distros vs NixOS
- In traditional distros, system configuration is **imperative**.
- NixOS defines **entire system state**, in a single version-controlled configuration file.

---
# Features of Nix
## Declarative Configuration
Everything from user accounts to systemd services is described in `/etc/nixos/configuration.nix`.

## Atomic Upgrades & Rollbacks
System upgrades are **transactional**. If anything breaks, you can instantly rollback to previous working configuration.

## Reproducibility
Nix builds are **pure and deterministic**. Environments are created identically on any machine.

## Isolation via Sandboxing
- Packages are installed in isolated `/nix/store` paths. This avoids dependency hell.
- This isolation ensures dependencies are never shared **implicitly**.
- Traditional package managers install files into **global locations** like `/usr/bin` or `/lib`.

---

