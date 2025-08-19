# Define Custom Scripts inside `package.json`
`package.json`
``` json
{
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js"
  }
}
```

---
# Run
``` bash
npm start     # Runs "start" script
npm run dev   # Runs "dev" script
```

> Use `npm run <script>` for any script **except** `"start"` and `"test"` (they can be run without `run`).

---
