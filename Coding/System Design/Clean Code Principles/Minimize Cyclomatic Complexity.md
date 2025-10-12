The number of _independent paths_ through a function.

---
# Calculating It
> Start with 1  
> Add 1 for each of:
- `if`
- `else if`
- `for`
- `while`
- `case` or `match` arm
- `catch`
- `&&` or `||` in conditions (each counts as +1)
- ternary operator (`?:`)

---
# Examples
``` cpp
int func(int a, int b) {
    if (a > 0) {
        if (b > 0) {
            return 1;
        } else {
            return 2;
        }
    } else {
        return 3;
    }
}
```

>Start with 1
>`if` ---> +1
>`if` ---> +1
>`e;se` ---> 0
>Therefore, cc=3

---
# How to Reduce

| Anti-Pattern             | Solution                                |
| ------------------------ | --------------------------------------- |
| Deep nested `if-else`    | Use _guard clauses_ (`return early`)    |
| Long boolean expressions | Break into named helper functions       |
| Huge `switch`/`match`    | Use polymorphism or pattern matching    |
| Repeated conditionals    | Use strategy tables / data-driven logic |
##### Bad Example
``` cpp
// ❌ Nested nightmare
if (user != nullptr) {
    if (user->isActive()) {
        if (hasPermission(user)) {
            doStuff();
        }
    }
}
```
##### Good Example
``` cpp
// ✅ Guard clause FTW
if (user == nullptr) return;
if (!user->isActive()) return;
if (!hasPermission(user)) return;
doStuff();
```

---





