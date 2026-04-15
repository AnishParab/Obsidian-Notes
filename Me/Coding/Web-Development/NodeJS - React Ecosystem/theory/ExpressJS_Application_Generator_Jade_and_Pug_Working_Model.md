# Rendering Flow

```id="p7q1nb"
Client Request
   ↓
Route Handler
   ↓
res.render('view', data)
   ↓
Pug Compiler
   ↓
HTML Response
```

Templates execute only when `res.render()` is called.

---
# Key Rule

```id="d3h7yo"
No res.render() → No Pug execution
```

---
# Data Flow

Route sends data:
```js
res.render('index', { username: 'asp' })
```

Template receives:
```pug
p= username
```

---
# Express Configuration Link

```js
app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'pug')
```

Meaning:
- Express knows where templates live.
- Pug handles compilation.

---
# Execution Boundary

Pug affects only presentation:
```id="r0l6us"
Middleware → Router → Pug → Response
```

It does not change:
- Routing logic
- HTTP methods
- Middleware execution

---
# Debug Signals

| Symptom              | Likely Cause                     |
| -------------------- | -------------------------------- |
| Data undefined       | Missing object in `res.render()` |
| Layout issues        | Wrong indentation                |
| Render never happens | Route not calling `res.render()` |

---
