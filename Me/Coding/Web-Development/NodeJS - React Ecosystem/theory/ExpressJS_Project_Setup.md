# Pre-requisites

[[npm_Create_Project_package-jSON_file]]
[[NodeJS_Typescript_Types_and_LSP_Support]]

---
# Package Installation

```bash
# npm
npm install express
```

```bash
# pnpm
pnpm add express
```

```bash
# bun
bun add express
```

---
# Type Definitions — Express (TypeScript)

```bash
# npm
npm install -D @types/express
```

```bash
# pnpm
pnpm add -D @types/express
```

```bash
# bun
bun add -d @types/express
```
### Notes

- `@types/express` = community TypeScript typings (DefinitelyTyped).
- Needed because Express is not fully typed internally.
- Install as **dev dependency** (`-D` / `-d`).
### When NOT Needed

- Pure JavaScript projects.
- If a package ships its own types (`types` field in `package.json`).

---
# Also Refer to :

[[ExpressJS_Running_Locally_and_Testing]]

---
