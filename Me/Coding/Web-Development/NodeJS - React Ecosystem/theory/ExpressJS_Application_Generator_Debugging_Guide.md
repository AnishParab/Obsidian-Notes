# What It Generates (Conceptual Layers)

```
bin/www   → server startup
app.js    → middleware + routing wiring
routes/   → endpoint logic
views/    → SSR templates (optional)
public/   → static assets
```

Mental model:
```
HTTP Server → Express App → Middleware → Router → View/Response
```

---
# Important Generated Files

### `bin/www`

- Creates HTTP server.
- Handles port configuration.
- Emits server-level errors.
- Debug indicator:
> If server fails before routes execute, inspect here.

### `app.js`

- Central configuration file.
- Registers middleware.
- Mounts routers.
- Sets view engine.
- Debug indicator:
> Incorrect middleware order causes silent failures.

### `routes/`

- Modular route handlers.
- Mounted inside `app.js`.
- Debug indicator:
> Route exists but URL fails → check mount path.

### `views/` (Only if view engine enabled)

- Contains `.pug` templates.
- Used by `res.render()`.

### `public/`

- Static file serving.
- Executed before route matching.
- Failure example:
> Static file masking API route.

---
# Execution Flow (Generator Architecture)

```
bin/www
   ↓
app.js
   ↓
Middleware Stack
   ↓
Router
   ↓
View Engine (optional)
```

---
# Typical Debugging Checklist

### Server not starting

- Check `bin/www`
- Port conflicts
- Environment variables

### `Cannot GET /`

- Router missing in `routes/index.js`
- Router not mounted in `app.js`

### View rendering errors

- `app.set('view engine', 'pug')`
- Template syntax inside `views/`

---
