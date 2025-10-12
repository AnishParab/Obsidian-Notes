Ignored by compiler and is meant for the programmer's use only.

---
# Single Line Comment
``` cpp
// This is a single-line comment
```
Good convention is to place the comment above the statement it is commenting to.

---
# Multi-Line Comments
``` cpp
/* This
is
a
Multi-Line
Commnet
*/
```

---
# **NOTE**
If you ever write code that is so complex that needs a comment to explain _what_ a statement is doing, you probably need to rewrite your statement, not comment it.

---
# Example
1. **Bad comment:**
```cpp
// Set sight range to 0
sight = 0;
```
Reason: We already can see that sight is being set to 0 by looking at the statement

2. **Good comment:**
```cpp
// The player just drank a potion of blindness and can not see anything
sight = 0;
```
Reason: Now we know why the player’s sight is being set to 0

---
