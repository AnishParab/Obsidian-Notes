# Problem Statement
**You’re deciding whether to go for a walk based on two real-life conditions:**
- `is_sunny = True`
- `have_umbrella = False`

**Print the result of the following:**
- Is it not sunny today?
- Do you not have an umbrella?
- Should you go for a walk if it’s sunny and you don’t need an umbrella?
- Should you go for a walk if it’s sunny or if you have an umbrella?

---
# Code
``` python
is_sunny = True
have_umbrella = False

# Is it not sunny today?
print(not is_sunny)

# Do you not have an umbrella?
print(not have_umbrella)

# Should you go for a walk if it’s sunny and you don’t need an umbrella?
print(is_sunny and not have_umbrella)

# Should you go for a walk if it’s sunny or if you have an umbrella?
print(is_sunny or have_umbrella)
```

---
