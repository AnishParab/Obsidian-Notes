# Bundlers

> [!abstract] Definition
> 
> A tool that traverses your application's dependency graph to package multiple files (modules) into optimized static assets that a browser can understand.

---
# Core Responsibilities
- **Dependency Resolution**: Maps how files import one another to create a single "graph."
- **Concatenation**: Combines hundreds of small files into a few large "bundles" to reduce HTTP requests.
- **Transpilation**: Works with tools like **Babel** or **esbuild** to turn JSX/TypeScript into standard JavaScript.
- **Asset Management**: Processes CSS, images, and fonts alongside code.

---
# Optimization Techniques

| **Technique**      | **Purpose**                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| **Tree-shaking**   | Removes "dead code" (imported functions that are never used).                     |
| **Minification**   | Strips whitespace and renames variables to reduce file size.                      |
| **Code-splitting** | Breaks the bundle into chunks loaded on-demand (Lazy Loading).                    |
| **HMR**            | **Hot Module Replacement** updates the browser without a full refresh during dev. |

---
# Popular Modern Bundlers
1. **Vite**: The modern standard. Uses native ES Modules in dev for near-instant start times.
2. **Webpack**: The legacy powerhouse. Highly configurable but slower and more complex.
3. **esbuild**: An extremely fast bundler written in Go; often powers other tools (like Vite).
4. **Turbopack**: Designed as a successor to Webpack, specifically for the Next.js ecosystem.

---

> [!tip] Why do we need this?
> 
> Browsers struggle to manage 1,000+ individual JS files. Bundlers ensure the code is **efficiently delivered** and **compatible** across all user environments.

---
