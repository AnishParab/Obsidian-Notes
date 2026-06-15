# JavaScript Type Coercion

- JS automatically converts types when operators are applied — implicit conversion

---
**String coercion**
```js
"5" + 1      // "51" — number converted to string (+ concatenates)
"5" + true   // "5true"
"5" + null   // "5null"
```

---
**Numeric coercion**
```js
"5" - 1      // 4  — string converted to number
"5" * 2      // 10
"5" / 2      // 2.5
true + 1     // 2  — true → 1
false + 1    // 1  — false → 0
null + 1     // 1  — null → 0
undefined + 1 // NaN — undefined → NaN
```

---
**Loose equality (`==`) coercion**
```js
1 == "1"       // true  — string → number
0 == false     // true  — false → 0
0 == ""        // true  — "" → 0
null == undefined  // true  — special case
null == 0      // false — null only equals undefined
NaN == NaN     // false — NaN never equals anything
```

---
**Falsy values** — coerce to `false`:
```js
false, 0, "", null, undefined, NaN

console.log(undefined && 1)   // false
```

---
**Truthy** — everything else, including:
```js
"0", [], {}, -1    // all truthy — common gotcha

console.log("0" || 0)   // true
console.log("Anish" || false)   // true
```

---
**Short-circuiting**
``` js
console.log(false || true || false || false || false)   // true
```

---
**Explicit conversion (avoid coercion)**
```js
Number("5")      // 5
String(5)        // "5"
Boolean(0)       // false
parseInt("5px")  // 5
```

---
> Rule: always use `===`. Use explicit conversion when type matters.

---
