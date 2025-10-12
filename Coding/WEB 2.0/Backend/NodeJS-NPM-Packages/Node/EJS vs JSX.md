# EJS (Embedded JavaScript Templates)

- **Purpose**:  
	Server-side rendering of HTML using JavaScript logic in a **Node.js** (usually Express) backend.

- **File Extension**: `.ejs`

- **Where it's run**: **On the server**

- **Used with**: `Express.js`, traditional full-stack apps with server-rendered HTML

### Example
``` ejs
<h1>Hello, <%= user.name %>!</h1>
<% if (isAdmin) { %>
  <button>Delete</button>
<% } %>
```

> This gets rendered into plain HTML on the server and sent to the browser.


---
# JSX (JavaScript XML)
- **Purpose**:  
	Used in **React** to write UI components by combining JavaScript and HTML-like syntax.

- **File Extension**: `.jsx` or `.tsx` (if using TypeScript)

- **Where it's run**: **In the browser** (after being compiled by tools like Babel)

- **Used with**: `React.js`, React Native, etc.

### Example
``` jsx
function Welcome({ user }) {
  return <h1>Hello, {user.name}!</h1>;
}
```

> JSX is **not valid JS by itself** — it needs to be transpiled (usually via **Babel**) into standard JavaScript.

---
# Key Differences

| Feature            | EJS                              | JSX                                 |
| ------------------ | -------------------------------- | ----------------------------------- |
| Environment        | Server-side                      | Client-side                         |
| Used in            | Node.js + Express apps           | React apps                          |
| Syntax Style       | `<% %>`, `<%= %>`                | Looks like HTML inside JS (`<div>`) |
| Output             | Plain HTML                       | React elements                      |
| Needs compilation? | No (just rendered as template)   | Yes (transpiled by Babel)           |
| Logic Style        | JS control structures in `<% %>` | JS expressions in `{}`              |

---
