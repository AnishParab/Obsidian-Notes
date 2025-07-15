# Return Early
``` python
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
```

---
# DRY Principle
``` python
def restart_service(name):
    print(f"Restarting {name}...")

for svc in ["nginx", "mysql", "ssh"]:
    restart_service(svc)
```

---

