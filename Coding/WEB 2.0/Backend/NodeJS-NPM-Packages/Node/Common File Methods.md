# Official Documentation
[Follow This Link](https://nodejs.org/docs/latest/api/)

---
# Write in a File
``` js
const fs = require('node:fs');

fs.writeFile("hello.txt", "hello world", function(err){
	if(err) console.log(err);
	else console.log("done");
})
```

---
# Append to File
``` js
const fs = require('node:fs');

fs.appendFile("hello.txt", "hello world", function(err){
	if(err) console.log(err);
	else console.log("done");
})
```

---
# Rename File
