# Access Modifiers

- Access modifiers = keywords that control who can access a class member
- The enforcement mechanism behind encapsulation

---
# Three modifiers

- `public` — accessible from anywhere
- `private` — accessible only within the same class
- `protected` — accessible within the class and its subclasses (relevant in inheritance)

| Modifier    | Within Class | From Child Class | Outside Class |
| ----------- | ------------ | ---------------- | ------------- |
| `public`    | ✓            | ✓                | ✓             |
| `protected` | ✓            | ✓                | ✗             |
| `private`   | ✓            | ✗                | ✗             |

---
# In C++

- Strictly enforced by the compiler — accessing a `private` field from outside is a compile error
- Default access in a `class` is `private`, in a `struct` is `public`

---
# In Python

- No compiler enforcement — it's convention-based
- `field` → public, anyone can access
- `_field` → protected by convention, "don't touch unless you're a subclass"
- `__field` → name mangling, becomes `_ClassName__field` — not truly private but practically hidden

---
# **Python gotcha**

- `__field` doesn't block access, it just renames it
- `obj._SportsCar__currentSpeed` still works — Python trusts the developer
- Convention is the only real guard

---
# **Which modifier for what**

- Internal state that shouldn't leak → `private`
- State subclasses may need to extend → `protected`
- Interface the outside world uses → `public`

---
