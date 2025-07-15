# Super Globals / Pre-defined Variables
- Always available regardless of scope.
- Use `_` to access a pre-defined variable.
- All the super globals are an associative array.

---
## `$GLOBALS`
- An associative array containing access to all the variables which are currently defined in global scope of the script.
``` php
<?php
$x = 75;
$y = 25;

function addition() {
    $GLOBALS['z'] = $GLOBALS['x'] + $GLOBALS['y'];
}

addition();
echo $z;  // Outputs: 100
```

---
## `$_SERVER`
- Contains information about headers, path and script location.
``` php
<?php
echo $_SERVER["DOCUMENT_ROOT"];
echo "<br>";
echo $_SERVER["PHP_SELF"]; // File name of the currently executing script
echo "<br>";
echo $_SERVER["SERVER_NAME"]; // name of the server host
echo "<br>";
echo $_SERVER["REQUEST_METHOD"]; // GET or POST method
echo "<br>";
echo $_SERVER["REQUEST_URI"]; // URI path requested by the client
```

---
## `_GET`
- Outputs URL parameters **(query string)**.

`http://localhost:8000/index.php?name=anish&eyeColor=black`
``` php
<?php
echo $_GET["name"];
echo $_GET["eyeColor"]
```

---
## `_POST`
- Data sent via HTTP Post method.
``` php
<?php
// Assuming a form with method="post"
echo $_POST['email'];
```

---
## `_REQUEST`
- Contains the contents of `$_GET`, `$_POST`, and `$_COOKIE`. Used to collect data after submitting an HTML form.
``` php
<?php
echo $_REQUEST['username'];

```

---
## `_FILES`
- Get about a file that has been uploaded to your server.
- Double checking the file.
- For example ---> File size, File format etc.
``` php
<?php
$_FILES['file']['name']
$_FILES['file']['type']
$_FILES['file']['tmp_name']
$_FILES['file']['error']
$_FILES['file']['size']
```

---
## `_COOKIE`
- Cookie is a small file that your server embeds on the users computer.
- Contains variables passed to the current script via HTTP Cookies.
``` php
echo $_COOKIE['user'];
```

---
## `_SESSION`
- Used to store session variables to preserve data across multiple pages.
``` php
session_start();
$_SESSION['favcolor'] = "green";
echo $_SESSION['favcolor'];
```

---
## `_ENV`
- An associative array of environment variables passed to the current script.
``` php
echo $_ENV['PATH'];
```

---


