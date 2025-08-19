# Interface
An **interface** in Typescript defines the **shape of an object** — it tells the compiler what properties and types an object **must or can** have.

### Syntax
``` ts
interface User {
  id: number;
  name: string;
  email?: string; // optional property
}
```

You can now use this interface to **type-check** objects:
``` ts
const user: User = {
  id: 1,
  name: "Alice"
};
```

---
# Optional Properties
- Use `?:`
``` ts
interface Post {
  title: string;
  content?: string;
}
```

---

# Typescript Interfaces with MongoDB Schema
### Define Interface
``` ts
export interface IUser {
  _id?: string; // optional because MongoDB generates it
  name: string;
  email: string;
  age: number;
}
```

### Mongoose Schema
``` ts
import mongoose, { Schema, model, modles } from 'mongoose';

const UserSchema = new Schema<IUser>({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  age: { type: Number, default: 18 },
});
```

### Create the Mongoose Model
``` ts
const User = mongoose.models.User || mongoose.model<IUser>('User', UserSchema);

export default User;
```

---



