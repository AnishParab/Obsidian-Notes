# Syntax
Describes how the elements of your program must be written and arranged in order for the program to be considered valid.

---
# Syntax Error
- When you compile your program, the compiler is responsible for making sure your program follows these syntactical rules.
- If your program does something that deviates from the syntax of the language, the compiler will halt compilation and issue a _syntax error_.

---
# Example Syntax Error in Clang
``` bash
prog.cc:5:31: error: expected ';' after expression
```

Clang is telling us that on line 5 at the 31st character, the syntax rules require a semicolon, but we did not provide one. Therefore, compilation was halted with an error.

---

