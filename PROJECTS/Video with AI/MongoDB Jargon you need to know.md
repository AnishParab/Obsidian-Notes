# Schema, model and models
``` ts
import mongoose, { Schema, model, models } from "mongoose";

```
- A **Schema** defines the **structure and shape** of documents inside a MongoDB collection — basically the **blueprint** for your data.
- A **Model** is a **constructor compiled from a schema**, used to **interact with the actual MongoDB collection**. You can **query, update, delete, and create documents** through a model.
- **Models**, in environments like **Next.js (App Router)**, `mongoose.models` is used to **prevent model overwrite errors** during **hot reload** or **multiple model declarations** (since Next.js runs API routes in serverless fashion).

---
