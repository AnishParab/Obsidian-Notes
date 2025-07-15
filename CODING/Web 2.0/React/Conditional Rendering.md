# What is Conditional Rendering?
- Your components will often need to display different things depending on different conditions.
- There is no special syntax in JSX, instead you use regular JS code.
- It can be done using 4 ways given below.

---
# **Example** : Using `if-else`
`components/LoginBtn.jsx`
``` jsx"
import React from "react"

const LoginBtn = () => {
	return (
		<button>
			Login
		</button>
	)
}

export default LoginBtn
```

`components/LogoutBtn.jsx`
``` jsx
import React from 'react'

const LogoutBtn = () => {
	return (
		<button>
			Logout
		</button>
	)
}

export default LogoutBtn
```

`App.jsx`
``` jsx
function App() {
	const [isLoggedIn, setLoggedIn] = useState(true);

	if(isLoggedIn) {
		return (
			<LogoutBtn />
		)
	} else {
		return (
			<LoginBtn />
		)
	}
}

export default App
```

---
# **Example** : Using Ternary/Conditional Operator
`App.jsx`
``` jsx
function App() {
	const [isLoggedIn, setLoggedIn] = useState(true);

	return (
		<div>
			{isLoggedIn ? <LogoutBtn /> : <LoginBtn />}
		</div>
	)
}

export default App
```

---
# **Example** : Using Logical Operator
`App.jsx`
``` jsx
function App() {
	const [isLoggedIn, setLoggedIn] = useState(true);

	return (
		<div>
			<h1>Welcome!</h1>
			<div>
				{isLoggedIn && <LogoutBtn />}
			</div>
		</div>
	)
}

export default App
```

---
# **Example** : Early Return
`App.jsx`
``` jsx
function App() {
	const [isLoggedIn, setLoggedIn] = useState(true);

	if(!isLoggedIn) {
		return (
			<LoginBtn />
		)
	}

	return (
		<div>
			<h1>Welcome!</h1>
			<div>
				{isLoggedIn && <LogoutBtn />}
			</div>
		</div>
	)
}

export default App
```

---


