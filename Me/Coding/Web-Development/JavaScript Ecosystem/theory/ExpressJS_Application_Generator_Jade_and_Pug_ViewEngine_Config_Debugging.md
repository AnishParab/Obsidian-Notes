# Why this matters

Most rendering bugs are not inside `.pug` files.  
They come from incorrect engine wiring inside `app.js`.

You currently cover syntax and `views/`, but not the configuration layer.

---
# What this file should contain (scope)

Minimal focus areas:
```js
app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'pug')
```

Debug checks:
- Wrong views path
- Engine not registered
- Multiple template engines installed
- Legacy `jade` still referenced

Typical failure signals:
```text
Failed to lookup view
No default engine specified
```

Reason this is separate from views debugging:
```text
Config problems occur before template lookup begins.
```

---
