# Single Responsibility Principle (SRP)
- Smaller units are easier to understand, test and reuse.

---
# Small functions/methods
- Ideally 5-15 lines of code.
##### Bad Code
``` cpp
void someFunction() {
	// function code

	// Connect to DB
	// Authenticate
	// Log Activity
	// Redirect
}
```

##### Good Code
``` cpp
bool isInputValid() {};

bool authenticateUser() {};

void logLogin() {};

void redirectToDashBoard() {};

void handleUserLogin() {
	// A bunch of function calls
}
```

---
# Small Classes
##### Bad
``` cpp
class UserManager {
    void validateInput();
    void login();
    void registerUser();
    void generateJWT();
    void sendEmail();
    void logActivity();
};
```

##### Good
``` cpp
class InputValidator {};
class AuthService {};
class EmailService {};
class AuditLogger {};
```

---
# Small Files
200-400 lines per file max.

---
# Folder Structure
Organize by Feature, Not by Type

##### Instead of
``` bash
controllers/
services/
models/
```

##### Use
``` bash
user/
  handler.rs
  service.rs
  model.rs
auth/
  handler.rs
  token.rs
```

---


