# Package Managers
- Installs dependencies.
- Package versioning.

---
# npm
**Advantages**
- Default for node.
- Huge Ecosystem.
- Stable.

**Disadvantages**
- Slow.
- `node_modules` is too big of a file.
- Not so secure (I mean, two big security flaws in a single year??? bruh...)

---
# pnpm
- Speed Install.
- **Content addressable store**: Saves disk space OR **symlinks**.
- Fast.
- **Good for MonoRepos**.

---
# yarn
- Created by facebook.
- Uses **parallelization** to make it fast.
- Gives a workspace, **monorepo** (Out of the box).
- Two versions: yarn 1, yarn berry.
- **Dependency Linking**: To prevent large module files.

---
# bun
- nodejs + package manager + bundler + aws support.
- Fastest.

---
