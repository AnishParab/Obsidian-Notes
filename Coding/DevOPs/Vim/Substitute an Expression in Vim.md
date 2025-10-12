# Example
- Mass-refactor `exports.something = …` into ES module style `export const something = …`.

---
### 1. Quick single-file substitute
If every line follows that pattern, run this in normal mode:

```vim
:%s/^exports\.\(\w\+\)\s*=/export const \1 =/
```
Explanation:
- `^exports\.` → match only if the line starts with `exports.`
- `\(\w\+\)` → capture the identifier (like `getAllBooks`)
- `\s*=` → match the `=` after spaces
- `export const \1 =` → replace with `export const <identifier> =`
So:
```js
exports.getAllBooks = function(req, res) {
```
becomes:
```js
export const getAllBooks = function(req, res) {
```

---
### 2. Visual-multi way (multi-cursor)
Since you’re in LazyVim, you can do this interactively:
1. Place your cursor on `exports.`
2. Press `<C-n>` (Control-n) → it selects this occurrence and enters multi-cursor mode
3. Keep pressing `<C-n>` to select more `exports.` in the file
4. Once all are selected, just type `export const` and it will replace them all at once

---
### 3. Multi-file (project-wide) replace
If this pattern appears in multiple files, you can use `grep` + quickfix:
```vim
:args **/*.js | argdo %s/^exports\.\(\w\+\)\s*=/export const \1 =/ge | update
```
- `:args **/*.js` → load all JS files into the argument list
- `argdo` → run the substitution on each file
- `g` flag → replace all in line
- `e` flag → suppress “not found” errors
- `update` → save file if modified

---
