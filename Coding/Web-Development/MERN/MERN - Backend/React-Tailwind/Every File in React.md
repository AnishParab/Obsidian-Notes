# `package.json`
- Versioning
- Type : `module` or `commonjs` , **module** is preferred.
- Scripts
- Dependencies
- DevDependencies

---
# `src`
### `assets`
- Store assets like photos, videos, fonts etc.
### `main.jsx`
- We target an element `id` and use a method `render` for `App` component.
- `createRoot` creates a **Virtual DOM** (Programaticaly controlled DOM).
### `App.jsx`
- A functional component.

---
# `public`
- Serve public assets such as images, videos, css etc.

---
# `index.html`
- `id="root"` -> All of your javascript, react code is injected, and your application is built from there.
- `script` -> Helps inject the code from `src/main.jsx`

---
# `eslint.config.js`
- Important when you work in a team.

---
# `vite.config.js`
- Plugin injection.

---
