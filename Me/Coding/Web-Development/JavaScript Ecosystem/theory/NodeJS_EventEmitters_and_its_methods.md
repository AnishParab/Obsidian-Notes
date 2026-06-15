# Code 1 : `.on` and `.emit`

``` js
const EventEmitter = require('node:events')

const eventEmitter = new EventEmitter()

eventEmitter.on('greet', () => {
	console.log("Hello and Welcome to events in Node.js")
})

// Emit the event
eventEmitter.emit("greet")
```

**Output**:
``` text
Hello and Welcome to events in Node.js
```

---
# Code 2 : Passing Arguments

``` js
const EventEmitter = require('node:events')

const eventEmitter = new EventEmitter()

eventEmitter.on('greet', (username) => {
	console.log(`Hello ${username} and Welcome to events in Node.js`)
})

// Emit the event and pass some data
eventEmitter.emit("greet", "anish")
```

**Output**:
``` text
Hello anish and Welcome to events in Node.js
```

---
# Code 3 : `.once`

``` js
const EventEmitter = require('node:events')

const eventEmitter = new EventEmitter()

eventEmitter.on("greet", (username) => {
  console.log(`Hello ${username}`)
})

eventEmitter.once('pushnotify', () => {
  console.log("This event will run only once")
})

// Emit the event
eventEmitter.emit("greet", "anish")
eventEmitter.emit("greet", "chai")
eventEmitter.emit("pushnotify")
eventEmitter.emit("pushnotify")
```

**Output**:
``` text
Hello anish
Hello chai
This event will run only once
```

---
# Code 4 : `.removeListener`

``` js
const EventEmitter = require('node:events')

const eventEmitter = new EventEmitter()

const myListener = () => console.log("I am a test listener")

eventEmitter.on("test", myListener)
eventEmitter.emit("test")
eventEmitter.emit("test")

eventEmitter.removeListener("test", myListener)
eventEmitter.emit("test")
```

**Output**:
``` text
I am a test listener
I am a test listener
```

---
# Code 5 : `.listeners`

``` js
const EventEmitter = require('node:events')

const eventEmitter = new EventEmitter()


eventEmitter.on("greet", (username) => {
  console.log(`Hello ${username}`)
})

eventEmitter.once('pushnotify', () => {
  console.log("This event will run only once")
})

eventEmitter.once('pushnotify', () => {
  console.log("Another event")
})

const myListener = () => console.log("I am a test listener")

eventEmitter.on("test", myListener)
eventEmitter.emit("test")
eventEmitter.emit("test")
eventEmitter.removeListener("test", myListener)
eventEmitter.emit("test")

console.log(eventEmitter.listeners('test'))
console.log(eventEmitter.listeners('greet'))
console.log(eventEmitter.listeners('pushnotify'))
```

**Output**:
``` text
I am a test listener
I am a test listener
[]
[ [Function (anonymous)] ]
[ [Function (anonymous)], [Function (anonymous)] ]
```

---
