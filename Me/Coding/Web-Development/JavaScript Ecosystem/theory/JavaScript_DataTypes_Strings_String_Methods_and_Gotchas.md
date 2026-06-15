# JavaScript Strings

> Strings are **immutable** — methods return new strings, never modify original

---
**Declaration**
```js
let a = "hello"         // double quotes
let b = 'hello'         // single quotes
let c = `hello`         // template literal
```

---
**Template Literals**
```js
let name = "alice"
let age = 25
console.log(`Name: ${name}, Age: ${age}`)   // Name: alice, Age: 25
console.log(`2 + 2 = ${2 + 2}`)             // 2 + 2 = 4

// multiline
let msg = `line one
line two`
```

---
**Common Methods**
```js
let str = "Hello World"

// case
str.toUpperCase()          // "HELLO WORLD"
str.toLowerCase()          // "hello world"

// search
str.includes("World")      // true
str.startsWith("Hello")    // true
str.endsWith("World")      // true
str.indexOf("o")           // 4 — first occurrence
str.lastIndexOf("o")       // 7 — last occurrence

// extract
str.slice(0, 5)            // "Hello"
str.slice(-5)              // "World" — negative counts from end
str.substring(0, 5)        // "Hello"
str.charAt(0)              // "H"
str[0]                     // "H"

// modify
str.replace("World", "JS")  // "Hello JS" — first match only
str.replaceAll("l", "r")    // "Herro Worrd"
str.trim()                  // removes leading/trailing whitespace
str.trimStart()             // removes leading whitespace
str.trimEnd()               // removes trailing whitespace
str.padStart(15, "*")       // "****Hello World"
str.padEnd(15, "*")         // "Hello World****"
str.repeat(2)               // "Hello WorldHello World"

// split
str.split(" ")              // ["Hello", "World"]
str.split("")               // ["H","e","l","l","o"," ","W","o","r","l","d"]

// concat
"Hello" + " " + "World"    // "Hello World"
"Hello".concat(" ", "World") // "Hello World"
```

---
**String to Number / Number to String**
```js
Number("42")        // 42
parseInt("42px")    // 42
parseFloat("3.14")  // 3.14
String(42)          // "42"
(42).toString()     // "42"
```

---
**Useful Properties**
```js
str.length          // 11
```

---
# Gotchas:

- `slice` vs `substring` — `slice` accepts negative indices, `substring` does not
- `replace` replaces first match only — use `replaceAll` or regex `/pattern/g` for all

---
