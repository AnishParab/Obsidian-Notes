# What?
- **React Strict Mode** is a **tool for highlighting potential problems in an application**.  
- It **doesn’t render anything visible in the UI**

---
# Double Invoking
- Since in development mode, in `main.jsx` ---> `App.jsx` is wrapped in `<StrictMode` which runs the app twice (By convention).
- **Unexpected side effects** by intentionally double-invoking:
	- `constructor`
	- `render`
	- `setState` updater functions
	- `useState` / `useReducer` initializers

---
# Also helps Detect
- **Unsafe lifecycle methods** (like legacy methods that might break with concurrent rendering)
- **Side effects in render phase** (e.g., if you accidentally mutate state or run effects directly inside render)
- **Usage of deprecated APIs** (e.g., `findDOMNode`, `legacy context API`)

---
