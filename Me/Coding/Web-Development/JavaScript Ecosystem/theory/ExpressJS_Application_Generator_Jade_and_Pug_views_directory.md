# Purpose of `views/`

- Stores `.pug` template files.
- Used only when `res.render()` is called.

Typical structure:
```id="n2c7qt"
views/
├── layout.pug
├── index.pug
└── error.pug
```

---
# How Express Finds Views

Configured in `app.js`:

```js
app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'pug')
```

Meaning:
- Express searches this folder when rendering templates.

---
# Rendering Flow

```id="4k6u1g"
res.render('index')
   ↓
Express looks inside views/
   ↓
index.pug compiled → HTML
```

---
# Common Debug Issues

### 1. “Failed to lookup view”

Causes:
- Wrong file name.
- Incorrect `views` path.
- Missing `.pug` file.

### 2. Layout Not Applying

Check:
```pug
extends layout
block content
```

Missing `block` definitions break inheritance.

### 3. Static Files Not Loading

Reason:
- Static middleware serves from `public/`, not `views/`.
`views/` is not publicly accessible.

### 4. Wrong Render Name

```js
res.render('index')   // correct
res.render('index.pug') // incorrect
```

Express resolves extension automatically.

---
# Debug Mental Model

```id="v2o9wl"
routes/ → res.render()
           ↓
views/ lookup
           ↓
Pug compile
```

If rendering fails, inspect:
1. File name inside `views/`
2. Layout inheritance
3. Indentation errors in template

---
# Key Rule

```text
views/ is a template source directory, not a public folder.
```

---
