# Approach
- You will rely on Javascript features like:
	- `for loop`
	- `array map() function`
	to render lists of components.

---
# Example
- **You have array of products:**
``` js
const products = [
	{ title: 'Cabbage', id: 1},
	{ title: 'Garlic', id: 2},
	{ title: 'Apple', id: 3},
];
```

- **Inside your component, use the `map() function` to transform an array of products into an array of `<li>` items:**
``` jsx
const listItems = products.map(product =>
	<li key={product.id}>
		{product.title}
	</li>
);

return (
	<ul>{listItems}</ul>
);
```

#### Final Code
`App.jsx`
``` jsx
const products = [
	{ title: 'Cabbage', isFruit: false, id: 1 },
	{ title: 'Garlic', isFruit: false, id: 2 },
	{ title: 'Apple', isFruit: true, id: 3 },
];

export default function ShoppingList() {
	const listItems = products.map(product =>
		<li
		key={product.id}
		style={{
			color: product.isFruit ? 'magenta' : 'darkgreen'
		}}
		>
			{product.title}
		</li>
	);

	return (
		<ul>{listItems}</ul>
	);
}
```

---
