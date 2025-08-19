# Hashing
![[MongoDB_Hooks.excalidraw|700]]
- `userSchema.pre('save', ...)` registers a **pre-save middleware/hook**. It runs just before `.save()` (and before `create()`/`save()` operations).
- `function(next)` is a regular function (important: not an arrow function) so `this` refers to the document being saved.

- `this.isModified("password")` checks whether the `password` field was changed (or set on insert). If password wasn't changed, no need to re-hash.
- `bcrypt.hash(this.password, 10)` hashes the password with **10 salt rounds** (a common default).
- `next()` signals that middleware is done and Mongoose may continue with save.  
    **Note:** because the middleware is `async`, you can omit calling `next()` and just `return` — but calling `next()` after `await` is okay. However, ensure `this` is correctly typed if strict TS rules are enabled.
- **Edge cases**:
    - If hashing throws an error, you should call `next(err)` or let the exception bubble (in async middleware, throwing a rejection will be treated as an error by Mongoose).
    - Use a named `const SALT_ROUNDS = 10` for clarity and re-use.

---
