# Step 1: Install Dependencies (Local Only)

```bash
pnpm add -D tailwindcss postcss autoprefixer
```

Why:
- `tailwindcss` → utility generation
- `postcss` → CSS transformation pipeline
- `autoprefixer` → browser compatibility

All are **dev dependencies**.

---
# Step 2: Initialize Config Files

```bash
pnpm exec tailwindcss init -p
```

Creates:
- `tailwind.config.js`
- `postcss.config.js`

No global installs involved.

---
# Step 3: Configure Content Scanning

Edit `tailwind.config.js`:
```js
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

Why:
- Tailwind must know **exactly which files to scan**
- Missing paths → missing CSS in production

---
# Step 4: Add Tailwind Directives

Edit `src/index.css` (or equivalent):
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Why:
- These directives are expanded at build time
- Output becomes static CSS in `dist/`

---
# Step 5: Import CSS Entry

Ensure `main.jsx` imports the CSS file:
```js
import "./index.css"
```

Why:
- Vite must include Tailwind output in the bundle

---
# Step 6: Verify

Use a class in `App.jsx`:
```jsx
<h1 className="text-3xl font-bold text-blue-600">
  Tailwind is working
</h1>
```

Run:
```bash
pnpm dev
```

---
# Build-Time Behavior (Important)

During:
```bash
pnpm build
```

Tailwind:
- Scans declared files
- Removes unused classes
- Emits minimal CSS into `dist/`

No Tailwind logic exists at runtime.

---
