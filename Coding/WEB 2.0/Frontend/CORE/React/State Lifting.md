# What?
Sharing Data between components is known as **State Lifting.**

---
# Default Data Flow of Props
- Default Data Flow is from Parent to Child.
![[stateLifting.excalidraw]]

---
# State Lifting
- This concept can be used the following cases:
![[stateLiftind2.excalidraw|1000]]

---
# Example Solving
- Inorder to do this, you need to **create, manage, change and sync states** in the _parent_ itself.
`App.jsx`
``` jsx
import { useState } from 'react'
import Card from './components/Card'

function App() {
	const [name, setname] = useState('');

	return (
		<div>
			<Card title="Card1" name={name} setName={setName}/>
			
			<Card title="Card2" name={name} setName={setName}/>

			<p>I am inside Parent Component and Value of name is: {name} </p>
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
			<input type="text" onChange={() => props.setName(e.target.value)} />

			<p>Name state variable ki value inside {props.title}: {props.name}</p>
		</div>
	)
}

export default Card
```

---
# **A Simpler Counter Example**
`App.jsx`
``` jsx
import { useState } from 'react'

export default function MyApp() {
	const [count, setCount] = useState(0);

	function handleClick() {
		setCount(count + 1);
	}

	return (
		<div>
			<h1>Counters that update together</h1>
			<MyButton count={count} onClick={handleClick}/>
			<MyButton count={count} onClick={handleClick}/>
		</div>
	);
}

// TO Read the Props
function MyButton({ count, onClick}) {
	return (
		<button onClick={onClick}>
			Clicked {count} times
		</button>
	);
}
```

- Using `useState` ---> **Lifting State up**.
- Using `<MyButton count={count} onClick={handleClick}/>` ---> **Pass state down** using **Props**. 

---
