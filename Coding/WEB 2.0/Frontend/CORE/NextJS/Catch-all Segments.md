# Why do we need this?
**Example**
- For routes, `src/app/docs/feature1/concept1` , `.../concept2`, `.../concept3` and so on...
- Lets suppose there are 20 features and 20 concepts in each feature ---> This will need **20 * 20 = 400** separate files.
- This is solved using **Dynamic Routing**.

**Hence**
- Using `20 Features * 1 [conceptId]` ---> We can cut that down to only **20 files**.

**Similarly**
- Using `1 [featureId] * 1 [conceptId]` ---> We can cut that down to just **2 Folders**.

---
