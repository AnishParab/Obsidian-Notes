# Bundlers

- Tool that builds a **dependency graph**
- Outputs **optimized static assets** for browsers

---
# Why Needed

- Browsers handle few large files better than many small ones
- Ensures compatibility and performance

---
# Core Responsibilities

- **Dependency resolution**: track imports
- **Bundling**: merge files
- **Transpilation**: JSX / TS → JS
- **Asset handling**: CSS, images, fonts

---
# Optimizations

- **Tree-shaking**: remove unused code
- **Minification**: shrink output size
- **Code-splitting**: load on demand
- **HMR**: update modules without reload (dev only)

---
# Popular Bundlers

- **Vite**: fast dev, ESM-based
- **Webpack**: flexible, complex
- **esbuild**: very fast, low-level
- **Turbopack**: Webpack successor (Next.js)

---
# Notes

- Bundler = build-time system
- Runtime performance depends on output, not the tool itself

---
