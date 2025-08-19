``` js
const cookieParser = require('cookie-parser');
const express = require('express');
const app = express();
const bcrypt = require('bcrypt');

app.use(cookieParser())

app.get("/", function(req, res) {
	res.cookie("name", "anish");
	res.send("done");
})

app.get("/read", function(req, res) {
	console.log(req.cookies) // Install cookie-parser package to run this
	res.send("read page");
})

app.listen(3000)
```

---
``` js
const express = require('express');
const app = express();
const bcrypt = require('bcrypt');


app.get("/", function(req, res) {

	//Encryption
	bcrypt.genSalt(10, function(err, salt) {
		bcrypt.hash("mypassword", salt, function(err, hash) {
			console.log(hash);
		});
	});

// Compare Paaword with Hash
	bcrypt.compare("mypassword", "$2b$10$d9YtVRnJirVLB0C9u3QaiulY4sh8sTm1sBugbyu86D4.7jV4nHBMW", function(err, result) {
		console.log(result);
	});
})

app.listen(3000)
```

---
``` js
const express = require('express');
const app = express();
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const cookieParser = require('cookie-parser');

app.use(cookieParser());

app.get("/", function(req, res) {
	let token = jwt.sign({ email: "anish@example.com" }, "secret")
	res.cookie("token", token)
	res.send("Done")
})

app.get("/read", function(req, res) {
	let data = jwt.verify(req.cookies.token, "secret");
	console.log(data);
})

app.listen(3000)
```

---
