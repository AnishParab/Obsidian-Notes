# Better Option : `Nodemon`

> Node.js native watcher just sucks.

``` bash
npm install -D nodemon
```
- `-D` is a flag, for installing it as a dev-dependency.

`package.json`
``` json
{
  "scripts": {
    "start": "nodemon index.js"
  }
}
```

``` bash
npm start
```

---
# Native Node.js Watcher : **(It just sucks)**

`package.json`
``` json
{
  "scripts": {
    "start": "node --watch index.js"
  },
}
```

**Now run** :
``` bash
npm start
```

#### NOTE :

> `--watch` enables native node.js watcher.
>  A watcher monitors filesystem events and restarts the Node process when files change.

---
