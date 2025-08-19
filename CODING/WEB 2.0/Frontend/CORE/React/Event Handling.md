# `onClick` Event Listener
`App.jsx`
``` jsx
function App() {
	function handleClick() {
		alert("I am clicked");
	}

	return (
		<div>
			<button onClick={handleClick}>
				Click Me
			</button>
		</div>
	)
}

export default App
```

---
# `onMouseOver` Event Listener
`App.jsx`
``` jsx
function App() {
	function handleMouseOver() {
		alert("Blah Blah Blah");
	}

	return (
		<div>
			<p onMouseOver={handleMouseOver}>
				I am a Para.
			</p>
		</div>
	)
}

export default App
```

---
# `onChange` and `onSubmit` Event Listener
`App.jsx`
``` jsx
function App() {
	function handleInputChange(e) {
		console.log("Value till now: ", e.target.value)
	}

	function handleSubmit(e) {
		e.preventDefault(); // refresh aur reload mat karo
		// I am writing my custom behaviour down
		alert("Should we submit the form?");
	}

	return (
		<div>
			<form onSubmit={handleSubmit}>
				<input type='text' onChange={handleInputChange}/>

				<button>
					Submit
				</button>
			</form>
		</div>
	)
}

export default App
```

---
# **What is Immediate Invocation**
`App.jsx`
``` jsx
function App() {
	return (
		<div>
			<button onClick={alert("Button is Clicked")}>
				Click Me
			</button>
		</div>
	)
}

export default App
```
- If no function is called inside `onClick` event listener, whatever code that has been written is invoked.
- Hence, It should be written using **function reference**:
``` jsx
	<button onClick={() => alert("Button is Clicked")}>
```

---
# `e.stopPropagation`
- This stops event bubbling.

---
