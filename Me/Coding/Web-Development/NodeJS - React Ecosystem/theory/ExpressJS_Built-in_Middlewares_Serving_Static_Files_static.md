# Serving Static Files

- To serve static files such as images, CSS files, and JavaScript files, use the `express.static` built-in middleware function in Express.

**Use this middleware** :
- The function signature is:
``` js
express.static(root, [optional])
```

- `root` -> This argument specifies the root directory from which to serve static files.

---
# Code

``` js
const path = require('path')

app.use('/static', express.static(path.join(__dirname, 'public')))
```

- `__dirname` -> current directory
- `/static` -> route
- `public` -> `/public` directory

**Output**:
``` bash
http://localhost:3000/static/images/kitten.jpg
http://localhost:3000/static/css/style.css
http://localhost:3000/static/js/app.js
http://localhost:3000/static/images/bg.png
http://localhost:3000/static/hello.html
```

---
