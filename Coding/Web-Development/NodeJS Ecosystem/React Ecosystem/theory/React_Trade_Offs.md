# 1. Architectural Freedom vs. Fragmentation

React is a **library**, not a framework; it handles the "View" but ignores the rest.

- **The Choice Burden**: You must pick your own routing, state management, and styling solutions.
- **Inconsistency**: No standard folder structure means high onboarding friction between different projects.
- **Setup Overhead**: Achieving production features (SSR, SEO) requires manual configuration or a meta-framework like Next.js.

---
# 2. The Performance "Re-render" Trap

The declarative model can cause hidden bottlenecks.

- **Tree Reconciliation**: By default, a parent state change re-renders the entire subtree.
- **Memory Usage**: Maintaining a Virtual DOM and running "diffing" algorithms costs CPU and RAM.
- **State Design**: Global state (like Context) can trigger app-wide re-renders if not optimized.

---
# 3. Complexity & Abstractions

React requires learning a specific paradigm over standard web APIs.

- **Learning Curve**: You must master Immutability, Hook rules, and the lifecycle.
- **Leaky Abstractions**: JSX and Hooks can mask browser behavior, complicating debugging.
- **Prop Drilling**: Over-componentizing forces data through deep layers that don't need it.

| **Trade-off**       | **Impact**                                                                  |
| ------------------- | --------------------------------------------------------------------------- |
| **Logic Pollution** | Business and UI logic often get tangled, hurting testability.               |
| **Hook Rules**      | Mismanaging `useEffect` dependencies leads to infinite loops or stale data. |

---
# 4. Discipline Over Labor

- **Vanilla JS**: You pay in **manual labor** (DOM manipulation).
- **React**: You pay in **architectural discipline** (managing boundaries and state).

---
