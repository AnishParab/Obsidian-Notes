# What's Children?
- Anything passed **between** the opening and closing tags of a component becomes that component’s **`props.children`**.
``` jsx
<Card>
	//Anything between this is called as it's Children
</Card>
```

**Use-Cases:**
- Wrappers
- Layout components
- Modals, tooltips, etc.

---
# Syntax
`App.jsx`
``` jsx
import Card from './components/Card'

function App() {
	return (
		<div>
			<Card name="Anish">
				<h1>This is Children</h1>
				<p>This is Children</p>
			</Card>

			<Card children="Bonjourr">
				Hello There  // This is prefered
			</Card>
		</div>
	)
}

export default App
```

`components/Card.jsx`
``` jsx
import React from 'react'

const Card = (props) => {
	return (
		<div>
			{props.name}
			{props.children}
		</div>
	)
}

export default Card
```

---
# Passing Props as Function
`components/Button.jsx`
``` jsx
import React from 'react'

const Button = (props) => {
	return (
		<div>
			{props.children}
			<button onClick={props.handleClick}>
				{props.text}
			</button>
		</div>
	)
}

export default Button
```

`App.jsx`
``` jsx
import Button from './components/Button'

function App() {
	return (
		const [count, setCount] = useState(0);

		function handleClick() {
			setCount(count+1);
		}

		<div>
			<Button incrementCount={handleClick} text="Click me">
				<h1>{count}</h1>
			</Button>
		</div>
	)
}

export default App
```

---
