# Pre-requisites

[[npm_Create_Project_package-json_File]]
[[NodeJS_Typescript_Types_and_LSP_Support]]

---
# Package Installation

**npm**
```bash
npm install express
```

**pnpm**
```bash
pnpm add express
```

**bun**
```bash
bun add express
```

---
# Type Definitions — Express (TypeScript)

**npm**
```bash
npm install -D @types/express
```

**pnpm**
```bash
pnpm add -D @types/express
```

**bun**
```bash
bun add -d @types/express
```
##### Notes
- `@types/express` = community TypeScript typings (DefinitelyTyped).
- Needed because Express is not fully typed internally.
- Install as **dev dependency** (`-D` / `-d`).
##### When NOT Needed
- Pure JavaScript projects.
- If a package ships its own types (`types` field in `package.json`).

---
# Also Refer to :

[[ExpressJS_Basic_Code]]
[[ExpressJS_Running_Locally_and_Testing]]

---
