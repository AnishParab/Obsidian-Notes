# Vulnerable Regex in online repositories
### [ReGexLib,id=1757 (email validation)](http://regexlib.com/REDetails.aspx?regexp_id=1757) - see bold part, which is an **Evil Regex**

`^([a-zA-Z0-9])`**`(([\-.]|[_]+)?([a-zA-Z0-9]+))*`**`(@){1}[a-z0-9]+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))$`

Input:
`aaaaaaaaaaaaaaaaaaaaaaaa!`

---
### [OWASP Validation Regex Repository](https://wiki.owasp.org/index.php/OWASP_Validation_Regex_Repository), Java Classname - see bold part, which is an **Evil Regex**

`^`**`(([a-z])+.)+`**`[A-Z]([a-z])+$`

Input:
`aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!`

---
# Web application attack
- Open a JavaScript
- Find **Evil Regex**
- Craft a malicious input for the found Regex
- Submit a valid value via intercepting proxy
- Change the request to contain a malicious input
- You are done!

---
# ReDoS via Regex Injection
The following example checks if the username is part of the password entered by the user.
``` java
String userName = textBox1.Text;
String password = textBox2.Text;
Regex testPassword = new Regex(userName);
Match match = testPassword.Match(password);
if (match.Success)
{
    MessageBox.Show("Do not include name in password.");
}
else
{
    MessageBox.Show("Good password.");
}
```

- If an attacker enters `^(([a-z])+.)+[A-Z]([a-z])+$` as a username and `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!` as a password, the program will hang.

---
