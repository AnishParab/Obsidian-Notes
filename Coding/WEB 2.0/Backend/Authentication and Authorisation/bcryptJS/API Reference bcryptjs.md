| Function                             | Description                                        |
| ------------------------------------ | -------------------------------------------------- |
| `bcrypt.genSaltSync(rounds?)`        | Generates a salt (default 10 rounds)               |
| `bcrypt.genSalt(rounds?)`            | Async salt generation (Promise or Callback)        |
| `bcrypt.hashSync(password, salt?)`   | Hash password synchronously                        |
| `bcrypt.hash(password, salt)`        | Hash password asynchronously (Promise or Callback) |
| `bcrypt.compareSync(password, hash)` | Compare password with hash (sync)                  |
| `bcrypt.compare(password, hash)`     | Compare password with hash (async)                 |
| `bcrypt.truncates(password)`         | Returns `true` if password exceeds 72 bytes        |
| `bcrypt.getRounds(hash)`             | Gets number of rounds from hash                    |
| `bcrypt.getSalt(hash)`               | Extracts salt part of hash                         |

---
