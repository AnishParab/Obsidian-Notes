# CommonJS
- **CommonJS** is a **module system** used in Node.js to structure JavaScript code into reusable, isolated units using `require()` and `module.exports`.

### Key Features:
- Uses `require()` to import modules.
- Uses `module.exports` or `exports` to export functions/objects.
- Synchronous by design — ideal for server-side code in Node.js.
- Each file is treated as a module.

### Example
``` js
// math.js
function add(a, b) {
  return a + b;
}
module.exports = add;

// app.js
const add = require('./math');
console.log(add(2, 3)); // 5

```

---
# EJS (Embedded JS)
- **EJS** (Embedded JavaScript) is a **templating engine** for generating HTML with embedded JavaScript logic, commonly use in Express.js for server-side rendering.

### Key Features:
- Lets you embed JavaScript in HTML using `<% %>` syntax.
- Used to dynamically generate HTML pages with data from the backend.
- Supports partials, layouts, and logic like loops and conditionals.

### Example
`ejs`
``` ejs
<!-- views/index.ejs -->
<h1>Welcome, <%= user.name %>!</h1>
```

`js`
``` js
// server.js (using Express)
res.render('index', { user: { name: 'Aryan' } });

```

---
