> `bcryptjs` is a **pure JavaScript** implementation of the Bcrypt algorithm. Here's the internal working:

---
# Step-by-Step Workflow
### **Salt Generation**:
    
    - Random 128-bit salt is generated using a secure PRNG.
        
    - More rounds = more CPU cost.
- **Key Expansion**:
    - The salt and password are input into a modified **Blowfish key setup**.

### **Hashing**:
- The result is run through the Blowfish cipher in **multiple rounds (2^cost)**.
    - By default, cost = 10 ⇒ 1024 iterations.

### **Final Hash Format**:
``` bash
$2a$10$eImiTXuWVxfM37uY4JANjQ==hashhashhash

```

- Format:
``` pgsql
$2a$<cost>$<22-char-salt><31-char-hash>

```

### **Comparison**
- The input password is **hashed with the same salt and cost**, and the result is compared byte-by-byte with the stored hash.

---
