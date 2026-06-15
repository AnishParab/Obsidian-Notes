# Primitives - Stored by value

``` js
let age = 42               // number — -(2^53 - 1) to (2^53 - 1)
let price = 3.14           // number — floating point
let invalid = NaN          // number — result of invalid math
let infinite = Infinity    // number — overflow result

let name = "hello"         // string

let isActive = true        // boolean — true / false

let x                      // undefined — declared but not assigned

let empty = null           // null — intentional absence of value

let big = 9007199254740991n // bigint — bigger than number type

let id = Symbol("id")      // symbol — unique identifier, Symbol("id") !== Symbol("id")
```

---
