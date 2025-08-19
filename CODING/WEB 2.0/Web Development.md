## 0) System & Workflow (Arch + Neovim + Git)
-  **Dotfiles & shells**
    -  zsh + fzf + ripgrep + bat
    -  asdf / fnm for Node versions
    -  pnpm + corepack
-  **Neovim IDE**
    -  Lazy.nvim (or equivalent)
    -  LSP: tsserver, eslint, tailwindcss, jsonls
    -  Treesitter, Telescope, Gitsigns, Conform/Null-ls
    -  Debugging: nvim-dap (JS/TS)
-  **Git mastery**
    -  Rebase vs merge, fixup/squash, bisect, blame
    -  Signing commits, hooks (lint-staged)
-  **Hard Mode**: Use only terminal + tmux + nvim to build and ship a tiny site.

---
## 1) Internet & Web Foundations
-  HTTP/HTTPS, DNS, TCP/IP, CORS, caching, CDNs
-  Request lifecycle (browser → edge → server → DB → server → browser)
-  REST, GraphQL (concepts), gRPC (concepts), WebSockets vs SSE
-  **Hard Mode**: Build a raw HTTP server in Node _without_ frameworks that serves HTML, static files, and a JSON API.

---
## 2) HTML (Hard Mode)
-  Semantic tags, forms, ARIA basics, a11y patterns
-  SEO essentials (meta, OpenGraph), microdata/JSON-LD
-  Progressive enhancement
-  **Hard Mode**: Recreate a complex form (nested fieldsets, validation, a11y) with zero JS.

---
## 3) CSS (Deep Dive)
-  Layouts: Flexbox, Grid; fluid typography; container queries
-  Specificity, cascade layers; custom properties; dark mode
-  Animations (pure CSS), rendering/perf (paint, composite)
-  **Hard Mode**: Build a responsive dashboard with Grid only; no frameworks.

---
## 4) Modern JavaScript (No crutches)
-  Execution model: call stack, event loop, microtasks
-  Scope/closures, prototypes, this/bind/call/apply
-  Modules (ESM), fetch/streaming, AbortController
-  **Hard Mode**: Implement a minimal state store and a virtual DOM patcher.

---
## 5) TypeScript (Strict)
-  tsconfig (strictest reasonable), moduleResolution, path aliases
-  Generics, discriminated unions, conditional types
-  Typing React/Next patterns (server actions, RSC, zod schemas)
-  **Hard Mode**: Refactor your JS state store to TS with full type safety.

---
## 6) React (from first principles → ecosystem)
-  Mental model: rendering, reconciliation, Suspense
-  Hooks deeply: useMemo/useCallback pitfalls; custom hooks
-  Concurrent features, transitions, error boundaries
-  **State & Data under React**
    -  **Zustand** (co-located global state)
    -  **Redux Toolkit** (normalized entities, RTK Query basics)
    -  **TanStack Query** (server cache, mutations, invalidation)
    -  **TanStack Router** (file routing alt), **SWR** (lightweight fetch cache)
-  **Icons & UX Add-ons**
    -  **react-icons** usage patterns
    -  **lucide-react** tree-shaking + icon theming
-  **Hard Mode**: Build a Trello-like board with optimistic updates (TanStack Query) and a global slice (Zustand/RTK) for UI state.

---
## 7) TailwindCSS Ecosystem (component primitives → full systems)
-  Tailwind fundamentals + design tokens; v4 utilities & best practices
-  **Radix UI**: accessible, unstyled primitives (focus, keyboard nav)
-  **shadcn/ui**: copy-in component system built on Tailwind + Radix (understand “not a package”, customize tokens, slots). ([Medium](https://medium.com/%40immairaj/my-tiny-guide-to-shadcn-radix-and-tailwind-da50fce3140a?utm_source=chatgpt.com "My Tiny Guide to Shadcn, Radix, and Tailwind | by Mairaj Pirzada"))
-  **Skiper UI**: Tailwind + TS component set; integrates with shadcn but optional; uses Framer Motion for animations. ([skiper/ui](https://skiper-ui.com/docs/installation?utm_source=chatgpt.com "Installation - skiper/ui"))
-  Composition patterns: headless primitives (Radix) → styled (shadcn / Skiper)
-  **Hard Mode**: Recreate a complex UI kit (tabs, dialog, command palette) from Radix primitives before adopting shadcn/Skiper. (Skiper provides components and can live alongside shadcn.) ([skiper/ui](https://skiper-ui.com/docs/installation?utm_source=chatgpt.com "Installation - skiper/ui"), [shadcn.io](https://www.shadcn.io/template/skiper-ui-skiper-ui?utm_source=chatgpt.com "Skiper UI - shadcn.io"))

---
## 8) Animation & Motion
-  **Framer Motion**: layout animations, gestures, shared layout, scroll
-  Perf: will-change, reduced motion, avoiding layout thrash
-  **Hard Mode**: Animate route transitions and nested layouts with exit/enter + staggered lists at 60fps.

---
## 9) Next.js (App Router, Full-stack)
-  App Router + RSC: server components, client boundaries, Suspense
-  Data fetching & caching: fetch cache tags, ISR, route handlers, **Server Actions** (with Zod validation)
-  Middleware & Edge Runtime; headers/cookies
-  SEO: metadata API, dynamic sitemaps, OpenGraph images
-  File uploads: **Multer** (Node route handlers) vs edge-safe options; **ImageKit** for CDN, transforms, signed uploads
-  **Hard Mode**: Build a multi-tenant app with org routing (`/org/[slug]`), RBAC middleware, and streaming RSC payloads.

---
## 10) Data & Backends (Modern, typed, production-grade)
**Primary stack:** TypeScript • Next.js Route Handlers/Server Actions • Postgres • Prisma/Drizzle • Redis • Clerk • Zod

### 10A) Databases & ORMs
-  Relational: PostgreSQL (Neon/Aiven), MySQL (PlanetScale), SQLite (Turso/LibSQL)
-  NoSQL: MongoDB (Atlas) where document model fits; Redis for cache/queues
-  Modeling: normalization vs denormalization; indexes; transactions
-  Migrations & schema drift; connection pooling on serverless
-  **ORM**: Prisma (Zod inference, type-safe queries) or Drizzle (SQL-first)
-  **Hard Mode**: Design schema for a social app: followers, activity feed, notifications with `READ COMMITTED` + outbox pattern.

### 10B) API Design & Delivery
-  REST best practices: versioning, pagination, filtering, rate limits
-  tRPC (optional): TS-end-to-end types using Zod schemas
-  Webhooks & retries; idempotency keys; background jobs
-  **Hard Mode**: Build an idempotent checkout API with retries and poison-queue handling.

### 10C) AuthN/AuthZ (Modern)
-  **Clerk**: email/OAuth/passwordless, orgs, sessions, webhooks; SSR/RSC integration; middleware guards
-  RBAC/ABAC design; row-level security at DB when applicable
-  Session fixation, CSRF/XSS protections; cookie vs JWT tradeoffs
-  **Hard Mode**: Implement organization-scoped roles and feature flags enforced at API + UI + SQL levels.

### 10D) Validation & Schemas
-  **Zod**: server actions, forms, API contracts; `zodResolver` with forms; error mapping
-  Runtime validation vs static types; safeParse pipelines
-  **Hard Mode**: A single Zod schema drives: (1) form UI, (2) server validation, (3) DB constraints (via migration).

### 10E) Files, Media, and Image Pipeline
-  **Multer** multipart handling (Node/Next route handlers)
-  **ImageKit**: signed uploads, transformation URLs, responsive images; cache headers strategy
-  **Hard Mode**: Direct-to-ImageKit uploads from client with server-signed tokens; generate low-quality placeholders on the fly.

---
## 11) State, Data-Fetching & i18n (Front of House)
-  **Zustand**: co-located stores, middleware (persist, immer)
-  **Redux Toolkit**: entity adapters, RTK Query for CRUD
-  **TanStack Query**: dedup, staleTime, suspense, optimistic updates
-  **SWR**: tiny fetch cache (compare to TSQ)
-  **react-i18next**: namespaces, lazy loading, RSC-safe translations
-  **Hard Mode**: Offline-first notes app: cache, background sync, i18n switcher, conflict resolution.

---
## 12) 3D & Visuals
-  **Three.js** basics: scene, camera, renderer; GLTF pipeline
-  React integration (react-three-fiber) + drei helpers
-  Perf: instancing, BVH, suspense for assets
-  **Hard Mode**: Landing page hero with 3D model + Framer Motion UI sync.

---
## 13) Testing, Quality & Tooling
-  **Jest**: unit + integration; test doubles; TS config; coverage thresholds
-  **Cypress**: e2e + component test; CI parallelization; network stubbing
-  Linting/formatting: eslint (ts, react, tailwind), biome or prettier
-  **Hard Mode**: Red/Green/Refactor pipeline for a feature: unit → integration → e2e with fixtures & data seeding.

---
## 14) Performance, Security & Observability
-  Web perf: Core Web Vitals, RUM, code-split, prefetch, image strategy
-  Backend perf: N+1 avoidance, caching tiers (CDN → Redis → DB)
-  Security: OWASP Top 10; CSP, CSRF tokens, prepared statements
-  Observability: structured logs, metrics (Prometheus), tracing (OpenTelemetry), error tracking (Sentry)
-  **Hard Mode**: Reproduce and fix a production-only race condition using distributed traces.

---
## 15) DevOps for Web Devs (Ship like a pro)
-  Docker basics (multi-stage builds), docker-compose for local stacks
-  CI/CD: GitHub Actions (lint → test → build → deploy)
-  Infra targets: Vercel (Next + Edge), Fly.io/Render for workers, Cloudflare for KV/Queues/Workers
-  Secrets & envs: Doppler/1Password; `.env.production` hygiene
-  **Hard Mode**: Blue/green or canary deploy with feature flags + DB migration safety (shadow tables).

---
## 16) React Native + Expo (TypeScript)

-  Expo project structure, **expo-router** (file routing)
-  Styling: NativeWind (Tailwind-like) or Tamagui; icons (lucide-react-native)
-  Image handling: **expo-image**; caching; ImageKit upload flow
-  Navigation: tabs, stacks, deep linking; safe-area; gestures
-  Data layer: TanStack Query + Clerk for mobile (JWT/session)
-  **Hard Mode**: Offline-capable app with background sync and biometric auth.

---
## 17) Capstones (Pick one and go all in)
-  **SaaS dashboard** (multi-tenant): Next.js (App Router) + Clerk + Postgres + Prisma + Redis + ImageKit + TanStack Query + shadcn/Skiper UI + Radix + Zod + Jest + Cypress + Vercel
-  **Realtime collaboration tool**: CRDT or OT, websockets, optimistic UX, presence indicators
-  **3D commerce landing**: Three.js hero + edge cached product pages + signed media
**Capstone Hard Mode**: instrument with tracing, add feature flags, and run a load test to SLAs you define.

---
# Appendices
## A) Backend Master List (quick reference)
-  **App architecture**: monolith → modular → microservices; CQRS/event-driven; clean/hexagonal
-  **APIs**: REST, tRPC (TS end-to-end), Webhooks, WebSockets
-  **DB**: Postgres/MySQL/SQLite; Redis; Mongo; sharding/replication; migrations
-  **Auth**: Clerk; sessions vs JWT; RBAC/ABAC; MFA; SSO
-  **Validation**: Zod (runtime), schema inference
-  **Files/Media**: Multer; ImageKit (CDN, transforms)
-  **Perf**: caching tiers; queues (BullMQ/Redis), backpressure
-  **Security**: OWASP 10; secrets; rate limiting; audit logs
-  **Observability**: logs/metrics/traces; SLOs; error budgets
-  **DevOps**: Docker; CI/CD; edge/serverless deploy; IaC (light)

## B) Project Sequence (milestones)
1.  **Foundations App**: static site → Node raw server → TS refactor
2.  **React Core**: SPA with custom store → data fetching with TSQ
3.  **UI System**: Radix primitives → shadcn components → Skiper components swap test ([skiper/ui](https://skiper-ui.com/docs/installation?utm_source=chatgpt.com "Installation - skiper/ui"))
4.  **Next Full-stack**: RSC + Server Actions + Zod; Clerk auth; Postgres + Prisma; ImageKit uploads; tests; deploy
5.  **Mobile Twin**: Expo app consuming the same API (and/or tRPC)

## C) Opinionated Defaults & Tips
- Prefer **TanStack Query** over SWR for complex server state; use **Zustand** for local UI state; **RTK** only when entity graphs or large teams need stricter patterns.
- Start with **Prisma**, switch to **Drizzle** if you want SQL-first migrations.
- Use **Clerk** for auth flows (passwordless/MFA/orgs).
- Use **ImageKit** for media; avoid storing originals on the app server.
- Build UI on **Radix primitives**; layer **shadcn** for speed; add **Skiper UI** selectively where its components fit your design system. ([skiper/ui](https://skiper-ui.com/docs/installation?utm_source=chatgpt.com "Installation - skiper/ui"), [Medium](https://medium.com/%40immairaj/my-tiny-guide-to-shadcn-radix-and-tailwind-da50fce3140a?utm_source=chatgpt.com "My Tiny Guide to Shadcn, Radix, and Tailwind | by Mairaj Pirzada"))

---

# Progress Checklist (single glance)
-  0) System & Workflow
-  1) Internet & Web Foundations
-  2) HTML
-  3) CSS
-  4) JavaScript
-  5) TypeScript
-  6) React
-  7) Tailwind + Radix + shadcn + Skiper
-  8) Animation (Framer Motion)
-  9) Next.js (App Router, RSC, Server Actions)
-  10) Data & Backends (DB/ORM/Auth/Zod/Files)
-  11) State/Data/i18n
-  12) Three.js
-  13) Testing (Jest/Cypress)
-  14) Perf/Security/Observability
-  15) DevOps (Docker/CI/CD/Edge)
-  16) React Native + Expo
-  17) Capstone

---
