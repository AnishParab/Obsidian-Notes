# Code

`chatRoom.js`
``` js
const EventEmitter = require('node:events')

class ChatRoom extends EventEmitter {
  constructor() {
    super()
    this.users = new Set()
  }

  join(user) {
    this.users.add(user)
    this.emit('join', user)
  }

  sendMessage(user, message) {
    if (this.users.has(user)) {
      this.emit('message', user, message)
    } else {
      console.log(`${user} is not in chat`)
    }
  }

  leave(user) {
    if (this.users.has(user)) {
      this.users.delete(user)
      this.emit('leave', user)
    } else {
      console.log(`${user} is not in the chat`)
    }
  }
}

module.exports = ChatRoom
```

`index.js`
``` js
const ChatRoom = require('./chatRoom.js')

const chat = new ChatRoom()

chat.on('join', (user) => {
  console.log(`${user} has joined the chat`)
})

chat.on('message', (user, message) => {
  console.log(`${user} : ${message}`)
})

chat.on('leave', (user) => {
  console.log(`${user} has left the chat`)
})

// simulating the chat
chat.join('Alice')
chat.join('Bob')

chat.sendMessage("Alice", "Hey Alice, fuck you")
chat.sendMessage("Bob", "Hey Bob, Mz")

chat.leave("Alice")
chat.sendMessage("Alice", "This message won't be sent")
chat.leave("Bob")
```

**Output**:
``` text
Alice has joined the chat
Bob has joined the chat
Alice : Hey Alice, fuck you
Bob : Hey Bob, Mz
Alice has left the chat
Alice is not in chat
Bob has left the chat
```

---
