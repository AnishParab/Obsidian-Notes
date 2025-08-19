``` ts
import bcrypt from 'bcryptjs';

const salt = bcrypt.genSaltSync(10);
const hash = bcrypt.hashSync("myPassword", salt);

const isMatch = bcrypt.compareSync("myPassword", hash); // true
```

---
