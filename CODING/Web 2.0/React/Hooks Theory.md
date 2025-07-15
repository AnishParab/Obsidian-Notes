# What are Hooks?
- Functions starting with `use` are called **Hooks**.
- Hooks are special functions that let you _hook into_ React's in-built features from _functional components_

---
# Why Hooks?
- Before Hooks, only **class components** could manage state and use lifecycle methods.
- Hooks brought those features to **functional components**.

---
# Commonly used Hooks
| Hook          | Purpose                                              |
| ------------- | ---------------------------------------------------- |
| `useState`    | Manage state inside a functional component           |
| `useEffect`   | Run side-effects (e.g. API calls, timers)            |
| `useContext`  | Share state globally via context                     |
| `useRef`      | Hold mutable values and access DOM nodes             |
| `useReducer`  | More advanced alternative to `useState` (like Redux) |
| `useMemo`     | Optimize expensive calculations                      |
| `useCallback` | Optimize function references between renders         |

---
# Rules of Hooks
- Only call hooks **at the top level** (not inside loops, conditions, or nested functions).
- Only call hooks **inside functional components** or **custom hooks**.
- Never call hooks inside regular JS functions or class components.

---







