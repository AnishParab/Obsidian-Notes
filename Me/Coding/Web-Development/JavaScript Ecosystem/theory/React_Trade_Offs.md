# React Costs and Tradeoffs

- Freedom → fragmentation: no standard structure, high setup cost, SSR/SEO needs Next.js
- Re-render trap: parent state change re-renders subtree; bad state placement = slow app; VDOM has CPU + memory overhead
- Abstraction cost: must internalize immutability, Hooks, lifecycle; JSX hides browser behavior; prop drilling
- Bad `useEffect` deps → infinite loops or stale state
- Mixed logic → hard to test

> Cost model: Vanilla JS = manual DOM work. React = discipline and structure.

---
