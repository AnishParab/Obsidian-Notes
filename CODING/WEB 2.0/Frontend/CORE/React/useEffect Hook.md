# What is `useEffect` Hook?
- It is a react hook to generate **side-effects**.
- **example** ---> When DOM content loads (Event) , Connect to DB (Side-Effect).
- **example** ---> Whenever content renders (Event) , fetch API (Side-Effect).
- **example** ---> Whenever count state variable updates from useState (Event) , show an alert (Side-Effect).
- **example** ---> Whenver logged in (Event) , Show profile photo (Side-Effect)

---
# Syntax
`App.jsx`
``` jsx
import { useEffect } from 'react'

function App() {
	useEffect(() => {
		first

		return () => {
			second
		}
	}, [third])

	return (
		<div>
			Hello Jee
		</div>
	)
}

export default App
```

- **first** ---> Side-Effect Function.
- **second** ---> Clean-up Function.
- **third** ---> Comma-separated dependency list.

---
# Each of the variations are with respect to the Counter App using `useState` Hook
- Basically a button to update the _count_ each time the button is clicked.

---
# **Variation 1 : Runs on every Render**
``` jsx
useEffect(() => {
	alert("I will run on each render")
})
```
- This will run on each render.
- Since in development mode, in `main.jsx` ---> `App.jsx` is wrapped in `<StrictMode />` which runs the app **twice** (By convention).

> **Basically**, it runs everytime UI is rendered.

---
# **Variation 2 : Runs on only First Render**
``` jsx
useEffect(() => {
	alert("I will run on only first render")
}, [])
```
- Instead of every render, This will run only on **First Render**.

> **Basically**, it runs only on first UI render.

---
# **Variation 3 : Runs every-time when count is updated**
``` jsx
// Implement count using useState

useEffect(() => {
	alert("I will run everytime when count is updated")
}, [count])
```
- Runs only when count is updated.

> **Basically**, it runs only after count is updated and before the UI is rendered.

---
# **Variation 4 : Multiple Dependencies**
``` jsx
import { useState } from 'react'

function App() {
	const [count, setCount] = useState(0);
	const [total, setTotal] = useState(1);

	useEffect(() => {
		alert("I will run every time when count OR total is updated")
	}, [count, total])

	function handleClick() {
		setCount(count+1)
	}

	function handleClickTotal() {
		setTotal(total+1)
	}

	return (
		<div>
			<button onClick={handleClick}>
				Update Count
			</button>
			<br />
			Count is : {count}

			<button onClick={handleClickTotal}>
				Update Total
			</button>
			<br />
			Total is : {total}
		</div>
	)
}
```

---
# **Adding a Cleanup Function**
- For example, when count is **unmounted** from the UI.
``` jsx
useSffect(() => {
	alert("Count is updated")

	return () => {
		alert("Count is unmounted from UI")
	}
}, [count])
```
- Count = 0.
- Count unmounted from UI.
- Count + 1.
- Count = 1.
- Count unmounted from UI.
- Count + 1.
- Count = 2.
- Counted unmounted from UI..........

**unmount** ---> Component removed from code.

---