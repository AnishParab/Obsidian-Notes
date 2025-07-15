# General Flow
`index.html` ---> `main.jsx` ---> `App.jsx`

---
# General, Modern Project Structure
``` css
my-app/
├── public/
│   ├── index.html
│   └── favicon.svg
├── src/
│   ├── assets/              # Static assets (images, fonts, etc.)
│   ├── components/          # Reusable UI components
│   │   └── Button/
│   │       ├── Button.tsx
│   │       └── Button.module.css
│   ├── features/            # Feature-specific components & logic (domain-driven)
│   │   └── auth/
│   │       ├── components/
│   │       ├── hooks/
│   │       ├── api.ts
│   │       └── authSlice.ts
│   ├── hooks/               # Global custom hooks
│   ├── layouts/             # Page layouts / layout wrappers
│   ├── pages/               # Top-level pages
│   │   └── Home.tsx
│   ├── routes/              # Routing configs
│   │   └── AppRoutes.tsx
│   ├── services/            # API service layer (axios, fetch)
│   │   └── apiClient.ts
│   ├── store/               # Global state management (Redux, Zustand, etc.)
│   │   ├── index.ts
│   │   └── slices/
│   ├── styles/              # Global styles (Tailwind config, CSS variables)
│   ├── types/               # Global TypeScript types/interfaces
│   ├── utils/               # Utility functions/helpers
│   ├── App.tsx
│   └── main.tsx
├── .editorconfig
├── .eslintrc.cjs
├── .prettierrc
├── tailwind.config.js
├── tsconfig.json
├── package.json
└── README.md
```

---
