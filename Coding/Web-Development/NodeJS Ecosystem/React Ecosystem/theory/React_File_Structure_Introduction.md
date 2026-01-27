# `package.json`
- Project manifest.
- Declares dependencies, scripts, and tool versions.
- Defines the dependency graph boundary.

---
# `public/`
- Static files served as-is.
- Not processed by Vite or the bundler.

---
# `src/`
- Application source code.
- Fully controlled and transformed by the build tool.

### `assets/`
- Imported static assets (images, fonts, etc.).
- Processed and hashed by the bundler.

---
# `eslint.config.js`
- Linting rules and code quality constraints.
- Enforced during development and CI.

---
# `index.html`
- HTML entry point.
- Bootstraps the app.
- Loads `main.jsx`.

---
# `main.jsx`
- JavaScript entry point.
- Creates the React root.
- Mounts the component tree in `StrictMode`.
- Renders `App.jsx`.

---
# `App.jsx`
- Root UI component.
- Defines the initial component structure.

---
# `pnpm-lock.yaml`
- Exact dependency graph snapshot.
- Guarantees deterministic installs.
- Must be committed.

---
# `node_modules/`
- Project-local dependency entry point.
- Constructed via symlinks to pnpm store.
- Never committed.

---
# `vite.config.js` / `vite.config.ts`
- Vite build and dev server configuration.
- Defines plugins, aliases, and build behavior.

---
# `.gitignore`
- Prevents committing generated and local-only files.
- Typically excludes `node_modules`, build output, env files.

---
# `.npmrc`
- Project-level package manager configuration.
- Controls pnpm behavior (strictness, peers, hoisting).

---
# `README.md`
- Project documentation entry point.
- Explains setup, scripts, and usage.

---
# `dist/` (generated)
- Production build output.
- Created by `pnpm build`.
- Not committed.

---
