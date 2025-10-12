# Named Exports
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
```

`index.js`
``` js
const value = require('./math.js');

console.log(value.myAddFunction(2, 3));
```
**OR**
``` js
const { myAddFunction, sub, mul, div} = require('./math.js');

console.log(myAddFunction(2, 3));
```

---
