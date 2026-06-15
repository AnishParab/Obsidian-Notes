# CommonJS v/s ESM

| CommonJS        | ESM                          |                     |
| --------------- | ---------------------------- | ------------------- |
| Syntax          | `require` / `module.exports` | `import` / `export` |
| Loading         | Synchronous                  | Asynchronous        |
| `package.json`  | `"type": "commonjs"`         | `"type": "module"`  |
| Extension       | `.js` / `.cjs`               | `.js` / `.mjs`      |
| Top-level await | No                           | Yes                 |
| `__dirname`     | Available                    | Not available       |
| Tree shaking    | No                           | Yes                 |
| Browser support | No                           | Yes                 |

- CJS loads modules synchronously — blocks execution until module is ready
- ESM loads asynchronously — enables parallel loading, better performance
- Tree shaking — bundlers (Webpack, Vite) can eliminate unused ESM exports; CJS exports are dynamic so bundlers can't analyze them statically
- CJS is still default in Node.js — most legacy packages use it
- ESM is the standard going forward — use it for new projects

---
# Interop gotcha:

- ESM can import CJS — works mostly fine
- CJS cannot `require()` ESM — throws error; must use dynamic `import()`

---
