# Synchronous Code (Blocking Code)

``` js
const fs = require('node:fs')

console.log('Start of Script')

// Sync => Blocking Operations
const content = fs.readFileSync('notes.txt', 'utf-8')

console.log('Contents', content)

console.log('End of Script')
```

---
# Asynchronous Code (Non-Blocking Code)

![[what_if_sync_operation_in_web_server.excalidraw|500]]

``` js
const fs = require('node:fs')

fs.readFfile('notes.txt', 'utf-8', function(error, data) {
	if (error) console.log(error)
	else console.log('Content got', data)
})

console.log('End of Script')
```

> Note, the function inside is called as a **Function Callback.**

---
