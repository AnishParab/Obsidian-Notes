# JSX is just **Sugar**
- This:
``` jsx
const element = <h1>Hello</h1>;
```

- ......gets compiled to:
```js
const element = React.createElement("h1", null, "Hello");
```

---
