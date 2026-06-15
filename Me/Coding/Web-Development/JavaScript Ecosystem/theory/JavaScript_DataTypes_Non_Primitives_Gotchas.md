# Gotchas

- Copy = reference copy, not value copy
```js
const a = {x: 1}
const b = a
b.x = 99          // a.x is also 99
```

- Equality checks reference, not content
```js
{} === {}         // false
[] === []         // false
```

---
