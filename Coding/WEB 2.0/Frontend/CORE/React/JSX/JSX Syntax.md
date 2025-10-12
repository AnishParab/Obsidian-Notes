# Basic Syntax
- You can embed HTML directly into JS:
``` jsx
const element = <h1>Hello, World!</h1>;
```
- This returns a React element, not a string or HTML.

---
# Rules of JSX
- It must return a single parent element:
``` jsx
return (
  <div>
    <h1>Title</h1>
    <p>Paragraph</p>
  </div>
);
```

---
# Use `classname` instead of `class`
- HTML Code:
``` html
<div class="container"></div>
```

- JSX Code:
``` jsx
<div className="container"></div>
```

---
# JSX in Javascript
- You can embed JS expressions using `{}`
``` jsx
const name = "Anish";

return <h1>Hello, {name}!</h1>;
```

---
# Self closing tags are required for empty elements
``` jsx
<br />
<img src="logo.png" />
```

---














