# Problem Statement
**Age Verification System**
- You’re building a system to verify user age for access.

**Tasks:**
1. Define a function verify_age that accepts a **string** input named age_str.
2. Convert age_str to an integer using int().
3. Use a **ternary operator** to return:
    - "Access Granted" if age is 18 or older
    - "Access Denied" otherwise

---
# Code
``` python
def verify_age(age_str: str):
    age_int = int(age_str)
    print("Access Granted") if age_int >= 18 else print("Access Denied")


verify_age("10")
```

---
