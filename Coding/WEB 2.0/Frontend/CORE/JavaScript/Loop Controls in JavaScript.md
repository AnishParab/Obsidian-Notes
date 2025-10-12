# Loop Controls
- `break` → exits loop completely.
- `continue` → skips current iteration and goes to next.
``` js
for (let i = 0; i < 5; i++) {
  if (i === 2) continue;
  if (i === 4) break;
  console.log(i);
}
// 0, 1, 3
```

---
