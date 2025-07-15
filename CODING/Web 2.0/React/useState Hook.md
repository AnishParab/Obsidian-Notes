# `useState` Theory
- You will want your component to "remember" some information and display it.
- `useState` provides us with **state variable** and **state function**.
- **State variable** ---> To store the state.
- **State function** ---> To change state.

---
# What is State?
- State is an object that determines **how a component renders & behaves**.  
- When state changes, React **re-renders** the component to reflect the updated data.

---
# Why `useState`?
Before hooks:
- Only **class components** could have local state.
- Functional components were **stateless**, useful only for presentational logic.

Hooks like `useState` enabled:
- Functional components to have local state.
- Simpler, cleaner, and more reusable logic.

---
# **Counter Example**
#### `components/Counter.jsx`
``` jsx
import { useState } from 'react'
import React from 'react'

const Counter = () => {
	const [count, setCount] = useState(0);

	return (
		<div className='counter-container'>
			<p id='para'>You have clicked {count} times</p>
			<button id='btn' onClick={() => { setCount(count+1)} }>Click me</button>
		</div>
	)
}

export default Counter
```

---
#### `App.jsx`
``` jsx
import Counter from './components/Counter'

function App() {
	return (
		<div>
			<Counter />
			<Counter />
		</div>
	)
}

export default App
```
- Note that each `Counter component` will remember it's own state and will not affect the other. 

---


