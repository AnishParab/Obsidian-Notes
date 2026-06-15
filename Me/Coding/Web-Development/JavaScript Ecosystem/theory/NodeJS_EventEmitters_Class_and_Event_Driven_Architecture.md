# Code

``` js
const EventEmitter = require('node:events')

class Chat extends EventEmitter {
  sendMessage(msg) {
    console.log(`Message sent: ${msg}`)
    this.emit('messageReceived', msg)
  }
}

const chat = new Chat()
chat.on('messageReceived', (msg) => {
  console.log(`New message: ${msg}`)
})

// Trigger event
chat.sendMessage("Hello Anish")
```

**Output**:
``` text
Message sent: Hello Anish
New message: Hello Anish
```

---
