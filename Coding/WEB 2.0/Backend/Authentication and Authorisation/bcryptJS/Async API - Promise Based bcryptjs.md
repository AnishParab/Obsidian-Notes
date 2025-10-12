``` ts
import bcrypt from 'bcryptjs';

const salt = await bcrypt.genSalt(10);
const hash = await bcrypt.hash("myPassword", salt);

const isMatch = await bcrypt.compare("myPassword", hash); // true

```

---
