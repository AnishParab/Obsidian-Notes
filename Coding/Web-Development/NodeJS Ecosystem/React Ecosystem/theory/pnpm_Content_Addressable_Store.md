# Content-Addressable Store (pnpm)

## Core Idea

- One global store (`~/.pnpm-store`)
- Packages stored **once**, shared across projects

---
## Disk Efficiency

- pnpm:
    - `disk = size(package@version) × 1`
- npm / Yarn:
    - `disk = size(package@version) × n`

---
## Linking Model

- **Hard links**: connect project to global store (no copying)
- **Symlinks**: enforce strict dependency boundaries

---
## Result

- No duplication
- No phantom dependencies
- Node-compatible resolution

---
## Design Goal

- Correct dependency graphs
- Minimal disk usage

---
