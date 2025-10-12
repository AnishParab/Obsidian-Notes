# Opening and Closing Delimiter
``` php
<?php
	// Write your php code here
	echo "Hello World"
?>
```
**Note** : The closing php tag implies a semicolon. Hence no semicolon is needed for the last line of php.
### Good Practice (For separate php files)
If the file ends with php code, omit the closing delimiter.
- This prevents accidental whitespace or newline output after PHP code.
``` php
<?php
// Good practice: leave it open if the file ends with PHP code
function sum($a, $b) {
    return $a + $b;
}
```

---
# Embedding HTML in PHP
Avoid This Approach.
``` php
<body>

<?php
	if(true) {
		echo "<p>Some HTML Text</p>"
	}
?>

</body>
```
It is seen as a PHP String and not HTML.

### Optimal way to embed HTML in PHP
``` php
<body>

<?php if(true) { ?>
<p>Some HTML Text</p>
<?php } ?>

</body>
```

---
# Commenting
``` php
// This is a comment
<?php
	echo "Hello World"
?>
/*
This
is
a
multi-line
comment
*/*
```

---
# Most Basic Setup
``` shell
sudo pacman -S php
```

- PHP Built-in Server
``` bash
php -S localhost:8000
```

- One of your file should be named `index.php`.

---
