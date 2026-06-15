# Using `sendStatus()` Shortcut

```js
res.sendStatus(404)
```

Equivalent to:
```js
res.status(404).send('Not Found')
```

- Sends status + default text body.

---
