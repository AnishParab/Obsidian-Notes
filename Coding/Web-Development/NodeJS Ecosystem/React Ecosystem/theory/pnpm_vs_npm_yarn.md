# The Three Main Pain Points of npm/Yarn Classic

1. **Dependency Duplication**: Every project saves its own copy of a package, leading to massive disk bloat.
2. **Phantom Dependencies**: npm flattens (hoists) the tree, allowing you to import packages you didn't explicitly define in `package.json`.
3. **Slow Installation**: Copying files from a cache to `node_modules` is an $O(n)$ operation that scales poorly.

---
