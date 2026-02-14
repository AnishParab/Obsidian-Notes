# Virtual DOM Workflow

## Core Idea
- React does **not** re-render the entire DOM
- Updates are calculated, then minimized

---
## Steps

1. **Render**
    - UI → lightweight JS objects (VDOM)
2. **Diffing**
    - Compare new VDOM with previous snapshot
3. **Reconcile**
    - Apply only changed nodes to real DOM

---
## Important Note

- Virtual DOM is **not inherently faster**
- Value = declarative model + batched, minimal updates

---
