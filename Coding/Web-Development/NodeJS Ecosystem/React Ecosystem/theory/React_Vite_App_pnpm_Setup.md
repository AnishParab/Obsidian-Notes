# Pre-requisites
[[React_pnpm_corepack_Setup]]

---
# Step 1: Create a Dedicated Project Directory
Isolation starts at the filesystem level.

```bash
mkdir react-vite-pnpm
cd react-vite-pnpm
```

Rule:
> One project = one directory = one `node_modules`

Never share project directories.

---
# Step 2: Scaffold React with Vite (pnpm-native)
Use pnpm’s executor, **not npm**.

```bash
pnpm create vite
```

You will be prompted:
- Project name → `.` (current directory) or a subfolder
- Framework → React
- Variant → React + TypeScript (recommended)

Why this is safe:
- `pnpm create` runs in a temp context
- No global state mutation

---
# Step 3: Pin pnpm Version (Critical for Isolation)

Edit `package.json`:
```json
{
  "packageManager": "pnpm@9.0.0"
}
```

Why:
- Prevents different pnpm versions across projects
- Corepack enforces this automatically

Failure mode avoided:
> “Same lockfile, different behavior”

---
# Step 4: Install Dependencies (Deterministic)

```bash
pnpm install
```

What happens:
- Dependencies resolved
- `pnpm-lock.yaml` created
- `node_modules` populated via symlinks
- Global store reused safely

Isolation note:
> The global store is **read-only content-addressed data**.  
> It cannot mutate other projects.

---
# Step 5: Verify Isolation Guarantees

Run:
```bash
ls node_modules
```

You should see:
- `.pnpm/`
- Minimal top-level entries
- No massive flat dependency dump

This confirms:
- Strict dependency graph
- No hoisting leakage

---
# Step 6: Run the Dev Server
```bash
pnpm dev
```

This uses:
- Local `node_modules`
- Local config
- Local Vite instance

No global binaries involved.

---
# Step 7: Project Boundary Rules and Commit Rules

To ensure this project never affects others:
#### 1. Never Use Global Installs
```bash
npm install -g vite
pnpm add -g anything
```
###### Always use:
```bash
pnpm <script>
pnpm exec <tool>
```

---
#### 2. Never Share `node_modules`
- Do not copy `node_modules`
- Do not symlink between projects
Each project resolves independently.

---
#### 3. Commit These Files Only
Required:
- `package.json`
- `pnpm-lock.yaml`
- `vite.config.*`

Never commit:
- `node_modules`
- pnpm store

---
# Step 8: Optional but Strongly Recommended Hardening
### Lock Node Version (Prevents ABI Drift)

Add `.nvmrc` (or equivalent):
```
18.19.0
```

This ensures:
- Native modules behave consistently
- CI matches local

---
#### Use `.npmrc` for Explicit Behavior

```ini
strict-peer-dependencies=true
auto-install-peers=true
```

This prevents:
- Silent peer mismatches
- Runtime dependency errors

---
