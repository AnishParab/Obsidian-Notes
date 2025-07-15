# Passing Complex Expressions inside JSX curly braces
**Example**: String Concatenation
``` jsx
const user = {
	name: 'Anish Parab',
	imageUrl: 'https://i.imgur.com/yXOvdOSs.jpg',
	imageSize: 90,
};

export default function Profile() {
	return (
		<>
			<h1>{user.name}</h1>
			<img
				className="avatar"
				src={user.imageUrl}
				alt={'Photo of ' + user.name}
				style={{
					width: user.imageSize,
					height: user.imageSize
				}}
			/>
		</>
	);
}
```

**NOTE :** You can use `style` attribute when your styles depend on JavaScript variables.

---

