> There can be only one default export in one module.

---
- Default exports do not have any name.

---
# Code
`math.js`
``` js
exports.myAddFunction = function add(a, b) {
  return a + b;
}

exports.sub = function sub(a, b) {
  return a - b;
}

exports.mul = function mul(a, b) {
  return a * b;
}

exports.div = function div(a, b) {
  return a / b;
}

// Default export
module.exports = function() {
  console.log('I am a default export');
}
```

`index.js`
``` js
const xyz = require('./math.js');

console.log(xyz());
```

##### Output
``` bash
I am a default export
undefined
```

---
