# Use of Curly Braces
- JSX lets you put markup into javascript.
- **Curly braces let you "escape back" into Javascript .**

---
# Example for Method 1
``` jsx
return (  
	<h1> {user.name} </h1>
);
```

---
# Use of Curly Braces in JSX Attributes

#### `src` attribute
``` jsx
return (
	<img
		classname="avatar"
		src={user.imageUrl}
	/>
);
```

---
