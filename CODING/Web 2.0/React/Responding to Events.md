- You can respond to events by declaring _event handler_ functions inside your components:

---
# Example Code
- By using `onClick` Event Handler.
``` jsx
function MyButton() {
	function handleClick {
		alert("Button was clicked")
	}

	return (
		<button onClick={handleClick}>
			Click Me
		</button>
	);
}
```
- Notice how `onClick={handleClick}` has no parentheses at the end! Do not _call_ the event handler function: you only need to _pass it down_.

---
