# Jade & Pug

- Server-side template engines used for SSR in Express.
- Compile indentation-based templates → HTML.

```id="v1x3na"
res.render('file') → Pug compiles → HTML response
```

Jade = old name (legacy).  
Pug = maintained successor.

---
# **Separation of Concerns**

- **Routing** -> map _URL_ -> handler
- **Business Logic** -> fetch/process data
- **Presentation** -> generate _HTML_

> **Jade/Pug** exists to isolate these 3.

---
# Mental Model

```id="y0u4dw"
Route → res.render() → Pug → HTML
```

---
# Where It Connects in Express

Configured in `app.js`:
```js
app.set('view engine', 'pug')
```

Used inside routes:
```js
res.render('index')
```

---
# Core Syntax

### Indentation = Structure
```pug
ul
  li One
  li Two
```

### Tags

```pug
h1 Title
p Text
```

### Attributes

```pug
a(href="/home") Home
```

### Variables

```pug
p= username
```

### Conditionals

```pug
if loggedIn
  p Welcome
```

---
# Debug Notes

- Wrong indentation → broken layout.
- “Failed to lookup view” → wrong `views` path.

> Syntax errors occur during render, not routing.

---
