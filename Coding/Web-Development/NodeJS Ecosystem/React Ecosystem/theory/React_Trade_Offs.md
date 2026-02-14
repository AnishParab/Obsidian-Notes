# React: Costs and Trade-offs

## 1. Freedom → Fragmentation
- React = UI only
- You choose everything else

**Results**
- No standard structure
- Higher setup cost
- SSR / SEO need Next.js

---
## 2. Re-render Trap

- Parent state change → subtree re-renders
- VDOM costs CPU + memory
- Bad state placement = slow app

---
## 3. Abstraction Cost

- React-specific model required

**Issues**
- Immutability, Hooks, lifecycle
- JSX hides browser behavior
- Prop drilling
[]()
**Failure Modes**
- Mixed logic → hard to test
- Bad `useEffect` deps → loops / stale state

---
## 4. Cost Model

- Vanilla JS: manual DOM work
- React: discipline and structure

---
