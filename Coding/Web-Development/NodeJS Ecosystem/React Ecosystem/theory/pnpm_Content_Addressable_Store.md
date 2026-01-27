# Content-Addressable Store

- Instead of copying files, pnpm stores all packages in a single global store (usually at `~/.pnpm-store`).

#### 1. The Mathematical Efficiency

If $P$ is a package and $V$ is a version, pnpm ensures that for any number of projects $n$:
$$\text{Disk Space Usage} = \text{Size}(P_V) \times 1$$
In traditional managers:
$$\text{Disk Space Usage} = \text{Size}(P_V) \times n$$

#### 2. Hard Links & Symlinks

- **Hard Links**: Connect the global store to the project's virtual store.
- **Symlinks**: Create the nested structure that prevents phantom dependencies while keeping Node.js happy.

---
# Design Goal

> Enforce **correct dependency graphs** while remaining compatible with the Node ecosystem.

---
