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
const value = require('./math.js'); console.log(value.myAddFunction(2, 3));
```

##### Output
``` bash
TypeError: value.myAddFunction is not a function
```

---
# Problem
- The problem is, **default exports** **overwrites everything you added to `exports` earlier**.
- After this assignment, `module.exports` only points to that function, so when you `require('./math.js')`, `value` is that function — not an object with `myAddFunction` or others.

---
# Fix
- Use `module.exports` as an object.
`math.js`
``` js
// math.js
module.exports = {
  default: function () {
    console.log('I am a default export');
  },
  myAddFunction: function (a, b) {
    return a + b;
  },
  sub: function (a, b) {
    return a - b;
  },
  mul: function (a, b) {
    return a * b;
  },
  div: function (a, b) {
    return a / b;
  }
};
```

`index.js`
``` js
const { default: xyz, myAddFunction, sub, mul, div } = require('./math.js');

console.log(xyz());              // "I am a default export"
console.log(myAddFunction(2, 3)); // 5
```

---

